# 120840_구슬을_나누는_경우의_수.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 자연수 balls와 share가 주어진다.
# - balls개의 구슬 중에서 share개를 선택하는 경우의 수를 구한다.
# - 조합 공식:
#   C(balls, share) = balls! / (share! * (balls - share)!)
#
# ✅ 입력:
# - balls (1 ≤ balls ≤ 30)
# - share (1 ≤ share ≤ balls)
#
# ✅ 출력:
# - 경우의 수 (정수)
#
# ✅ 예시:
#   입력: balls = 5, share = 3
#   출력: 10  (5C3 = 10)
# -----------------------------------------------------

def solution(balls, share):
    # ✅ 팩토리얼 계산 함수 정의 (재귀)
    def factorial(n):
        # 0! = 1, 1! = 1
        if n == 0 or n == 1:
            return 1
        # n! = n * (n-1)!
        return n * factorial(n - 1)
    
    # ✅ 조합 공식 적용
    # C(balls, share) = balls! / (share! * (balls - share)!)
    return factorial(balls) // (factorial(share) * factorial(balls - share))

# -----------------------------------------------------
# ✅ 사용된 개념 요약:
# - **조합 공식**: nCr = n! / (r!(n-r)!)
# - **팩토리얼**: 재귀 함수 사용
# - **정수 나눗셈**: `//`로 몫만 반환
#
# ✅ 시간 복잡도:
# - factorial 계산 O(n) → 최대 n=30 → 매우 빠름
#
# ✅ 더 효율적인 방법:
# - Python 내장 함수 사용 가능:
#   from math import comb
#   return comb(balls, share)
# -----------------------------------------------------
