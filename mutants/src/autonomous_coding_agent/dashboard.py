"""Dashboard/UI Server for Autonomous Coding Agent
실시간 진행률 시각화, 로그 스트리밍, 메트릭 대시보드
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import uvicorn
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

log = logging.getLogger("autonomous_coding_agent.dashboard")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁConnectionManagerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionManagerǁconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionManagerǁdisconnect__mutmut: MutantDict = {}  # type: ignore
mutants_xǁConnectionManagerǁbroadcast__mutmut: MutantDict = {}  # type: ignore


class ConnectionManager:
    """WebSocket 연결 관리"""

    @_mutmut_mutated(mutants_xǁConnectionManagerǁ__init____mutmut)
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    def xǁConnectionManagerǁ__init____mutmut_orig(self):
        self.active_connections: list[WebSocket] = []

    def xǁConnectionManagerǁ__init____mutmut_1(self):
        self.active_connections: list[WebSocket] = None

    @_mutmut_mutated(mutants_xǁConnectionManagerǁconnect__mutmut)
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def xǁConnectionManagerǁconnect__mutmut_orig(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def xǁConnectionManagerǁconnect__mutmut_1(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(None)

    @_mutmut_mutated(mutants_xǁConnectionManagerǁdisconnect__mutmut)
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    def xǁConnectionManagerǁdisconnect__mutmut_orig(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    def xǁConnectionManagerǁdisconnect__mutmut_1(self, websocket: WebSocket):
        if websocket not in self.active_connections:
            self.active_connections.remove(websocket)

    def xǁConnectionManagerǁdisconnect__mutmut_2(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(None)

    @_mutmut_mutated(mutants_xǁConnectionManagerǁbroadcast__mutmut)
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

    async def xǁConnectionManagerǁbroadcast__mutmut_orig(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = []
        for conn in self.active_connections:
            try:
                await conn.send_json(message)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(d)

    async def xǁConnectionManagerǁbroadcast__mutmut_1(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = None
        for conn in self.active_connections:
            try:
                await conn.send_json(message)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(d)

    async def xǁConnectionManagerǁbroadcast__mutmut_2(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = []
        for conn in self.active_connections:
            try:
                await conn.send_json(None)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(d)

    async def xǁConnectionManagerǁbroadcast__mutmut_3(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = []
        for conn in self.active_connections:
            try:
                await conn.send_json(message)
            except Exception:
                dead.append(None)
        for d in dead:
            self.disconnect(d)

    async def xǁConnectionManagerǁbroadcast__mutmut_4(self, message: dict[str, Any]):
        """모든 연결된 클라이언트에 메시지 브로드캐스트"""
        dead = []
        for conn in self.active_connections:
            try:
                await conn.send_json(message)
            except Exception:
                dead.append(conn)
        for d in dead:
            self.disconnect(None)

mutants_xǁConnectionManagerǁ__init____mutmut['_mutmut_orig'] = ConnectionManager.xǁConnectionManagerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁ__init____mutmut['xǁConnectionManagerǁ__init____mutmut_1'] = ConnectionManager.xǁConnectionManagerǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁConnectionManagerǁconnect__mutmut['_mutmut_orig'] = ConnectionManager.xǁConnectionManagerǁconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁconnect__mutmut['xǁConnectionManagerǁconnect__mutmut_1'] = ConnectionManager.xǁConnectionManagerǁconnect__mutmut_1 # type: ignore # mutmut generated

mutants_xǁConnectionManagerǁdisconnect__mutmut['_mutmut_orig'] = ConnectionManager.xǁConnectionManagerǁdisconnect__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁdisconnect__mutmut['xǁConnectionManagerǁdisconnect__mutmut_1'] = ConnectionManager.xǁConnectionManagerǁdisconnect__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁdisconnect__mutmut['xǁConnectionManagerǁdisconnect__mutmut_2'] = ConnectionManager.xǁConnectionManagerǁdisconnect__mutmut_2 # type: ignore # mutmut generated

mutants_xǁConnectionManagerǁbroadcast__mutmut['_mutmut_orig'] = ConnectionManager.xǁConnectionManagerǁbroadcast__mutmut_orig # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁbroadcast__mutmut['xǁConnectionManagerǁbroadcast__mutmut_1'] = ConnectionManager.xǁConnectionManagerǁbroadcast__mutmut_1 # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁbroadcast__mutmut['xǁConnectionManagerǁbroadcast__mutmut_2'] = ConnectionManager.xǁConnectionManagerǁbroadcast__mutmut_2 # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁbroadcast__mutmut['xǁConnectionManagerǁbroadcast__mutmut_3'] = ConnectionManager.xǁConnectionManagerǁbroadcast__mutmut_3 # type: ignore # mutmut generated
mutants_xǁConnectionManagerǁbroadcast__mutmut['xǁConnectionManagerǁbroadcast__mutmut_4'] = ConnectionManager.xǁConnectionManagerǁbroadcast__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDashboardServerǁ_create_app__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDashboardServerǁ_broadcast_update__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDashboardServerǁrun__mutmut: MutantDict = {}  # type: ignore


class DashboardServer:
    """대시보드 서버"""

    @_mutmut_mutated(mutants_xǁDashboardServerǁ__init____mutmut)
    def __init__(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_orig(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_1(self, host: str = "XX0.0.0.0XX", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_2(self, host: str = "0.0.0.0", port: int = 8900):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_3(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = None
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_4(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = None
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_5(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = None
        self.sessions: dict[str, SessionProgress] = {}
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_6(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = None
        self.app = self._create_app()

    def xǁDashboardServerǁ__init____mutmut_7(self, host: str = "0.0.0.0", port: int = 8899):
        self.host = host
        self.port = port
        self.manager = ConnectionManager()
        self.sessions: dict[str, SessionProgress] = {}
        self.app = None

    @_mutmut_mutated(mutants_xǁDashboardServerǁ_create_app__mutmut)
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

    def xǁDashboardServerǁ_create_app__mutmut_orig(self) -> FastAPI:
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

    def xǁDashboardServerǁ_create_app__mutmut_1(self) -> FastAPI:
        app = None

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

    def xǁDashboardServerǁ_create_app__mutmut_2(self) -> FastAPI:
        app = FastAPI(title=None)

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

    def xǁDashboardServerǁ_create_app__mutmut_3(self) -> FastAPI:
        app = FastAPI(title="XXAutonomous Coding Agent DashboardXX")

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

    def xǁDashboardServerǁ_create_app__mutmut_4(self) -> FastAPI:
        app = FastAPI(title="autonomous coding agent dashboard")

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

    def xǁDashboardServerǁ_create_app__mutmut_5(self) -> FastAPI:
        app = FastAPI(title="AUTONOMOUS CODING AGENT DASHBOARD")

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

    def xǁDashboardServerǁ_create_app__mutmut_6(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = None
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

    def xǁDashboardServerǁ_create_app__mutmut_7(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent * "templates"
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

    def xǁDashboardServerǁ_create_app__mutmut_8(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(None).parent / "templates"
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

    def xǁDashboardServerǁ_create_app__mutmut_9(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "XXtemplatesXX"
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

    def xǁDashboardServerǁ_create_app__mutmut_10(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "TEMPLATES"
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

    def xǁDashboardServerǁ_create_app__mutmut_11(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=None)
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

    def xǁDashboardServerǁ_create_app__mutmut_12(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=False)
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

    def xǁDashboardServerǁ_create_app__mutmut_13(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = None
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

    def xǁDashboardServerǁ_create_app__mutmut_14(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent * "static"
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

    def xǁDashboardServerǁ_create_app__mutmut_15(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(None).parent / "static"
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

    def xǁDashboardServerǁ_create_app__mutmut_16(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "XXstaticXX"
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

    def xǁDashboardServerǁ_create_app__mutmut_17(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "STATIC"
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

    def xǁDashboardServerǁ_create_app__mutmut_18(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=None)

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

    def xǁDashboardServerǁ_create_app__mutmut_19(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=False)

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

    def xǁDashboardServerǁ_create_app__mutmut_20(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount(None, StaticFiles(directory=static_dir), name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_21(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", None, name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_22(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name=None)
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

    def xǁDashboardServerǁ_create_app__mutmut_23(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount(StaticFiles(directory=static_dir), name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_24(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_25(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), )
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

    def xǁDashboardServerǁ_create_app__mutmut_26(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("XX/staticXX", StaticFiles(directory=static_dir), name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_27(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/STATIC", StaticFiles(directory=static_dir), name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_28(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=None), name="static")
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

    def xǁDashboardServerǁ_create_app__mutmut_29(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name="XXstaticXX")
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

    def xǁDashboardServerǁ_create_app__mutmut_30(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name="STATIC")
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

    def xǁDashboardServerǁ_create_app__mutmut_31(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name="static")
        templates = None

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

    def xǁDashboardServerǁ_create_app__mutmut_32(self) -> FastAPI:
        app = FastAPI(title="Autonomous Coding Agent Dashboard")

        # 정적 파일 및 템플릿
        templates_dir = Path(__file__).parent / "templates"
        templates_dir.mkdir(exist_ok=True)
        static_dir = Path(__file__).parent / "static"
        static_dir.mkdir(exist_ok=True)

        app.mount("/static", StaticFiles(directory=static_dir), name="static")
        templates = Jinja2Templates(directory=None)

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

    @_mutmut_mutated(mutants_xǁDashboardServerǁ_update_overall_progress__mutmut)
    def _update_overall_progress(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_orig(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_1(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_2(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = None
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_3(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 1.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_4(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = None
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_5(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(None)
        session.overall_progress = total / len(session.steps)

    def xǁDashboardServerǁ_update_overall_progress__mutmut_6(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = None

    def xǁDashboardServerǁ_update_overall_progress__mutmut_7(self, session: SessionProgress):
        """전체 진행률 업데이트"""
        if not session.steps:
            session.overall_progress = 0.0
            return
        total = sum(step.progress for step in session.steps.values())
        session.overall_progress = total * len(session.steps)

    @_mutmut_mutated(mutants_xǁDashboardServerǁ_broadcast_update__mutmut)
    async def _broadcast_update(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_orig(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_1(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id not in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_2(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = None
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_3(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                None
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_4(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "XXtypeXX": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_5(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "TYPE": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_6(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "XXsession_updateXX",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_7(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "SESSION_UPDATE",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_8(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "XXsession_idXX": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_9(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "SESSION_ID": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_10(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "XXdataXX": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_11(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "DATA": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_12(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "XXoverall_progressXX": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_13(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "OVERALL_PROGRESS": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_14(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "XXcurrent_stepXX": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_15(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "CURRENT_STEP": s.current_step,
                        "total_steps": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_16(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "XXtotal_stepsXX": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_17(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "TOTAL_STEPS": s.total_steps,
                        "status": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_18(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "XXstatusXX": s.status,
                    },
                }
            )

    async def xǁDashboardServerǁ_broadcast_update__mutmut_19(self, session_id: str):
        """세션 업데이트 브로드캐스트"""
        if session_id in self.sessions:
            s = self.sessions[session_id]
            await self.manager.broadcast(
                {
                    "type": "session_update",
                    "session_id": session_id,
                    "data": {
                        "overall_progress": s.overall_progress,
                        "current_step": s.current_step,
                        "total_steps": s.total_steps,
                        "STATUS": s.status,
                    },
                }
            )

    @_mutmut_mutated(mutants_xǁDashboardServerǁrun__mutmut)
    def run(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_orig(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_1(self):
        """서버 실행"""
        uvicorn.run(None, host=self.host, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_2(self):
        """서버 실행"""
        uvicorn.run(self.app, host=None, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_3(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=None, log_level="info")

    def xǁDashboardServerǁrun__mutmut_4(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level=None)

    def xǁDashboardServerǁrun__mutmut_5(self):
        """서버 실행"""
        uvicorn.run(host=self.host, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_6(self):
        """서버 실행"""
        uvicorn.run(self.app, port=self.port, log_level="info")

    def xǁDashboardServerǁrun__mutmut_7(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, log_level="info")

    def xǁDashboardServerǁrun__mutmut_8(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, )

    def xǁDashboardServerǁrun__mutmut_9(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="XXinfoXX")

    def xǁDashboardServerǁrun__mutmut_10(self):
        """서버 실행"""
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="INFO")

mutants_xǁDashboardServerǁ__init____mutmut['_mutmut_orig'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_1'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_2'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_3'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_4'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_5'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_6'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ__init____mutmut['xǁDashboardServerǁ__init____mutmut_7'] = DashboardServer.xǁDashboardServerǁ__init____mutmut_7 # type: ignore # mutmut generated

mutants_xǁDashboardServerǁ_create_app__mutmut['_mutmut_orig'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_1'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_2'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_3'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_4'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_5'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_6'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_7'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_8'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_9'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_10'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_11'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_12'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_13'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_14'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_15'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_16'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_17'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_18'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_19'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_20'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_21'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_22'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_23'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_24'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_25'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_26'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_26 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_27'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_27 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_28'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_28 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_29'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_29 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_30'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_30 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_31'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_31 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_create_app__mutmut['xǁDashboardServerǁ_create_app__mutmut_32'] = DashboardServer.xǁDashboardServerǁ_create_app__mutmut_32 # type: ignore # mutmut generated

mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['_mutmut_orig'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_1'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_2'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_3'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_4'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_5'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_6'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_update_overall_progress__mutmut['xǁDashboardServerǁ_update_overall_progress__mutmut_7'] = DashboardServer.xǁDashboardServerǁ_update_overall_progress__mutmut_7 # type: ignore # mutmut generated

mutants_xǁDashboardServerǁ_broadcast_update__mutmut['_mutmut_orig'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_1'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_2'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_3'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_4'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_5'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_6'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_7'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_8'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_9'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_10'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_11'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_12'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_13'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_14'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_15'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_16'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_17'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_18'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁ_broadcast_update__mutmut['xǁDashboardServerǁ_broadcast_update__mutmut_19'] = DashboardServer.xǁDashboardServerǁ_broadcast_update__mutmut_19 # type: ignore # mutmut generated

mutants_xǁDashboardServerǁrun__mutmut['_mutmut_orig'] = DashboardServer.xǁDashboardServerǁrun__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_1'] = DashboardServer.xǁDashboardServerǁrun__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_2'] = DashboardServer.xǁDashboardServerǁrun__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_3'] = DashboardServer.xǁDashboardServerǁrun__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_4'] = DashboardServer.xǁDashboardServerǁrun__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_5'] = DashboardServer.xǁDashboardServerǁrun__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_6'] = DashboardServer.xǁDashboardServerǁrun__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_7'] = DashboardServer.xǁDashboardServerǁrun__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_8'] = DashboardServer.xǁDashboardServerǁrun__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_9'] = DashboardServer.xǁDashboardServerǁrun__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDashboardServerǁrun__mutmut['xǁDashboardServerǁrun__mutmut_10'] = DashboardServer.xǁDashboardServerǁrun__mutmut_10 # type: ignore # mutmut generated


# 글로벌 대시보드 인스턴스
_dashboard: DashboardServer | None = None
mutants_x_get_dashboard__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_dashboard__mutmut)
def get_dashboard(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def x_get_dashboard__mutmut_orig(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def x_get_dashboard__mutmut_1(host: str = "XX0.0.0.0XX", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def x_get_dashboard__mutmut_2(host: str = "0.0.0.0", port: int = 8900) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def x_get_dashboard__mutmut_3(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is not None:
        _dashboard = DashboardServer(host, port)
    return _dashboard


def x_get_dashboard__mutmut_4(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = None
    return _dashboard


def x_get_dashboard__mutmut_5(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(None, port)
    return _dashboard


def x_get_dashboard__mutmut_6(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, None)
    return _dashboard


def x_get_dashboard__mutmut_7(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(port)
    return _dashboard


def x_get_dashboard__mutmut_8(host: str = "0.0.0.0", port: int = 8899) -> DashboardServer:
    """싱글톤 대시보드 인스턴스 반환"""
    global _dashboard
    if _dashboard is None:
        _dashboard = DashboardServer(host, )
    return _dashboard

mutants_x_get_dashboard__mutmut['_mutmut_orig'] = x_get_dashboard__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_1'] = x_get_dashboard__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_2'] = x_get_dashboard__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_3'] = x_get_dashboard__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_4'] = x_get_dashboard__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_5'] = x_get_dashboard__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_6'] = x_get_dashboard__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_7'] = x_get_dashboard__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_dashboard__mutmut['x_get_dashboard__mutmut_8'] = x_get_dashboard__mutmut_8 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_start_dashboard__mutmut)
def start_dashboard(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_orig(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_1(host: str = "XX0.0.0.0XX", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_2(host: str = "0.0.0.0", port: int = 8900):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_3(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = None
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_4(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(None, port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_5(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, None)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_6(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(port)
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_7(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, )
    thread = threading.Thread(target=dashboard.run, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_8(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = None
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_9(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=None, daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_10(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=None)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_11(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(daemon=True)
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_12(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, )
    thread.start()
    return dashboard


def x_start_dashboard__mutmut_13(host: str = "0.0.0.0", port: int = 8899):
    """대시보드 서버 시작 (백그라운드)"""
    import threading

    dashboard = get_dashboard(host, port)
    thread = threading.Thread(target=dashboard.run, daemon=False)
    thread.start()
    return dashboard

mutants_x_start_dashboard__mutmut['_mutmut_orig'] = x_start_dashboard__mutmut_orig # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_1'] = x_start_dashboard__mutmut_1 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_2'] = x_start_dashboard__mutmut_2 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_3'] = x_start_dashboard__mutmut_3 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_4'] = x_start_dashboard__mutmut_4 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_5'] = x_start_dashboard__mutmut_5 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_6'] = x_start_dashboard__mutmut_6 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_7'] = x_start_dashboard__mutmut_7 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_8'] = x_start_dashboard__mutmut_8 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_9'] = x_start_dashboard__mutmut_9 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_10'] = x_start_dashboard__mutmut_10 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_11'] = x_start_dashboard__mutmut_11 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_12'] = x_start_dashboard__mutmut_12 # type: ignore # mutmut generated
mutants_x_start_dashboard__mutmut['x_start_dashboard__mutmut_13'] = x_start_dashboard__mutmut_13 # type: ignore # mutmut generated
