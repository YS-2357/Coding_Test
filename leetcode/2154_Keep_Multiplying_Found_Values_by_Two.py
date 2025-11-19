# 2154_Keep_Multiplying_Found_Values_by_Two.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2154. Keep Multiplying Found Values by Two
# ✅ 문제 설명(요약):
#   - 정수 배열 nums와 정수 original이 주어진다.
#   - original이 nums 안에 존재하면, original *= 2 를 수행한다.
#   - 증가한 값이 다시 nums 안에 있으면, 다시 *= 2 … 를 반복한다.
#   - nums 전체를 확인한 뒤 더 이상 값이 존재하지 않으면 최종 original 값을 반환한다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]
#   - original: int
#
# ✅ 규칙 요약:
#   - nums에서 original을 찾으면 즉시 original *= 2
#   - 여러 번 반복 가능
#   - nums는 정렬된 상태가 아니므로 먼저 정렬 후 탐색하는 방법도 가능(정렬 O(n log n))
#   - 배열을 한 번만 순회하여 값을 갱신하는 방식

# ✅ 정답 코드(나의 원본 풀이; 절대 수정 금지)
#   - 아래 코드는 사용자가 제출한 최종 코드이며,
#     로직 및 변수명/순서 등을 변경하지 않고 주석만 추가한다.

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        now = original           # 현재 검사할 값(초기값은 original)
        nums.sort()              # nums를 정렬해 작은 값부터 순서대로 비교
        
        for num in nums:         # 정렬된 nums를 순회하며
            if num == now:       # 현재 값 now가 nums 안에 존재하는 경우
                now *= 2         # 규칙에 따라 now를 두 배로 증가시킴
        
        return now if now != original else original
        # now가 한 번이라도 업데이트되었다면 최종 now 반환
        # 업데이트가 없으면 original 그대로 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - nums를 정렬한 뒤 작은 값부터 now와 비교하는 단순·직관적 해결 방식.
#   - 문제의 규칙 그대로 구현했기 때문에 바로 정답 처리됨.
#   - 정렬 후 한 번의 순회로 모든 검사 완료.

# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음. 구현이 규칙을 정확히 반영함.
#   - 사용한 개념:
#       - 정렬(sort)을 통한 선형 탐색 단순화
#       - 값 갱신형 그리디(greedy): 발견 즉시 now *= 2
#       - 조건 충족 시 즉시 업데이트하는 단일 패스 방식

# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(n log n)
#       - nums.sort()가 지배적
#       - 이후 for 루프는 O(n)
#   - 공간 복잡도: O(1)
#       - 정렬은 제자리 정렬이며, 추가 메모리 거의 없음

# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 집합(set)을 사용하면 정렬 없이 O(n)으로 해결 가능:
#       - nums를 set으로 변환한 뒤
#       - while now in set: now *= 2
#   - 이 경우 시간 복잡도는 O(n), 공간 복잡도는 O(n)
