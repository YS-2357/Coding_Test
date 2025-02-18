# 백준 11053번: 가장 긴 증가하는 부분 수열 (LIS - Longest Increasing Subsequence, DP)
# 문제 설명:
# - 주어진 수열에서 가장 긴 증가하는 부분 수열(LIS)의 길이를 구하는 문제
# - 증가하는 부분 수열이란, 현재 값보다 큰 값이 연속하여 등장하는 부분 수열을 의미
# - 결과는 정수로 출력

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 수열의 길이 입력
nums = list(map(int, sys.stdin.readline().split()))  # 수열 입력

# ✅ DP 테이블 초기화 (각 요소는 최소 자기 자신만으로 LIS 길이 1을 가짐)
dp = [1] * N

# ✅ 점화식을 사용한 DP 테이블 채우기 (O(N^2) 방식)
for i in range(1, N):
    for j in range(i):  # i 이전의 값들과 비교
        if nums[j] < nums[i]:  # 증가하는 부분 수열이 성립하는 경우
            dp[i] = max(dp[i], dp[j] + 1)  # 이전 수열 중 최댓값을 갱신

# ✅ 결과 출력 (가장 긴 증가하는 부분 수열의 길이)
print(max(dp))

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `dp` 크기 설정 문제 해결:
#    - 기존 코드에서 `dp = [1] * (N + 1)`이었으나, `dp = [1] * N`으로 수정하여 올바른 크기로 설정
#
# 2. ✅ `for j in range(i+1, N+1):` → `for j in range(i):` 수정:
#    - LIS 점화식에서는 `j`가 `i`보다 앞에 있어야 하므로 `j`는 `0`부터 `i-1`까지 탐색해야 함
#
# 3. ✅ `if nums[i] < nums[j]:`의 비교 순서 문제 해결:
#    - `i`가 `j`보다 크므로, `nums[j] < nums[i]`가 되어야 함.
#
# 4. ✅ `print(dp[N])` → `print(max(dp))` 수정:
#    - `dp[N]`에는 LIS의 길이가 저장되지 않으며, `max(dp)`가 올바른 LIS 길이를 반환
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
