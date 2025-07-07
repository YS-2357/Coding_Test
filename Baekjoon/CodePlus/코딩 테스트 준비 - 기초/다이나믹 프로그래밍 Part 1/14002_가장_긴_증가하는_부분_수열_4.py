# 백준 14002번: 가장 긴 증가하는 부분 수열 4 (LIS - Longest Increasing Subsequence, DP & 추적)
# 문제 설명:
# - 주어진 수열에서 가장 긴 증가하는 부분 수열(LIS)의 길이와 해당 수열을 출력하는 문제
# - LIS를 출력하기 위해 경로 추적이 필요함

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 수열의 길이 입력
nums = list(map(int, sys.stdin.readline().split()))  # 수열 입력

# ✅ DP 테이블 초기화 (각 숫자는 자기 자신만을 포함하는 LIS를 가짐)
dp = [[1, [nums[i]]] for i in range(N)]

# ✅ 점화식을 사용한 DP 테이블 채우기 (O(N^2) 방식)
for i in range(1, N):
    for j in range(i):  # i 이전의 값들과 비교
        if nums[j] < nums[i]:  # 증가하는 부분 수열이 성립하는 경우
            if dp[i][0] < dp[j][0] + 1:  # 최댓값을 갱신할 경우에만 업데이트
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = dp[j][1] + [nums[i]]

# ✅ 가장 긴 LIS를 찾기
max_lis = max(dp, key=lambda x: x[0])

# ✅ 결과 출력
print(max_lis[0])  # LIS의 길이 출력
print(*max_lis[1])  # LIS 출력

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `dp = [[1, []] * N]` → `dp = [[1, [nums[i]]] for i in range(N)]`으로 수정:
#    - 기존 코드에서는 모든 리스트가 동일한 참조를 가짐
#    - 해결: 각 `dp[i][1]`을 `[nums[i]]`로 초기화하여 독립된 리스트를 유지
#
# 2. ✅ `dp[i][1] = dp[j][1] + [nums[i]]` 오류 수정:
#    - `dp[j][1]`을 `dp[i][1]`로 잘못 복사하여 일부 케이스에서 LIS가 잘못 저장됨
#    - 해결: `dp[i][1] = dp[j][1] + [nums[i]]`를 **최댓값이 갱신될 때만** 수행하도록 수정
#
# 3. ✅ `print(max(dp, key=lambda x: x[0])[0])` 및 `print(*max(dp, key=lambda x: x[0])[1])` 수정:
#    - `max(dp, key=lambda x: x[0])`을 두 번 호출하여 비효율적 연산 발생
#    - 해결: `max_lis = max(dp, key=lambda x: x[0])`을 미리 저장하고, 한 번만 사용
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
