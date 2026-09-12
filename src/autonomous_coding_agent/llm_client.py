"""
통합 LLM 클라이언트 (Day 6: LLM Coder 기반)
- 우선순위: Ollama 로컬 → OpenRouter → OpenAI → Anthropic
- stdlib만 사용 (urllib), 실패 시 (False, reason) 반환 — 절대 예외 없음
- OPENROUTER_API_KEY / OPENAI_API_KEY / ANTHROPIC_API_KEY는 환경변수에서만
"""

from __future__ import annotations

import json
import logging
import os
import urllib.request

log = logging.getLogger("autonomous_coding_agent.llm_client")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:8b")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")


def _post_json(
    url: str, payload: dict, headers: dict | None = None, timeout: int = 120
) -> tuple[bool, dict | str]:
    """JSON POST. 성공 시 (True, 응답dict), 실패 시 (False, 사유)."""
    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json", **(headers or {})},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, json.loads(resp.read().decode())
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def ollama_chat(
    prompt: str, system: str = "", model: str = OLLAMA_MODEL, timeout: int = 180
) -> tuple[bool, str]:
    """Ollama 로컬 채팅. 성공 시 (True, 텍스트)."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    ok, res = _post_json(
        f"{OLLAMA_URL}/api/chat",
        {"model": model, "messages": messages, "stream": False},
        timeout=timeout,
    )
    if not ok:
        return False, str(res)
    try:
        return True, str(res["message"]["content"])  # type: ignore[index]
    except (KeyError, TypeError) as e:
        return False, f"응답 파싱 실패: {e}"


def openrouter_chat(
    prompt: str, system: str = "", model: str = OPENROUTER_MODEL, timeout: int = 180
) -> tuple[bool, str]:
    """OpenRouter 채팅. 성공 시 (True, 텍스트)."""
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key:
        return False, "OPENROUTER_API_KEY 없음"
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    ok, res = _post_json(
        OPENROUTER_URL,
        {"model": model, "messages": messages},
        headers={"Authorization": f"Bearer {key}"},
        timeout=timeout,
    )
    if not ok:
        return False, str(res)
    try:
        return True, str(res["choices"][0]["message"]["content"])  # type: ignore[index]
    except (KeyError, IndexError, TypeError) as e:
        return False, f"응답 파싱 실패: {e}"


def chat(prompt: str, system: str = "") -> tuple[str, str]:
    """통합 진입점. (provider, 텍스트) 반환 — 전부 실패 시 ("none", "").

    우선순위: Ollama 로컬 → OpenRouter. 유료 API(OpenAI/Anthropic)는
    기존 llm_planner/llm_critic 경로를 유지하고 여기선 제외 (로컬 우선 원칙).
    """
    ok, text = ollama_chat(prompt, system)
    if ok and text.strip():
        log.info("LLM provider=ollama")
        return "ollama", text
    log.warning("Ollama 실패(%s), OpenRouter 시도", text[:100])
    ok, text = openrouter_chat(prompt, system)
    if ok and text.strip():
        log.info("LLM provider=openrouter")
        return "openrouter", text
    log.warning("OpenRouter 실패(%s)", text[:100])
    return "none", ""
