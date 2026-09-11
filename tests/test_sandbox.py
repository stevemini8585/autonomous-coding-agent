"""sandbox.py 테스트 — 격리·제한·스크럽 동작 검증."""

import os
import shutil
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from autonomous_coding_agent.sandbox import SandboxConfig, assert_inside, run_sandboxed

HAS_SANDBOX_EXEC = shutil.which("sandbox-exec") is not None


@pytest.fixture()
def workdir(tmp_path):
    d = tmp_path / "wt"
    d.mkdir()
    return d


def test_echo(workdir):
    r = run_sandboxed(["/bin/echo", "hello"], SandboxConfig(workdir=workdir))
    assert r.returncode == 0 and r.stdout.strip() == "hello" and not r.timed_out


def test_timeout(workdir):
    r = run_sandboxed(["/bin/sleep", "10"], SandboxConfig(workdir=workdir, timeout_s=1))
    assert r.timed_out and r.returncode == -1


def test_env_scrub(workdir):
    os.environ["SANDBOX_TEST_SECRET_KEY"] = "shhh"
    try:
        r = run_sandboxed(["/usr/bin/env"], SandboxConfig(workdir=workdir))
        assert "SANDBOX_TEST_SECRET_KEY" not in r.stdout
    finally:
        del os.environ["SANDBOX_TEST_SECRET_KEY"]


def test_missing_command(workdir):
    r = run_sandboxed(["/nonexistent-cmd-xyz"], SandboxConfig(workdir=workdir))
    assert r.returncode == -1 and "명령 없음" in r.error


def test_bad_workdir(tmp_path):
    r = run_sandboxed(["/bin/echo", "x"], SandboxConfig(workdir=tmp_path / "nope"))
    assert r.returncode == -1 and "workdir 없음" in r.error


def test_assert_inside_ok(workdir):
    assert assert_inside("a/b.txt", workdir) == (workdir / "a/b.txt").resolve()


def test_assert_inside_escape(workdir):
    with pytest.raises(ValueError):
        assert_inside("../escape.txt", workdir)
    with pytest.raises(ValueError):
        assert_inside("/etc/passwd", workdir)


@pytest.mark.skipif(not HAS_SANDBOX_EXEC, reason="sandbox-exec 없음")
def test_network_blocked(workdir):
    r = run_sandboxed(
        ["/usr/bin/curl", "-m", "6", "-s", "-o", "/dev/null", "https://example.com"],
        SandboxConfig(workdir=workdir, allow_network=False),
    )
    assert r.network_blocked and r.returncode != 0


@pytest.mark.skipif(not HAS_SANDBOX_EXEC, reason="sandbox-exec 없음")
def test_network_allowed(workdir):
    r = run_sandboxed(
        [
            "/usr/bin/curl",
            "-m",
            "8",
            "-s",
            "-o",
            "/dev/null",
            "-w",
            "%{http_code}",
            "https://example.com",
        ],
        SandboxConfig(workdir=workdir, allow_network=True),
    )
    assert not r.network_blocked and r.returncode == 0 and r.stdout.strip() == "200"
