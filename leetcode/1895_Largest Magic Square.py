# 1895_Largest Magic Square.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1895. Largest Magic Square
# 🏷️ 유형: 누적합 / 브루트포스 / 대각선 누적
#
# ✅ 문제 설명(요약):
#   - grid에서 k×k 정사각형을 골랐을 때,
#   - 모든 행의 합, 모든 열의 합, 두 대각선 합이 모두 같은 경우를 “매직 스퀘어”로 본다.
#   - 가능한 k의 최댓값을 반환한다.
#
# ✅ 입력 형식(요지):
#   - grid: List[List[int]]  (m×n 정수 격자)
#
# ✅ 규칙 요약:
#   - k는 1 이상이며, 1×1은 항상 매직 스퀘어다.
#   - 가장 큰 k를 찾아 반환한다.
#
# 🧠 핵심 불변식(Invariant):
#   - k×k 후보의 기준 합(diag_sum 또는 s)을 하나 정하면,
#     모든 행/열/대각선이 그 합과 같아야 한다.
#   - 누적합을 쓰면 행/열/대각선 합을 O(1)로 계산할 수 있어 큰 k부터 검사하기에 유리하다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#
# -----------------------------------------------------
# ✅ 정답 1 (Prefix Sum 최적화 버전)

from itertools import accumulate                              # 행 누적합 계산을 위해 accumulate를 임포트
from typing import List                                       # 타입 힌트를 위해 List를 임포트

class Solution:                                               # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def largestMagicSquare(self, grid: List[List[int]]) -> int:  # 가장 큰 매직 스퀘어의 한 변 길이를 반환하는 함수
        m, n = len(grid), len(grid[0])                         # 격자의 행(m)과 열(n) 크기를 저장

        rs = [[0] + list(accumulate(row)) for row in grid]     # 각 행의 prefix sum(rs)을 만들어 행 구간합을 O(1)로 계산
        cs = [[0] * n for _ in range(m + 1)]                   # 각 열의 prefix sum(cs)을 만들기 위한 2D 배열 초기화

        ds = [[0] * (n + 1) for _ in range(m + 1)]             # 주대각선 prefix sum(ds) 배열을 0으로 초기화
        ads = [[0] * (n + 1) for _ in range(m + 1)]            # 부대각선 prefix sum(ads) 배열을 0으로 초기화

        for r in range(m):                                     # 격자의 모든 행 r을 순회
            for c in range(n):                                 # 격자의 모든 열 c를 순회
                x = grid[r][c]                                 # 현재 칸의 값을 x에 저장
                cs[r + 1][c] = cs[r][c] + x                    # 열 prefix sum을 한 칸 아래로 누적해 갱신
                ds[r + 1][c + 1] = ds[r][c] + x                # 주대각선 prefix sum을 왼쪽 위에서 현재로 누적해 갱신
                ads[r + 1][c] = ads[r][c + 1] + x              # 부대각선 prefix sum을 오른쪽 위에서 현재로 누적해 갱신

        for k in range(min(m, n), 0, -1):                      # 가능한 정사각형 크기 k를 큰 값부터 1까지 감소시키며 탐색
            for R in range(k, m + 1):                          # 1-based prefix 공간에서 정사각형의 하단 경계 R을 순회
                for C in range(k, n + 1):                      # 1-based prefix 공간에서 정사각형의 우측 경계 C를 순회

                    diag_sum = ds[R][C] - ds[R - k][C - k]      # 현재 k×k의 주대각선 합을 prefix 차로 계산

                    if ads[R][C - k] - ads[R - k][C] != diag_sum:  # 현재 k×k의 부대각선 합이 주대각선 합과 같은지 확인
                        continue                                # 다르면 매직 스퀘어가 아니므로 다음 후보로 넘어감

                    if any(rs[r][C] - rs[r][C - k] != diag_sum for r in range(R - k, R)):  # 모든 행 구간합이 기준합과 같은지 확인
                        continue                                # 하나라도 다르면 매직 스퀘어가 아니므로 다음 후보로 넘어감

                    if any(cs[R][c] - cs[R - k][c] != diag_sum for c in range(C - k, C)):  # 모든 열 구간합이 기준합과 같은지 확인
                        continue                                # 하나라도 다르면 매직 스퀘어가 아니므로 다음 후보로 넘어감

                    return k                                    # 조건을 모두 만족하면 현재 k가 최대이므로 즉시 반환

        return 1                                                # 어떤 k>1도 없으면 최소값 1을 반환

