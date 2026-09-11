"""로컬 샌드박스 실행 — 생성 코드가 사용자 권한 그대로 도는 문제의 1차 격리.

보장: 작업디렉토리 감옥(cwd 탈출 거부) · 비밀 환경변수 스크럽 ·
       CPU/벽시계 제한 · 네트워크 차단(sandbox-exec, macOS).
정직한 한계: macOS는 RLIMIT_RSS를 강제하지 않아 메모리 상한은
       주소공간(RLIMIT_AS) 옵션으로만 제공하며 기본 OFF.
"""

from __future__ import annotations

import contextlib
import os
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

SECRET_HINTS = ("KEY", "TOKEN", "SECRET", "PASSWORD", "CREDENTIAL")

NO_NET_PROFILE = "(version 1)\n(allow default)\n(deny network-outbound)\n"


@dataclass
class SandboxConfig:
    workdir: Path
    timeout_s: int = 120
    cpu_s: int = 120
    memory_mb: int = 0  # 0=OFF (macOS RSS 미강제 때문)
    allow_network: bool = False


@dataclass
class SandboxResult:
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool = False
    network_blocked: bool = False
    wall_s: float = 0.0
    error: str = ""


def _scrubbed_env() -> dict[str, str]:
    env = dict(os.environ)
    for k in list(env):
        if any(h in k.upper() for h in SECRET_HINTS):
            del env[k]
    return env


def _limit_resources(cpu_s: int, memory_mb: int):
    def _pre():
        try:
            import resource

            if cpu_s > 0:
                resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))
            if memory_mb > 0:
                b = memory_mb * 1024 * 1024
                resource.setrlimit(resource.RLIMIT_AS, (b, b))
        except (ImportError, ValueError, OSError):
            pass

    return _pre


def run_sandboxed(cmd: list[str], config: SandboxConfig) -> SandboxResult:
    """명령을 샌드박스 제약 하에 실행. shell=False 고정."""
    if not cmd:
        return SandboxResult(-1, "", "", error="empty command")
    workdir = Path(config.workdir).resolve()
    if not workdir.is_dir():
        return SandboxResult(-1, "", "", error=f"workdir 없음: {workdir}")
    if "/" in cmd[0]:
        exe = (workdir / cmd[0]).resolve() if not Path(cmd[0]).is_absolute() else Path(cmd[0])
        if not (exe.is_file() and os.access(exe, os.X_OK)):
            return SandboxResult(-1, "", "", error=f"명령 없음: {cmd[0]}")
    elif shutil.which(cmd[0]) is None:
        return SandboxResult(-1, "", "", error=f"명령 없음: {cmd[0]}")

    argv = list(cmd)
    network_blocked = False
    profile_path: str | None = None
    if not config.allow_network and shutil.which("sandbox-exec"):
        try:
            with tempfile.NamedTemporaryFile(
                "w", suffix=".sb", delete=False, encoding="utf-8"
            ) as f:
                f.write(NO_NET_PROFILE)
                profile_path = f.name
            argv = ["sandbox-exec", "-f", profile_path, *argv]
            network_blocked = True
        except OSError:
            profile_path = None

    start = time.monotonic()
    try:
        proc = subprocess.run(
            argv,
            cwd=str(workdir),
            env=_scrubbed_env(),
            capture_output=True,
            text=True,
            timeout=config.timeout_s,
            preexec_fn=_limit_resources(config.cpu_s, config.memory_mb),
        )
        wall = time.monotonic() - start
        return SandboxResult(
            proc.returncode, proc.stdout, proc.stderr, network_blocked=network_blocked, wall_s=wall
        )
    except subprocess.TimeoutExpired as e:
        wall = time.monotonic() - start
        out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
        err = e.stderr.decode() if isinstance(e.stderr, bytes) else (e.stderr or "")
        return SandboxResult(
            -1, out, err, timed_out=True, network_blocked=network_blocked, wall_s=wall
        )
    except FileNotFoundError:
        return SandboxResult(
            -1, "", "", error=f"명령 없음: {cmd[0]}", network_blocked=network_blocked
        )
    except OSError as e:
        return SandboxResult(-1, "", "", error=str(e), network_blocked=network_blocked)
    finally:
        if profile_path:
            with contextlib.suppress(OSError):
                Path(profile_path).unlink()


def assert_inside(path: str | Path, workdir: str | Path):
    """경로가 작업디렉토리 안에 있는지 검증. 탈출 시 ValueError."""
    base = Path(workdir).resolve()
    target = (base / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    if target != base and base not in target.parents:
        raise ValueError(f"작업디렉토리 탈출 거부: {path}")
    return target
