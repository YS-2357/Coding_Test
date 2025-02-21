# 백준 11054번: 가장 긴 바이토닉 부분 수열 (다이나믹 프로그래밍 - O(N^2))
# -----------------------------------------------------
# ✅ 문제 설명:
# - 주어진 수열에서 증가하는 부분 수열 + 감소하는 부분 수열을 결합하여 가장 긴 바이토닉 부분 수열을 찾는 문제.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 수열의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# - 두 번째 줄에 N개의 정수가 주어진다. (1 ≤ 정수 ≤ 1,000)
#
# ✅ 출력 형식:
# - 가장 긴 바이토닉 부분 수열의 길이를 출력한다.
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   10
#   1 5 2 1 4 3 4 5 2 1
# 🔹 예제 출력 1:
#   7
# -----------------------------------------------------

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# ✅ DP 배열 초기화
ascending = [1] * N  # 증가하는 부분 수열 길이 저장
descending = [1] * N  # 감소하는 부분 수열 길이 저장

# ✅ LIS 계산 (왼쪽에서 오른쪽으로 증가하는 부분 수열)
for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:  # 증가 조건
            ascending[i] = max(ascending[i], ascending[j] + 1)

# ✅ LDS 계산 (오른쪽에서 왼쪽으로 감소하는 부분 수열)
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):        
        if nums[j] < nums[i]:  # 감소 조건
            descending[i] = max(descending[i], descending[j] + 1)

# ✅ 결과 계산 (각 지점을 중심으로 증가 + 감소를 합침)
dp = [0] * N
for i in range(N):
    dp[i] = ascending[i] + descending[i] - 1  # 중복된 i값 제거

# ✅ 최종 결과 출력 (가장 긴 바이토닉 부분 수열)
print(max(dp))

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `descending` 계산 오류 수정 → `if nums[j] > nums[i]` → `if nums[j] < nums[i]`로 변경
#    🔹 감소하는 부분 수열을 찾을 때, **기존 코드에서는 증가하는 조건으로 비교하여 잘못된 결과가 나왔음**
# 2. ✅ `dp[i]` 계산 검증 완료 → `ascending[i] + descending[i] - 1`이 정확하게 적용됨.
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
