# 0016_3sum_closest.py
# -----------------------------------------------------
# ✅ 제목: 3Sum Closest
# ✅ 문제 설명(요약):
# - 정수 배열 nums와 정수 target이 주어질 때,
#   nums[i] + nums[j] + nums[k]의 합이 target에 가장 가까운 값을 반환한다.
# - 정확히 target을 만들 수 있으면 그 값을 즉시 반환해도 된다.
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 n (n ≥ 3)
# - target: int
#
# ✅ 규칙 요약:
# 1) 배열을 정렬한다.
# 2) i를 고정하고, 나머지를 left/right 투 포인터로 스캔한다.
# 3) 현재 합 s와 target의 차이 |target - s|가 더 작으면 정답 갱신.
# 4) s < target → left++ (합을 키움), s > target → right-- (합을 줄임)
# 5) s == target이면 바로 반환(최적).
#
# ✅ 입출력 예시(1개):
# - nums = [-1,2,1,-4], target = 1 → 2   (조합: -1 + 2 + 1 = 2)
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()                              # 정렬로 투 포인터 전제 마련
        n = len(nums)
        answer = None                            # 현재까지 가장 가까운 합
        best_diff = float("inf")                 # 현재까지의 최소 |target - s|

        for i in range(n - 2):                   # i 고정: 0..n-3
            left, right = i + 1, n - 1           # 양끝 포인터

            while left < right:
                s = nums[i] + nums[left] + nums[right]  # 현재 합
                diff = target - s                        # 양수면 s가 작음, 음수면 s가 큼

                if abs(diff) < best_diff:       # 더 가까우면 정답 갱신
                    best_diff = abs(diff)
                    answer = s

                if diff == 0:                   # 정확히 일치 → 최적해
                    return s
                elif diff > 0:                  # s < target → 더 크게
                    left += 1
                else:                           # s > target → 더 작게
                    right -= 1

        return answer                           # 가장 가까운 합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - "더 가까워질 때만 포인터 이동"으로 작성해 무한루프(TLE) 발생 가능.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 포인터 이동 조건을 "|target - s|가 줄어든 경우"에 종속
#   → 동일/악화 시 포인터가 멈춰 while 무한 반복.
#   → (수정) "정답 갱신"과 "포인터 이동"을 분리:
#      - 갱신은 더 가까워질 때만,
#      - 이동은 s와 target의 대소 비교에 따라 **항상** 수행.
#
# 📚 사용된/필수 개념(최소):
# - 정렬 + 투 포인터로 O(n^2) 탐색
# - 절대차(minimize |target - s|) 갱신 패턴
# - 조기 종료(s == target)
# - 시간복잡도: O(n^2), 공간복잡도: O(1)
