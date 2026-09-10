"""
Tests for autonomous_coding_agent.notify (auto-generated smoke).
Goal: GitHub 이슈 #15: Rename single-letter locals in notify.send_telegram

send_telegram 안의 한 글자 변수(data→payload, req→request)로 이름 변경. 수용 기준: data, req 이름이 사
"""

import pytest

try:
    from autonomous_coding_agent.notify import send_telegram
except ImportError:
    send_telegram = None


def test_send_telegram_callable():
    """send_telegram 호출 가능 여부(스모크)"""
    assert callable(send_telegram)
