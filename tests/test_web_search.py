"""web_search 테스트 — 네트워크는 모킹, 파서는 실측"""

import io
import json

import pytest

from autonomous_coding_agent.web_search import (
    DocumentationParser,
    VersionChecker,
    WebSearcher,
)


class FakeResp:
    def __init__(self, payload: bytes):
        self._buf = io.BytesIO(payload)

    def read(self):
        return self._buf.read()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class FakeOpener:
    def __init__(self, payload: bytes = b"", fail=False):
        self._payload = payload
        self.fail = fail
        self.urls = []

    def open(self, req, timeout=None):
        self.urls.append(getattr(req, "full_url", str(req)))
        if self.fail:
            from urllib.error import URLError

            raise URLError("down")
        return FakeResp(self._payload)


@pytest.fixture
def searcher(monkeypatch):
    s = WebSearcher(timeout=5)
    opener = FakeOpener()
    s._opener = opener
    return s, opener


class TestDispatch:
    def test_unknown_engine(self):
        with pytest.raises(ValueError):
            WebSearcher().search("x", engine="nope")

    def test_google_no_keys(self):
        assert WebSearcher().search("x", engine="google") == []

    def test_search_multi_dedupe(self, searcher):
        s, opener = searcher
        gh = {
            "items": [
                {
                    "full_name": "a/b",
                    "html_url": "http://u1",
                    "description": "d",
                    "stargazers_count": 5,
                    "language": "Python",
                    "topics": [],
                }
            ]
        }
        opener._payload = json.dumps(gh).encode()
        out = s.search_multi("q", engines=["github", "github"], max_results_per_engine=5)
        assert [r.url for r in out] == ["http://u1"]

    def test_search_multi_bad_engine_skipped(self, searcher):
        s, _ = searcher
        assert s.search_multi("q", engines=["nope"]) == []


class TestEngines:
    DDG = (
        '<div class="result__title"><a href="http://ex.com/a">Title A</a></div>'
        '<div class="result__snippet">snap A</a></div>'
    )

    def test_duckduckgo(self, searcher):
        s, opener = searcher
        opener._payload = self.DDG.encode()
        out = s.search("hi", engine="duckduckgo", max_results=5)
        assert len(out) == 1
        assert out[0].title == "Title A" and out[0].source == "duckduckgo"

    def test_duckduckgo_redirect(self, searcher):
        s, opener = searcher
        opener._payload = (
            b'<div class="result__title">'
            b'<a href="//duckduckgo.com/l/?uddg=http%3A%2F%2Freal.com&rut=x">R</a>'
            b"</div>"
        )
        out = s.search("hi", engine="duckduckgo")
        assert out[0].url == "http://real.com"

    def test_duckduckgo_fail(self, searcher):
        s, opener = searcher
        opener.fail = True
        assert s.search("hi", engine="duckduckgo") == []

    def test_github(self, searcher):
        s, opener = searcher
        opener._payload = json.dumps(
            {
                "items": [
                    {
                        "full_name": "o/r",
                        "html_url": "http://g",
                        "description": None,
                        "stargazers_count": 1,
                        "language": "Go",
                        "topics": ["t"],
                    }
                ]
            }
        ).encode()
        out = s.search("x", engine="github")
        assert out[0].title == "o/r" and out[0].snippet == ""
        assert out[0].metadata["language"] == "Go"

    def test_pypi(self, searcher):
        s, opener = searcher
        opener._payload = (
            b'<div class="package-snippet">'
            b'<span class="package-snippet__name">pkg</span>'
            b'<span class="package-snippet__version">1.0</span>'
            b'<p class="package-snippet__description">desc</p></div>'
        )
        out = s.search("x", engine="pypi")
        assert out[0].title == "pkg 1.0"
        assert out[0].url.endswith("/project/pkg/")

    def test_npm(self, searcher):
        s, opener = searcher
        opener._payload = json.dumps(
            {
                "objects": [
                    {
                        "package": {
                            "name": "n",
                            "version": "2.0",
                            "description": "d",
                            "keywords": ["k"],
                        },
                        "score": {"final": 0.9},
                    }
                ]
            }
        ).encode()
        out = s.search("x", engine="npm")
        assert out[0].title == "n@2.0"

    def test_google_with_keys(self, searcher):
        s, opener = searcher
        opener._payload = json.dumps(
            {"items": [{"title": "T", "link": "http://l", "snippet": "S", "displayLink": "l"}]}
        ).encode()
        out = s.search("x", engine="google", api_key="k", cse_id="c")
        assert out[0].source == "google" and out[0].metadata["display_link"] == "l"


