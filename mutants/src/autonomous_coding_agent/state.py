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


from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated

mutants_xǁStateManagerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁsave_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁload_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁlist_sessions__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁdelete_session__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁcreate_checkpoint__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁlist_checkpoints__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_serialize_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_serialize_plan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_serialize_explore__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_deserialize_state__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_deserialize_plan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁStateManagerǁ_deserialize_explore__mutmut: MutantDict = {}  # type: ignore


class StateManager:
    """에이전트 상태 영구 저장 및 복원"""

    @_mutmut_mutated(mutants_xǁStateManagerǁ__init____mutmut)
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_orig(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_1(self, workspace: Path):
        self.workspace = None
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_2(self, workspace: Path):
        self.workspace = Path(None).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_3(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = None
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_4(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace * ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_5(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / "XX.autonomous_stateXX"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_6(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".AUTONOMOUS_STATE"
        self.state_dir.mkdir(parents=True, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_7(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=None, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_8(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=None)

    def xǁStateManagerǁ__init____mutmut_9(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_10(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(
            parents=True,
        )

    def xǁStateManagerǁ__init____mutmut_11(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=False, exist_ok=True)

    def xǁStateManagerǁ__init____mutmut_12(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.state_dir = self.workspace / ".autonomous_state"
        self.state_dir.mkdir(parents=True, exist_ok=False)

    @_mutmut_mutated(mutants_xǁStateManagerǁsave_state__mutmut)
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

    def xǁStateManagerǁsave_state__mutmut_orig(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_1(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = None
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_2(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = None

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_3(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir * f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_4(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(None, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_5(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, None, encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_6(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding=None) as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_7(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open("w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_8(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_9(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(
                state_file,
                "w",
            ) as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_10(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "XXwXX", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_11(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "W", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_12(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="XXutf-8XX") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_13(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="UTF-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_14(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(None, f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_15(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), None, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_16(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=None, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_17(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=None)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_18(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_19(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_20(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_21(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(
                    self._serialize_state(state),
                    f,
                    ensure_ascii=False,
                )
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_22(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(None), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_23(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=True, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_24(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=3)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_25(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(None)
        except Exception as e:
            log.error(f"상태 저장 실패: {e}")

    def xǁStateManagerǁsave_state__mutmut_26(self, state: AgentState) -> None:
        """상태 저장"""
        state.updated_at = datetime.now()
        state_file = self.state_dir / f"{state.session_id}.json"

        try:
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(self._serialize_state(state), f, ensure_ascii=False, indent=2)
            log.debug(f"상태 저장: {state_file}")
        except Exception as e:
            log.error(None)

    @_mutmut_mutated(mutants_xǁStateManagerǁload_state__mutmut)
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

    def xǁStateManagerǁload_state__mutmut_orig(self, session_id: str) -> AgentState | None:
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

    def xǁStateManagerǁload_state__mutmut_1(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = None

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_2(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir * f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_3(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_4(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(None, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_5(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding=None) as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_6(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_7(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(
                state_file,
            ) as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_8(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="XXutf-8XX") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_9(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="UTF-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_10(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = None
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_11(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(None)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_12(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(None)
        except Exception as e:
            log.error(f"상태 로드 실패: {e}")
            return None

    def xǁStateManagerǁload_state__mutmut_13(self, session_id: str) -> AgentState | None:
        """상태 로드"""
        state_file = self.state_dir / f"{session_id}.json"

        if not state_file.exists():
            return None

        try:
            with open(state_file, encoding="utf-8") as f:
                data = json.load(f)
            return self._deserialize_state(data)
        except Exception as e:
            log.error(None)
            return None

    @_mutmut_mutated(mutants_xǁStateManagerǁlist_sessions__mutmut)
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

    def xǁStateManagerǁlist_sessions__mutmut_orig(self) -> list[dict[str, Any]]:
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

    def xǁStateManagerǁlist_sessions__mutmut_1(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = None
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

    def xǁStateManagerǁlist_sessions__mutmut_2(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob(None):
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

    def xǁStateManagerǁlist_sessions__mutmut_3(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("XX*.jsonXX"):
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

    def xǁStateManagerǁlist_sessions__mutmut_4(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.JSON"):
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

    def xǁStateManagerǁlist_sessions__mutmut_5(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(None, encoding="utf-8") as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_6(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding=None) as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_7(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(encoding="utf-8") as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_8(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(
                    state_file,
                ) as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_9(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="XXutf-8XX") as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_10(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="UTF-8") as f:
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

    def xǁStateManagerǁlist_sessions__mutmut_11(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = None
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

    def xǁStateManagerǁlist_sessions__mutmut_12(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(None)
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

    def xǁStateManagerǁlist_sessions__mutmut_13(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(None)
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_14(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "XXsession_idXX": data.get("session_id"),
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

    def xǁStateManagerǁlist_sessions__mutmut_15(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "SESSION_ID": data.get("session_id"),
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

    def xǁStateManagerǁlist_sessions__mutmut_16(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get(None),
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

    def xǁStateManagerǁlist_sessions__mutmut_17(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("XXsession_idXX"),
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

    def xǁStateManagerǁlist_sessions__mutmut_18(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("SESSION_ID"),
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

    def xǁStateManagerǁlist_sessions__mutmut_19(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "XXgoalXX": data.get("goal"),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_20(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "GOAL": data.get("goal"),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_21(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "goal": data.get(None),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_22(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "goal": data.get("XXgoalXX"),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_23(self) -> list[dict[str, Any]]:
        """세션 목록"""
        sessions = []
        for state_file in self.state_dir.glob("*.json"):
            try:
                with open(state_file, encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append(
                    {
                        "session_id": data.get("session_id"),
                        "goal": data.get("GOAL"),
                        "iteration": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_24(self) -> list[dict[str, Any]]:
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
                        "XXiterationXX": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_25(self) -> list[dict[str, Any]]:
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
                        "ITERATION": data.get("iteration", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_26(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get(None, 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_27(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get("iteration", None),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_28(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get(0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_29(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get(
                            "iteration",
                        ),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_30(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get("XXiterationXX", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_31(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get("ITERATION", 0),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_32(self) -> list[dict[str, Any]]:
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
                        "iteration": data.get("iteration", 1),
                        "started_at": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_33(self) -> list[dict[str, Any]]:
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
                        "XXstarted_atXX": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_34(self) -> list[dict[str, Any]]:
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
                        "STARTED_AT": data.get("started_at"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_35(self) -> list[dict[str, Any]]:
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
                        "started_at": data.get(None),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_36(self) -> list[dict[str, Any]]:
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
                        "started_at": data.get("XXstarted_atXX"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_37(self) -> list[dict[str, Any]]:
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
                        "started_at": data.get("STARTED_AT"),
                        "updated_at": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_38(self) -> list[dict[str, Any]]:
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
                        "XXupdated_atXX": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_39(self) -> list[dict[str, Any]]:
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
                        "UPDATED_AT": data.get("updated_at"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_40(self) -> list[dict[str, Any]]:
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
                        "updated_at": data.get(None),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_41(self) -> list[dict[str, Any]]:
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
                        "updated_at": data.get("XXupdated_atXX"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_42(self) -> list[dict[str, Any]]:
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
                        "updated_at": data.get("UPDATED_AT"),
                        "current_step": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_43(self) -> list[dict[str, Any]]:
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
                        "XXcurrent_stepXX": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_44(self) -> list[dict[str, Any]]:
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
                        "CURRENT_STEP": data.get("current_step_id"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_45(self) -> list[dict[str, Any]]:
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
                        "current_step": data.get(None),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_46(self) -> list[dict[str, Any]]:
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
                        "current_step": data.get("XXcurrent_step_idXX"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_47(self) -> list[dict[str, Any]]:
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
                        "current_step": data.get("CURRENT_STEP_ID"),
                    }
                )
            except Exception:
                pass
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_48(self) -> list[dict[str, Any]]:
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
        return sorted(None, key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_49(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=None, reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_50(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=None)

    def xǁStateManagerǁlist_sessions__mutmut_51(self) -> list[dict[str, Any]]:
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
        return sorted(key=lambda x: x.get("updated_at", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_52(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_53(self) -> list[dict[str, Any]]:
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
        return sorted(
            sessions,
            key=lambda x: x.get("updated_at", ""),
        )

    def xǁStateManagerǁlist_sessions__mutmut_54(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: None, reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_55(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get(None, ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_56(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("updated_at", None), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_57(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get(""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_58(self) -> list[dict[str, Any]]:
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
        return sorted(
            sessions,
            key=lambda x: x.get(
                "updated_at",
            ),
            reverse=True,
        )

    def xǁStateManagerǁlist_sessions__mutmut_59(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("XXupdated_atXX", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_60(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("UPDATED_AT", ""), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_61(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("updated_at", "XXXX"), reverse=True)

    def xǁStateManagerǁlist_sessions__mutmut_62(self) -> list[dict[str, Any]]:
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
        return sorted(sessions, key=lambda x: x.get("updated_at", ""), reverse=False)

    @_mutmut_mutated(mutants_xǁStateManagerǁdelete_session__mutmut)
    def delete_session(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir / f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return True
        return False

    def xǁStateManagerǁdelete_session__mutmut_orig(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir / f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return True
        return False

    def xǁStateManagerǁdelete_session__mutmut_1(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = None
        if state_file.exists():
            state_file.unlink()
            return True
        return False

    def xǁStateManagerǁdelete_session__mutmut_2(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir * f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return True
        return False

    def xǁStateManagerǁdelete_session__mutmut_3(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir / f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return False
        return False

    def xǁStateManagerǁdelete_session__mutmut_4(self, session_id: str) -> bool:
        """세션 삭제"""
        state_file = self.state_dir / f"{session_id}.json"
        if state_file.exists():
            state_file.unlink()
            return True
        return True

    @_mutmut_mutated(mutants_xǁStateManagerǁcreate_checkpoint__mutmut)
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_orig(
        self, state: AgentState, label: str = ""
    ) -> str:
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_1(
        self, state: AgentState, label: str = "XXXX"
    ) -> str:
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_2(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = None
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_3(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:9]}"
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_4(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = None

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

    def xǁStateManagerǁcreate_checkpoint__mutmut_5(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = None

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

    def xǁStateManagerǁcreate_checkpoint__mutmut_6(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir * f"{state.session_id}_{checkpoint_id}.json"

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

    def xǁStateManagerǁcreate_checkpoint__mutmut_7(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = None
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_8(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "XXcheckpoint_idXX": checkpoint_id,
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_9(self, state: AgentState, label: str = "") -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "CHECKPOINT_ID": checkpoint_id,
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_10(
        self, state: AgentState, label: str = ""
    ) -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "checkpoint_id": checkpoint_id,
                "XXlabelXX": label,
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_11(
        self, state: AgentState, label: str = ""
    ) -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "checkpoint_id": checkpoint_id,
                "LABEL": label,
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

    def xǁStateManagerǁcreate_checkpoint__mutmut_12(
        self, state: AgentState, label: str = ""
    ) -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "checkpoint_id": checkpoint_id,
                "label": label,
                "XXcreated_atXX": datetime.now().isoformat(),
                "state": self._serialize_state(state),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_13(
        self, state: AgentState, label: str = ""
    ) -> str:
        """체크포인트 생성 (롤백용)"""
        checkpoint_id = f"checkpoint_{uuid.uuid4().hex[:8]}"
        if label:
            checkpoint_id = f"{checkpoint_id}_{label}"

        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        try:
            checkpoint_data = {
                "checkpoint_id": checkpoint_id,
                "label": label,
                "CREATED_AT": datetime.now().isoformat(),
                "state": self._serialize_state(state),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_14(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                "XXstateXX": self._serialize_state(state),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_15(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                "STATE": self._serialize_state(state),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_16(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                "state": self._serialize_state(None),
            }
            with open(checkpoint_file, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_17(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(None, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_18(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, None, encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_19(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, "w", encoding=None) as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_20(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open("w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_21(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_22(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(
                checkpoint_file,
                "w",
            ) as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_23(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, "XXwXX", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_24(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, "W", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_25(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, "w", encoding="XXutf-8XX") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_26(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            with open(checkpoint_file, "w", encoding="UTF-8") as f:
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_27(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(None, f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_28(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, None, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_29(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, f, ensure_ascii=None, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_30(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=None)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_31(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(f, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_32(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, ensure_ascii=False, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_33(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, f, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_34(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(
                    checkpoint_data,
                    f,
                    ensure_ascii=False,
                )
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_35(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, f, ensure_ascii=True, indent=2)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_36(
        self, state: AgentState, label: str = ""
    ) -> str:
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
                json.dump(checkpoint_data, f, ensure_ascii=False, indent=3)
            log.info(f"체크포인트 생성: {checkpoint_id}")
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_37(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            log.info(None)
            return checkpoint_id
        except Exception as e:
            log.error(f"체크포인트 생성 실패: {e}")
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_38(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            log.error(None)
            return ""

    def xǁStateManagerǁcreate_checkpoint__mutmut_39(
        self, state: AgentState, label: str = ""
    ) -> str:
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
            return "XXXX"

    @_mutmut_mutated(mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut)
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_orig(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_1(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = None

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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_2(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir * f"{state.session_id}_{checkpoint_id}.json"

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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_3(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if checkpoint_file.exists():
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_4(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(None)
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_5(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return True

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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_6(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(None, encoding="utf-8") as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_7(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding=None) as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_8(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(encoding="utf-8") as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_9(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(
                checkpoint_file,
            ) as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_10(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="XXutf-8XX") as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_11(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="UTF-8") as f:
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_12(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = None

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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_13(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(None)

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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_14(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(f)

            restored = None
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_15(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(f)

            restored = self._deserialize_state(None)
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_16(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(f)

            restored = self._deserialize_state(data["XXstateXX"])
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_17(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
        """체크포인트로 롤백"""
        checkpoint_file = self.state_dir / f"{state.session_id}_{checkpoint_id}.json"

        if not checkpoint_file.exists():
            log.error(f"체크포인트 없음: {checkpoint_id}")
            return False

        try:
            with open(checkpoint_file, encoding="utf-8") as f:
                data = json.load(f)

            restored = self._deserialize_state(data["STATE"])
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

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_18(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            state.plan = None
            state.explore_result = restored.explore_result
            state.current_step_id = restored.current_step_id
            state.iteration = restored.iteration

            log.info(f"롤백 완료: {checkpoint_id}")
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_19(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            state.explore_result = None
            state.current_step_id = restored.current_step_id
            state.iteration = restored.iteration

            log.info(f"롤백 완료: {checkpoint_id}")
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_20(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            state.current_step_id = None
            state.iteration = restored.iteration

            log.info(f"롤백 완료: {checkpoint_id}")
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_21(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            state.iteration = None

            log.info(f"롤백 완료: {checkpoint_id}")
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_22(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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

            log.info(None)
            return True
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_23(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            return False
        except Exception as e:
            log.error(f"롤백 실패: {e}")
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_24(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            log.error(None)
            return False

    def xǁStateManagerǁrollback_to_checkpoint__mutmut_25(
        self, state: AgentState, checkpoint_id: str
    ) -> bool:
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
            return True

    @_mutmut_mutated(mutants_xǁStateManagerǁlist_checkpoints__mutmut)
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

    def xǁStateManagerǁlist_checkpoints__mutmut_orig(self, session_id: str) -> list[dict[str, Any]]:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_1(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = None
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

    def xǁStateManagerǁlist_checkpoints__mutmut_2(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(None):
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

    def xǁStateManagerǁlist_checkpoints__mutmut_3(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(None, encoding="utf-8") as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_4(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding=None) as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_5(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(encoding="utf-8") as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_6(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(
                    cp_file,
                ) as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_7(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="XXutf-8XX") as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_8(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="UTF-8") as f:
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

    def xǁStateManagerǁlist_checkpoints__mutmut_9(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = None
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

    def xǁStateManagerǁlist_checkpoints__mutmut_10(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(None)
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

    def xǁStateManagerǁlist_checkpoints__mutmut_11(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(None)
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_12(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "XXcheckpoint_idXX": data.get("checkpoint_id"),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_13(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "CHECKPOINT_ID": data.get("checkpoint_id"),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_14(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get(None),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_15(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("XXcheckpoint_idXX"),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_16(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("CHECKPOINT_ID"),
                        "label": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_17(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "XXlabelXX": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_18(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "LABEL": data.get("label", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_19(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get(None, ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_20(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get("label", None),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_21(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get(""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_22(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get(
                            "label",
                        ),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_23(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get("XXlabelXX", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_24(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get("LABEL", ""),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_25(self, session_id: str) -> list[dict[str, Any]]:
        """체크포인트 목록"""
        checkpoints = []
        for cp_file in self.state_dir.glob(f"{session_id}_checkpoint_*.json"):
            try:
                with open(cp_file, encoding="utf-8") as f:
                    data = json.load(f)
                checkpoints.append(
                    {
                        "checkpoint_id": data.get("checkpoint_id"),
                        "label": data.get("label", "XXXX"),
                        "created_at": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_26(self, session_id: str) -> list[dict[str, Any]]:
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
                        "XXcreated_atXX": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_27(self, session_id: str) -> list[dict[str, Any]]:
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
                        "CREATED_AT": data.get("created_at"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_28(self, session_id: str) -> list[dict[str, Any]]:
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
                        "created_at": data.get(None),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_29(self, session_id: str) -> list[dict[str, Any]]:
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
                        "created_at": data.get("XXcreated_atXX"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_30(self, session_id: str) -> list[dict[str, Any]]:
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
                        "created_at": data.get("CREATED_AT"),
                    }
                )
            except Exception:
                pass
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_31(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(None, key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_32(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=None, reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_33(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=None)

    def xǁStateManagerǁlist_checkpoints__mutmut_34(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(key=lambda x: x.get("created_at", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_35(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_36(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(
            checkpoints,
            key=lambda x: x.get("created_at", ""),
        )

    def xǁStateManagerǁlist_checkpoints__mutmut_37(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: None, reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_38(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get(None, ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_39(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("created_at", None), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_40(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get(""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_41(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(
            checkpoints,
            key=lambda x: x.get(
                "created_at",
            ),
            reverse=True,
        )

    def xǁStateManagerǁlist_checkpoints__mutmut_42(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("XXcreated_atXX", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_43(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("CREATED_AT", ""), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_44(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("created_at", "XXXX"), reverse=True)

    def xǁStateManagerǁlist_checkpoints__mutmut_45(self, session_id: str) -> list[dict[str, Any]]:
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
        return sorted(checkpoints, key=lambda x: x.get("created_at", ""), reverse=False)

    @_mutmut_mutated(mutants_xǁStateManagerǁ_serialize_state__mutmut)
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

    def xǁStateManagerǁ_serialize_state__mutmut_orig(self, state: AgentState) -> dict[str, Any]:
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

    def xǁStateManagerǁ_serialize_state__mutmut_1(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "XXsession_idXX": state.session_id,
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

    def xǁStateManagerǁ_serialize_state__mutmut_2(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "SESSION_ID": state.session_id,
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

    def xǁStateManagerǁ_serialize_state__mutmut_3(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "XXworkspaceXX": str(state.workspace),
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

    def xǁStateManagerǁ_serialize_state__mutmut_4(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "WORKSPACE": str(state.workspace),
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

    def xǁStateManagerǁ_serialize_state__mutmut_5(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(None),
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

    def xǁStateManagerǁ_serialize_state__mutmut_6(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "XXgoalXX": state.goal,
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

    def xǁStateManagerǁ_serialize_state__mutmut_7(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "GOAL": state.goal,
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

    def xǁStateManagerǁ_serialize_state__mutmut_8(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "XXiterationXX": state.iteration,
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

    def xǁStateManagerǁ_serialize_state__mutmut_9(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "ITERATION": state.iteration,
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

    def xǁStateManagerǁ_serialize_state__mutmut_10(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "XXmax_iterationsXX": state.max_iterations,
            "current_step_id": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_11(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "MAX_ITERATIONS": state.max_iterations,
            "current_step_id": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_12(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "XXcurrent_step_idXX": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_13(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "CURRENT_STEP_ID": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_14(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "current_step_id": state.current_step_id,
            "XXstarted_atXX": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_15(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "current_step_id": state.current_step_id,
            "STARTED_AT": state.started_at.isoformat() if state.started_at else None,
            "updated_at": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_16(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "current_step_id": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "XXupdated_atXX": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_17(self, state: AgentState) -> dict[str, Any]:
        """상태 직렬화"""
        return {
            "session_id": state.session_id,
            "workspace": str(state.workspace),
            "goal": state.goal,
            "iteration": state.iteration,
            "max_iterations": state.max_iterations,
            "current_step_id": state.current_step_id,
            "started_at": state.started_at.isoformat() if state.started_at else None,
            "UPDATED_AT": state.updated_at.isoformat() if state.updated_at else None,
            "plan": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_18(self, state: AgentState) -> dict[str, Any]:
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
            "XXplanXX": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_19(self, state: AgentState) -> dict[str, Any]:
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
            "PLAN": self._serialize_plan(state.plan) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_20(self, state: AgentState) -> dict[str, Any]:
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
            "plan": self._serialize_plan(None) if state.plan else None,
            "explore_result": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_21(self, state: AgentState) -> dict[str, Any]:
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
            "XXexplore_resultXX": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_22(self, state: AgentState) -> dict[str, Any]:
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
            "EXPLORE_RESULT": (
                self._serialize_explore(state.explore_result) if state.explore_result else None
            ),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_23(self, state: AgentState) -> dict[str, Any]:
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
            "explore_result": (self._serialize_explore(None) if state.explore_result else None),
            "checkpoints": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_24(self, state: AgentState) -> dict[str, Any]:
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
            "XXcheckpointsXX": state.checkpoints,
        }

    def xǁStateManagerǁ_serialize_state__mutmut_25(self, state: AgentState) -> dict[str, Any]:
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
            "CHECKPOINTS": state.checkpoints,
        }

    @_mutmut_mutated(mutants_xǁStateManagerǁ_serialize_plan__mutmut)
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

    def xǁStateManagerǁ_serialize_plan__mutmut_orig(self, plan: Plan) -> dict[str, Any]:
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

    def xǁStateManagerǁ_serialize_plan__mutmut_1(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "XXgoalXX": plan.goal,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_2(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "GOAL": plan.goal,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_3(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "XXstepsXX": [
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

    def xǁStateManagerǁ_serialize_plan__mutmut_4(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "STEPS": [
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

    def xǁStateManagerǁ_serialize_plan__mutmut_5(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "XXidXX": s.id,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_6(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "ID": s.id,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_7(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "XXtypeXX": s.type.value,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_8(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "TYPE": s.type.value,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_9(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "XXtitleXX": s.title,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_10(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "TITLE": s.title,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_11(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "title": s.title,
                    "XXdescriptionXX": s.description,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_12(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "title": s.title,
                    "DESCRIPTION": s.description,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_13(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "title": s.title,
                    "description": s.description,
                    "XXdependenciesXX": s.dependencies,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_14(self, plan: Plan) -> dict[str, Any]:
        """계획 직렬화"""
        return {
            "goal": plan.goal,
            "steps": [
                {
                    "id": s.id,
                    "type": s.type.value,
                    "title": s.title,
                    "description": s.description,
                    "DEPENDENCIES": s.dependencies,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_15(self, plan: Plan) -> dict[str, Any]:
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
                    "XXstatusXX": s.status.value,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_16(self, plan: Plan) -> dict[str, Any]:
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
                    "STATUS": s.status.value,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_17(self, plan: Plan) -> dict[str, Any]:
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
                    "XXassigned_filesXX": s.assigned_files,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_18(self, plan: Plan) -> dict[str, Any]:
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
                    "ASSIGNED_FILES": s.assigned_files,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_19(self, plan: Plan) -> dict[str, Any]:
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
                    "XXexpected_outputsXX": s.expected_outputs,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_20(self, plan: Plan) -> dict[str, Any]:
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
                    "EXPECTED_OUTPUTS": s.expected_outputs,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_21(self, plan: Plan) -> dict[str, Any]:
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
                    "XXverification_criteriaXX": s.verification_criteria,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_22(self, plan: Plan) -> dict[str, Any]:
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
                    "VERIFICATION_CRITERIA": s.verification_criteria,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_23(self, plan: Plan) -> dict[str, Any]:
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
                    "XXmax_retriesXX": s.max_retries,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_24(self, plan: Plan) -> dict[str, Any]:
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
                    "MAX_RETRIES": s.max_retries,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_25(self, plan: Plan) -> dict[str, Any]:
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
                    "XXretry_countXX": s.retry_count,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_26(self, plan: Plan) -> dict[str, Any]:
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
                    "RETRY_COUNT": s.retry_count,
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

    def xǁStateManagerǁ_serialize_plan__mutmut_27(self, plan: Plan) -> dict[str, Any]:
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
                    "XXstarted_atXX": s.started_at.isoformat() if s.started_at else None,
                    "completed_at": s.completed_at.isoformat() if s.completed_at else None,
                    "error": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_28(self, plan: Plan) -> dict[str, Any]:
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
                    "STARTED_AT": s.started_at.isoformat() if s.started_at else None,
                    "completed_at": s.completed_at.isoformat() if s.completed_at else None,
                    "error": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_29(self, plan: Plan) -> dict[str, Any]:
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
                    "XXcompleted_atXX": s.completed_at.isoformat() if s.completed_at else None,
                    "error": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_30(self, plan: Plan) -> dict[str, Any]:
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
                    "COMPLETED_AT": s.completed_at.isoformat() if s.completed_at else None,
                    "error": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_31(self, plan: Plan) -> dict[str, Any]:
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
                    "XXerrorXX": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_32(self, plan: Plan) -> dict[str, Any]:
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
                    "ERROR": s.error,
                    "artifacts": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_33(self, plan: Plan) -> dict[str, Any]:
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
                    "XXartifactsXX": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_34(self, plan: Plan) -> dict[str, Any]:
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
                    "ARTIFACTS": s.artifacts,
                }
                for s in plan.steps
            ],
            "created_at": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_35(self, plan: Plan) -> dict[str, Any]:
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
            "XXcreated_atXX": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_36(self, plan: Plan) -> dict[str, Any]:
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
            "CREATED_AT": plan.created_at.isoformat(),
            "updated_at": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_37(self, plan: Plan) -> dict[str, Any]:
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
            "XXupdated_atXX": plan.updated_at.isoformat(),
        }

    def xǁStateManagerǁ_serialize_plan__mutmut_38(self, plan: Plan) -> dict[str, Any]:
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
            "UPDATED_AT": plan.updated_at.isoformat(),
        }

    @_mutmut_mutated(mutants_xǁStateManagerǁ_serialize_explore__mutmut)
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

    def xǁStateManagerǁ_serialize_explore__mutmut_orig(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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

    def xǁStateManagerǁ_serialize_explore__mutmut_1(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "XXsymbolsXX": [
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

    def xǁStateManagerǁ_serialize_explore__mutmut_2(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "SYMBOLS": [
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

    def xǁStateManagerǁ_serialize_explore__mutmut_3(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "XXnameXX": s.name,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_4(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "NAME": s.name,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_5(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "XXtypeXX": s.type,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_6(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "TYPE": s.type,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_7(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "XXfile_pathXX": s.file_path,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_8(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "FILE_PATH": s.file_path,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_9(self, explore: ExploreResult) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "XXline_startXX": s.line_start,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_10(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "LINE_START": s.line_start,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_11(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "line_start": s.line_start,
                    "XXline_endXX": s.line_end,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_12(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "line_start": s.line_start,
                    "LINE_END": s.line_end,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_13(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "line_start": s.line_start,
                    "line_end": s.line_end,
                    "XXsignatureXX": s.signature,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_14(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
        """탐색 결과 직렬화"""
        return {
            "symbols": [
                {
                    "name": s.name,
                    "type": s.type,
                    "file_path": s.file_path,
                    "line_start": s.line_start,
                    "line_end": s.line_end,
                    "SIGNATURE": s.signature,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_15(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXdocstringXX": s.docstring,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_16(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "DOCSTRING": s.docstring,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_17(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXreferencesXX": s.references,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_18(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "REFERENCES": s.references,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_19(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXfilesXX": [
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

    def xǁStateManagerǁ_serialize_explore__mutmut_20(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "FILES": [
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

    def xǁStateManagerǁ_serialize_explore__mutmut_21(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXpathXX": f.path,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_22(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "PATH": f.path,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_23(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXlanguageXX": f.language,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_24(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "LANGUAGE": f.language,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_25(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXsizeXX": f.size,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_26(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "SIZE": f.size,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_27(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXlinesXX": f.lines,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_28(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "LINES": f.lines,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_29(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXimportsXX": f.imports,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_30(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "IMPORTS": f.imports,
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

    def xǁStateManagerǁ_serialize_explore__mutmut_31(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "XXexportsXX": f.exports,
                }
                for f in explore.files
            ],
            "import_graph": explore.import_graph,
            "call_graph": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_32(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
                    "EXPORTS": f.exports,
                }
                for f in explore.files
            ],
            "import_graph": explore.import_graph,
            "call_graph": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_33(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXimport_graphXX": explore.import_graph,
            "call_graph": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_34(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "IMPORT_GRAPH": explore.import_graph,
            "call_graph": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_35(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXcall_graphXX": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_36(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "CALL_GRAPH": explore.call_graph,
            "entry_points": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_37(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXentry_pointsXX": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_38(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "ENTRY_POINTS": explore.entry_points,
            "config_files": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_39(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXconfig_filesXX": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_40(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "CONFIG_FILES": explore.config_files,
            "test_files": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_41(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "XXtest_filesXX": explore.test_files,
        }

    def xǁStateManagerǁ_serialize_explore__mutmut_42(
        self, explore: ExploreResult
    ) -> dict[str, Any]:
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
            "TEST_FILES": explore.test_files,
        }

    @_mutmut_mutated(mutants_xǁStateManagerǁ_deserialize_state__mutmut)
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

    def xǁStateManagerǁ_deserialize_state__mutmut_orig(self, data: dict[str, Any]) -> AgentState:
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

    def xǁStateManagerǁ_deserialize_state__mutmut_1(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = None

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

    def xǁStateManagerǁ_deserialize_state__mutmut_2(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_3(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_4(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_5(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_6(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_7(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=None,
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

    def xǁStateManagerǁ_deserialize_state__mutmut_8(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
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

    def xǁStateManagerǁ_deserialize_state__mutmut_9(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_10(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_11(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_12(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_13(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_14(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["XXsession_idXX"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_15(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["SESSION_ID"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_16(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(None),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_17(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["XXworkspaceXX"]),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_18(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["WORKSPACE"]),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_19(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["XXgoalXX"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_20(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["GOAL"],
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

    def xǁStateManagerǁ_deserialize_state__mutmut_21(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get(None, 0),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_22(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration"),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_23(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get(0),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_24(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get(
                "iteration",
            ),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_25(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("XXiterationXX", 0),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_26(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("ITERATION", 0),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_27(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 1),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_28(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get(None, 5),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_29(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations"),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_30(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get(5),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_31(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get(
                "max_iterations",
            ),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_32(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("XXmax_iterationsXX", 5),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_33(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("MAX_ITERATIONS", 5),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_34(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 6),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_35(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get(None),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_36(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("XXcurrent_step_idXX"),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_37(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("CURRENT_STEP_ID"),
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

    def xǁStateManagerǁ_deserialize_state__mutmut_38(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("current_step_id"),
        )

        if data.get(None):
            state.started_at = datetime.fromisoformat(data["started_at"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_39(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("current_step_id"),
        )

        if data.get("XXstarted_atXX"):
            state.started_at = datetime.fromisoformat(data["started_at"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_40(self, data: dict[str, Any]) -> AgentState:
        """상태 역직렬화"""
        state = AgentState(
            session_id=data["session_id"],
            workspace=Path(data["workspace"]),
            goal=data["goal"],
            iteration=data.get("iteration", 0),
            max_iterations=data.get("max_iterations", 5),
            current_step_id=data.get("current_step_id"),
        )

        if data.get("STARTED_AT"):
            state.started_at = datetime.fromisoformat(data["started_at"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_41(self, data: dict[str, Any]) -> AgentState:
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
            state.started_at = None
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_42(self, data: dict[str, Any]) -> AgentState:
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
            state.started_at = datetime.fromisoformat(None)
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_43(self, data: dict[str, Any]) -> AgentState:
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
            state.started_at = datetime.fromisoformat(data["XXstarted_atXX"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_44(self, data: dict[str, Any]) -> AgentState:
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
            state.started_at = datetime.fromisoformat(data["STARTED_AT"])
        if data.get("updated_at"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_45(self, data: dict[str, Any]) -> AgentState:
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
        if data.get(None):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_46(self, data: dict[str, Any]) -> AgentState:
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
        if data.get("XXupdated_atXX"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_47(self, data: dict[str, Any]) -> AgentState:
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
        if data.get("UPDATED_AT"):
            state.updated_at = datetime.fromisoformat(data["updated_at"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_48(self, data: dict[str, Any]) -> AgentState:
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
            state.updated_at = None

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_49(self, data: dict[str, Any]) -> AgentState:
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
            state.updated_at = datetime.fromisoformat(None)

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_50(self, data: dict[str, Any]) -> AgentState:
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
            state.updated_at = datetime.fromisoformat(data["XXupdated_atXX"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_51(self, data: dict[str, Any]) -> AgentState:
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
            state.updated_at = datetime.fromisoformat(data["UPDATED_AT"])

        if data.get("plan"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_52(self, data: dict[str, Any]) -> AgentState:
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

        if data.get(None):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_53(self, data: dict[str, Any]) -> AgentState:
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

        if data.get("XXplanXX"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_54(self, data: dict[str, Any]) -> AgentState:
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

        if data.get("PLAN"):
            state.plan = self._deserialize_plan(data["plan"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_55(self, data: dict[str, Any]) -> AgentState:
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
            state.plan = None
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_56(self, data: dict[str, Any]) -> AgentState:
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
            state.plan = self._deserialize_plan(None)
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_57(self, data: dict[str, Any]) -> AgentState:
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
            state.plan = self._deserialize_plan(data["XXplanXX"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_58(self, data: dict[str, Any]) -> AgentState:
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
            state.plan = self._deserialize_plan(data["PLAN"])
        if data.get("explore_result"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_59(self, data: dict[str, Any]) -> AgentState:
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
        if data.get(None):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_60(self, data: dict[str, Any]) -> AgentState:
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
        if data.get("XXexplore_resultXX"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_61(self, data: dict[str, Any]) -> AgentState:
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
        if data.get("EXPLORE_RESULT"):
            state.explore_result = self._deserialize_explore(data["explore_result"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_62(self, data: dict[str, Any]) -> AgentState:
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
            state.explore_result = None

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_63(self, data: dict[str, Any]) -> AgentState:
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
            state.explore_result = self._deserialize_explore(None)

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_64(self, data: dict[str, Any]) -> AgentState:
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
            state.explore_result = self._deserialize_explore(data["XXexplore_resultXX"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_65(self, data: dict[str, Any]) -> AgentState:
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
            state.explore_result = self._deserialize_explore(data["EXPLORE_RESULT"])

        state.checkpoints = data.get("checkpoints", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_66(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = None

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_67(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get(None, [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_68(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get("checkpoints")

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_69(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get([])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_70(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get(
            "checkpoints",
        )

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_71(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get("XXcheckpointsXX", [])

        return state

    def xǁStateManagerǁ_deserialize_state__mutmut_72(self, data: dict[str, Any]) -> AgentState:
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

        state.checkpoints = data.get("CHECKPOINTS", [])

        return state

    @_mutmut_mutated(mutants_xǁStateManagerǁ_deserialize_plan__mutmut)
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_orig(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_1(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = None
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_2(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=None)
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_3(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["XXgoalXX"])
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_4(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["GOAL"])
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_5(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = None
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_6(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(None)
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_7(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["XXcreated_atXX"])
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_8(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["CREATED_AT"])
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_9(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = None

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

    def xǁStateManagerǁ_deserialize_plan__mutmut_10(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(None)

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

    def xǁStateManagerǁ_deserialize_plan__mutmut_11(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["XXupdated_atXX"])

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

    def xǁStateManagerǁ_deserialize_plan__mutmut_12(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["UPDATED_AT"])

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

    def xǁStateManagerǁ_deserialize_plan__mutmut_13(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["XXstepsXX"]:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_14(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["STEPS"]:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_15(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = None
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_16(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_17(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_18(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_19(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["title"],
                description=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_20(self, data: dict[str, Any]) -> Plan:
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
                dependencies=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_21(self, data: dict[str, Any]) -> Plan:
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
                status=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_22(self, data: dict[str, Any]) -> Plan:
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
                assigned_files=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_23(self, data: dict[str, Any]) -> Plan:
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
                expected_outputs=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_24(self, data: dict[str, Any]) -> Plan:
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
                verification_criteria=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_25(self, data: dict[str, Any]) -> Plan:
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
                max_retries=None,
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_26(self, data: dict[str, Any]) -> Plan:
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
                retry_count=None,
                error=s_data["error"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_27(self, data: dict[str, Any]) -> Plan:
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
                error=None,
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_28(self, data: dict[str, Any]) -> Plan:
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
                artifacts=None,
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_29(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_30(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_31(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_32(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["title"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_33(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_34(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_35(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_36(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_37(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_38(self, data: dict[str, Any]) -> Plan:
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_39(self, data: dict[str, Any]) -> Plan:
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
                error=s_data["error"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_40(self, data: dict[str, Any]) -> Plan:
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
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_41(self, data: dict[str, Any]) -> Plan:
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
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_42(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["XXidXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_43(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["ID"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_44(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(None),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_45(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["XXtypeXX"]),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_46(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["TYPE"]),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_47(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["XXtitleXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_48(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["TITLE"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_49(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["title"],
                description=s_data["XXdescriptionXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_50(self, data: dict[str, Any]) -> Plan:
        """계획 역직렬화"""
        plan = Plan(goal=data["goal"])
        plan.created_at = datetime.fromisoformat(data["created_at"])
        plan.updated_at = datetime.fromisoformat(data["updated_at"])

        for s_data in data["steps"]:
            step = PlanStep(
                id=s_data["id"],
                type=StepType(s_data["type"]),
                title=s_data["title"],
                description=s_data["DESCRIPTION"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_51(self, data: dict[str, Any]) -> Plan:
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
                dependencies=s_data["XXdependenciesXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_52(self, data: dict[str, Any]) -> Plan:
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
                dependencies=s_data["DEPENDENCIES"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_53(self, data: dict[str, Any]) -> Plan:
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
                status=StepStatus(None),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_54(self, data: dict[str, Any]) -> Plan:
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
                status=StepStatus(s_data["XXstatusXX"]),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_55(self, data: dict[str, Any]) -> Plan:
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
                status=StepStatus(s_data["STATUS"]),
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_56(self, data: dict[str, Any]) -> Plan:
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
                assigned_files=s_data["XXassigned_filesXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_57(self, data: dict[str, Any]) -> Plan:
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
                assigned_files=s_data["ASSIGNED_FILES"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_58(self, data: dict[str, Any]) -> Plan:
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
                expected_outputs=s_data["XXexpected_outputsXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_59(self, data: dict[str, Any]) -> Plan:
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
                expected_outputs=s_data["EXPECTED_OUTPUTS"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_60(self, data: dict[str, Any]) -> Plan:
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
                verification_criteria=s_data["XXverification_criteriaXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_61(self, data: dict[str, Any]) -> Plan:
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
                verification_criteria=s_data["VERIFICATION_CRITERIA"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_62(self, data: dict[str, Any]) -> Plan:
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
                max_retries=s_data["XXmax_retriesXX"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_63(self, data: dict[str, Any]) -> Plan:
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
                max_retries=s_data["MAX_RETRIES"],
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

    def xǁStateManagerǁ_deserialize_plan__mutmut_64(self, data: dict[str, Any]) -> Plan:
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
                retry_count=s_data["XXretry_countXX"],
                error=s_data["error"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_65(self, data: dict[str, Any]) -> Plan:
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
                retry_count=s_data["RETRY_COUNT"],
                error=s_data["error"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_66(self, data: dict[str, Any]) -> Plan:
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
                error=s_data["XXerrorXX"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_67(self, data: dict[str, Any]) -> Plan:
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
                error=s_data["ERROR"],
                artifacts=s_data["artifacts"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_68(self, data: dict[str, Any]) -> Plan:
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
                artifacts=s_data["XXartifactsXX"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_69(self, data: dict[str, Any]) -> Plan:
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
                artifacts=s_data["ARTIFACTS"],
            )
            if s_data.get("started_at"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_70(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get(None):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_71(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get("XXstarted_atXX"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_72(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get("STARTED_AT"):
                step.started_at = datetime.fromisoformat(s_data["started_at"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_73(self, data: dict[str, Any]) -> Plan:
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
                step.started_at = None
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_74(self, data: dict[str, Any]) -> Plan:
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
                step.started_at = datetime.fromisoformat(None)
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_75(self, data: dict[str, Any]) -> Plan:
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
                step.started_at = datetime.fromisoformat(s_data["XXstarted_atXX"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_76(self, data: dict[str, Any]) -> Plan:
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
                step.started_at = datetime.fromisoformat(s_data["STARTED_AT"])
            if s_data.get("completed_at"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_77(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get(None):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_78(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get("XXcompleted_atXX"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_79(self, data: dict[str, Any]) -> Plan:
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
            if s_data.get("COMPLETED_AT"):
                step.completed_at = datetime.fromisoformat(s_data["completed_at"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_80(self, data: dict[str, Any]) -> Plan:
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
                step.completed_at = None
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_81(self, data: dict[str, Any]) -> Plan:
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
                step.completed_at = datetime.fromisoformat(None)
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_82(self, data: dict[str, Any]) -> Plan:
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
                step.completed_at = datetime.fromisoformat(s_data["XXcompleted_atXX"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_83(self, data: dict[str, Any]) -> Plan:
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
                step.completed_at = datetime.fromisoformat(s_data["COMPLETED_AT"])
            plan.steps.append(step)

        return plan

    def xǁStateManagerǁ_deserialize_plan__mutmut_84(self, data: dict[str, Any]) -> Plan:
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
            plan.steps.append(None)

        return plan

    @_mutmut_mutated(mutants_xǁStateManagerǁ_deserialize_explore__mutmut)
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

    def xǁStateManagerǁ_deserialize_explore__mutmut_orig(
        self, data: dict[str, Any]
    ) -> ExploreResult:
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

    def xǁStateManagerǁ_deserialize_explore__mutmut_1(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = None

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

    def xǁStateManagerǁ_deserialize_explore__mutmut_2(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get(None, []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_3(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols"):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_4(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get([]):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_5(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get(
            "symbols",
        ):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_6(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("XXsymbolsXX", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_7(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("SYMBOLS", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_8(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(None)

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_9(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get(None, []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_10(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files"):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_11(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get([]):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_12(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get(
            "files",
        ):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_13(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("XXfilesXX", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_14(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("FILES", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_15(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(None)

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_16(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = None
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_17(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get(None, {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_18(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph")
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_19(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get({})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_20(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get(
            "import_graph",
        )
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_21(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("XXimport_graphXX", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_22(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("IMPORT_GRAPH", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_23(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = None
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_24(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get(None, {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_25(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph")
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_26(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get({})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_27(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get(
            "call_graph",
        )
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_28(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("XXcall_graphXX", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_29(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("CALL_GRAPH", {})
        explore.entry_points = data.get("entry_points", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_30(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = None
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_31(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get(None, [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_32(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("entry_points")
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_33(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get([])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_34(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get(
            "entry_points",
        )
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_35(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("XXentry_pointsXX", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_36(self, data: dict[str, Any]) -> ExploreResult:
        """탐색 결과 역직렬화"""
        from .models import CodeSymbol, FileInfo

        explore = ExploreResult()

        for s_data in data.get("symbols", []):
            explore.symbols.append(CodeSymbol(**s_data))

        for f_data in data.get("files", []):
            explore.files.append(FileInfo(**f_data))

        explore.import_graph = data.get("import_graph", {})
        explore.call_graph = data.get("call_graph", {})
        explore.entry_points = data.get("ENTRY_POINTS", [])
        explore.config_files = data.get("config_files", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_37(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = None
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_38(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get(None, [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_39(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get("config_files")
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_40(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get([])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_41(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get(
            "config_files",
        )
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_42(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get("XXconfig_filesXX", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_43(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.config_files = data.get("CONFIG_FILES", [])
        explore.test_files = data.get("test_files", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_44(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = None

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_45(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get(None, [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_46(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get("test_files")

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_47(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get([])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_48(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get(
            "test_files",
        )

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_49(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get("XXtest_filesXX", [])

        return explore

    def xǁStateManagerǁ_deserialize_explore__mutmut_50(self, data: dict[str, Any]) -> ExploreResult:
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
        explore.test_files = data.get("TEST_FILES", [])

        return explore


mutants_xǁStateManagerǁ__init____mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ__init____mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_1"] = StateManager.xǁStateManagerǁ__init____mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_2"] = StateManager.xǁStateManagerǁ__init____mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_3"] = StateManager.xǁStateManagerǁ__init____mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_4"] = StateManager.xǁStateManagerǁ__init____mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_5"] = StateManager.xǁStateManagerǁ__init____mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_6"] = StateManager.xǁStateManagerǁ__init____mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_7"] = StateManager.xǁStateManagerǁ__init____mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_8"] = StateManager.xǁStateManagerǁ__init____mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_9"] = StateManager.xǁStateManagerǁ__init____mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_10"] = StateManager.xǁStateManagerǁ__init____mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_11"] = StateManager.xǁStateManagerǁ__init____mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ__init____mutmut["xǁStateManagerǁ__init____mutmut_12"] = StateManager.xǁStateManagerǁ__init____mutmut_12  # type: ignore # mutmut generated

mutants_xǁStateManagerǁsave_state__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁsave_state__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_1"] = StateManager.xǁStateManagerǁsave_state__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_2"] = StateManager.xǁStateManagerǁsave_state__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_3"] = StateManager.xǁStateManagerǁsave_state__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_4"] = StateManager.xǁStateManagerǁsave_state__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_5"] = StateManager.xǁStateManagerǁsave_state__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_6"] = StateManager.xǁStateManagerǁsave_state__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_7"] = StateManager.xǁStateManagerǁsave_state__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_8"] = StateManager.xǁStateManagerǁsave_state__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_9"] = StateManager.xǁStateManagerǁsave_state__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_10"] = StateManager.xǁStateManagerǁsave_state__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_11"] = StateManager.xǁStateManagerǁsave_state__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_12"] = StateManager.xǁStateManagerǁsave_state__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_13"] = StateManager.xǁStateManagerǁsave_state__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_14"] = StateManager.xǁStateManagerǁsave_state__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_15"] = StateManager.xǁStateManagerǁsave_state__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_16"] = StateManager.xǁStateManagerǁsave_state__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_17"] = StateManager.xǁStateManagerǁsave_state__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_18"] = StateManager.xǁStateManagerǁsave_state__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_19"] = StateManager.xǁStateManagerǁsave_state__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_20"] = StateManager.xǁStateManagerǁsave_state__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_21"] = StateManager.xǁStateManagerǁsave_state__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_22"] = StateManager.xǁStateManagerǁsave_state__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_23"] = StateManager.xǁStateManagerǁsave_state__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_24"] = StateManager.xǁStateManagerǁsave_state__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_25"] = StateManager.xǁStateManagerǁsave_state__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁsave_state__mutmut["xǁStateManagerǁsave_state__mutmut_26"] = StateManager.xǁStateManagerǁsave_state__mutmut_26  # type: ignore # mutmut generated

mutants_xǁStateManagerǁload_state__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁload_state__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_1"] = StateManager.xǁStateManagerǁload_state__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_2"] = StateManager.xǁStateManagerǁload_state__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_3"] = StateManager.xǁStateManagerǁload_state__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_4"] = StateManager.xǁStateManagerǁload_state__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_5"] = StateManager.xǁStateManagerǁload_state__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_6"] = StateManager.xǁStateManagerǁload_state__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_7"] = StateManager.xǁStateManagerǁload_state__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_8"] = StateManager.xǁStateManagerǁload_state__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_9"] = StateManager.xǁStateManagerǁload_state__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_10"] = StateManager.xǁStateManagerǁload_state__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_11"] = StateManager.xǁStateManagerǁload_state__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_12"] = StateManager.xǁStateManagerǁload_state__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁload_state__mutmut["xǁStateManagerǁload_state__mutmut_13"] = StateManager.xǁStateManagerǁload_state__mutmut_13  # type: ignore # mutmut generated

mutants_xǁStateManagerǁlist_sessions__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_1"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_2"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_3"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_4"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_5"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_6"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_7"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_8"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_9"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_10"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_11"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_12"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_13"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_14"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_15"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_16"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_17"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_18"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_19"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_20"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_21"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_22"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_23"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_24"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_25"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_26"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_27"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_28"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_29"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_30"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_31"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_32"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_33"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_34"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_35"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_36"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_37"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_38"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_39"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_40"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_41"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_42"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_42  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_43"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_43  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_44"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_44  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_45"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_45  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_46"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_46  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_47"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_47  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_48"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_48  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_49"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_49  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_50"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_50  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_51"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_51  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_52"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_52  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_53"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_53  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_54"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_54  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_55"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_55  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_56"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_56  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_57"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_57  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_58"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_58  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_59"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_59  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_60"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_60  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_61"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_61  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_sessions__mutmut["xǁStateManagerǁlist_sessions__mutmut_62"] = StateManager.xǁStateManagerǁlist_sessions__mutmut_62  # type: ignore # mutmut generated

mutants_xǁStateManagerǁdelete_session__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁdelete_session__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁdelete_session__mutmut["xǁStateManagerǁdelete_session__mutmut_1"] = StateManager.xǁStateManagerǁdelete_session__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁdelete_session__mutmut["xǁStateManagerǁdelete_session__mutmut_2"] = StateManager.xǁStateManagerǁdelete_session__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁdelete_session__mutmut["xǁStateManagerǁdelete_session__mutmut_3"] = StateManager.xǁStateManagerǁdelete_session__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁdelete_session__mutmut["xǁStateManagerǁdelete_session__mutmut_4"] = StateManager.xǁStateManagerǁdelete_session__mutmut_4  # type: ignore # mutmut generated

mutants_xǁStateManagerǁcreate_checkpoint__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_1"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_2"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_3"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_4"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_5"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_6"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_7"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_8"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_9"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_10"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_11"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_12"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_13"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_14"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_15"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_16"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_17"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_18"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_19"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_20"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_21"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_22"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_23"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_24"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_25"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_26"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_27"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_28"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_29"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_30"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_31"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_32"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_33"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_34"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_35"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_36"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_37"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_38"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁcreate_checkpoint__mutmut["xǁStateManagerǁcreate_checkpoint__mutmut_39"] = StateManager.xǁStateManagerǁcreate_checkpoint__mutmut_39  # type: ignore # mutmut generated

mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_1"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_2"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_3"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_4"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_5"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_6"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_7"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_8"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_9"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_10"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_11"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_12"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_13"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_14"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_15"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_16"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_17"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_18"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_19"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_20"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_21"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_22"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_23"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_24"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁrollback_to_checkpoint__mutmut["xǁStateManagerǁrollback_to_checkpoint__mutmut_25"] = StateManager.xǁStateManagerǁrollback_to_checkpoint__mutmut_25  # type: ignore # mutmut generated

mutants_xǁStateManagerǁlist_checkpoints__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_1"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_2"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_3"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_4"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_5"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_6"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_7"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_8"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_9"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_10"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_11"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_12"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_13"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_14"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_15"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_16"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_17"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_18"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_19"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_20"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_21"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_22"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_23"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_24"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_25"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_26"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_27"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_28"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_29"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_30"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_31"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_32"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_33"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_34"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_35"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_36"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_37"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_38"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_39"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_40"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_41"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_42"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_42  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_43"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_43  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_44"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_44  # type: ignore # mutmut generated
mutants_xǁStateManagerǁlist_checkpoints__mutmut["xǁStateManagerǁlist_checkpoints__mutmut_45"] = StateManager.xǁStateManagerǁlist_checkpoints__mutmut_45  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_serialize_state__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_1"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_2"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_3"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_4"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_5"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_6"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_7"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_8"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_9"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_10"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_11"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_12"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_13"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_14"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_15"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_16"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_17"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_18"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_19"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_20"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_21"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_22"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_23"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_24"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_state__mutmut["xǁStateManagerǁ_serialize_state__mutmut_25"] = StateManager.xǁStateManagerǁ_serialize_state__mutmut_25  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_serialize_plan__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_1"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_2"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_3"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_4"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_5"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_6"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_7"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_8"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_9"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_10"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_11"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_12"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_13"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_14"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_15"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_16"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_17"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_18"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_19"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_20"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_21"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_22"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_23"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_24"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_25"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_26"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_27"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_28"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_29"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_30"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_31"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_32"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_33"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_34"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_35"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_36"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_37"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_plan__mutmut["xǁStateManagerǁ_serialize_plan__mutmut_38"] = StateManager.xǁStateManagerǁ_serialize_plan__mutmut_38  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_serialize_explore__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_1"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_2"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_3"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_4"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_5"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_6"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_7"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_8"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_9"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_10"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_11"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_12"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_13"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_14"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_15"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_16"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_17"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_18"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_19"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_20"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_21"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_22"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_23"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_24"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_25"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_26"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_27"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_28"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_29"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_30"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_31"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_32"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_33"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_34"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_35"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_36"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_37"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_38"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_39"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_40"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_41"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_serialize_explore__mutmut["xǁStateManagerǁ_serialize_explore__mutmut_42"] = StateManager.xǁStateManagerǁ_serialize_explore__mutmut_42  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_deserialize_state__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_1"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_2"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_3"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_4"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_5"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_6"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_7"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_8"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_9"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_10"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_11"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_12"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_13"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_14"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_15"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_16"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_17"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_18"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_19"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_20"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_21"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_22"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_23"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_24"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_25"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_26"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_27"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_28"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_29"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_30"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_31"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_32"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_33"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_34"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_35"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_36"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_37"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_38"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_39"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_40"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_41"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_42"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_42  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_43"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_43  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_44"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_44  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_45"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_45  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_46"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_46  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_47"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_47  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_48"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_48  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_49"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_49  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_50"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_50  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_51"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_51  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_52"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_52  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_53"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_53  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_54"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_54  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_55"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_55  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_56"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_56  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_57"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_57  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_58"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_58  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_59"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_59  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_60"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_60  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_61"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_61  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_62"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_62  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_63"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_63  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_64"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_64  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_65"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_65  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_66"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_66  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_67"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_67  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_68"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_68  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_69"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_69  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_70"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_70  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_71"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_71  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_state__mutmut["xǁStateManagerǁ_deserialize_state__mutmut_72"] = StateManager.xǁStateManagerǁ_deserialize_state__mutmut_72  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_deserialize_plan__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_1"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_2"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_3"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_4"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_5"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_6"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_7"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_8"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_9"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_10"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_11"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_12"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_13"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_14"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_15"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_16"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_17"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_18"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_19"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_20"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_21"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_22"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_23"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_24"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_25"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_26"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_27"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_28"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_29"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_30"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_31"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_32"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_33"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_34"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_35"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_36"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_37"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_38"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_39"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_40"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_41"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_42"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_42  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_43"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_43  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_44"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_44  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_45"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_45  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_46"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_46  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_47"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_47  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_48"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_48  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_49"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_49  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_50"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_50  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_51"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_51  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_52"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_52  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_53"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_53  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_54"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_54  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_55"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_55  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_56"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_56  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_57"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_57  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_58"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_58  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_59"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_59  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_60"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_60  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_61"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_61  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_62"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_62  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_63"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_63  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_64"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_64  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_65"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_65  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_66"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_66  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_67"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_67  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_68"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_68  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_69"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_69  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_70"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_70  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_71"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_71  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_72"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_72  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_73"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_73  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_74"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_74  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_75"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_75  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_76"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_76  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_77"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_77  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_78"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_78  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_79"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_79  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_80"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_80  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_81"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_81  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_82"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_82  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_83"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_83  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_plan__mutmut["xǁStateManagerǁ_deserialize_plan__mutmut_84"] = StateManager.xǁStateManagerǁ_deserialize_plan__mutmut_84  # type: ignore # mutmut generated

mutants_xǁStateManagerǁ_deserialize_explore__mutmut["_mutmut_orig"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_1"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_1  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_2"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_2  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_3"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_3  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_4"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_4  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_5"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_5  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_6"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_6  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_7"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_7  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_8"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_8  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_9"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_9  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_10"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_10  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_11"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_11  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_12"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_12  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_13"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_13  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_14"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_14  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_15"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_15  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_16"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_16  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_17"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_17  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_18"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_18  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_19"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_19  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_20"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_20  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_21"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_21  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_22"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_22  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_23"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_23  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_24"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_24  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_25"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_25  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_26"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_26  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_27"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_27  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_28"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_28  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_29"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_29  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_30"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_30  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_31"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_31  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_32"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_32  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_33"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_33  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_34"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_34  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_35"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_35  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_36"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_36  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_37"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_37  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_38"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_38  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_39"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_39  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_40"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_40  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_41"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_41  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_42"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_42  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_43"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_43  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_44"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_44  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_45"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_45  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_46"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_46  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_47"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_47  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_48"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_48  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_49"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_49  # type: ignore # mutmut generated
mutants_xǁStateManagerǁ_deserialize_explore__mutmut["xǁStateManagerǁ_deserialize_explore__mutmut_50"] = StateManager.xǁStateManagerǁ_deserialize_explore__mutmut_50  # type: ignore # mutmut generated
mutants_x_get_state_manager__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_state_manager__mutmut)
def get_state_manager(workspace: Path) -> StateManager:
    """상태 관리자 헬퍼"""
    return StateManager(workspace)


def x_get_state_manager__mutmut_orig(workspace: Path) -> StateManager:
    """상태 관리자 헬퍼"""
    return StateManager(workspace)


def x_get_state_manager__mutmut_1(workspace: Path) -> StateManager:
    """상태 관리자 헬퍼"""
    return StateManager(None)


mutants_x_get_state_manager__mutmut["_mutmut_orig"] = x_get_state_manager__mutmut_orig  # type: ignore # mutmut generated
mutants_x_get_state_manager__mutmut["x_get_state_manager__mutmut_1"] = x_get_state_manager__mutmut_1  # type: ignore # mutmut generated
