# 0037_sudoku_solver.py
# -----------------------------------------------------
# ✅ 제목: Sudoku Solver
# ✅ 문제 설명(요약):
# - 9x9 스도쿠 보드를 규칙(행/열/3x3 박스 중복 금지)에 맞게 완성한다.
# - 해는 항상 존재하며, 보드를 제자리(in-place)에서 수정해야 한다.
#
# ✅ 입력 형식(요지):
# - board: List[List[str]] (각 칸은 '1'~'9' 또는 '.')
#
# ✅ 규칙 요약:
# 1) 행 r에 같은 숫자 2개 이상 금지
# 2) 열 c에 같은 숫자 2개 이상 금지
# 3) 3x3 박스 b=((r//3)*3+(c//3))에 같은 숫자 2개 이상 금지
#
# ✅ 입출력 예시(1개):
# - 입력 보드가 유효하면 하나의 해로 채워진 보드를 반환(제자리 수정)
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]                   # 각 행에 이미 있는 숫자 집합
        cols = [set() for _ in range(9)]                   # 각 열에 이미 있는 숫자 집합
        boxes = [set() for _ in range(9)]                  # 각 3x3 박스에 이미 있는 숫자 집합
        empties = []                                       # 빈 칸 좌표 목록

        for r in range(9):                                 # 초기 스캔
            for c in range(9):
                v = board[r][c]
                if v == '.':                               # 빈 칸이면 목록에 추가
                    empties.append((r, c))
                else:
                    b = (r//3)*3 + (c//3)                  # 박스 인덱스
                    rows[r].add(v); cols[c].add(v); boxes[b].add(v)

        def backtrack(k=0):                                # k번째 빈 칸을 채우는 재귀
            if k == len(empties):                          # 모두 채웠으면 성공
                return True
            r, c = empties[k]                              # 현재 채울 칸
            b = (r//3)*3 + (c//3)                          # 해당 박스
            for ch in '123456789':                         # 1~9 시도
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c] = ch                       # 배치
                    rows[r].add(ch); cols[c].add(ch); boxes[b].add(ch)
                    if backtrack(k+1): return True         # 다음 칸으로 진행
                    rows[r].remove(ch); cols[c].remove(ch); boxes[b].remove(ch)
                    board[r][c] = '.'                      # 실패 시 원복
            return False                                   # 어떤 숫자도 안 되면 실패(백트랙)

        backtrack()                                        # 풀이 시작

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 백트래킹 + 행/열/박스 집합으로 무난히 통과 (최악 케이스에서는 백트래킹 분기 많을 수 있음).
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (잠재) 탐색 순서가 고정(k 순서)라 가지가 커질 수 있음.
#   → 개선 아이디어: MRV(가장 후보 적은 칸 먼저 선택), 비트마스크로 후보 계산/갱신 O(1).
#
# 📚 사용된/필수 개념(최소):
# - 백트래킹(DFS)과 상태 원복
# - 행/열/박스 제약 검사(set)
# - 시간복잡도: 최악 지수적(하지만 문제 보장상 실전 통과)
# - 공간복잡도: O(1) (보드 크기 고정, 보조 자료구조 상수 크기)
