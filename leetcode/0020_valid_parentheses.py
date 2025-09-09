# 20_valid_parentheses.py
# -----------------------------------------------------
# ✅ 제목: Valid Parentheses
# ✅ 문제 설명(요약):
# - 문자열 s가 주어졌을 때, (), {}, [] 괄호가 올바르게 열리고 닫혔는지 판별.
# - 올바른 괄호 조건:
#   1) 열린 괄호는 같은 종류의 괄호로 닫혀야 함.
#   2) 열린 괄호는 올바른 순서로 닫혀야 함.
#
# ✅ 입력 형식(요지):
# - s: str (문자열, 길이 1 이상)
#
# ✅ 규칙 요약:
# - 스택(stack)을 사용해 열린 괄호를 push.
# - 닫힌 괄호가 나오면 스택의 마지막과 비교해 짝이 맞으면 pop.
# - 마지막에 스택이 비어 있어야 True.
#
# ✅ 입출력 예시(1개):
# - s = "()[]{}" → True
# - s = "(]"     → False
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def isValid(self, s: str) -> bool:
        answer = []                                  # 스택 역할
        for bracket in s:                            # 문자열 순회
            if bracket in ["[", "(", "{"]:           # 열린 괄호 → push
                answer.append(bracket)
            elif answer and bracket == "]" and answer[-1] == "[":  # 닫힌 괄호 짝 확인
                answer.pop()
            elif answer and bracket == ")" and answer[-1] == "(":  # 닫힌 괄호 짝 확인
                answer.pop()
            elif answer and bracket == "}" and answer[-1] == "{":  # 닫힌 괄호 짝 확인
                answer.pop()
            else:                                    # 짝이 맞지 않으면 push → 이후 실패
                answer.append(bracket)
        return not answer                            # 스택이 비어 있으면 올바른 괄호

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 다양한 테스트 케이스에 대해 True/False 올바르게 반환.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 특별한 오류 없음. 다만 else에서 append 대신 바로 False 반환하면 더 효율적임.
# - 하지만 현재 구조도 문제없이 동작.
#
# 📚 사용된/필수 개념(최소):
# - 스택(stack) 자료구조
# - 조건문으로 괄호 쌍 검사
# - 시간복잡도: O(n), 공간복잡도: O(n)
