"""
웹 검색 및 문서 조회 모듈
DuckDuckGo HTML 스크래핑, Google Custom Search API, 공식 문서 파싱
"""

from __future__ import annotations

import json
import logging
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import UTC, datetime
from html import unescape as _unescape
from typing import Any, ClassVar
from urllib.error import HTTPError, URLError

log = logging.getLogger("autonomous_coding_agent.web_search")


@dataclass
class SearchResult:
    """검색 결과"""

    title: str
    url: str
    snippet: str
    source: str  # "duckduckgo", "google", "github", "pypi", "npm"
    relevance_score: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class Documentation:
    """파싱된 문서"""

    title: str
    url: str
    content: str
    sections: list[dict[str, str]] = field(default_factory=list)  # [{heading, content}]
    code_examples: list[str] = field(default_factory=list)
    version: str | None = None
    language: str | None = None
    fetched_at: datetime = field(default_factory=datetime.now)


class WebSearcher:
    """웹 검색기"""

    # 검색 엔진 설정
    SEARCH_ENGINES: ClassVar[dict[str, dict[str, Any]]] = {
        "duckduckgo": {
            "base_url": "https://html.duckduckgo.com/html/",
            "params": {"q": "{query}"},
            "method": "POST",
            "headers": {"User-Agent": "Mozilla/5.0 (compatible; AutonomousCodingAgent/1.0)"},
        },
        "google": {
            "base_url": "https://www.googleapis.com/customsearch/v1",
            "params": {"q": "{query}", "key": "{api_key}", "cx": "{cse_id}"},
            "method": "GET",
        },
        "github": {
            "base_url": "https://api.github.com/search/repositories",
            "params": {"q": "{query}", "sort": "stars", "order": "desc"},
            "method": "GET",
            "headers": {"Accept": "application/vnd.github.v3+json"},
        },
        "pypi": {
            "base_url": "https://pypi.org/search/",
            "params": {"q": "{query}"},
            "method": "GET",
        },
        "npm": {
            "base_url": "https://registry.npmjs.org/-/v1/search",
            "params": {"text": "{query}", "size": 10},
            "method": "GET",
        },
    }

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self._opener = urllib.request.build_opener()
        self._opener.addheaders = [
            ("User-Agent", "Mozilla/5.0 (compatible; AutonomousCodingAgent/1.0)")
        ]

    def search(
        self,
        query: str,
        engine: str = "duckduckgo",
        max_results: int = 10,
        **kwargs,
    ) -> list[SearchResult]:
        """웹 검색 수행"""
        log.info(f"웹 검색: '{query}' (engine: {engine})")

        if engine == "duckduckgo":
            return self._search_duckduckgo(query, max_results)
        elif engine == "google":
            return self._search_google(query, max_results, **kwargs)
        elif engine == "github":
            return self._search_github(query, max_results)
        elif engine == "pypi":
            return self._search_pypi(query, max_results)
        elif engine == "npm":
            return self._search_npm(query, max_results)
        else:
            raise ValueError(f"지원하지 않는 검색 엔진: {engine}")

    def _search_duckduckgo(self, query: str, max_results: int) -> list[SearchResult]:
        """DuckDuckGo HTML 스크래핑"""
        results = []

        try:
            # DuckDuckGo는 POST 요청 필요
            data = urllib.parse.urlencode({"q": query}).encode()
            req = urllib.request.Request(
                "https://html.duckduckgo.com/html/",
                data=data,
                headers={"User-Agent": "Mozilla/5.0 (compatible; AutonomousCodingAgent/1.0)"},
                method="POST",
            )

            with self._opener.open(req, timeout=self.timeout) as response:
                html = response.read().decode("utf-8", errors="ignore")

            # 결과 파싱 (정규식으로 간단 추출)
            # 결과 항목: class="result__title" -> 링크, class="result__snippet" -> 요약
            title_pattern = re.compile(
                r'class="result__title"[^>]*>\s*<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>'
            )
            snippet_pattern = re.compile(r'class="result__snippet"[^>]*>([^<]*)</a>')

            titles = title_pattern.findall(html)
            snippets = snippet_pattern.findall(html)

            for i, (url, title) in enumerate(titles[:max_results]):
                # URL 정리 (DuckDuckGo 리다이렉트 제거)
                if url.startswith("//duckduckgo.com/l/?uddg="):
                    url = urllib.parse.unquote(url.split("uddg=")[1].split("&")[0])

                snippet = snippets[i] if i < len(snippets) else ""

                results.append(
                    SearchResult(
                        title=title.strip(),
                        url=url,
                        snippet=snippet.strip(),
                        source="duckduckgo",
                        relevance_score=1.0 - (i * 0.1),
                    )
                )

        except (HTTPError, URLError, TimeoutError) as e:
            log.warning(f"DuckDuckGo 검색 실패: {e}")

        return results

    def _search_google(self, query: str, max_results: int, **kwargs) -> list[SearchResult]:
        """Google Custom Search API (API 키 필요)"""
        results = []
        api_key = kwargs.get("api_key")
        cse_id = kwargs.get("cse_id")

        if not api_key or not cse_id:
            log.warning("Google Search API 키가 설정되지 않음")
            return results

        try:
            params = {
                "q": query,
                "key": api_key,
                "cx": cse_id,
                "num": min(max_results, 10),
            }
            url = "https://www.googleapis.com/customsearch/v1?" + urllib.parse.urlencode(params)

            with self._opener.open(url, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())

            for i, item in enumerate(data.get("items", [])):
                results.append(
                    SearchResult(
                        title=item.get("title", ""),
                        url=item.get("link", ""),
                        snippet=item.get("snippet", ""),
                        source="google",
                        relevance_score=1.0 - (i * 0.1),
                        metadata={"display_link": item.get("displayLink", "")},
                    )
                )

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"Google 검색 실패: {e}")

        return results

    def _search_github(self, query: str, max_results: int) -> list[SearchResult]:
        """GitHub 저장소 검색"""
        results = []

        try:
            params = {
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": max_results,
            }
            url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(params)

            req = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/vnd.github.v3+json",
                    "User-Agent": "AutonomousCodingAgent/1.0",
                },
            )

            with self._opener.open(req, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())

            for i, item in enumerate(data.get("items", [])):
                results.append(
                    SearchResult(
                        title=item.get("full_name", ""),
                        url=item.get("html_url", ""),
                        snippet=item.get("description", "") or "",
                        source="github",
                        relevance_score=1.0 - (i * 0.1),
                        metadata={
                            "stars": item.get("stargazers_count", 0),
                            "language": item.get("language", ""),
                            "topics": item.get("topics", []),
                        },
                    )
                )

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"GitHub 검색 실패: {e}")

        return results

    def _search_pypi(self, query: str, max_results: int) -> list[SearchResult]:
        """PyPI 패키지 검색"""
        results = []

        try:
            params = {"q": query, "page": 1, "per_page": max_results}
            url = "https://pypi.org/search/?" + urllib.parse.urlencode(params)

            with self._opener.open(url, timeout=self.timeout) as response:
                html = response.read().decode("utf-8", errors="ignore")

            # PyPI 검색 결과 파싱 (JSON API 사용이 더 좋음)
            # 간단히 HTML에서 추출
            pattern = re.compile(
                r'class="package-snippet"[^>]*>.*?<span class="package-snippet__name">([^<]+)</span>.*?'
                r'<span class="package-snippet__version">([^<]+)</span>.*?'
                r'<p class="package-snippet__description">([^<]*)</p>',
                re.DOTALL,
            )

            for i, match in enumerate(pattern.findall(html)[:max_results]):
                name, version, desc = match
                results.append(
                    SearchResult(
                        title=f"{name.strip()} {version.strip()}",
                        url=f"https://pypi.org/project/{name.strip()}/",
                        snippet=desc.strip(),
                        source="pypi",
                        relevance_score=1.0 - (i * 0.1),
                        metadata={
                            "package_name": name.strip(),
                            "version": version.strip(),
                        },
                    )
                )

        except (HTTPError, URLError, TimeoutError) as e:
            log.warning(f"PyPI 검색 실패: {e}")

        return results

    def _search_npm(self, query: str, max_results: int) -> list[SearchResult]:
        """npm 패키지 검색"""
        results = []

        try:
            params = {"text": query, "size": max_results}
            url = "https://registry.npmjs.org/-/v1/search?" + urllib.parse.urlencode(params)

            with self._opener.open(url, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())

            for i, pkg in enumerate(data.get("objects", [])):
                pkg_info = pkg.get("package", {})
                results.append(
                    SearchResult(
                        title=f"{pkg_info.get('name', '')}@{pkg_info.get('version', '')}",
                        url=f"https://www.npmjs.com/package/{pkg_info.get('name', '')}",
                        snippet=pkg_info.get("description", "") or "",
                        source="npm",
                        relevance_score=pkg.get("score", {}).get("final", 1.0) - (i * 0.1),
                        metadata={
                            "name": pkg_info.get("name", ""),
                            "version": pkg_info.get("version", ""),
                            "keywords": pkg_info.get("keywords", []),
                        },
                    )
                )

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"npm 검색 실패: {e}")

        return results

    def search_multi(
        self,
        query: str,
        engines: list[str] | None = None,
        max_results_per_engine: int = 5,
        **kwargs,
    ) -> list[SearchResult]:
        """다중 엔진 검색 및 결과 병합"""
        if engines is None:
            engines = ["duckduckgo", "github", "pypi"]

        all_results = []
        for engine in engines:
            try:
                results = self.search(query, engine, max_results_per_engine, **kwargs)
                all_results.extend(results)
            except (HTTPError, URLError, TimeoutError, ValueError) as e:
                log.warning(f"{engine} 검색 실패: {e}")

        # 관련도 점수로 정렬 후 중복 제거
        seen_urls = set()
        unique_results = []
        for result in sorted(all_results, key=lambda r: r.relevance_score, reverse=True):
            if result.url not in seen_urls:
                seen_urls.add(result.url)
                unique_results.append(result)

        return unique_results[: max_results_per_engine * len(engines)]


