"""
자율 코딩 에이전트 - 코드베이스 탐색기 (Explorer)
"""

from __future__ import annotations

import ast
import logging
import os
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from .models import CodeSymbol, ExploreResult, FileInfo

log = logging.getLogger("autonomous_coding_agent.explorer")


class CodeExplorer:
    """코드베이스 탐색 및 분석"""
    
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._file_cache: Dict[str, str] = {}
        self._ast_cache: Dict[str, ast.AST] = {}
    
    def explore(self, target_paths: Optional[List[str]] = None) -> ExploreResult:
        """전체 코드베이스 탐색"""
        log.info(f"코드베이스 탐색 시작: {self.workspace}")
        
        result = ExploreResult()
        
        # 1. 파일 수집
        files = self._collect_files(target_paths)
        log.info(f"  발견된 파일: {len(files)}개")
        
        # 2. 각 파일 분석
        for file_path in files:
            try:
                file_info = self._analyze_file(file_path)
                result.files.append(file_info)
                
                # 심볼 추출
                symbols = self._extract_symbols(file_path, file_info)
                result.symbols.extend(symbols)
                
                # 임포트 그래프 구성
                if file_info.imports:
                    result.import_graph[file_info.path] = file_info.imports
                    
            except Exception as e:
                log.warning(f"파일 분석 실패 {file_path}: {e}")
        
        # 3. 호출 그래프 구성 (심볼 간 참조)
        result.call_graph = self._build_call_graph(result.symbols)
        
        # 4. 진입점 식별
        result.entry_points = self._find_entry_points(result.files, result.symbols)
        
        # 5. 설정/테스트 파일 식별
        result.config_files = self._find_config_files(result.files)
        result.test_files = self._find_test_files(result.files)
        
        log.info(f"  심볼: {len(result.symbols)}개, 임포트 엣지: {sum(len(v) for v in result.import_graph.values())}개")
        
        return result
    
    def _collect_files(self, target_paths: Optional[List[str]] = None) -> List[Path]:
        """분석 대상 파일 수집"""
        files = []
        
        # 제외 패턴
        exclude_dirs = {
            '__pycache__', '.git', '.venv', 'venv', 'env', 'node_modules',
            'dist', 'build', '.pytest_cache', '.mypy_cache', '.ruff_cache',
            'target', 'vendor', '.idea', '.vscode', '__MACOSX'
        }
        exclude_patterns = {
            '*.pyc', '*.pyo', '*.pyd', '*.so', '*.dll', '*.dylib',
            '*.min.js', '*.min.css', '*.map', '*.lock',
            'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml',
            'Cargo.lock', 'go.sum', 'poetry.lock', 'uv.lock'
        }
        
        search_paths = [self.workspace / p for p in target_paths] if target_paths else [self.workspace]
        
        for search_path in search_paths:
            if not search_path.exists():
                continue
                
            for root, dirs, filenames in os.walk(search_path):
                # 제외 디렉토리 필터링
                dirs[:] = [d for d in dirs if d not in exclude_dirs]
                
                for filename in filenames:
                    # 제외 패턴 체크
                    skip = False
                    for pattern in exclude_patterns:
                        if self._match_pattern(filename, pattern):
                            skip = True
                            break
                    if skip:
                        continue
                    
                    # 코드 파일만 (확장자 기반)
                    if self._is_code_file(filename):
                        files.append(Path(root) / filename)
        
        return files
    
    def _match_pattern(self, filename: str, pattern: str) -> bool:
        """글로브 패턴 매칭"""
        import fnmatch
        return fnmatch.fnmatch(filename, pattern)
    
    def _is_code_file(self, filename: str) -> bool:
        """코드 파일 여부"""
        code_extensions = {
            '.py', '.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte',
            '.go', '.rs', '.java', '.kt', '.kts', '.scala',
            '.cpp', '.cc', '.cxx', '.c', '.h', '.hpp',
            '.cs', '.fs', '.vb',
            '.rb', '.php', '.pl', '.pm',
            '.swift', '.m', '.mm',
            '.r', '.R', '.jl',
            '.sh', '.bash', '.zsh', '.fish',
            '.ps1', '.bat', '.cmd',
            '.sql', '.graphql', '.gql',
            '.yaml', '.yml', '.toml', '.ini', '.cfg', '.conf',
            '.json', '.jsonc', '.xml', '.html', '.htm',
            '.css', '.scss', '.sass', '.less',
            '.md', '.rst', '.txt',
            '.dockerfile', '.Dockerfile',
            '.tf', '.tfvars',
        }
        return any(filename.endswith(ext) for ext in code_extensions)
    
    def _analyze_file(self, file_path: Path) -> FileInfo:
        """파일 메타데이터 분석"""
        rel_path = file_path.relative_to(self.workspace)
        stat = file_path.stat()
        
        # 언어 감지
        language = self._detect_language(file_path)
        
        # 파일 내용 읽기
        try:
            content = file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                content = file_path.read_text(encoding='latin-1')
            except Exception:
                content = ""
        
        lines = content.count('\n') + 1 if content else 0
        
        # 임포트 추출
        imports = self._extract_imports(file_path, content, language)
        
        return FileInfo(
            path=str(rel_path),
            language=language,
            size=stat.st_size,
            lines=lines,
            imports=imports,
        )
    
    def _detect_language(self, file_path: Path) -> str:
        """언어 감지"""
        ext = file_path.suffix.lower()
        language_map = {
            '.py': 'python',
            '.js': 'javascript', '.jsx': 'javascript',
            '.ts': 'typescript', '.tsx': 'typescript',
            '.vue': 'vue', '.svelte': 'svelte',
            '.go': 'go',
            '.rs': 'rust',
            '.java': 'java',
            '.kt': 'kotlin', '.kts': 'kotlin',
            '.scala': 'scala',
            '.cpp': 'cpp', '.cc': 'cpp', '.cxx': 'cpp', '.c': 'c', '.h': 'c', '.hpp': 'cpp',
            '.cs': 'csharp',
            '.fs': 'fsharp', '.vb': 'vbnet',
            '.rb': 'ruby',
            '.php': 'php',
            '.swift': 'swift',
            '.r': 'r', '.R': 'r', '.jl': 'julia',
            '.sh': 'bash', '.bash': 'bash', '.zsh': 'zsh', '.fish': 'fish',
            '.ps1': 'powershell', '.bat': 'batch', '.cmd': 'batch',
            '.sql': 'sql',
            '.graphql': 'graphql', '.gql': 'graphql',
            '.yaml': 'yaml', '.yml': 'yaml',
            '.toml': 'toml',
            '.ini': 'ini', '.cfg': 'ini', '.conf': 'ini',
            '.json': 'json', '.jsonc': 'json',
            '.xml': 'xml',
            '.html': 'html', '.htm': 'html',
            '.css': 'css', '.scss': 'scss', '.sass': 'sass', '.less': 'less',
            '.md': 'markdown', '.rst': 'rst',
            '.dockerfile': 'dockerfile',
            '.tf': 'terraform', '.tfvars': 'terraform',
        }
        return language_map.get(ext, 'unknown')
    
    def _extract_imports(self, file_path: Path, content: str, language: str) -> List[str]:
        """임포트 구문 추출"""
        imports = []
        
        if language == 'python':
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            imports.append(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        module = node.module or ''
                        for alias in node.names:
                            imports.append(f"{module}.{alias.name}" if module else alias.name)
            except SyntaxError:
                pass
                
        elif language in ('javascript', 'typescript'):
            # 간단한 regex 기반 추출
            import re
            # import ... from ...
            for match in re.finditer(r'import\s+(?:[^;\n]*\s+from\s+)?[\'"]([^\'"]+)[\'"]', content):
                imports.append(match.group(1))
            # require(...)
            for match in re.finditer(r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)', content):
                imports.append(match.group(1))
                
        elif language == 'go':
            import re
            for match in re.finditer(r'import\s+(?:\(([^)]+)\)|[\'"]([^\'"]+)[\'"])', content):
                if match.group(1):
                    for line in match.group(1).split('\n'):
                        line = line.strip().strip('"')
                        if line:
                            imports.append(line)
                elif match.group(2):
                    imports.append(match.group(2))
                    
        elif language == 'rust':
            import re
            for match in re.finditer(r'use\s+([^;]+);', content):
                imports.append(match.group(1).strip())
        
        return imports
    
    def _extract_symbols(self, file_path: Path, file_info: FileInfo) -> List[CodeSymbol]:
        """심볼(함수, 클래스 등) 추출"""
        symbols = []
        
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            return symbols
        
        if file_info.language == 'python':
            symbols.extend(self._extract_python_symbols(file_path, content))
        elif file_info.language in ('javascript', 'typescript'):
            symbols.extend(self._extract_js_ts_symbols(file_path, content, file_info.language))
        elif file_info.language == 'go':
            symbols.extend(self._extract_go_symbols(file_path, content))
        elif file_info.language == 'rust':
            symbols.extend(self._extract_rust_symbols(file_path, content))
        
        return symbols
    
    def _extract_python_symbols(self, file_path: Path, content: str) -> List[CodeSymbol]:
        """Python 심볼 추출 (AST 기반)"""
        symbols = []
        rel_path = file_path.relative_to(self.workspace)
        
        try:
            tree = ast.parse(content)
        except SyntaxError:
            return symbols
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                symbols.append(CodeSymbol(
                    name=node.name,
                    type='function' if not self._is_method(node, tree) else 'method',
                    file_path=str(rel_path),
                    line_start=node.lineno,
                    line_end=node.end_lineno or node.lineno,
                    signature=self._get_function_signature(node),
                    docstring=ast.get_docstring(node) or '',
                ))
            elif isinstance(node, ast.ClassDef):
                symbols.append(CodeSymbol(
                    name=node.name,
                    type='class',
                    file_path=str(rel_path),
                    line_start=node.lineno,
                    line_end=node.end_lineno or node.lineno,
                    signature=f"class {node.name}",
                    docstring=ast.get_docstring(node) or '',
                ))
            elif isinstance(node, ast.AsyncFunctionDef):
                symbols.append(CodeSymbol(
                    name=node.name,
                    type='async_function' if not self._is_method(node, tree) else 'async_method',
                    file_path=str(rel_path),
                    line_start=node.lineno,
                    line_end=node.end_lineno or node.lineno,
                    signature=self._get_async_function_signature(node),
                    docstring=ast.get_docstring(node) or '',
                ))
        
        return symbols
    
    def _is_method(self, node: ast.FunctionDef, tree: ast.AST) -> bool:
        """클래스 내 메서드인지 확인"""
        for parent in ast.walk(tree):
            if isinstance(parent, ast.ClassDef):
                for item in parent.body:
                    if item is node:
                        return True
        return False
    
    def _get_function_signature(self, node: ast.FunctionDef) -> str:
        """함수 시그니처 문자열 생성"""
        args = []
        for arg in node.args.args:
            arg_str = arg.arg
            if arg.annotation:
                arg_str += f": {ast.unparse(arg.annotation) if hasattr(ast, 'unparse') else ''}"
            args.append(arg_str)
        
        if node.args.vararg:
            args.append(f"*{node.args.vararg.arg}")
        if node.args.kwarg:
            args.append(f"**{node.args.kwarg.arg}")
        
        returns = f" -> {ast.unparse(node.returns)}" if node.returns and hasattr(ast, 'unparse') else ""
        
        return f"def {node.name}({', '.join(args)}){returns}"
    
    def _get_async_function_signature(self, node: ast.AsyncFunctionDef) -> str:
        """비동기 함수 시그니처"""
        return "async " + self._get_function_signature(node)
    
    def _extract_js_ts_symbols(self, file_path: Path, content: str, language: str) -> List[CodeSymbol]:
        """JavaScript/TypeScript 심볼 추출 (간단한 regex)"""
        symbols = []
        rel_path = file_path.relative_to(self.workspace)
        import re
        
        # function 선언
        for match in re.finditer(
            r'(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='function',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"function {match.group(1)}({match.group(2)})",
            ))
        
        # 화살표 함수 (const/let/var)
        for match in re.finditer(
            r'(?:export\s+)?(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(([^)]*)\)\s*=>',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='arrow_function',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"const {match.group(1)} = ({match.group(2)}) =>",
            ))
        
        # 클래스
        for match in re.finditer(
            r'(?:export\s+)?class\s+(\w+)(?:\s+extends\s+\w+)?\s*\{',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='class',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"class {match.group(1)}",
            ))
        
        return symbols
    
    def _extract_go_symbols(self, file_path: Path, content: str) -> List[CodeSymbol]:
        """Go 심볼 추출"""
        symbols = []
        rel_path = file_path.relative_to(self.workspace)
        import re
        
        # 함수
        for match in re.finditer(
            r'func\s+(?:\([^)]+\)\s+)?(\w+)\s*\(([^)]*)\)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='function',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"func {match.group(1)}({match.group(2)})",
            ))
        
        # 구조체
        for match in re.finditer(
            r'type\s+(\w+)\s+struct\s*\{',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='struct',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"type {match.group(1)} struct",
            ))
        
        # 인터페이스
        for match in re.finditer(
            r'type\s+(\w+)\s+interface\s*\{',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='interface',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"type {match.group(1)} interface",
            ))
        
        return symbols
    
    def _extract_rust_symbols(self, file_path: Path, content: str) -> List[CodeSymbol]:
        """Rust 심볼 추출"""
        symbols = []
        rel_path = file_path.relative_to(self.workspace)
        import re
        
        # 함수
        for match in re.finditer(
            r'(?:pub\s+)?(?:async\s+)?fn\s+(\w+)\s*\(([^)]*)\)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='function',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"fn {match.group(1)}({match.group(2)})",
            ))
        
        # 구조체
        for match in re.finditer(
            r'(?:pub\s+)?struct\s+(\w+)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='struct',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"struct {match.group(1)}",
            ))
        
        # 열거형
        for match in re.finditer(
            r'(?:pub\s+)?enum\s+(\w+)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='enum',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"enum {match.group(1)}",
            ))
        
        # 트레이트
        for match in re.finditer(
            r'(?:pub\s+)?trait\s+(\w+)',
            content
        ):
            symbols.append(CodeSymbol(
                name=match.group(1),
                type='trait',
                file_path=str(rel_path),
                line_start=content[:match.start()].count('\n') + 1,
                line_end=content[:match.end()].count('\n') + 1,
                signature=f"trait {match.group(1)}",
            ))
        
        return symbols
    
    def _build_call_graph(self, symbols: List[CodeSymbol]) -> Dict[str, List[str]]:
        """호출 그래프 구성 (간단한 휴리스틱)"""
        call_graph = defaultdict(list)
        
        # 파일별 심볼 인덱스
        file_symbols = defaultdict(list)
        for sym in symbols:
            file_symbols[sym.file_path].append(sym)
        
        # 각 파일 내용 읽어서 함수 호출 패턴 찾기
        for file_path, syms in file_symbols.items():
            full_path = self.workspace / file_path
            try:
                content = full_path.read_text(encoding='utf-8')
            except Exception:
                continue
            
            for sym in syms:
                if sym.type in ('function', 'method', 'async_function', 'async_method'):
                    # 함수 내부에서 다른 심볼 이름 호출 패턴 찾기
                    # 간단화: 심볼 이름이 코드에 나타나는지 체크
                    for other_sym in symbols:
                        if other_sym.name != sym.name and other_sym.name in content:
                            # 같은 파일 내 호출이거나 임포트된 것
                            call_graph[sym.name].append(other_sym.name)
        
        return dict(call_graph)
    
    def _find_entry_points(self, files: List[FileInfo], symbols: List[CodeSymbol]) -> List[str]:
        """진입점 찾기 (main, CLI, 테스트 등)"""
        entry_points = []
        
        for sym in symbols:
            name_lower = sym.name.lower()
            if name_lower in ('main', 'run', 'cli', 'execute', 'handler', 'lambda_handler'):
                entry_points.append(f"{sym.file_path}:{sym.name}")
        
        # 파일명 기반
        for file_info in files:
            name_lower = Path(file_info.path).stem.lower()
            if name_lower in ('main', 'cli', 'app', 'server', 'worker', 'handler', 'lambda'):
                entry_points.append(file_info.path)
            if name_lower.startswith('test_') or name_lower.endswith('_test'):
                entry_points.append(file_info.path)
        
        return list(set(entry_points))
    
    def _find_config_files(self, files: List[FileInfo]) -> List[str]:
        """설정 파일 찾기"""
        config_names = {
            'pyproject.toml', 'setup.py', 'setup.cfg', 'requirements.txt', 'Pipfile', 'poetry.lock',
            'package.json', 'tsconfig.json', 'eslint.config.js', 'prettier.config.js',
            'Cargo.toml', 'go.mod', 'pom.xml', 'build.gradle', 'build.gradle.kts',
            '.env', '.env.example', '.env.local',
            'docker-compose.yml', 'docker-compose.yaml', 'Dockerfile',
            '.github/workflows', '.gitlab-ci.yml', 'jenkinsfile',
            'pyrightconfig.json', 'mypy.ini', 'ruff.toml', '.ruff.toml',
            'jest.config.js', 'vitest.config.ts', 'playwright.config.ts',
        }
        
        configs = []
        for file_info in files:
            if Path(file_info.path).name in config_names:
                configs.append(file_info.path)
            # 디렉토리 기반 체크
            for config in config_names:
                if config in file_info.path:
                    configs.append(file_info.path)
                    break
        
        return list(set(configs))
    
    def _find_test_files(self, files: List[FileInfo]) -> List[str]:
        """테스트 파일 찾기"""
        test_files = []
        
        for file_info in files:
            name = Path(file_info.path).name
            stem = Path(file_info.path).stem
            
            # 패턴 매칭
            is_test = (
                name.startswith('test_') or
                name.endswith('_test.py') or
                name.endswith('.test.js') or
                name.endswith('.test.ts') or
                name.endswith('.spec.js') or
                name.endswith('.spec.ts') or
                stem.endswith('_test') or
                stem.endswith('Test') or
                'test' in Path(file_info.path).parts or
                '__tests__' in Path(file_info.path).parts or
                'tests' in Path(file_info.path).parts
            )
            
            if is_test:
                test_files.append(file_info.path)
        
        return test_files
    
    def find_related_files(self, symbol_name: str, explore_result: ExploreResult) -> List[str]:
        """심볼과 관련된 파일들 찾기"""
        related = []
        
        # 1. 심볼이 정의된 파일
        for sym in explore_result.symbols:
            if sym.name == symbol_name:
                related.append(sym.file_path)
        
        # 2. 해당 심볼을 임포트하는 파일들
        for file_path, imports in explore_result.import_graph.items():
            for imp in imports:
                if symbol_name in imp or imp.endswith(f".{symbol_name}"):
                    related.append(file_path)
        
        # 3. 호출 그래프에서 참조하는 것들
        for caller, callees in explore_result.call_graph.items():
            if symbol_name in callees:
                # caller가 정의된 파일 찾기
                for sym in explore_result.symbols:
                    if sym.name == caller:
                        related.append(sym.file_path)
        
        return list(set(related))
    
    def get_file_content(self, file_path: str) -> str:
        """파일 내용 읽기 (캐시)"""
        if file_path in self._file_cache:
            return self._file_cache[file_path]
        
        full_path = self.workspace / file_path
        try:
            content = full_path.read_text(encoding='utf-8')
            self._file_cache[file_path] = content
            return content
        except Exception as e:
            log.error(f"파일 읽기 실패 {file_path}: {e}")
            return ""


def explore_codebase(workspace: Path, target_paths: Optional[List[str]] = None) -> ExploreResult:
    """탐색 실행 헬퍼"""
    explorer = CodeExplorer(workspace)
    return explorer.explore(target_paths)