class TestParsers:
    @pytest.fixture
    def parser(self):
        return DocumentationParser()

    def test_strip_html(self, parser):
        html = "<script>x()</script><style>.a{}</style><p>hi&nbsp;&amp;bye</p>"
        assert parser._strip_html(html) == "hi &bye"

    def test_extract_title(self, parser):
        assert parser._extract_title("<title>T</title>") == "T"
        assert parser._extract_title("<h1>H</h1>") == "H"
        assert parser._extract_title("<p>x</p>") is None

    def test_markdown_sections(self, parser):
        md = "# A\nbody a\n## B\nbody b\n"
        secs = parser._extract_markdown_sections(md)
        assert [s["heading"] for s in secs] == ["A", "B"]
        assert secs[1]["level"] == 2

    def test_markdown_code_blocks(self, parser):
        md = "```python\nprint('0123456789abcdefg')\n```\n"
        assert len(parser._extract_markdown_code_blocks(md)) == 1

    def test_indent_code_fallback(self, parser):
        md = "text\n\n    line1 code here yes\n    line2 code here yes\n    line3 code here yes\n"
        assert len(parser._extract_markdown_code_blocks(md)) >= 1

    def test_html_code_blocks(self, parser):
        html = "<pre><code>print('0123456789abcdefg')</code></pre>"
        assert len(parser._extract_code_blocks(html)) == 1

    def test_html_to_markdown(self, parser):
        html = '<h2>H</h2><p>bold <b>x</b> and <a href="http://u">lnk</a></p>'
        md = parser._html_to_markdown(html)
        assert "## H" in md and "**x**" in md and "[lnk](http://u)" in md

    def test_detect_language(self, parser):
        assert parser._detect_language("pip install django") == "python"
        assert parser._detect_language("npm run react") == "javascript"
        assert parser._detect_language("lorem ipsum dolor") is None

    def test_pypi_page(self, parser):
        html = (
            "<title>P</title>"
            '<p class="project-description">D</p>'
            '<span class="release__version">3.1</span>'
        )
        d = parser._parse_pypi_page("http://x", html)
        assert d.content == "D" and d.version == "3.1" and d.language == "python"

    def test_npm_page(self, parser):
        html = '<p class="description">D</p>'
        d = parser._parse_npm_page("http://x", html)
        assert d.content == "D" and d.language == "javascript"

    def test_generic_docs(self, parser):
        html = "<title>Doc</title>" '<div class="rst-content"><h1>T</h1><p>body text here</p></div>'
        d = parser._parse_generic_docs("http://docs.x", html)
        assert d.title == "Doc" and "body text here" in d.content

    def test_generic_html(self, parser):
        html = "<title>W</title><p>hello world content</p>"
        d = parser._parse_generic_html("http://x", html)
        assert d.title == "W" and "hello world" in d.content

    def test_github_readme_html_fallback(self, parser, monkeypatch):
        parser._opener = FakeOpener(b"", fail=True)
        html = (
            "<title>o/r</title>"
            '<article class="markdown-body"><h1>R</h1># Sec\nbody here</article>'
        )
        d = parser._parse_github_readme("https://github.com/o/r", html)
        assert "Sec" in d.content or "body here" in d.content

    def test_github_readme_api(self, parser):
        parser._opener = FakeOpener(b"# Title\n\nsome readme body text here")
        d = parser._parse_github_readme("https://github.com/o/r", "<title>t</title>")
        assert "readme body" in d.content

    def test_fetch_routing(self, parser):
        parser._opener = FakeOpener(b"<title>T</title><p>body</p>")
        assert parser.fetch_documentation("https://pypi.org/project/x/").language == "python"
        assert (
            parser.fetch_documentation("https://www.npmjs.com/package/x").language == "javascript"
        )
        assert parser.fetch_documentation("https://docs.x.io").title == "T"
        assert parser.fetch_documentation("https://example.com").title == "T"

    def test_fetch_fail(self, parser):
        parser._opener = FakeOpener(b"", fail=True)
        assert parser.fetch_documentation("https://example.com") is None


class TestVersionChecker:
    def _checker(self, payload: bytes):
        c = VersionChecker()
        c._opener = FakeOpener(payload)
        return c

    def test_pypi(self):
        payload = json.dumps(
            {
                "info": {"summary": "s"},
                "releases": {"1.0": [], "2.0a1": [], "1.5": []},
            }
        ).encode()
        out = self._checker(payload).check_pypi_package("pkg")
        assert out and out.get("latest_stable") == "1.5"

    def test_pypi_fail(self):
        c = VersionChecker()
        c._opener = FakeOpener(b"", fail=True)
        assert c.check_pypi_package("pkg") is None
