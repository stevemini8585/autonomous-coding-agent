"""
텔레그램 알림 (Autopilot 운영 알림용)
- stdlib만 사용, 실패해도 절대 예외를 던지지 않음 (알림 실패가 본류를 깨지 않도록)
- 토큰/채팅ID는 환경변수에서만 (하드코딩 금지)

Usage:
    >>> send_telegram(...)  # 텔레그램 메시지 발송 시 최대 3회 재시도. 성공 시 True, 어떤 실패든 False.
"""

from __future__ import annotations

import logging
import os
import urllib.parse
import urllib.request

log = logging.getLogger("autonomous_coding_agent.notify")

MAX_LEN = 4000


def send_telegram(text: str, chat_id: str | None = None, token: str | None = None) -> bool:
    """텔레그램 메시지 발송. 성공 시 True, 어떤 실패든 False."""
    token = token or os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat = chat_id or os.getenv("TELEGRAM_CHAT_ID", "")
    if not token or not chat:
        log.debug("telegram credentials missing, skip notify")
        return False
    text = text[:MAX_LEN]
    for i in range(3):  # 재시도 3회
        try:
            payload = urllib.parse.urlencode({"chat_id": chat, "text": text}).encode()
            request = urllib.request.Request(
                f"https://api.telegram.org/bot{token}/sendMessage", data=payload
            )
            with urllib.request.urlopen(request, timeout=10) as resp:
                if resp.status == 200:
                    return True
                else:
                    log.warning("telegram send failed: status code %d", resp.status)
        except Exception as e:
            log.warning("telegram send failed: %s", e)
    return False
