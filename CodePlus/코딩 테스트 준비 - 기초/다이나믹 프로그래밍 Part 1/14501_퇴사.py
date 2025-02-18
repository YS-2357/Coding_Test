# 백준 14501번: 퇴사 (DP - 일정 최적화 문제)
# 문제 설명:
# - 주어진 N일 동안 상담을 수행하여 최대 수익을 얻는 문제
# - 상담을 선택하면 T[i]일 뒤부터 가능하며, P[i]만큼의 수익을 얻을 수 있음
# - 퇴사일(N)을 넘지 않도록 최적의 상담 배치를 찾아야 함

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 일정 기간 (퇴사일)
T = []  # 상담 소요 기간
P = []  # 상담 수익

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

# ✅ DP 테이블 초기화 (각 날짜별 최대 이익 저장)
dp = [0] * (N + 1)

# ✅ 점화식을 사용한 DP 테이블 채우기 (O(N) 방식)
for i in range(N - 1, -1, -1):  # 뒤에서부터 계산
    if i + T[i] <= N:  # 상담이 퇴사일을 넘지 않는 경우만 선택 가능
        dp[i] = max(dp[i + 1], dp[i + T[i]] + P[i])  # 상담을 할 경우 vs 안 할 경우 비교
    else:
        dp[i] = dp[i + 1]  # 상담을 할 수 없으므로 그대로 유지

# ✅ 결과 출력 (최대 이익)
print(max(dp))

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `dp = [0] * N` → `dp = [0] * (N + 1)`으로 수정:
#    - 기존 코드에서 퇴사일을 초과하는 경우를 고려하지 않음.
#    - 해결: `N+1` 크기의 `dp` 테이블을 사용하여 안전하게 저장.
#
# 2. ✅ `if i + T[i] < N:` → `if i + T[i] <= N:`으로 수정:
#    - 마지막 날에 상담을 하는 경우도 고려해야 함.
#    - 해결: `<=` 조건을 포함하여 마지막 날까지 선택 가능하도록 수정.
#
# 3. ✅ `dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])`을 기본값 `dp[i] = dp[i+1]`으로 설정:
#    - `dp[i+T[i]]`이 `N`을 초과할 때 접근 오류가 발생할 수 있으므로,
#      `dp[i] = dp[i+1]`을 기본값으로 설정하여 안전하게 연산.
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
