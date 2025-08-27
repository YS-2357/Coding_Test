# 0018_4sum.py
# -----------------------------------------------------
# ✅ 제목: 4Sum
# ✅ 문제 설명(요약):
# - 정수 배열 nums와 정수 target이 주어질 때,
#   합이 target이 되는 서로 다른 네 수 [a,b,c,d]의 조합을 모두 반환한다.
# - 결과 내 중복 조합은 허용되지 않는다.
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 n (n ≥ 4)
# - target: int
#
# ✅ 규칙 요약:
# 1) 배열을 정렬하여 중복 제거와 투 포인터 적용을 용이하게 한다.
# 2) i, j 를 고정하고 나머지 두 수는 left/right 투 포인터로 찾는다.
# 3) i, j, left, right 각각에서 같은 값은 스킵하여 중복 조합을 예방한다.
# 4) 최소/최대 합으로 가지치기(pruning)하여 불필요한 탐색을 줄인다.
#
# ✅ 입출력 예시(1개):
# - nums = [1,0,-1,0,-2,2], target = 0
#   → [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()                                        # 정렬: 중복제거/투포인터 전제
        n = len(nums)
        answer = []                                        # 정답 조합들을 담을 리스트

        for i in range(n-3):                               # 첫 번째 고정 인덱스 i (0..n-4)
            if i > 0 and nums[i] == nums[i-1]: continue   # i 중복 값 스킵

            # i-레벨 가지치기: 가장 작은 3개/가장 큰 3개와의 합으로 불가능 판정
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target: continue

            for j in range(i+1, n-2):                     # 두 번째 고정 인덱스 j (i+1..n-3)
                if j > i + 1 and nums[j] == nums[j-1]: continue  # j 중복 값 스킵

                # j-레벨 가지치기: 남은 2개 최소/최대 더해 불가능 판정
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target: continue

                left, right = j + 1, n - 1                # 투 포인터 시작

                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]  # 현재 4수의 합

                    if s == target and [nums[i], nums[j], nums[left], nums[right]] not in answer:
                        # 합이 정확히 target이고(중복 예방을 위해 answer에 존재 여부도 체크)
                        answer.append([nums[i], nums[j], nums[left], nums[right]])  # 정답 추가
                        left += 1
                        right -= 1
                        # left/right 중복 값 스킵
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1                          # 합이 작으면 더 크게 (left++)
                    else:
                        right -= 1                         # 합이 크면 더 작게 (right--)
        return answer                                      # 모든 조합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 잘못된 가지치기(예: nums[i] > target 즉시 break)로 해를 누락할 수 있었음.
#   현재 버전은 i/j 레벨에서 최소/최대 합 기반 가지치기로 안정화.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) i만 중복 스킵 → j/left/right 중복으로 동일 조합 반복 발생 가능.
#   → j/left/right 중복 스킵 추가로 중복 제거.
# - (이전) 루프 밖/레벨 밖 합 조건 미흡 → 불필요 탐색 과다.
#   → i/j 레벨 프루닝 2식씩 추가로 탐색 축소.
#
# 💡 개선 여지(선택):
# - `[...] not in answer`는 리스트 포함 여부 O(k) 검사라 불필요(이미 중복 스킵으로 방지됨).
#   제거하면 상수 시간 개선 가능.
#
# 📚 사용된/필수 개념(최소):
# - 정렬(Sorting) + 투 포인터(Two Pointers)
# - 다중 레벨 중복 제거(i, j, left, right)
# - 가지치기(최소/최대 합 기반)
# - 시간복잡도: O(n^3), 공간복잡도: O(1) (정답 저장 제외)