class DocumentationParser:
    """공식 문서 파서"""

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self._opener = urllib.request.build_opener()
        self._opener.addheaders = [
            ("User-Agent", "Mozilla/5.0 (compatible; AutonomousCodingAgent/1.0)")
        ]

    def fetch_documentation(self, url: str) -> Documentation | None:
        """문서 페이지 가져오기 및 파싱"""
        log.info(f"문서 가져오기: {url}")

        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with self._opener.open(req, timeout=self.timeout) as response:
                html = response.read().decode("utf-8", errors="ignore")

            # 사이트별 파싱
            if "github.com" in url:
                return self._parse_github_readme(url, html)
            elif "pypi.org" in url:
                return self._parse_pypi_page(url, html)
            elif "npmjs.com" in url:
                return self._parse_npm_page(url, html)
            elif "readthedocs.io" in url or "docs." in url:
                return self._parse_generic_docs(url, html)
            else:
                return self._parse_generic_html(url, html)

        except (HTTPError, URLError, TimeoutError) as e:
            log.warning(f"문서 가져오기 실패: {url} - {e}")
            return None

    def _parse_github_readme(self, url: str, html: str) -> Documentation:
        """GitHub README 파싱 - GitHub API로 원본 마크다운 가져오기"""
        # URL에서 owner/repo 추출
        match = re.search(r"github\.com/([^/]+)/([^/]+)", url)
        readme_content = ""

        if match:
            owner, repo = match.group(1), match.group(2)
            # GitHub API로 README 원본 가져오기
            try:
                api_url = f"https://api.github.com/repos/{owner}/{repo}/readme"
                req = urllib.request.Request(
                    api_url,
                    headers={
                        "Accept": "application/vnd.github.v3.raw",
                        "User-Agent": "AutonomousCodingAgent/1.0",
                    },
                )
                with self._opener.open(req, timeout=self.timeout) as response:
                    readme_content = response.read().decode("utf-8", errors="ignore")
            except (HTTPError, URLError, TimeoutError):
                pass

        # API 실패 시 HTML에서 추출 시도
        if not readme_content:
            readme_match = re.search(
                r'<article class="markdown-body[^>]*>(.*?)</article>',
                html,
                re.DOTALL,
            )
            if readme_match:
                readme_content = self._strip_html(readme_match.group(1))

        # 섹션 추출 (마크다운 헤더 기반)
        sections = self._extract_markdown_sections(readme_content)

        # 코드 블록 추출 (마크다운 ``` 패턴)
        code_examples = self._extract_markdown_code_blocks(readme_content)

        return Documentation(
            title=self._extract_title(html) or f"{owner}/{repo}" if match else "GitHub Repository",
            url=url,
            content=readme_content[:10000],
            sections=sections,
            code_examples=code_examples,
            language=self._detect_language(readme_content or html),
        )

    def _extract_markdown_sections(self, markdown: str) -> list[dict[str, str]]:
        """마크다운에서 섹션 추출 (헤더 기반)"""
        sections = []
        # 마크다운 헤더 패턴 (# ## ### 등)
        header_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

        matches = list(header_pattern.finditer(markdown))
        for i, match in enumerate(matches):
            level = len(match.group(1))
            heading = match.group(2).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
            section_content = markdown[start:end].strip()

            if section_content:
                sections.append(
                    {
                        "heading": heading,
                        "content": section_content[:3000],
                        "level": level,
                    }
                )

        return sections[:30]

    def _extract_markdown_code_blocks(self, markdown: str) -> list[str]:
        """마크다운 코드 블록 추출 (``` 패턴)"""
        codes = []
        # ```language\ncode\n``` 패턴
        pattern = re.compile(r"```[\w]*\n(.*?)\n```", re.DOTALL)
        for match in pattern.finditer(markdown):
            code = match.group(1).strip()
            if len(code) > 20:
                codes.append(code[:5000])

        # 인덴트 코드 블록 (4 spaces)
        if not codes:
            indent_pattern = re.compile(r"(?:^    .*\n)+", re.MULTILINE)
            for match in indent_pattern.finditer(markdown):
                code = match.group(0).strip()
                if len(code) > 50:
                    codes.append(code[:5000])

        return codes[:15]

    def _parse_pypi_page(self, url: str, html: str) -> Documentation:
        """PyPI 프로젝트 페이지 파싱"""
        # 프로젝트 설명 추출
        desc_match = re.search(
            r'<p class="project-description">([^<]*)</p>',
            html,
        )
        description = desc_match.group(1) if desc_match else ""

        # 버전 추출
        version_match = re.search(r'class="release__version"[^>]*>([^<]+)</', html)
        version = version_match.group(1) if version_match else None

        return Documentation(
            title=self._extract_title(html) or "PyPI Package",
            url=url,
            content=description,
            version=version,
            language="python",
        )

    def _parse_npm_page(self, url: str, html: str) -> Documentation:
        """npm 패키지 페이지 파싱"""
        desc_match = re.search(
            r'<p class="[^"]*description[^"]*">([^<]*)</p>',
            html,
        )
        description = desc_match.group(1) if desc_match else ""

        return Documentation(
            title=self._extract_title(html) or "npm Package",
            url=url,
            content=description,
            language="javascript",
        )

    def _parse_generic_docs(self, url: str, html: str) -> Documentation:
        """일반 문서 사이트 파싱 (ReadTheDocs, Sphinx, MkDocs, GitBook 등)"""
        # 다양한 문서 사이트별 메인 콘텐츠 선택자
        content_selectors = [
            r'<main[^>]*role="main"[^>]*>(.*?)</main>',
            r'<div[^>]*class="[^"]*documentation[^"]*"[^>]*>(.*?)</div>',
            r'<div[^>]*class="[^"]*content[^"]*"[^>]*role="main"[^>]*>(.*?)</div>',
            r'<div[^>]*class="[^"]*rst-content[^"]*"[^>]*>(.*?)</div>',  # Sphinx
            r'<div[^>]*class="[^"]*mkdocs-content[^"]*"[^>]*>(.*?)</div>',  # MkDocs
            r'<div[^>]*class="[^"]*gitbook[^"]*"[^>]*>(.*?)</div>',  # GitBook
            r'<article[^>]*class="[^"]*markdown[^"]*"[^>]*>(.*?)</article>',
            r'(?:<main[^>]*>|<div[^>]*class="[^"]*(?:content|documentation|main)[^"]*"[^>]*>)(.*?)(?:</main>|</div>)',
        ]

        content_html = ""
        for pattern in content_selectors:
            match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
            if match:
                content_html = match.group(1)
                break

        if not content_html:
            content_html = html

        # 마크다운 변환을 위해 HTML 정리
        content = self._html_to_markdown(content_html)

        # 섹션 추출 (마크다운 헤더 기반)
        sections = self._extract_markdown_sections(content)

        # 코드 블록 추출
        code_examples = self._extract_markdown_code_blocks(content)

        # HTML에서도 코드 블록 추출 (백업)
        if not code_examples:
            code_examples = self._extract_code_blocks(html)

        return Documentation(
            title=self._extract_title(html) or "Documentation",
            url=url,
            content=content[:15000],
            sections=sections,
            code_examples=code_examples,
        )

    def _html_to_markdown(self, html: str) -> str:
        """간단한 HTML -> 마크다운 변환"""
        # 코드 블록 보존
        code_blocks = []

        def save_code(match):
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{len(code_blocks)-1}__"

        html = re.sub(
            r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>",
            save_code,
            html,
            flags=re.DOTALL | re.IGNORECASE,
        )
        html = re.sub(
            r"<code[^>]*>(.*?)</code>", lambda m: f"`{m.group(1)}`", html, flags=re.DOTALL
        )

        # 헤더 변환
        for i in range(6, 0, -1):
            html = re.sub(
                f"<h{i}[^>]*>(.*?)</h{i}>",
                f'{"#"*i} \\1',
                html,
                flags=re.DOTALL | re.IGNORECASE,
            )

        # 링크 변환
        html = re.sub(
            r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
            r"[\2](\1)",
            html,
            flags=re.DOTALL | re.IGNORECASE,
        )

        # 리스트 변환
        html = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1", html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r"</?(ul|ol)[^>]*>", "", html, flags=re.IGNORECASE)

        # 단락
        html = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r"<br[^>]*>", "\n", html, flags=re.IGNORECASE)

        # 굵게/기울임
        html = re.sub(
            r"<(strong|b)[^>]*>(.*?)</\1>", r"**\2**", html, flags=re.DOTALL | re.IGNORECASE
        )
        html = re.sub(r"<(em|i)[^>]*>(.*?)</\1>", r"*\2*", html, flags=re.DOTALL | re.IGNORECASE)

        # 나머지 태그 제거
        html = re.sub(r"<[^>]+>", " ", html)

        # 엔티티 디코딩
        html = _unescape(html.replace("&nbsp;", " "))

        # 코드 블록 복원
        for i, code in enumerate(code_blocks):
            code_clean = self._strip_html(code)
            html = html.replace(f"__CODE_BLOCK_{i}__", f"\n```\n{code_clean}\n```\n")

        # 공백 정리
        html = re.sub(r"\n{3,}", "\n\n", html)
        html = re.sub(r"[ \t]+", " ", html)

        return html.strip()

    def _parse_generic_html(self, url: str, html: str) -> Documentation:
        """일반 HTML 페이지 파싱"""
        content = self._strip_html(html)
        sections = self._extract_sections(content)
        code_examples = self._extract_code_blocks(html)

        return Documentation(
            title=self._extract_title(html) or "Web Page",
            url=url,
            content=content[:5000],
            sections=sections,
            code_examples=code_examples,
        )

    def _strip_html(self, html: str) -> str:
        """HTML 태그 제거 및 텍스트 정리"""
        # 스크립트/스타일 제거
        html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
        html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
        # 태그 제거
        text = re.sub(r"<[^>]+>", " ", html)
        # 엔티티 디코딩
        text = _unescape(text.replace("&nbsp;", " "))
        # 공백 정리
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def _extract_title(self, html: str) -> str | None:
        """페이지 제목 추출"""
        match = re.search(r"<title[^>]*>([^<]+)</title>", html, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        match = re.search(r"<h1[^>]*>([^<]+)</h1>", html, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return None

    def _extract_sections(self, text: str) -> list[dict[str, str]]:
        """텍스트에서 섹션 추출 (헤더 기반)"""
        sections = []
        # 마크다운 스타일 헤더
        header_pattern = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

        matches = list(header_pattern.finditer(text))
        for i, match in enumerate(matches):
            level = len(match.group(1))
            heading = match.group(2).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            section_content = text[start:end].strip()

            if section_content:
                sections.append(
                    {
                        "heading": heading,
                        "content": section_content[:2000],
                        "level": level,
                    }
                )

        return sections[:20]

    def _extract_code_blocks(self, html: str) -> list[str]:
        """코드 블록 추출"""
        codes = []
        # <pre><code> 패턴
        pattern = re.compile(
            r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>", re.DOTALL | re.IGNORECASE
        )
        for match in pattern.finditer(html):
            code = self._strip_html(match.group(1))
            if len(code) > 20:  # 의미있는 코드만
                codes.append(code[:3000])

        # ``` 패턴 (마크다운)
        if not codes:
            md_pattern = re.compile(r"```[\w]*\n(.*?)\n```", re.DOTALL)
            for match in md_pattern.finditer(html):
                code = match.group(1).strip()
                if len(code) > 20:
                    codes.append(code[:3000])

        return codes[:10]

    def _detect_language(self, html: str) -> str | None:
        """프로그래밍 언어 감지"""
        lang_indicators = {
            "python": ["python", "pip", "pypi", "django", "flask", "fastapi"],
            "javascript": ["javascript", "npm", "node", "react", "vue"],
            "typescript": ["typescript", "tsx", "tsconfig"],
            "go": ["golang", "go.mod", "go "],
            "rust": ["rust", "cargo", "crates.io"],
            "java": ["java", "maven", "gradle", "spring"],
        }

        html_lower = html.lower()
        for lang, keywords in lang_indicators.items():
            if any(k in html_lower for k in keywords):
                return lang
        return None


# 편의 함수
def search_web(
    query: str, engines: list[str] | None = None, max_results: int = 10
) -> list[SearchResult]:
    """웹 검색 편의 함수"""
    searcher = WebSearcher()
    return searcher.search_multi(query, engines, max_results)


def fetch_docs(url: str) -> Documentation | None:
    """문서 가져오기 편의 함수"""
    parser = DocumentationParser()
    return parser.fetch_documentation(url)


def search_and_fetch_docs(
    query: str,
    engines: list[str] | None = None,
    max_results: int = 5,
    fetch_docs_count: int = 3,
) -> tuple[list[SearchResult], list[Documentation]]:
    """검색 후 상위 결과 문서 가져오기"""
    searcher = WebSearcher()
    parser = DocumentationParser()

    results = searcher.search_multi(query, engines, max_results)

    docs = []
    for result in results[:fetch_docs_count]:
        doc = parser.fetch_documentation(result.url)
        if doc:
            docs.append(doc)

    return results, docs


class VersionChecker:
    """패키지 버전 호환성 확인기"""

    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self._opener = urllib.request.build_opener()
        self._opener.addheaders = [
            ("User-Agent", "Mozilla/5.0 (compatible; AutonomousCodingAgent/1.0)")
        ]

    def check_pypi_package(self, package_name: str) -> dict[str, Any] | None:
        """PyPI 패키지 정보 조회 (최신 버전, 의존성, 메타데이터)"""
        log.info(f"PyPI 패키지 확인: {package_name}")

        try:
            url = f"https://pypi.org/pypi/{package_name}/json"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with self._opener.open(req, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())

            info = data.get("info", {})
            releases = data.get("releases", {})

            # 최신 안정 버전 (pre-release 제외)
            versions = list(releases.keys())
            stable_versions = [
                v for v in versions if not any(x in v for x in ["a", "b", "rc", "dev"])
            ]

            def version_key(v: str) -> tuple:
                """버전 문자열을 비교 가능한 튜플로 변환"""
                parts = []
                for part in v.split("."):
                    try:
                        parts.append(int(part))
                    except ValueError:
                        # 숫자가 아닌 부분은 0으로 처리
                        parts.append(0)
                return tuple(parts)

            latest_stable = (
                max(stable_versions, key=version_key) if stable_versions else info.get("version")
            )

            return {
                "name": info.get("name"),
                "version": info.get("version"),
                "latest_stable": latest_stable,
                "summary": info.get("summary"),
                "description": info.get("description"),
                "author": info.get("author"),
                "license": info.get("license"),
                "home_page": info.get("home_page"),
                "project_urls": info.get("project_urls", {}),
                "requires_python": info.get("requires_python"),
                "dependencies": info.get("requires_dist", []),
                "classifiers": info.get("classifiers", []),
                "all_versions": sorted(versions, key=version_key, reverse=True)[:10],
            }

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"PyPI 패키지 확인 실패: {package_name} - {e}")
            return None

    def check_npm_package(self, package_name: str) -> dict[str, Any] | None:
        """npm 패키지 정보 조회 (최신 버전, 의존성, 메타데이터)"""
        log.info(f"npm 패키지 확인: {package_name}")

        try:
            url = f"https://registry.npmjs.org/{package_name}"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with self._opener.open(req, timeout=self.timeout) as response:
                data = json.loads(response.read().decode())

            latest_version = data.get("dist-tags", {}).get("latest")
            versions = list(data.get("versions", {}).keys())
            latest_info = data.get("versions", {}).get(latest_version, {})

            return {
                "name": data.get("name"),
                "version": latest_version,
                "latest_stable": latest_version,
                "description": latest_info.get("description"),
                "main": latest_info.get("main"),
                "scripts": latest_info.get("scripts", {}),
                "dependencies": latest_info.get("dependencies", {}),
                "devDependencies": latest_info.get("devDependencies", {}),
                "peerDependencies": latest_info.get("peerDependencies", {}),
                "engines": latest_info.get("engines", {}),
                "license": latest_info.get("license"),
                "repository": latest_info.get("repository"),
                "keywords": latest_info.get("keywords", []),
                "all_versions": sorted(versions, reverse=True)[:10],
            }

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"npm 패키지 확인 실패: {package_name} - {e}")
            return None

    def check_github_repo(self, owner: str, repo: str) -> dict[str, Any] | None:
        """GitHub 저장소 정보 조회 (릴리스, 태그, 의존성)"""
        log.info(f"GitHub 저장소 확인: {owner}/{repo}")

        try:
            # 릴리스 정보
            url = f"https://api.github.com/repos/{owner}/{repo}/releases?per_page=5"
            req = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/vnd.github.v3+json",
                    "User-Agent": "AutonomousCodingAgent/1.0",
                },
            )
            with self._opener.open(req, timeout=self.timeout) as response:
                releases = json.loads(response.read().decode())

            # 최신 릴리스
            latest_release = releases[0] if releases else None

            # 저장소 기본 정보
            url = f"https://api.github.com/repos/{owner}/{repo}"
            req = urllib.request.Request(
                url,
                headers={
                    "Accept": "application/vnd.github.v3+json",
                    "User-Agent": "AutonomousCodingAgent/1.0",
                },
            )
            with self._opener.open(req, timeout=self.timeout) as response:
                repo_info = json.loads(response.read().decode())

            return {
                "owner": owner,
                "repo": repo,
                "full_name": repo_info.get("full_name"),
                "description": repo_info.get("description"),
                "stars": repo_info.get("stargazers_count"),
                "language": repo_info.get("language"),
                "license": (
                    repo_info.get("license", {}).get("spdx_id")
                    if repo_info.get("license")
                    else None
                ),
                "latest_release": {
                    "tag": latest_release.get("tag_name") if latest_release else None,
                    "name": latest_release.get("name") if latest_release else None,
                    "published_at": latest_release.get("published_at") if latest_release else None,
                    "prerelease": latest_release.get("prerelease") if latest_release else None,
                },
                "topics": repo_info.get("topics", []),
                "default_branch": repo_info.get("default_branch"),
            }

        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            log.warning(f"GitHub 저장소 확인 실패: {owner}/{repo} - {e}")
            return None

    def check_compatibility(
        self,
        packages: list[
            dict[str, str]
        ],  # [{"name": "fastapi", "type": "pypi", "current_version": "0.68.0"}]
    ) -> dict[str, Any]:
        """여러 패키지의 호환성 종합 확인"""
        results = {
            "checked_at": datetime.now(UTC).isoformat(),
            "packages": [],
            "warnings": [],
            "recommendations": [],
        }

        for pkg in packages:
            name = pkg.get("name")
            pkg_type = pkg.get("type", "pypi")
            current_version = pkg.get("current_version")

            if pkg_type == "pypi":
                info = self.check_pypi_package(name)
            elif pkg_type == "npm":
                info = self.check_npm_package(name)
            elif pkg_type == "github":
                owner, repo = name.split("/")
                info = self.check_github_repo(owner, repo)
            else:
                info = None

            if info:
                # 버전 비교
                latest = info.get("latest_stable") or info.get("version")
                version_status = "unknown"
                if current_version and latest:
                    try:
                        current_tuple = tuple(map(int, current_version.split(".")))
                        latest_tuple = tuple(map(int, latest.split(".")))
                        if current_tuple < latest_tuple:
                            version_status = "outdated"
                        elif current_tuple == latest_tuple:
                            version_status = "current"
                        else:
                            version_status = "ahead"
                    except ValueError:
                        version_status = "unknown"

                results["packages"].append(
                    {
                        "name": name,
                        "type": pkg_type,
                        "current_version": current_version,
                        "latest_version": latest,
                        "version_status": version_status,
                        "info": info,
                    }
                )

                # 경고 생성
                if version_status == "outdated":
                    results["warnings"].append(f"{name}: 현재 {current_version} → 최신 {latest}")
            else:
                results["warnings"].append(f"{name}: 정보 조회 실패")

        return results


