"""Dashboard/UI Server for Autonomous Coding Agent
실시간 진행률 시각화, 로그 스트리밍, 메트릭 대시보드
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any
from collections import defaultdict

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

log = logging.getLogger("autonomous_coding_agent.dashboard")


@dataclass
class StepProgress:
    """단계별 진행 상태"""
    step_id: str
    title: str
    status: str  # pending, running, completed, failed
    progress: float = 0.0  # 0.0 ~ 1.0
    start_time: float | None = None
    end_time: float | None = None
    logs: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)


@dataclass
class SessionProgress:
    """세션 전체 진행 상태"""
    session_id: str
    goal: str
    status: str  # running, completed, failed
    current_step: int = 0
    total_steps: int = 0
    steps: dict[str, StepProgress] = field(default_factory=dict)
    start_time: float = field(default_factory=time.time)
    end_time: float | None = None
    overall_progress: float = 0.0
    metrics: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """직렬화용 딕셔너리"""
        return {
            "session_id": self.session_id,
            "goal": self.goal,
            "status": self.status,
            "current_step": self.current_step,
            "total_steps": self.total_steps,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "overall_progress": self.overall_progress,
            "metrics": self.metrics,
        }


class ConnectionManager:
    """WebSocket 연결 관리"""

    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = []
        for conn in self.active_connections:
            try:
                await conn.send_json(message)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(d)


class DashboardServer:
    """대시보드 서버"""

    def __init__(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def _create_app(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name="static")
        templates = Jinja2Templates(directory=templates_dir)

        @app.get("/", response_class=HTMLResponse)
        async def index(request: Request):
            return templates.TemplateResponse("dashboard.html", {"request": request})

        @app.get("/api/sessions")
        async def list_sessions():
            return {
                "sessions": [
                    {
                        "session_id": s.session_id,
                        "goal": s.goal,
                        "status": s.status,
                        "progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "start_time": s.start_time,
                        "end_time": s.end_time,
                    }
                    for s in self.sessions.values()
                ]
            }

        @app.get("/api/sessions/{session_id}")
        async def get_session(session_id: str):
            if session_id not in self.sessions:
                return {"error": "Session not found"}, 404
            s = self.sessions[session_id]
            return {
                "session_id": s.session_id,
                "goal": s.goal,
                "status": s.status,
                "overall_progress": s.overall_progress,
                "current_step": s.current_step,
                "total_steps": s.total_steps,
                "start_time": s.start_time,
                "end_time": s.end_time,
                "steps": {
                    k: {
                        "step_id": v.step_id,
                        "title": v.title,
                        "status": v.status,
                        "progress": v.progress,
                        "start_time": v.start_time,
                        "end_time": v.end_time,
                        "logs": v.logs[-50:],  # 최근 50개만
                        "metrics": v.metrics,
                    }
                    for k, v in s.steps.items()
                },
                "metrics": s.metrics,
            }

        @app.post("/api/sessions/{session_id}/start")
        async def start_session(session_id: str, data: dict):
            session = SessionProgress(
                session_id=session_id,
                goal=data.get("goal", ""),
                status="running",
                total_steps=data.get("total_steps", 0),
            )
            self.sessions[session_id] = session
            await self.manager.broadcast({"type": "session_started", "session": session_id})
            return {"status": "started"}

        @app.post("/api/sessions/{session_id}/step/{step_id}/start")
        async def start_step(session_id: str, step_id: str, data: dict):
            if session_id not in self.sessions:
                return {"error": "Session not found"}, 404
            s = self.sessions[session_id]
            step = StepProgress(
                step_id=step_id,
                title=data.get("title", step_id),
                status="running",
                start_time=time.time(),
            )
            s.steps[step_id] = step
            s.current_step += 1
            await self._broadcast_update(session_id)
            return {"status": "started"}

        @app.post("/api/sessions/{session_id}/step/{step_id}/progress")
        async def update_step_progress(session_id: str, step_id: str, data: dict):
            if session_id not in self.sessions:
                return {"error": "Session not found"}, 404
            s = self.sessions[session_id]
            if step_id not in s.steps:
                return {"error": "Step not found"}, 404
            step = s.steps[step_id]
            step.progress = data.get("progress", step.progress)
            if "log" in data:
                step.logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] {data['log']}")
            if "metrics" in data:
                step.metrics.update(data["metrics"])
            self._update_overall_progress(s)
            await self._broadcast_update(session_id)
            return {"status": "updated"}

        @app.post("/api/sessions/{session_id}/step/{step_id}/complete")
        async def complete_step(session_id: str, step_id: str, data: dict):
            if session_id not in self.sessions:
                return {"error": "Session not found"}, 404
            s = self.sessions[session_id]
            if step_id not in s.steps:
                return {"error": "Step not found"}, 404
            step = s.steps[step_id]
            step.status = data.get("status", "completed")
            step.progress = 1.0
            step.end_time = time.time()
            if "metrics" in data:
                step.metrics.update(data["metrics"])
            self._update_overall_progress(s)
            await self._broadcast_update(session_id)
            return {"status": "completed"}

        @app.post("/api/sessions/{session_id}/complete")
        async def complete_session(session_id: str, data: dict):
            if session_id not in self.sessions:
                return {"error": "Session not found"}, 404
            s = self.sessions[session_id]
            s.status = data.get("status", "completed")
            s.end_time = time.time()
            s.overall_progress = 1.0
            if "metrics" in data:
                s.metrics.update(data["metrics"])
            await self._broadcast_update(session_id)
            return {"status": "completed"}

        @app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await self.manager.connect(websocket)
            try:
                while True:
                    await websocket.receive_text()
            except WebSocketDisconnect:
                self.manager.disconnect(websocket)

        return app

    def _update_overall_progress(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    async def _broadcast_update(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast({
                "type": "session_update",
                "session_id": session_id,
                "data": {
                    "overall_progress": s.overall_progress,
                    "current_step": s.current_step,
                    "total_steps": s.total_steps,
                    "status": s.status,
                }
            })

    def run(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="info")


# 글로벌 대시보드 인스턴스
_dashboard: DashboardServer | None = None


def get_dashboard(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def start_dashboard(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading
    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard