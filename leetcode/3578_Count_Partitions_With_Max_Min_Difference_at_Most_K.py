# 3578_Count_Partitions_With_Max_Min_Difference_at_Most_K.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3578. Count Partitions With Max-Min Difference at Most K
# -----------------------------------------------------
# ✅ 문제 설명(요약):
#   - 정수 배열 nums와 정수 k가 주어진다.
#   - 배열을 **연속된 부분 배열(subarray)** 들로 분할(partition)할 때,
#     각 부분 배열에서 (최댓값 - 최솟값) ≤ k 를 만족해야 한다.
#   - 이러한 조건을 만족하는 배열의 분할 방법의 수를 구하는 문제이며,
#     답은 10^9 + 7 로 나눈 나머지를 반환한다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]
#       · 길이 n인 정수 배열.
#   - k: int
#       · 허용되는 (max - min)의 최대값.
#
# ✅ 규칙 요약:
#   - 분할은 배열의 인덱스 사이에 경계를 두어, 인접한 subarray로 나누는 모든 방법을 의미.
#   - 각 subarray의 원소들은 연속된 인덱스로 구성되어야 한다.
#   - 각 subarray에 대해 max(subarray) - min(subarray) ≤ k 조건이 반드시 만족되어야 한다.
#   - 분할의 순서는 배열 순서를 유지하는 조건에서 자연스럽게 정의된다 (재배열 불가).
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지, 주석만 추가)
#   - 아이디어:
#       1) 투 포인터 + 정렬구조(SortedList)를 통해, 각 위치 i에서
#          "끝이 i인 subarray 중 (max-min) ≤ k 를 만족하는 가장 왼쪽 시작점 j"를 찾는다.
#       2) dp[i] = nums[:i] 까지의 prefix를 적절히 분할하는 방법의 수.
#       3) dp[i+1] = sum(dp[t]) for t in [j..i] (끝이 i인 마지막 subarray의 시작 위치).
#          → prefix sum 배열 prefix를 이용해 이 구간 합을 O(1)에 계산.
# -----------------------------------------------------

from typing import List
from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7           # 나머지 연산에 사용할 모듈러
        n = len(nums)             # 배열 길이

        dp = [0] * (n+1)          # dp[i] = nums[0..i-1]을 조건에 맞게 분할하는 방법 수
        dp[0] = 1                 # 빈 prefix를 분할하는 방법은 1가지(아무 것도 안 나누는 것)

        prefix = [0] * (n+1)      # prefix[i] = dp[0] + dp[1] + ... + dp[i] (dp의 prefix sum)
        prefix[0] = 1             # prefix[0] = dp[0]

        cnt = SortedList()        # 현재 윈도우 [j..i] 구간의 값들을 정렬 상태로 유지하는 구조

        j = 0                     # 투 포인터 왼쪽 인덱스(현재 윈도우의 시작점)
        for i in range(n):        # i: 현재 고려 중인 subarray의 끝 인덱스
            cnt.add(nums[i])      # 윈도우에 nums[i] 포함 (정렬 상태 유지)

            # 현재 윈도우 [j..i]에서 max-min > k 이면, 조건을 만족할 때까지 j를 오른쪽으로 이동
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])  # 왼쪽 끝 값을 윈도우에서 제거
                j += 1               # 윈도우 시작점 자리를 한 칸 오른쪽으로 이동

            # 이제 [j..i]는 (max-min) ≤ k 를 만족하는 **최대**의 구간이 되어 있음.
            # 끝이 i인 마지막 subarray의 시작점 t는 j ≤ t ≤ i 이고,
            # 각 t에 대해 "prefix t까지의 분할 방법(dp[t]) + 마지막 구간[t..i]" 조합이 가능.
            # 따라서 dp[i+1] = sum(dp[t]) for t in [j..i]
            # → prefix sum을 이용해 구간 합 계산:
            #   sum(dp[j..i]) = prefix[i] - prefix[j-1] (j > 0일 때),
            #   j == 0 이면 prefix[i] 전체를 쓰면 된다.
            dp[i+1] = (prefix[i] - (prefix[j-1] if j > 0 else 0)) % MOD

            # prefix[i+1] 업데이트: prefix[i+1] = prefix[i] + dp[i+1]
            prefix[i+1] = (prefix[i] + dp[i+1]) % MOD

        return dp[n]              # 전체 배열(nums[0..n-1])을 분할하는 방법 수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 슬라이딩 윈도우 + 정렬 자료구조(SortedList) + DP + prefix sum을 결합한 풀이로 정답 획득.
#   - 각 i마다 "끝이 i인 subarray가 만족할 수 있는 최소 시작점 j"만 찾으면,
#     dp[i+1]을 dp[j..i]의 합으로 갱신하는 구조가 잘 작동함을 확인.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - (잠재적 오답 접근) 단순하게 모든 구간 [l..r]마다 max-min을 계산하면 O(n^2) 이상이 되어 TLE 위험.
#   - 이 풀이에서는 다음 개념을 활용:
#       1) 투 포인터(슬라이딩 윈도우):
#          - i를 오른쪽으로 확장하면서 윈도우 [j..i]의 max-min이 k를 넘지 않도록 j를 조절.
#          - 한 번 증가한 j는 다시 줄어들지 않으므로 전체 복잡도는 O(n log n) 수준.
#       2) 정렬 구조(SortedList):
#          - 윈도우 안의 최소, 최대 값을 O(1)에 얻고, 삽입/삭제는 O(log n).
#          - 이를 통해 max-min 조건 확인을 빠르게 수행.
#       3) DP + Prefix Sum:
#          - dp[i]를 직접 모든 t에 대해 sum(dp[t])로 계산하면 O(n^2).
#          - prefix[i] = dp[0] + ... + dp[i] 를 유지하여,
#            dp[i+1] = sum(dp[j..i])를 상수 시간에 계산.
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도:
#       · 바깥 루프 i: n번
#       · 각 i마다 cnt.add / cnt.remove: O(log n)
#       · 따라서 전체는 O(n log n).
#   - 공간 복잡도:
#       · dp, prefix: O(n)
#       · cnt: 최악의 경우 O(n) (윈도우 크기)
#       · 전체 공간: O(n)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - nums가 정렬 가능한 상황에서, 인덱스 기준 대신 값 기준으로 투 포인터를 움직이는 변형도 가능하지만,
#     이 문제는 **연속 subarray**가 핵심이므로, 인덱스 기반 슬라이딩 윈도우가 자연스럽다.
#   - 정렬 구조 대신 세그먼트 트리 / 펜윅 트리로 max/min을 관리하는 방법도 있으나,
#     구현 복잡도 대비 SortedList를 사용하는 방식이 직관적이고 충분히 효율적이다.
# -----------------------------------------------------
