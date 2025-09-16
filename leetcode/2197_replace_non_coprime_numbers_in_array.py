# 2197_replace_non_coprime_numbers_in_array.py
# -----------------------------------------------------
# ✅ 제목: Replace Non-Coprime Numbers in Array (LeetCode 2197)
# ✅ 문제 설명(요약):
# - 배열을 왼쪽부터 보면서 인접한 두 수의 gcd > 1이면 두 수를 그들의 lcm으로 교체.
# - 교체 후 새 값이 앞 원소들과 다시 gcd > 1이면 연쇄적으로 병합을 반복.
# - 더 이상 병합할 쌍이 없을 때의 배열을 반환.
#
# ✅ 입력 형식(요지):
# - nums: List[int]
#
# ✅ 규칙 요약:
# 1) 인접 쌍 (a,b)의 gcd(a,b) > 1이면 병합하여 lcm(a,b)로 대체.
# 2) 새 값은 스택 상단의 이전 원소들과도 반복 검사(연쇄 병합).
# 3) lcm은 a // gcd(a,b) * b 순서로 계산(곱 오버플로우/중간값 폭증 완화).
#
# ✅ 입출력 예시(1개):
# - 입력: [6,4,3]
# - 과정: (6,4)→lcm=12 → (12,3)→lcm=12
# - 출력: [12]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        stack = []                                   # 결과를 누적할 스택
        for x in nums:                               # 왼→오 순회
            while stack and gcd(stack[-1], x) > 1:   # top과 공약수 있으면
                x = stack[-1] // gcd(stack[-1], x) * x  # lcm으로 병합
                stack.pop()                          # top 제거 후 연쇄 검사
            stack.append(x)                          # 더 이상 병합 불가 시 push
        return stack                                 # 최종 배열

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 스택+연쇄 병합 로직으로 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 단일 if로 한 번만 병합하면 앞쪽과의 추가 병합을 놓침 → while로 연쇄 처리로 수정.
# - lcm을 a*b//g로 계산 시 중간 곱이 커짐 → a//g*b 순서로 변경.
#
# 📚 사용된/필수 개념(최소):
# - 유클리드 알고리즘(gcd), lcm 계산
# - 스택을 이용한 연쇄 병합(단조 스택 유사 패턴)
# - 시간복잡도: O(n log M), 공간복잡도: O(n)  (M: 값의 최대치)
#
# ✅ (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 파이썬 math.gcd 사용으로 가독성 향상 가능.
# - 큰 수가 자주 등장하면 lcm 계산을 함수로 분리해 테스트 용이성 확보.