# 편의 함수
def check_package_version(package_name: str, pkg_type: str = "pypi") -> dict[str, Any] | None:
    """단일 패키지 버전 확인 편의 함수"""
    checker = VersionChecker()
    if pkg_type == "pypi":
        return checker.check_pypi_package(package_name)
    elif pkg_type == "npm":
        return checker.check_npm_package(package_name)
    elif pkg_type == "github":
        owner, repo = package_name.split("/")
        return checker.check_github_repo(owner, repo)
    return None


def check_compatibility(
    packages: list[dict[str, str]],
) -> dict[str, Any]:
    """호환성 종합 확인 편의 함수"""
    checker = VersionChecker()
    return checker.check_compatibility(packages)


if __name__ == "__main__":
    # 테스트
    searcher = WebSearcher()

    # DuckDuckGo 검색 테스트
    print("=== DuckDuckGo 검색 테스트 ===")
    results = searcher.search("FastAPI async tutorial", "duckduckgo", max_results=3)
    for r in results:
        print(f"  - {r.title}")
        print(f"    URL: {r.url}")
        print(f"    Snippet: {r.snippet[:100]}...")
        print()

    # GitHub 검색 테스트
    print("=== GitHub 검색 테스트 ===")
    results = searcher.search("FastAPI async", "github", max_results=3)
    for r in results:
        print(f"  - {r.title} ({r.metadata.get('stars', 0)} stars)")
        print(f"    URL: {r.url}")
        print()
