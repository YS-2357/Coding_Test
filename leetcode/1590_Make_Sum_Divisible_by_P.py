# 1590_Make_Sum_Divisible_by_P.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1590. Make Sum Divisible by P
# ✅ 문제 설명(요약):
#   - 정수 배열 nums와 정수 p가 주어진다.
#   - 배열의 연속 부분 배열(subarray) 하나를 제거해서,
#     남은 원소들의 합이 p로 나누어떨어지도록 만들고 싶다.
#   - 제거할 subarray의 "최소 길이"를 구하는 문제이며,
#     제거 후 배열은 비어 있으면 안 된다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]  — 정수 배열
#   - p: int           — 나눌 기준이 되는 양의 정수
#
# ✅ 규칙 요약:
#   - 전체 합 S = sum(nums) 에 대해, S % p == 0 이면 이미 조건을 만족하므로 0 반환.
#   - 그렇지 않다면, 어떤 연속 구간 sum(l..r)을 제거해서
#       (S - sum(l..r)) % p == 0
#     이 되도록 해야 한다.
#   - 이는 sum(l..r) % p == S % p 인 subarray 중 "길이가 가장 짧은 것"을 찾는 문제로 바뀐다.
#   - prefix sum + mod p + 해시맵(prefix mod → index)을 사용하여 O(n)에 해결 가능하다.

# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - total = sum(nums) % p 를 구한 뒤, target = total 로 두고,
#     "합 % p == target" 인 subarray를 제거하면 남은 합이 p로 나누어떨어진다.
#   - prefix sum의 현재 나머지를 cur, 필요한 이전 나머지를 need로 두고,
#     need를 과거에 본 적이 있는지 해시맵(mod_map: mod → index)에 기록해두고 탐색한다.
#   - i 번째 위치에서 cur, need를 이용해 제거 가능한 subarray 길이(i - mod_map[need])를 계산하고,
#     그 중 최솟값을 정답으로 삼는다.

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)                     # 배열 길이
        total = 0                         # 전체 합의 p에 대한 나머지를 누적할 변수

        for num in nums:                  # nums 전체를 순회하며
            total = (total + num) % p     # 전체 합의 나머지를 누적 (overflow 방지용 mod)

        target = total % p                # 제거해야 하는 subarray의 합이 가져야 할 나머지
        if target == 0:                   # 이미 전체 합이 p로 나누어떨어지면
            return 0                      # 아무 subarray도 제거할 필요 없음

        mod_map = {0: -1}                 # prefix mod → 가장 최근 index
                                          # prefix sum == 0 (mod p) 를 '인덱스 -1'에서 출발한다고 가정

        cur = 0                           # 현재 prefix sum의 나머지 (0부터 시작)
        min_len = n                       # 제거할 subarray 길이의 최솟값 (최대 n으로 초기화)

        for i in range(n):
            cur = (cur + nums[i]) % p     # nums[0..i]까지의 prefix sum % p

            need = (cur - target + p) % p # sum(l..i) % p == target 이 되려면
                                          # prefix[l-1] % p == need 여야 한다.

            if need in mod_map:           # 과거에 같은 need 나머지를 가진 prefix가 있었다면
                min_len = min(min_len, i - mod_map[need])
                # 그 prefix 이후부터 현재 i까지의 subarray가 제거 후보 (길이: i - mod_map[need])

            mod_map[cur] = i              # 현재 prefix 나머지를 최신 index로 기록 (가장 최근 값이 길이 최소에 유리)

        return -1 if min_len == n else min_len
        # min_len이 한 번도 갱신되지 않았다면 제거 가능한 subarray가 없음 → -1
        # 그렇지 않다면 min_len이 요구 조건을 만족하는 최소 길이

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 전체 합의 나머지 target = sum(nums) % p 를 구한 뒤,
#     "합 % p == target" 인 연속 subarray를 찾아서 제거하는 방식으로 문제를 재구성했다.
#   - prefix sum의 mod p 값을 누적(cur)하고,
#     각 단계에서 필요한 이전 값 need = (cur - target + p) % p 를 해시맵에서 조회해
#     길이 최소를 갱신하는 구조로 정리했다.
#   - prefix mod → index를 dict로 관리해 O(1)에 필요 정보를 찾도록 만들어,
#     전체 시간복잡도 O(n)을 달성했다.

# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답/실수(초기 관점 기준):
#       - 단순히 sum(nums) % p == 0 체크까지만 하고,
#         “어떤 subarray를 제거해야 하는지”를 prefix 관점에서 재구성하지 않으면
#         효율적인 탐색이 불가능하다.
#   - 사용한 알고리즘/개념:
#       1) prefix sum + mod:
#            - sum(l..r) = prefix[r] - prefix[l-1]
#            - sum(l..r) % p == target ⇔ prefix[r] % p - prefix[l-1] % p == target (mod p)
#       2) 식 변형:
#            - prefix[l-1] % p == (prefix[r] - target + p) % p = need
#       3) 해시맵 활용:
#            - 각 prefix mod 상태를 dict에 저장해 두고,
#              필요할 때마다 O(1)로 과거 인덱스를 찾는 방식.
#       4) 최소 길이 탐색:
#            - 각 인덱스 i에서 i - mod_map[need]를 계산해 최소값 갱신.

# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(n)
#       - nums를 한 번 순회하면서 prefix mod 계산 및 dict 조회/갱신만 수행.
#   - 공간 복잡도: O(min(n, p))
#       - mod_map에 최대 min(n, p) 개의 서로 다른 mod 상태가 저장될 수 있다.

# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 이 문제는 prefix sum mod + 해시맵 패턴의 전형적인 응용이며,
#     LeetCode 974 (Subarray Sums Divisible by K) 의 변형으로 볼 수 있다.
#   - 다른 복잡한 DP나 슬라이딩 윈도우는 필요 없고,
#     현재 풀이 방식이 사실상 최적(시간/공간 면에서 모두 효율적)이다.
