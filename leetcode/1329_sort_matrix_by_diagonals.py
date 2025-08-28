# 1329_sort_matrix_by_diagonals.py
# -----------------------------------------------------
# ✅ 제목: Sort Matrix by Diagonals
# ✅ 문제 설명(요약):
# - 좌상단→우하단 대각선(키: i - j)별로 원소를 모아 정렬한 뒤, 같은 대각선 위치에 다시 채워 넣는다.
#
# ✅ 입력 형식(요지):
# - grid: List[List[int]]  (일반적으로 m×n 직사각형 가능)
#
# ✅ 규칙 요약:
# 1) 같은 대각선의 원소는 i - j 값이 동일하다.
# 2) 각 대각선을 오름차순으로 정렬해 원래 자리 순서(행 증가, 열 증가)대로 채운다.
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        n = len(grid)                                   # (주의) 현재 구현은 정사각형만 가정
        diag = defaultdict(list)

        for i, row in enumerate(grid):                  # 대각선별로 값 수집: 키는 i-j
            for j, num in enumerate(row):
                diag[i-j].append(num)
        
        for i in range(n-1):                            # (비고) 비음수 대각선 정렬(현재는 오름차순)
            diag[i].sort()
        for j in range(-1, -n+1, -1):                   # (비고) 음수 대각선 정렬(현재는 내림차순)
            diag[j].sort(reverse=True)
        
        mat = [[0] * n for _ in range(n)]               # (주의) m×n 일반 케이스 미지원
        
        for i in range(n):                              # 수집한 대각선에서 pop() 하며 채우기
            for j in range(n):
                mat[i][j] = diag[i-j].pop()

        return mat

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 대각선 키(i-j)로 그룹화 후 정렬·재배치하는 큰 흐름은 적절.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (핵심) **오름차순 채우기 일관성**:
#   - 현재 구현은 키 ≥ 0 대각선을 오름차순 정렬 후 pop()으로 뒤에서 꺼내므로
#     그 대각선은 **내림차순**으로 채워집니다. 반면 음수 키는 reverse 정렬 + pop()으로
#     **오름차순**이 되어 **대각선마다 정렬 방향이 달라지는 문제**가 발생합니다.
#   - 해결 가이드(중 하나 선택):
#     1) 모든 대각선 리스트를 `sort(reverse=True)`로 정렬하고 `pop()` → 오름차순 채움.
#     2) 모든 대각선을 `sort()`로 정렬하고 `pop(0)` → 비효율(O(L))이라 비추.
#     3) 각 대각선을 min-heap으로 관리하여 `heappop()`로 채우기.
# - (범용성) 입력이 **m×n 직사각형**일 수 있는데, 현재 코드는 n×n에 고정됨.
#   - `m, n = len(grid), len(grid[0])`로 받고, 결과도 m×n로 생성해야 안전.
#
# 📚 사용된/필수 개념(최소):
# - 대각선 분류 키: i - j
# - 리스트 정렬/힙으로 대각선별 정렬
# - 시간복잡도: O(mn log(min(m,n))) / 공간 O(mn)
