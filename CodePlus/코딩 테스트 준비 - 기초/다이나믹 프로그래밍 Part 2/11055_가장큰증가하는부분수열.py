# 백준 11055번: 가장 큰 증가하는 부분 수열 (다이나믹 프로그래밍 - O(N^2))
# -----------------------------------------------------
# ✅ 문제 설명:
# - 주어진 수열에서 증가하는 부분 수열을 선택하여 합이 가장 큰 값을 구하는 문제.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 수열의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# - 두 번째 줄에 N개의 정수가 주어진다. (1 ≤ 정수 ≤ 1,000)
#
# ✅ 출력 형식:
# - 가장 큰 증가하는 부분 수열의 합을 출력한다.
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   10
#   1 100 2 50 60 3 5 6 7 8
# 🔹 예제 출력 1:
#   113
# -----------------------------------------------------

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# ✅ DP 배열 초기화 (각 원소 자체가 최소 부분 수열)
dp = [nums[i] for i in range(N)]

# ✅ DP 테이블 채우기 (O(N^2))
for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:  # 증가하는 부분 수열 조건
            dp[i] = max(dp[i], dp[j] + nums[i])  # 올바른 DP 업데이트 방식

# ✅ 결과 출력 (최대 증가 부분 수열 합 찾기)
print(max(dp))  # dp 배열에서 최댓값을 찾아 출력

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `dp[i-1]` 비교 오류 수정 → `dp[i] = max(dp[i], dp[j] + nums[i])`로 변경
# 2. ✅ `print(dp[N])` 인덱스 오류 수정 → `print(max(dp))`로 변경
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
