# 3005_count_elements_with_maximum_frequency.py
# -----------------------------------------------------
# ✅ 제목: Count Elements With Maximum Frequency (LeetCode 3005)
# ✅ 문제 설명(요약):
# - 배열 nums가 주어짐.
# - 가장 많이 등장한 빈도 f_max를 찾는다.
# - 이 빈도를 가진 값들이 차지하는 원소 개수의 총합을 반환.
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 1 이상
#
# ✅ 규칙 요약:
# 1) 최빈도 f_max = max(freq.values()).
# 2) freq[v] == f_max인 값들의 빈도를 전부 합한다.
# 3) 결과 = f_max * (f_max인 값들의 개수).
#
# ✅ 입출력 예시(1개):
# - 입력: nums = [1,2,2,3,1,4]
# - freq = {1:2, 2:2, 3:1, 4:1}, f_max = 2
# - f_max 가진 값 = {1,2} 두 개 → 총합 = 2+2=4
# - 출력: 4
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}                                     # 각 원소 빈도 저장
        for num in nums:
            freq[num] = freq.get(num, 0) + 1          # 빈도 누적
        maxFreq = max(value for value in freq.values())  # 최빈도 구하기
        return sum(maxFreq for value in freq.values() if value == maxFreq)
        # 최빈도에 해당하는 값이 k개면 maxFreq * k 합산됨

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 통과. 조건에 맞는 최빈 원소들을 잘 합산함.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기 코드에서 sum 부분에 `1 * maxFreq`를 썼는데 사실상 `maxFreq`와 동일.
# - 로직 자체에는 문제 없음.
#
# 📚 사용된/필수 개념(최소):
# - 해시맵(딕트)로 빈도수 계산
# - 최빈도 값 찾기
# - 조건부 합산
# - 시간복잡도 O(n), 공간복잡도 O(U) (U=고유 원소 수)
