"""Explorer 심볼 추출 회귀 테스트 (O(n²) 무한루프급 저하 방지)"""

import time
from pathlib import Path

from autonomous_coding_agent.explorer import CodeExplorer


def _explorer(tmp_path: Path) -> CodeExplorer:
    return CodeExplorer(tmp_path)


class TestMethodDetection:
    SRC = """\
def top():
    return 1

class A:
    def m(self):
        return 2

    class Inner:
        def deep(self):
            return 3

async def afunc():
    return 4
"""

    def test_types(self, tmp_path):
        exp = _explorer(tmp_path)
        syms = exp._extract_python_symbols(tmp_path / "a.py", self.SRC)
        by_name = {s.name: s.type for s in syms}
        assert by_name["top"] == "function"
        assert by_name["m"] == "method"
        assert by_name["deep"] == "method"
        assert by_name["A"] == "class"
        assert by_name["afunc"] == "async_function"

    def test_broken_source_empty(self, tmp_path):
        exp = _explorer(tmp_path)
        assert exp._extract_python_symbols(tmp_path / "b.py", "def broken(:\n") == []


class TestPerformance:
    def test_large_file_fast(self, tmp_path):
        # 함수 1500개짜리 파일이 5초 안에 끝나야 함 (구 O(n²)는 수십 초 이상)
        body = "".join(f"def f{i}(x):\n    return x + {i}\n\n" for i in range(1500))
        src = (
            "class C:\n"
            + "".join(f"    def m{i}(self):\n        return {i}\n\n" for i in range(300))
            + body
        )
        exp = _explorer(tmp_path)
        t0 = time.time()
        syms = exp._extract_python_symbols(tmp_path / "big.py", src)
        dt = time.time() - t0
        assert dt < 5.0, f"너무 느림: {dt:.1f}s"
        kinds = {s.type for s in syms}
        assert {"function", "method", "class"} <= kinds


class TestExcludes:
    def test_junk_dirs_excluded(self, tmp_path):
        (tmp_path / "mutants" / "x.py").parent.mkdir(parents=True)
        (tmp_path / "mutants" / "x.py").write_text("a = 1\n")
        (tmp_path / ".autonomous_memory" / "s.json").parent.mkdir(parents=True)
        (tmp_path / ".autonomous_memory" / "s.json").write_text("{}\n")
        (tmp_path / "ok.py").write_text("b = 2\n")
        exp = _explorer(tmp_path)
        collected = {f.name for f in exp._collect_files(None)}
        assert "x.py" not in collected
        assert "s.json" not in collected
        assert "ok.py" in collected
