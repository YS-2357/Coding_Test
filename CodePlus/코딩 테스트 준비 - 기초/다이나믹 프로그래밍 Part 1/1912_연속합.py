# 백준 1912번: 연속합 (Kadane's Algorithm, DP)
# 문제 설명:
# - 주어진 수열에서 연속된 몇 개의 수를 선택하여 만들 수 있는 최대 합을 구하는 문제
# - 연속된 수를 선택해야 하며, 한 개의 숫자만 선택하는 것도 가능함

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 수열의 길이 입력
nums = list(map(int, sys.stdin.readline().split()))  # 수열 입력

# ✅ DP 테이블 초기화 (각 원소를 포함하는 연속합을 저장)
dp = [nums[i] for i in range(N)]

# ✅ 점화식을 사용한 DP 테이블 채우기 (O(N) 방식 - Kadane’s Algorithm)
for i in range(N):
    if i > 0:
        dp[i] = max(dp[i], dp[i-1] + nums[i])  # 이전 값과 합치는 것이 더 나은지 비교

# ✅ 결과 출력 (최대 연속 부분합)
print(max(dp))

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `dp[i] = max(dp[i], dp[i-1] + nums[i])`에서 `i=0`일 때 `dp[i-1]`을 참조하는 오류 발생:
#    - 기존 코드에서는 `dp[-1]`을 참조하여 논리적으로 잘못된 접근이 발생함.
#    - 해결: `if i > 0:` 조건을 추가하여 첫 번째 원소는 `nums[i]` 그대로 유지하도록 처리.
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
