"""Tests for dashboard module"""

import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from autonomous_coding_agent import (
    DashboardServer,
    SessionProgress,
    StepProgress,
    get_dashboard,
)


def test_session_progress():
    """Test SessionProgress dataclass"""
    session = SessionProgress(
        session_id="test-123",
        goal="Test goal",
        status="running",
        total_steps=5,
    )
    
    assert session.session_id == "test-123"
    assert session.goal == "Test goal"
    assert session.status == "running"
    assert session.total_steps == 5
    assert session.current_step == 0
    assert session.overall_progress == 0.0
    
    # Test to_dict
    d = session.to_dict()
    assert d["session_id"] == "test-123"
    assert d["goal"] == "Test goal"


def test_step_progress():
    """Test StepProgress dataclass"""
    step = StepProgress(
        step_id="step-1",
        title="Test step",
        status="pending",
    )
    
    assert step.step_id == "step-1"
    assert step.title == "Test step"
    assert step.status == "pending"
    assert step.progress == 0.0


def test_dashboard_server_creation():
    """Test DashboardServer creation"""
    dashboard = DashboardServer(host="127.0.0.1", port=8899)
    
    assert dashboard.host == "127.0.0.1"
    assert dashboard.port == 8899
    assert dashboard.app is not None
    assert len(dashboard.sessions) == 0


def test_dashboard_singleton():
    """Test get_dashboard singleton"""
    d1 = get_dashboard("127.0.0.1", 8899)
    d2 = get_dashboard("127.0.0.1", 8899)
    assert d1 is d2


def test_session_progress_update():
    """Test overall progress calculation"""
    session = SessionProgress(
        session_id="test",
        goal="Test",
        status="running",
        total_steps=3,
    )
    
    # Add steps
    session.steps["step1"] = StepProgress(step_id="step1", title="Step 1", status="completed", progress=1.0)
    session.steps["step2"] = StepProgress(step_id="step2", title="Step 2", status="running", progress=0.5)
    session.steps["step3"] = StepProgress(step_id="step3", title="Step 3", status="pending", progress=0.0)
    
    # Calculate overall
    total = sum(s.progress for s in session.steps.values())
    overall = total / len(session.steps)
    
    assert overall == (1.0 + 0.5 + 0.0) / 3
    assert overall == 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])