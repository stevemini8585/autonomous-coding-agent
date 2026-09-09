"""
자율 코딩 에이전트 - 상태 관리 (State)
"""

from __future__ import annotations

import json
import logging
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from .models import AgentState, ExploreResult, Plan, PlanStep, StepStatus

log = logging.getLogger("autonomous_coding_agent.state")


class StateManager:
    """에이전트 상태 영구 저장 및 복원"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def save_state(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def load_state(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def list_sessions(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "goal": data.get("goal"),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def delete_session(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir / f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return True
        return False

    def create_checkpoint(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "checkpoint_id": checkpoint_id,
                "label": label,
                "created_at": datetime.now().isoformat(),
                "state": self._serialize_state(state),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def rollback_to_checkpoint(self, state: AgentState, checkpoint_id: str) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(f)

            restored = self._deserialize_state(data["state"])
            # 상태 복원
            state.plan = restored.plan
            state.explore_result = restored.explore_result
            state.current_step_id = restored.current_step_id
            state.iteration = restored.iteration

            log.info(f"롤백 완료: {checkpoint_id}")
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def list_checkpoints(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def _serialize_state(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "current_step_id": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def _serialize_plan(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "title": s.title,
                    "description": s.description,
                    "dependencies": s.dependencies,
                    "status": s.status.value,
                    "assigned_files": s.assigned_files,
                    "expected_outputs": s.expected_outputs,
                    "verification_criteria": s.verification_criteria,
                    "max_retries": s.max_retries,
                    "retry_count": s.retry_count,
                    "started_at": s.started_at.isoformat() if s.started_at else None,
                    "completed_at": s.completed_at.isoformat() if s.completed_at else None,
                    "error": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def _serialize_explore(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "line_start": s.line_start,
                    "line_end": s.line_end,
                    "signature": s.signature,
                    "docstring": s.docstring,
                    "references": s.references,
                }
                for s in explore.symbols
            ],
            "files": [
                {
                    "path": f.path,
                    "language": f.language,
                    "size": f.size,
                    "lines": f.lines,
                    "imports": f.imports,
                    "exports": f.exports,
                }
                for f in explore.files
            ],
            "import_graph": explore.import_graph,
            "call_graph": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def _deserialize_state(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("current_step_id"),
        )

        if data.get("started_at"):
            state.started_at = datetime.fromisoformat(data["started_at"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def _deserialize_plan(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["title"],
                description=s_data["description"],
                dependencies=s_data["dependencies"],
                status=StepStatus(s_data["status"]),
                assigned_files=s_data["assigned_files"],
                expected_outputs=s_data["expected_outputs"],
                verification_criteria=s_data["verification_criteria"],
                max_retries=s_data["max_retries"],
                retry_count=s_data["retry_count"],
                error=s_data["error"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def _deserialize_explore(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore


def get_state_manager(workspace: Path) -> StateManager:
    """상태 관리자 헬퍼"""
    return StateManager(workspace)