# Time = O(m n min(m, n)), Space = O(m n)                       # 시간/공간 복잡도 요약 주석

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답 1: Accepted.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 행/열/대각선 누적합(prefix sums) 기반 빠른 검증 + 큰 k부터 탐색.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(m * n * min(m, n))
#   - 공간: O(m * n)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - k를 큰 값부터 줄이는 전략은 유지하되, 후보 위치를 줄이는 휴리스틱/조기 가지치기 최적화도 가능하다.

# -----------------------------------------------------
# ✅ 정답 2 (직접 합 계산 버전)

class Solution:                                               # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def largestMagicSquare(self, grid: List[List[int]]) -> int:  # 가장 큰 매직 스퀘어의 한 변 길이를 반환하는 함수
        m, n = len(grid), len(grid[0])                         # 격자의 행(m)과 열(n) 크기를 저장
        res = 1                                                # 가능한 최소 정답은 1이므로 결과를 1로 초기화

        def isValid(i, j, k):                                  # (i, j)를 좌상단으로 하는 k×k가 매직 스퀘어인지 확인하는 함수
            s = None                                           # 기준 합을 저장할 변수로, 첫 행 합을 보고 결정
            for x in range(i, i + k):                          # 후보 정사각형의 모든 행 x를 순회
                row = sum(grid[x][j:j + k])                    # 현재 행의 구간합을 직접 계산
                if s is None:                                  # 기준 합이 아직 정해지지 않았다면
                    s = row                                    # 첫 행 합을 기준 합으로 설정
                elif s != row:                                 # 기준 합과 현재 행 합이 다르면
                    return False                               # 매직 스퀘어가 아니므로 False 반환

            for y in range(j, j + k):                          # 후보 정사각형의 모든 열 y를 순회
                if sum(grid[x][y] for x in range(i, i + k)) != s:  # 현재 열의 합이 기준 합과 같은지 확인
                    return False                               # 다르면 매직 스퀘어가 아니므로 False 반환

            if sum(grid[i + d][j + d] for d in range(k)) != s:  # 주대각선 합이 기준 합과 같은지 확인
                return False                                   # 다르면 매직 스퀘어가 아니므로 False 반환

            if sum(grid[i + d][j + k - 1 - d] for d in range(k)) != s:  # 부대각선 합이 기준 합과 같은지 확인
                return False                                   # 다르면 매직 스퀘어가 아니므로 False 반환

            return True                                        # 모든 조건을 만족하면 True 반환

        for k in range(2, min(m, n) + 1):                      # k=2부터 가능한 최대 크기까지 증가시키며 검사
            for i in range(m - k + 1):                         # 좌상단 행 인덱스 i의 가능한 범위를 순회
                for j in range(n - k + 1):                     # 좌상단 열 인덱스 j의 가능한 범위를 순회
                    if isValid(i, j, k):                       # 현재 (i, j, k)가 매직 스퀘어라면
                        res = k                                # 가능한 최대 크기를 k로 갱신

        return res                                             # 최종적으로 찾은 최대 k를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답 2: Accepted.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 모든 k와 모든 위치를 검사하는 브루트포스 + 행/열/대각선 직접 합 계산.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(m * n * min(m, n) * min(m, n)) 수준으로 커질 수 있음(각 검증에서 합 계산 포함)
#   - 공간: O(1)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 누적합을 도입하면 isValid 내부 합 계산을 O(1)로 줄여 대폭 가속할 수 있다.
