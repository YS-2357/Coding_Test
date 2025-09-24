# 0166_fraction_to_recurring_decimal.py
# -----------------------------------------------------
# ✅ 제목: Fraction to Recurring Decimal
# ✅ 문제 설명(요약):
# - 정수 numerator, denominator가 주어졌을 때 나눗셈 결과를 문자열로 반환.
# - 유한 소수는 그대로 출력, 순환 소수는 반복되는 부분을 괄호로 감싸야 함.
# - 예: 1/2 → "0.5", 2/1 → "2", 2/3 → "0.(6)".
#
# ✅ 입력 형식(요지):
# - numerator, denominator: int (음수 포함 가능)
#
# ✅ 규칙 요약:
# 1) 결과 부호는 두 수의 곱이 음수일 때만 "-" 붙임.
# 2) 정수부: 몫을 먼저 계산.
# 3) 나머지가 0이면 정수부만 반환.
# 4) 나머지가 있으면 소수부를 자리수별로 계산:
#    - 나머지를 10배 해 나누면서 각 자리 추가
#    - 같은 나머지가 다시 나오면 그 시점부터 반복 → 괄호 처리
#
# ✅ 입출력 예시(1개):
# - numerator = 4, denominator = 333 → "0.(012)"
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator * denominator < 0:           # 부호 결정
            sign = "-"
        else:
            sign = ""

        num, denom = abs(numerator), abs(denominator)  # 절댓값으로 계산
        q, r = divmod(num, denom)                      # 정수부 몫과 나머지

        if r == 0:                                     # 나머지가 없으면 정수 반환
            return sign + str(q)

        seen = {}                                      # 나머지 → 소수부 인덱스 기록
        frac = ""                                      # 소수부 누적 문자열
        while r != 0:
            if r in seen:                              # 반복된 나머지 발견 → 순환 시작
                idx = seen[r]
                frac = frac[:idx] + "(" + frac[idx:] + ")"
                break
            seen[r] = len(frac)                        # 현재 나머지 위치 저장
            r *= 10
            digit, r = divmod(r, denom)                # 다음 자리 계산
            frac += str(digit)

        return sign + str(q) + "." + frac              # 최종 문자열 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 순환 감지용 해시맵을 올바르게 활용하여 정답 도출.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기 구현에서는 나머지를 잘못 업데이트(r *= denom)하는 오류 → divmod 사용으로 수정.
# - 부호 처리에서 "+"를 붙이는 실수 → 음수일 때만 "-"로 고정.
#
# 📚 사용된/필수 개념(최소):
# - 나눗셈 나머지 추적
# - 해시맵(나머지 → 위치)으로 순환 시작점 기록
# - 문자열 처리로 소수부 구성
# - 시간복잡도: O(L), L은 순환 주기 길이(≤ denominator)
