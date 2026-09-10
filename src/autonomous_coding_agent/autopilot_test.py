"""
Tests for autonomous_coding_agent.autopilot (auto-generated smoke).
Goal: GitHub 이슈 #15: Rename single-letter locals in notify.send_telegram

send_telegram 안의 한 글자 변수(data→payload, req→request)로 이름 변경. 수용 기준: data, req 이름이 사
"""

import pytest

try:
    from autonomous_coding_agent.autopilot import create_autopilot
except ImportError:
    create_autopilot = None


def test_create_autopilot_callable():
    """create_autopilot 호출 가능 여부(스모크)"""
    assert callable(create_autopilot)
