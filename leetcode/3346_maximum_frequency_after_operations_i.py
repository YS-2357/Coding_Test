# 3346_maximum_frequency_after_operations_i.py
# -----------------------------------------------------
# ✅ 제목: Maximum Frequency of an Element After Performing Operations I (LeetCode 3346)
# ✅ 문제 설명(요약):
# - 정수 배열 nums와 정수 k, numOperations가 주어진다.
# - numOperations번의 연산 동안, 한 번도 선택하지 않은 인덱스 i를 고르고
#   nums[i]에 [-k, k] 범위의 정수를 더할 수 있다.
# - 연산 후 nums에서 **가장 많이 등장하는 값의 빈도 최대치**를 구하라.
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 ≤ 10⁵
# - 1 ≤ nums[i], k ≤ 10⁵
# - 0 ≤ numOperations ≤ len(nums)
#
# ✅ 규칙 요약:
# 1) 각 원소 num은 [num−k, num+k] 구간 내의 정수로 변경 가능하다.
# 2) 어떤 값 v를 만들 수 있는 원소의 수 = 
#    ‘v가 포함되는 모든 [num−k, num+k] 구간 개수(cover)’.
# 3) v로 이미 존재하는 원소 수(keep) +  
#    (변경으로 만들 수 있는 원소 수 중 최대 numOperations개) = 최종 가능한 빈도.
# 4) 즉, 최댓값 = max( keep + min(numOperations, cover − keep) ).
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지) — 한 줄 주석 포함
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxNum = max(nums) + 1                            # 전체 값 범위(최대값+1)
        count = [0] * maxNum                              # count[n]: n의 원래 등장 횟수

        for num in nums:                                  # nums의 빈도 집계
            count[num] += 1
        
        diff = [0] * (maxNum + 2)                         # 차분 배열(diff) 초기화
        for num in nums:
            left = max(1, num - k)                        # num이 영향을 주는 구간의 시작
            right = min(maxNum, num + k)                  # num이 영향을 주는 구간의 끝
            diff[left] += 1                               # [left, right] 구간 덮기 시작
            diff[right+1] -= 1                            # [right+1, …) 구간 덮기 해제

        answer = 0                                        # 최대 빈도 결과값
        cover = 0                                         # 현재 값 n이 덮이는 구간 개수
        for n in range(1, maxNum):
            cover += diff[n]                              # 현재 n에서 덮개 수 누적
            keep = count[n]                               # 이미 n인 원소의 수
            change = cover - keep                         # 변경 가능 원소 수(= 덮개−keep)
            answer = max(answer, keep + min(numOperations, change))  
                                                          # 가능한 최대 빈도 갱신
        
        return answer                                     # 결과 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 차분배열 + 누적합(prefix)로 구간 덮임 수를 계산해 통과함.
#
# 🔧 오답 및 실수, 사용된 개념 요약:
# - 핵심 아이디어:
#   * 각 원소 num은 [num−k, num+k] 구간으로 확장.
#   * diff[left]++, diff[right+1]-- 로 전체 값축에서 “몇 개의 구간이 현재 위치를 덮는지” 계산.
#   * 각 값 n에 대해:
#       - keep: 이미 값 n인 개수
#       - cover: n을 만들 수 있는 원소 총합
#       - cover−keep: n이 아니지만 n으로 변환 가능한 개수
#       - min(numOperations, cover−keep): 실제 바꿀 수 있는 개수
#   * 최종 빈도 = keep + min(numOperations, cover−keep)
#
# 📚 시간·공간 복잡도:
# - 시간: O(V + n)  (V = max(nums))
# - 공간: O(V)
#
# -----------------------------------------------------
# (선택) 다른 풀이 또는 개선 제안:
# - 값의 범위가 크다면 해시맵 기반 차분(dict)으로 메모리 절약 가능.
# - 정렬+슬라이딩 윈도우 버전도 동일 복잡도(O(n log n))로 구현 가능.
