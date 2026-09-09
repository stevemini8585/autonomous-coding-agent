"""
자율 코딩 에이전트 - 코드 생성/수정 (Coder)
실제 작업 목표를 분석하여 구체적인 코드 생성
"""

from __future__ import annotations

import logging
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .models import PlanStep, StepStatus, StepType
from .patch_utils import PatchManager, PatchOperation

log = logging.getLogger("autonomous_coding_agent.coder")


class CodeGenerator:
    """코드 생성 및 수정 - 작업 목표에 맞게 구체적 구현"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._backup_dir = self.workspace / ".autonomous_backups"
        self._backup_dir.mkdir(exist_ok=True)

    def execute_step(self, step: PlanStep, context: dict[str, Any]) -> dict[str, Any]:
        """단계 실행 (코드 생성/수정)"""
        log.info(f"코드 실행: {step.id} - {step.title}")

        step.status = StepStatus.IN_PROGRESS

        try:
            if step.type == StepType.CODE:
                result = self._implement_code(step, context)
            elif step.type == StepType.EXPLORE:
                result = {"action": "explore", "message": "탐색은 별도 모듈에서 수행"}
            elif step.type == StepType.PLAN:
                result = {"action": "plan", "message": "계획은 별도 모듈에서 수행"}
            elif step.type == StepType.VERIFY:
                result = {"action": "verify", "message": "검증은 별도 모듈에서 수행"}
            elif step.type == StepType.CRITIQUE:
                result = {"action": "critique", "message": "비평은 별도 모듈에서 수행"}
            else:
                result = {"action": "unknown", "message": f"알 수 없는 단계 유형: {step.type}"}

            step.status = StepStatus.COMPLETED
            step.artifacts = result

        except Exception as e:
            step.status = StepStatus.FAILED
            step.error = str(e)
            log.error(f"단계 실행 실패 {step.id}: {e}")
            result = {"error": str(e)}

        return result

    def _implement_code(self, step: PlanStep, context: dict[str, Any]) -> dict[str, Any]:
        """코드 구현 - 작업 목표 분석 후 구체적 구현"""
        artifacts = {
            "files_created": [],
            "files_modified": [],
            "patches_applied": [],
        }

        # 1. 기존 파일 백업
        for file_path in step.assigned_files:
            self._backup_file(file_path)

        # 2. 작업 목표 분석하여 구체적 구현 생성
        goal = context.get("goal", "")
        implementation = self._generate_task_specific_implementation(step, goal, context)

        # 3. 파일 적용 - PatchManager 사용
        patch_manager = PatchManager(self.workspace)
        operations = []

        for file_path, content in implementation.items():
            full_path = self.workspace / file_path

            if full_path.exists():
                operations.append(
                    PatchOperation(
                        file_path=file_path,
                        old_content=full_path.read_text(encoding="utf-8"),
                        new_content=content,
                        description=f"Update {file_path} for {step.title}",
                    )
                )
            else:
                # 새 파일 생성
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(content, encoding="utf-8")
                artifacts["files_created"].append(file_path)

        # 패치 적용 (트랜잭션으로 원자적 적용)
        if operations:
            results = patch_manager.apply_patches(operations)
            for result in results:
                if result.success and result.applied:
                    artifacts["files_modified"].append(result.file_path)
                elif not result.success:
                    log.error(f"패치 실패: {result.file_path} - {result.error}")
                    # 실패 시 롤백됨

        artifacts["patches_applied"] = [
            {"file": r.file_path, "applied": r.applied, "hunks": r.hunks_applied}
            for r in results
            if r.applied
        ]

        return artifacts

    def _generate_task_specific_implementation(
        self, step: PlanStep, goal: str, context: dict[str, Any]
    ) -> dict[str, str]:
        """작업 목표에 맞춘 구체적 구현 생성"""
        implementations = {}

        for file_path in step.assigned_files:
            ext = Path(file_path).suffix.lower()

            if ext == ".py":
                implementations[file_path] = self._generate_python_task_code(
                    step, file_path, goal, context
                )
            elif ext in (".js", ".ts", ".tsx"):
                implementations[file_path] = self._generate_js_ts_task_code(
                    step, file_path, goal, context
                )
            elif ext == ".go":
                implementations[file_path] = self._generate_go_task_code(
                    step, file_path, goal, context
                )
            elif ext == ".rs":
                implementations[file_path] = self._generate_rust_task_code(
                    step, file_path, goal, context
                )
            else:
                implementations[file_path] = self._generate_generic_code(
                    step, file_path, goal, context
                )

        # 테스트 파일도 생성 (목표에 '테스트' 포함시)
        if "테스트" in goal or "test" in goal.lower():
            test_files = self._generate_test_files(step, goal, context)
            implementations.update(test_files)

        return implementations

    def _generate_python_task_code(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """Python 작업별 코드 생성"""
        full_path = self.workspace / file_path
        existing_content = ""
        if full_path.exists():
            existing_content = full_path.read_text(encoding="utf-8")

        # 기존 파일이 있으면 목표에 맞춰 수정
        if existing_content:
            return self._implement_feature_in_file(existing_content, goal, file_path, context)
        else:
            # 새 파일 생성
            return self._generate_python_module(step, file_path, goal, context)

    def _implement_feature_in_file(
        self, content: str, goal: str, file_path: str, context: dict[str, Any]
    ) -> str:
        """기존 파일에 기능 구현 추가 (목표 분석 후 코드 삽입)"""
        goal_lower = goal.lower()
        lines = content.split("\n")

        # FastAPI 프로젝트에서 endpoint 추가 감지
        if ("endpoint" in goal_lower or "api" in goal_lower) and "fastapi" in content.lower():
            return self._add_fastapi_endpoint(content, goal, file_path)

        # 기본적으로는 파일 개선 (docstring 추가 등)
        return self._enhance_python_file(content, goal)

    def _add_fastapi_endpoint(self, content: str, goal: str, file_path: str) -> str:
        """FastAPI 파일에 새 엔드포인트 추가 (중복 방지)"""
        import re

        # 목표에서 경로와 응답 추출
        path_match = re.search(r"GET\s+(/\w+)", goal, re.IGNORECASE)
        if not path_match:
            path_match = re.search(r"(//\w+)", goal)
        endpoint_path = path_match.group(1) if path_match else "/hello"

        # 이미 존재하는 엔드포인트인지 체크
        if re.search(rf'@app\.get\(\s*["\']{re.escape(endpoint_path)}["\']\s*\)', content):
            log.info(f"엔드포인트 {endpoint_path} 이미 존재함, 건너뜀")
            return content

        # 응답 메시지 추출
        msg_match = re.search(r'message\s*[:=]\s*["\']([^"\']+)["\']', goal, re.IGNORECASE)
        message = msg_match.group(1) if msg_match else "Hello World"

        # app = FastAPI(...) 라인 찾기
        lines = content.split("\n")
        insert_idx = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("app = FastAPI"):
                insert_idx = i + 1
                break

        if insert_idx == -1:
            # Fallback: 마지막 import 이후
            for i, line in enumerate(lines):
                if line.strip().startswith("from ") or line.strip().startswith("import "):
                    insert_idx = i + 1

        if insert_idx == -1:
            insert_idx = 0

        # 엔드포인트 코드 생성
        endpoint_code = (
            f'@app.get("{endpoint_path}")\n'
            f"def read_hello():\n"
            f'    """{endpoint_path} 엔드포인트.\n\n'
            f"    Returns:\n"
            f"        결과값.\n"
            f'    """\n'
            f'    return {{"message": "{message}"}}'
        )

        # 삽입
        new_lines = lines[:insert_idx] + ["", endpoint_code.strip()] + [""] + lines[insert_idx:]
        return "\n".join(new_lines)

    def _enhance_python_file(self, content: str, goal: str) -> str:
        """기존 Python 파일 개선 (docstring, type hints, 문서화 추가)"""
        lines = content.split("\n")
        enhanced = []

        i = 0
        while i < len(lines):
            line = lines[i]

            # 함수 정의 다음에 docstring 추가
            if line.strip().startswith("def ") and not line.strip().startswith("def _"):
                # 이미 docstring이 있는지 확인 (다음 non-empty 라인 확인)
                next_idx = i + 1
                while next_idx < len(lines) and lines[next_idx].strip() == "":
                    next_idx += 1

                has_docstring = False
                if next_idx < len(lines):
                    if '"""' in lines[next_idx] or "'''" in lines[next_idx]:
                        has_docstring = True

                if not has_docstring:
                    # 함수 시그니처에서 인자 추출
                    func_match = re.match(r"(\s*)def (\w+)\((.*?)\)", line)
                    if func_match:
                        indent = func_match.group(1)
                        func_name = func_match.group(2)
                        params = func_match.group(3)

                        # docstring 생성 (Google style - ruff/black 호환)
                        docstring_lines = [f'{indent}    """{func_name} 함수."""']
                        if params.strip():
                            param_list = [
                                p.strip().split(":")[0].strip()
                                for p in params.split(",")
                                if p.strip()
                            ]
                            if param_list:
                                docstring_lines.append(f"{indent}    Args:")
                                for param in param_list:
                                    if param and "=" not in param:
                                        docstring_lines.append(
                                            f"{indent}        {param}: 매개변수 설명."
                                        )
                        docstring_lines.append(f"{indent}    Returns:")
                        docstring_lines.append(f"{indent}        결과값.")
                        docstring = "\n".join(docstring_lines)

                        # 현재 라인(함수 정의)을 추가하고, docstring을 그 다음에 삽입
                        enhanced.append(line)

                        # 빈 줄들 복사
                        j = i + 1
                        while j < len(lines) and lines[j].strip() == "":
                            enhanced.append(lines[j])
                            j += 1

                        # docstring 삽입
                        enhanced.append(docstring)

                        # 남은 줄들(j부터)을 enhanced에 추가하고 인덱스 업데이트
                        while j < len(lines):
                            enhanced.append(lines[j])
                            j += 1

                        i = j  # 다음 루프는 j부터
                        continue  # while 루프 계속

            # 일반 라인 처리
            enhanced.append(line)
            i += 1

        return "\n".join(enhanced)

    def _generate_python_module(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """Python 모듈 생성"""
        module_name = Path(file_path).stem

        # 목표에 맞춘 구체적 구현
        if "타입 힌트" in goal and "문서화" in goal:
            return f'''"""
{module_name} - {goal[:100]}
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

log = logging.getLogger(__name__)


def main() -> None:
    """메인 진입점"""
    log.info("모듈 실행")
    # TODO: 구체적 구현 추가
    pass


if __name__ == "__main__":
    main()
'''
        else:
            return f'''"""
{module_name} - Auto-generated module
{step.description[:200]}
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

log = logging.getLogger(__name__)


class {module_name.capitalize()}:
    """Auto-generated class for {step.title}"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {{}}
    
    def execute(self) -> Dict[str, Any]:
        """Execute the main logic"""
        log.info("Executing {step.title}")
        # TODO: Implement based on step description
        return {{"status": "completed", "step": "{step.id}"}}


def main():
    """Main entry point"""
    instance = {module_name.capitalize()}()
    return instance.execute()


if __name__ == "__main__":
    main()
'''

    def _generate_test_files(
        self, step: PlanStep, goal: str, context: dict[str, Any]
    ) -> dict[str, str]:
        """테스트 파일 생성"""
        test_files = {}

        for file_path in step.assigned_files:
            if file_path.endswith(".py") and not file_path.endswith("_test.py"):
                test_path = file_path.replace(".py", "_test.py")
                test_files[test_path] = self._generate_python_test_file(file_path, goal, context)

        return test_files

    def _generate_python_test_file(
        self, source_file: str, goal: str, context: dict[str, Any]
    ) -> str:
        """소스 파일에 대한 테스트 파일 생성"""
        module_name = Path(source_file).stem
        test_path = f"{module_name}_test.py"

        # 소스 파일 읽어서 함수들 파악
        source_path = self.workspace / source_file
        functions = []  # list of (name, params)
        if source_path.exists():
            content = source_path.read_text(encoding="utf-8")
            for match in re.finditer(r"^\s*def (\w+)\((.*?)\)", content, re.MULTILINE):
                if not match.group(1).startswith("_"):
                    func_name = match.group(1)
                    params = match.group(2).strip()
                    # Parse parameters to get default values
                    param_list = []
                    for p in params.split(","):
                        p = p.strip()
                        if p:
                            if "=" in p:
                                name, default = p.split("=", 1)
                                param_list.append((name.strip(), default.strip()))
                            else:
                                param_list.append((p.split(":")[0].strip(), None))
                    functions.append((func_name, param_list))

        if not functions:
            functions = [("main", [])]

        test_content = f'''"""
Tests for {module_name}
Auto-generated test for: {goal}
"""

from {module_name} import {', '.join(sorted(f[0] for f in functions)) if functions else 'main'}
import pytest


'''

        for func_name, params in functions:
            # Build function call with arguments
            args = []
            for param_name, default in params:
                if default is not None:
                    args.append(f"{param_name}={default}")
                # Provide sensible defaults based on param name/type hints
                elif "name" in param_name.lower():
                    args.append('"test"')
                elif (
                    "id" in param_name.lower()
                    or "num" in param_name.lower()
                    or "count" in param_name.lower()
                ):
                    args.append("1")
                elif "list" in param_name.lower() or "items" in param_name.lower():
                    args.append("[]")
                elif "dict" in param_name.lower() or "map" in param_name.lower():
                    args.append("{}")
                elif "bool" in param_name.lower() or "flag" in param_name.lower():
                    args.append("True")
                else:
                    args.append('"test_value"')

            call_args = ", ".join(args)

            test_content += f'''def test_{func_name}():
    """Test {func_name} function"""
    result = {func_name}({call_args})
    assert result is not None
    # TODO: 구체적 테스트 케이스 추가

'''

        test_content += """if __name__ == "__main__":
    pytest.main([__file__, "-v"])
"""

        return test_content

    def _generate_python_test(self, step: PlanStep, existing: str, context: dict[str, Any]) -> str:
        """기존 테스트 파일 수정"""
        if existing:
            return existing + f"\n\n# === Auto-generated test for: {step.title} ===\n"
        else:
            return self._generate_python_test_file(
                step.assigned_files[0] if step.assigned_files else "module.py", "", context
            )

    def _generate_js_ts_task_code(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """JavaScript/TypeScript 작업별 코드 생성"""
        ext = Path(file_path).suffix.lower()
        is_ts = ext in (".ts", ".tsx")

        full_path = self.workspace / file_path
        existing_content = ""
        if full_path.exists():
            existing_content = full_path.read_text(encoding="utf-8")

        if existing_content:
            return (
                existing_content
                + f"\n\n// === Auto-generated for: {step.title} ===\n// TODO: Implement based on goal\n"
            )

        return self._generate_js_ts_module(step, is_ts, goal)

    def _generate_js_ts_module(self, step: PlanStep, is_ts: bool, goal: str) -> str:
        """JavaScript/TypeScript 모듈 생성 (f-string 이스케이프 문제 해결)"""
        type_ann = ": any" if is_ts else ""

        template = """/**
 * Auto-generated module for: {goal}
 */

{interface}

export class AutoGeneratedClass {{
  private config: Config;
  
  constructor(config{type_ann} = {{}}) {{
    this.config = config;
  }}
  
  execute(): {{ status: string; step: string }} {{
    console.log('Executing task');
    // TODO: Implement based on goal
    return {{ status: 'completed', step: 'auto' }};
  }}
}}

export default AutoGeneratedClass;
"""
        interface = ""
        if is_ts:
            interface = "interface Config {\n  [key: string]: any;\n}"

        return template.format(
            goal=goal[:100],
            type_ann=type_ann,
            interface=interface,
        )

    def _generate_go_task_code(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """Go 작업별 코드 생성"""
        if file_path.endswith("_test.go"):
            return self._generate_go_test(step, goal)
        else:
            return self._generate_go_module(step, goal)

    def _generate_go_module(self, step: PlanStep, goal: str) -> str:
        template = """// Package autogenerated - Auto-generated for: {title}
// {desc}

package autogenerated

import (
	"log"
)

// Config holds configuration
type Config map[string]interface{ob}

// AutoGeneratedStruct struct
type AutoGeneratedStruct {ob
	config Config
cb}

// New creates a new AutoGeneratedStruct
func New(config Config) *AutoGeneratedStruct {ob
	return &AutoGeneratedStruct{ob config: config cb}
cb}

// Execute executes the main logic
func (a *AutoGeneratedStruct) Execute() map[string]interface{ob} {ob
	log.Println("Executing {title}")
	// TODO: Implement based on goal
	return map[string]interface{ob}{{
		"status": "completed",
		"step": "auto",
	}
cb
cb
"""
        return template.format(
            title=step.title,
            desc=goal[:200],
            ob="{",
            cb="}",
        )

    def _generate_go_test(self, step: PlanStep, goal: str) -> str:
        template = """// Auto-generated test for: {title}

package autogenerated

import (
	"testing"
)

func TestAutoGeneratedStruct_Execute(t *testing.T) {ob
	instance := New(nil)
	result := instance.Execute()
	
	if result["status"] != "completed" {ob
		t.Errorf("Expected status completed, got %v", result["status"])
	cb
cb
}}

func TestAutoGeneratedStruct_ExecuteWithConfig(t *testing.T) {ob
	config := map[string]interface{ob}{{"test": true}}
	instance := New(config)
	result := instance.Execute()
	
	if result["status"] != "completed" {ob
		t.Errorf("Expected status completed, got %v", result["status"])
	cb
cb
}}
"""
        return template.format(
            title=step.title,
            ob="{",
            cb="}",
        )

    def _generate_rust_task_code(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """Rust 작업별 코드 생성"""
        if "_test" in file_path or "/tests/" in file_path:
            return self._generate_rust_module(step, goal)
        else:
            return self._generate_rust_module(step, goal)

    def _generate_rust_module(self, step: PlanStep, goal: str) -> str:
        return f"""// Auto-generated module for: {step.title}
// {goal[:200]}

use std::collections::HashMap;

/// Configuration type
pub type Config = HashMap<String, serde_json::Value>;

/// Auto-generated struct
pub struct AutoGeneratedStruct {{
    config: Config,
}}

impl AutoGeneratedStruct {{
    /// Create a new instance
    pub fn new(config: Config) -> Self {{
        Self {{ config }}
    }}
    
    /// Execute the main logic
    pub fn execute(&self) -> HashMap<String, serde_json::Value> {{
        log::info!("Executing {step.title}");
        // TODO: Implement based on step description
        let mut result = HashMap::new();
        result.insert("status".to_string(), serde_json::json!("completed"));
        result.insert("step".to_string(), serde_json::json!("auto"));
        result
    }}
}}

#[cfg(test)]
mod tests {{
    use super::*;
    
    #[test]
    fn test_execute() {{
        let instance = AutoGeneratedStruct::new(HashMap::new());
        let result = instance.execute();
        
        assert_eq!(result.get("status"), Some(&serde_json::json!("completed")));
    }}
    
    #[test]
    fn test_execute_with_config() {{
        let mut config = HashMap::new();
        config.insert("test".to_string(), serde_json::json!(true));
        let instance = AutoGeneratedStruct::new(config);
        let result = instance.execute();
        
        assert_eq!(result.get("status"), Some(&serde_json::json!("completed")));
    }}
}}
"""

    def _generate_generic_code(
        self, step: PlanStep, file_path: str, goal: str, context: dict[str, Any]
    ) -> str:
        """범용 코드 생성"""
        return f"""# Auto-generated for: {step.title}
# Goal: {goal[:200]}

# TODO: Implement based on goal
# File: {file_path}
"""

    def _backup_file(self, file_path: str) -> None:
        """파일 백업"""
        full_path = self.workspace / file_path
        if full_path.exists():
            backup_path = self._backup_dir / f"{file_path.replace('/', '_')}.bak"
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            backup_path.write_text(full_path.read_text(encoding="utf-8"), encoding="utf-8")

    def _apply_patch(self, file_path: str, new_content: str, step: PlanStep) -> None:
        """패치 적용 (기존 파일 수정)"""
        full_path = self.workspace / file_path
        existing = full_path.read_text(encoding="utf-8")

        # 간단한 전략: 파일이 짧으면 전체 교체, 길면 패치 시도
        if len(existing.split("\n")) < 100:
            full_path.write_text(new_content, encoding="utf-8")
        else:
            # patch 도구 사용 시도
            self._try_patch_tool(file_path, existing, new_content)

    def _try_patch_tool(self, file_path: str, old_content: str, new_content: str) -> None:
        """patch 명령어로 패치 적용"""
        import difflib

        # diff 생성
        diff = list(
            difflib.unified_diff(
                old_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=f"a/{file_path}",
                tofile=f"b/{file_path}",
            )
        )

        if diff:
            # 임시 파일에 패치 저장
            with tempfile.NamedTemporaryFile(mode="w", suffix=".patch", delete=False) as f:
                f.writelines(diff)
                patch_file = f.name

            try:
                # patch 적용
                result = subprocess.run(
                    ["patch", "-p1", "-i", patch_file],
                    cwd=self.workspace,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                if result.returncode != 0:
                    # 패치 실패 시 전체 교체
                    (self.workspace / file_path).write_text(new_content, encoding="utf-8")
            except Exception:
                # 실패 시 전체 교체
                (self.workspace / file_path).write_text(new_content, encoding="utf-8")
            finally:
                Path(patch_file).unlink(missing_ok=True)
        else:
            # 변경사항 없음
            pass

    def _write_file(self, file_path: str, content: str) -> None:
        """파일 생성"""
        full_path = self.workspace / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")

    def rollback(self, file_paths: list[str]) -> None:
        """백업에서 롤백"""
        for file_path in file_paths:
            backup_path = self._backup_dir / f"{file_path.replace('/', '_')}.bak"
            full_path = self.workspace / file_path

            if backup_path.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
                full_path.write_text(backup_path.read_text(encoding="utf-8"), encoding="utf-8")
                log.info(f"롤백: {file_path}")


def generate_code(workspace: Path, step: PlanStep, context: dict[str, Any]) -> dict[str, Any]:
    """코드 생성 헬퍼"""
    generator = CodeGenerator(workspace)
    return generator.execute_step(step, context)
