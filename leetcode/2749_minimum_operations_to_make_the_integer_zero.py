# 2749_minimum_operations_to_make_the_integer_zero.py
# -----------------------------------------------------
# ✅ 제목: Minimum Operations to Make the Integer Zero
# ✅ 문제 설명(요약):
# - 두 정수 num1, num2가 주어진다.
# - 연산: 임의의 i ∈ [0,60]를 골라 num1 -= (2^i + num2)를 수행.
# - num1을 정확히 0으로 만들 수 있는 최소 연산 횟수를 구하고, 불가능하면 -1 반환.
#
# ✅ 입력 형식(요지):
# - num1, num2: int
#
# ✅ 규칙 요약:
# 1) k번 연산 후: num1 - k*num2 = 합(2^i, 총 k개).
# 2) x = num1 - k*num2라 두면 조건:
#    - x ≥ 0
#    - x.bit_count() ≤ k ≤ x
#      (bit_count는 2진수에서 1의 개수 = 최소 항 개수)
# 3) 조건 만족하는 최소 k 반환, 없으면 -1
#
# ✅ 입출력 예시(1개):
# - num1=9, num2=1
#   k=1 → x=9-1*1=8 (1000₂, bit_count=1) → 조건 만족 → 정답=1
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):                  # 연산 횟수 후보 1~60
            x = num1 - k * num2                 # k번 연산 후 남은 값
            if x < 0:                           # 음수면 불가능
                continue
            if x.bit_count() <= k <= x:         # 조건 만족하면 k 반환
                return k
        return -1                               # 끝까지 없으면 불가능

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - num1, num2 케이스별 올바른 정답 도출.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전 코드) 단순히 2^i를 순서대로 빼나가는 방식 → 경우 놓침.
# - (수정) num1 - k*num2를 한 번에 계산 후 bit_count 조건 검사.
#
# 📚 사용된/필수 개념(최소):
# - popcount(x) = x.bit_count() → 2진수에서 1의 개수 = 최소 항 개수
# - 조건: popcount(x) ≤ k ≤ x
# - 시간복잡도: O(60)=O(1), 공간복잡도: O(1)
