"""
자율 코딩 에이전트 - 비평/개선 분석기 (Critic)
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import CritiqueResult, VerificationResult, PlanStep

log = logging.getLogger("autonomous_coding_agent.critic")


class Critic:
    """검증 결과 분석 및 코드 품질 비평"""
    
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
    
    def critique(
        self,
        step: PlanStep,
        verification: VerificationResult,
        context: Dict[str, Any],
    ) -> CritiqueResult:
        """비평 수행"""
        log.info(f"비평 시작: {step.id}")
        
        result = CritiqueResult(step_id=step.id)
        
        # 1. 검증 결과 기반 점수 계산
        result.score = self._calculate_score(verification)
        
        # 2. 이슈 분석
        result.issues = self._analyze_issues(verification, step, context)
        
        # 3. 개선 제안 생성
        result.improvements = self._generate_improvements(verification, step, context)
        
        # 4. 재시도 여부 결정
        result.should_retry = self._should_retry(result, verification)
        if result.should_retry:
            result.retry_feedback = self._generate_retry_feedback(result, verification)
        
        log.info(f"  비평 완료: 점수={result.score:.2f}, 재시도={result.should_retry}")
        
        return result
    
    def _calculate_score(self, verification: VerificationResult) -> float:
        """검증 결과 기반 종합 점수 (0.0 ~ 1.0)"""
        score = 1.0
        
        # 테스트 실패
        if not verification.test_results.get('passed', True):
            score -= 0.4
        
        # 타입 체크 실패
        if not verification.type_results.get('passed', True):
            score -= 0.3
        
        # 린트 경고
        if not verification.lint_results.get('passed', True):
            score -= 0.1
        
        # 커버리지 부족
        if verification.coverage < 80:
            score -= 0.1 * (80 - verification.coverage) / 20
        
        # 에러/경고 수
        score -= len(verification.errors) * 0.05
        score -= len(verification.warnings) * 0.02
        
        return max(0.0, min(1.0, score))
    
    def _analyze_issues(
        self,
        verification: VerificationResult,
        step: PlanStep,
        context: Dict[str, Any],
    ) -> List[Dict[str, Any]]:
        """이슈 분석"""
        issues = []
        
        # 테스트 실패 분석
        if not verification.test_results.get('passed', True):
            stderr = verification.test_results.get('stderr', '')
            issues.extend(self._parse_test_failures(stderr))
        
        # 타입 에러 분석
        if not verification.type_results.get('passed', True):
            stderr = verification.type_results.get('stderr', '')
            issues.extend(self._parse_type_errors(stderr))
        
        # 린트 이슈 분석
        if not verification.lint_results.get('passed', True):
            stderr = verification.lint_results.get('stderr', '')
            issues.extend(self._parse_lint_issues(stderr))
        
        # 커버리지 부족
        if verification.coverage < 80:
            issues.append({
                'type': 'coverage',
                'severity': 'warning' if verification.coverage >= 50 else 'error',
                'message': f'테스트 커버리지 낮음: {verification.coverage:.1f}% (목표: 80%)',
                'suggestion': '테스트 케이스 추가 필요',
            })
        
        return issues
    
    def _parse_test_failures(self, stderr: str) -> List[Dict[str, Any]]:
        """테스트 실패 파싱"""
        issues = []
        
        # Python pytest 실패 패턴
        patterns = [
            (r'FAILED\s+(\S+)::(\w+)', 'test_failure'),
            (r'AssertionError:\s*(.+)', 'assertion_error'),
            (r'Error:\s*(.+)', 'error'),
            (r'FAILED\s+(\S+)', 'test_failed'),
        ]
        
        for pattern, issue_type in patterns:
            for match in re.finditer(pattern, stderr):
                issues.append({
                    'type': issue_type,
                    'severity': 'error',
                    'message': match.group(0)[:200],
                    'suggestion': '테스트 케이스 검토 및 수정 필요',
                })
        
        return issues
    
    def _parse_type_errors(self, stderr: str) -> List[Dict[str, Any]]:
        """타입 에러 파싱"""
        issues = []
        
        patterns = [
            (r'error:\s*(.+)', 'type_error'),
            (r'(\S+:\d+):\s*error:', 'type_error_location'),
            (r'Incompatible types.*', 'incompatible_types'),
            (r'Missing type annotation.*', 'missing_annotation'),
        ]
        
        for pattern, issue_type in patterns:
            for match in re.finditer(pattern, stderr, re.IGNORECASE):
                issues.append({
                    'type': issue_type,
                    'severity': 'error',
                    'message': match.group(0)[:200],
                    'suggestion': '타입 힌트 추가 또는 수정 필요',
                })
        
        return issues
    
    def _parse_lint_issues(self, stderr: str) -> List[Dict[str, Any]]:
        """린트 이슈 파싱"""
        issues = []
        
        patterns = [
            (r'(\S+:\d+:\d+):\s*([WE]\d+)\s*(.+)', 'lint_issue'),
            (r'error:\s*(.+)', 'lint_error'),
            (r'warning:\s*(.+)', 'lint_warning'),
        ]
        
        for pattern, issue_type in patterns:
            for match in re.finditer(pattern, stderr):
                severity = 'error' if 'error' in issue_type else 'warning'
                issues.append({
                    'type': issue_type,
                    'severity': severity,
                    'message': match.group(0)[:200],
                    'suggestion': '코드 스타일 가이드 준수',
                })
        
        return issues
    
    def _generate_improvements(
        self,
        verification: VerificationResult,
        step: PlanStep,
        context: Dict[str, Any],
    ) -> List[str]:
        """개선 제안 생성"""
        improvements = []
        
        if not verification.test_results.get('passed', True):
            improvements.append("실패한 테스트 케이스 분석 및 수정")
            improvements.append("테스트 커버리지 향상을 위한 추가 테스트 작성")
        
        if not verification.type_results.get('passed', True):
            improvements.append("타입 힌트 추가 및 타입 에러 수정")
            improvements.append("mypy/pyright 설정 검토")
        
        if not verification.lint_results.get('passed', True):
            improvements.append("린트 규칙 준수 (포맷팅, 네이밍, 임포트 순서)")
            improvements.append("자동 포맷터 실행 (black, prettier, gofmt 등)")
        
        if verification.coverage < 80:
            improvements.append(f"커버리지 {verification.coverage:.1f}% → 80% 이상으로 향상")
            improvements.append("경계값, 예외 케이스 테스트 추가")
        
        # 일반적인 개선 사항
        improvements.extend([
            "문서화(docstring, 주석) 보강",
            "에러 처리 로직 강화",
            "로깅 추가로 디버깅 용이성 향상",
        ])
        
        return improvements[:5]  # 상위 5개만
    
    def _should_retry(self, critique: CritiqueResult, verification: VerificationResult) -> bool:
        """재시도 여부 결정"""
        # 점수가 낮거나 치명적 에러가 있으면 재시도
        if critique.score < 0.6:
            return True
        
        # 치명적 에러가 있으면 재시도
        if verification.errors:
            return True
        
        # 테스트 실패가 있으면 재시도
        if not verification.test_results.get('passed', True):
            return True
        
        return False
    
    def _generate_retry_feedback(
        self,
        critique: CritiqueResult,
        verification: VerificationResult,
    ) -> str:
        """재시도용 피드백 생성"""
        feedback_parts = [
            f"이전 시도 점수: {critique.score:.2f}/1.0",
            f"발견된 이슈: {len(critique.issues)}개",
        ]
        
        if verification.errors:
            feedback_parts.append(f"치명적 에러: {len(verification.errors)}개")
            for err in verification.errors[:3]:
                feedback_parts.append(f"  - {err[:100]}")
        
        if critique.issues:
            feedback_parts.append("주요 이슈:")
            for issue in critique.issues[:3]:
                feedback_parts.append(f"  - [{issue['severity']}] {issue['message'][:80]}")
        
        if critique.improvements:
            feedback_parts.append("개선 방향:")
            for imp in critique.improvements[:3]:
                feedback_parts.append(f"  - {imp}")
        
        return "\n".join(feedback_parts)
    
    def analyze_code_quality(self, file_path: Path) -> Dict[str, Any]:
        """파일 단위 코드 품질 분석"""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            return {}
        
        lines = content.split('\n')
        
        metrics = {
            'total_lines': len(lines),
            'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
            'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
            'blank_lines': len([l for l in lines if not l.strip()]),
            'max_line_length': max((len(l) for l in lines), default=0),
            'avg_line_length': sum(len(l) for l in lines) / max(len(lines), 1),
            'functions': len([l for l in lines if l.strip().startswith('def ') or l.strip().startswith('async def ')]),
            'classes': len([l for l in lines if l.strip().startswith('class ')]),
        }
        
        # 복잡도 추정 (간단한 휴리스틱)
        complexity_indicators = [
            'if ', 'elif ', 'for ', 'while ', 'try:', 'except ', 'with ',
            'and ', 'or ', 'not ', '?', 'match ', 'case ',
        ]
        complexity = sum(
            content.count(indicator) for indicator in complexity_indicators
        )
        metrics['estimated_complexity'] = complexity
        
        return metrics


def run_critique(
    step: PlanStep,
    verification: VerificationResult,
    workspace: Path,
    context: Dict[str, Any],
) -> CritiqueResult:
    """비평 헬퍼"""
    critic = Critic(workspace)
    return critic.critique(step, verification, context)