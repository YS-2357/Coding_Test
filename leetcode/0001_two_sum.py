# 0001_two_sum.py
# -----------------------------------------------------
# ✅ 제목: Two Sum
# ✅ 문제 설명(요약):
# - 정수 배열 nums와 정수 target이 주어진다.
# - 배열 내 서로 다른 두 수의 합이 target이 되는 인덱스 쌍을 반환한다.
# - 각 입력은 정확히 하나의 해만 가진다고 보장되며, 같은 원소를 두 번 사용하면 안 된다.
#
# ✅ 입력 형식(요지):
# - nums: List[int], 길이 ≥ 2
# - target: int
#
# ✅ 규칙 요약:
# 1) 서로 다른 인덱스 i, j에 대해 nums[i] + nums[j] == target
# 2) 그 쌍을 [i, j] 형태로 반환
#
# ✅ 입출력 예시(1개):
# - nums = [2,7,11,15], target = 9  →  [0,1]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}                                 # 값 → 인덱스 저장용 딕셔너리
        for i, num in enumerate(nums):            # nums를 순회하면서
            complement = target - num             # 짝이 되는 수 = target - 현재 수
            if complement in hash:                # 그 짝이 이미 hash에 있으면
                return [hash[complement], i]      # [짝의 인덱스, 현재 인덱스] 반환
            hash[num] = i                         # 현재 수를 해시에 기록
        return []                                 # 문제 보장상 도달하지 않음

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - dict에 index→value를 저장하여 짝 찾기가 불가능하거나 자기 자신을 짝으로 선택하는 오류 발생.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) hash[i] = num 구조 → complement in hash에서 항상 index만 탐색됨.
#   → (수정) hash[num] = i 로 바꿔 value→index 매핑,
#      complement를 빠르게 찾을 수 있도록 개선.
#
# 📚 사용된/필수 개념(최소):
# - 해시맵(dict)으로 O(1) 검색
# - 슬라이딩 없이 단일 패스
# - 시간복잡도: O(n), 공간복잡도: O(n)
