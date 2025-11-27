# 3381_Maximum_Subarray_Sum_With_Length_Divisible_by_K.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3381. Maximum Subarray Sum With Length Divisible by K
# ✅ 문제 설명(요약):
#   - 정수 배열 nums와 정수 k가 주어진다.
#   - 연속 부분 배열(subarray)들 중에서,
#       1) 길이가 k의 배수 (len % k == 0)
#       2) 합이 최대가 되는 값
#     을 구하는 문제이다.
#   - 부분 배열은 연속 구간이어야 하며, 길이는 k, 2k, 3k, ... 만 허용된다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]  (정수 배열)
#   - k: int           (길이 제약에 사용되는 양의 정수)
#
# ✅ 규칙 요약:
#   - 연속 부분 배열 nums[l..r]에 대하여 (r - l + 1) % k == 0 인 것만 고려한다.
#   - 그 중 합이 최대가 되는 값을 정수로 반환한다.
#   - 최소 한 개 이상의 길이가 k의 배수인 부분 배열이 존재한다고 가정한다.
#   - prefix sum과 인덱스 mod k 정보를 활용하여 O(n)에 해결 가능하다.

# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - prefix[i] = nums[0..i-1] 의 합을 저장하는 prefix 배열을 구성한다.
#   - 부분 배열 nums[l..r]의 합은: prefix[r+1] - prefix[l] 로 표현 가능하다.
#   - 이때 길이 조건:
#       (r - l + 1) % k == 0
#       ⇔ (r+1 - l) % k == 0
#       ⇔ (r+1) % k == l % k
#     즉, prefix 인덱스 i, j (i < j)에 대해 j % k == i % k 이면,
#     길이가 k의 배수인 subarray가 된다.
#   - 같은 mod 그룹에서 prefix 값을 관리하면서,
#     각 그룹별로 "현재까지의 최소 prefix"를 유지하면,
#     prefix[idx] - min_prefix[mod] 가 해당 그룹에서 가능한 최대 subarray 합이 된다.
#   - 이를 전체에 대해 갱신하며 최댓값을 ans에 저장한다.

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10 ** 15                      # 충분히 큰 양수 (최소값 초기화용)
        pref = [0] * (n + 1)                # prefix[i] = nums[0..i-1] 의 합

        pref[0] = 0                         # 길이 0 구간의 합은 0
        for i in range(1, n+1):
            pref[i] = pref[i-1] + nums[i-1] # prefix 합 갱신: 이전 prefix + 현재 원소

        # min_pref[mod] = 지금까지 본 prefix 인덱스 중,
        #   인덱스 % k == mod 인 것들 중 가장 작은 prefix 값
        min_pref = [INF] * k
        min_pref[0] = 0                     # prefix[0] = 0, 인덱스 0 % k == 0

        ans = -INF                          # 가능한 합들보다 작은 값으로 초기화

        for idx in range(1, n+1):
            mod = idx % k                   # 현재 prefix 인덱스의 mod k 그룹

            # min_pref[mod] 가 갱신된 적이 있다면 (즉, 유효한 prefix가 있다면)
            # prefix[idx] 를 오른쪽 끝으로 하는, 길이가 k의 배수인 subarray 후보를 구할 수 있다.
            # 해당 subarray 합 = prefix[idx] - min_pref[mod]
            if min_pref[mod] != INF:
                ans = max(ans, pref[idx] - min_pref[mod])

            # 현재 prefix[idx] 를 이용해 이 mod 그룹의 최소 prefix 값 갱신
            min_pref[mod] = min(min_pref[mod], pref[idx])
    
        return ans                          # 길이가 k의 배수인 subarray 중 최대 합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - prefix sum + mod k 기반 아이디어를 적용해,
#     "같은 mod 그룹 내에서의 prefix 차이"로 길이가 k의 배수인 subarray 합을 구하는 방식으로 정리했다.
#   - 각 mod 그룹에 대해 최소 prefix를 유지하면서, 매 index마다 최대 후보를 갱신하는 구조이다.
#   - DFS나 2중 루프 없이 O(n)에 수렴하는 효율적인 풀이를 완성했다.

# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 초기에 단순 DP/누적합 구조만 떠올리면 길이 제약(len % k == 0)을 강제하기 어렵다.
#   - 핵심 개념:
#       1) prefix sum:
#          - 부분합을 prefix 차이로 표현하여, 연속 구간 합을 O(1)로 계산.
#       2) 길이 제약을 mod k 로 변환:
#          - (r+1 - l) % k == 0  ⇔  prefix 인덱스 i, j가 같은 mod k 그룹.
#       3) 각 mod 그룹별 최소 prefix 관리:
#          - 같은 mod 그룹에서 prefix[j] - prefix[i] 를 최대화하려면,
#            prefix[i]는 가능한 한 작아야 한다.
#          - 따라서 min_pref[mod]만 유지하면 된다.
#   - 이 아이디어로, 모든 (i, j) 쌍을 직접 보지 않고도 최적 결과를 얻을 수 있다.

# 📚 시간·공간 복잡도:
#   - 시간 복잡도:
#       - prefix 계산: O(n)
#       - main loop: O(n)
#       - 전체: O(n)
#   - 공간 복잡도:
#       - prefix 배열: O(n)
#       - min_pref 배열: O(k)
#       - 전체: O(n + k)

# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 이 문제는 prefix + mod + 최소 prefix 조합을 사용한 풀이가 사실상 정석이다.
#   - Kadane's algorithm 변형처럼 볼 수 있으며,
#     "k개의 독립된 mod 그룹에 대해 동시에 최대 부분합을 관리한다"는 관점으로 이해할 수 있다.
