# 0015_3sum.py
# -----------------------------------------------------
# ✅ 제목: 3Sum
# ✅ 문제 설명(요약):
# - 정수 배열 nums에서 합이 0이 되는 서로 다른 세 수의 조합을 모두 찾아 반환한다.
# - 결과 내 중복 조합은 허용되지 않는다(값/인덱스 중복 제거 필요).
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 n (n ≥ 3)
#
# ✅ 규칙 요약:
# 1) 배열을 정렬하여 중복 스킵과 투 포인터 적용을 수월하게 한다.
# 2) i를 고정하고 left/right로 두 포인터를 좁혀가며 합을 확인한다.
# 3) i, left, right 각각에 대해 같은 값은 스킵하여 중복 조합을 제거한다.
# 4) 그리디 가지치기(pruning)로 불가능한 경우를 빠르게 건너뛴다.
#
# ✅ 입출력 예시(1개):
# - nums = [-1,0,1,2,-1,-4] → [[-1,-1,2], [-1,0,1]]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                   # 정렬: 중복 스킵/투포인터 전제
        n = len(nums)
        answer = []

        for i in range(n-2):                          # i는 0..n-3까지
            if i > 0 and nums[i] == nums[i-1]:       # 같은 시작 값은 한 번만 사용(중복 제거)
                continue
                
            if nums[i] > 0: break                     # i가 양수면 이후 합이 0 불가 → 종료
            if nums[i] + nums[i+1] + nums[i+2] > 0:  # 최소 합이 0보다 크면 더 진행 불필요
                break
            if nums[i] + nums[n-2] + nums[n-1] < 0:  # 최대 합이 0보다 작으면 다음 i로
                continue

            left, right = i + 1, n - 1               # 투 포인터 초기화
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]  # 현재 합

                if s == 0:
                    answer.append([nums[i], nums[left], nums[right]])  # 정답 추가
                    left += 1
                    right -= 1
                    # left/right 중복 값 스킵
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1                          # 합을 키우기 위해 left 이동
                else:
                    right -= 1                         # 합을 줄이기 위해 right 이동

        return answer                                  # 모든 조합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - while 밖에서 s를 고정하거나, 중복 스킵/프루닝이 부족해 누락·중복·시간낭비 발생 가능.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) s를 루프 내에서 매번 재계산하지 않음 → 포인터 이동 후 합 불일치.
# - (이전) 정답 발견 후 포인터 하나만 이동 → 동일 조합 반복/중복 발생.
# - (개선) i/left/right 중복 스킵 추가, 조기 종료·건너뛰기 프루닝으로 상수 시간 절약.
#
# 📚 사용된/필수 개념(최소):
# - 정렬(Sorting) + 투 포인터(Two Pointers)
# - 중복 제거 덤프(same value skip), 가지치기(pruning)
# - 시간복잡도: O(n^2), 공간복잡도: O(1) (정답 저장 제외)
