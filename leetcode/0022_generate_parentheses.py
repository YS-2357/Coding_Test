# 0022_generate_parentheses.py
# -----------------------------------------------------
# ✅ 제목: Generate Parentheses
# ✅ 문제 설명(요약):
# - 정수 n이 주어질 때, n쌍의 올바른 괄호 조합을 모두 생성.
# - 올바른 괄호: 여는 괄호는 항상 닫는 괄호보다 먼저 등장해야 하며,
#   닫는 괄호 수는 여는 괄호 수를 초과할 수 없음.
#
# ✅ 입력 형식(요지):
# - n: int (1 ≤ n ≤ 8)
#
# ✅ 규칙 요약:
# 1) 길이 2n의 문자열을 만들어야 함.
# 2) open < n이면 "(" 추가 가능.
# 3) close < open이면 ")" 추가 가능.
# 4) 길이 2n이 되면 정답에 추가.
#
# ✅ 입출력 예시(1개):
# - n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []                                # 결과 저장 리스트
        def backtrack(cur, open, close):           # cur: 현재 문자열, open/close: 사용한 괄호 수
            if len(cur) == 2 * n:                  # 길이가 2n이면 완성
                answer.append(cur)
                return
            if open < n:                           # 여는 괄호 추가 조건
                backtrack(cur + "(", open + 1, close)
            if close < open:                       # 닫는 괄호 추가 조건
                backtrack(cur + ")", open, close + 1)
        
        backtrack("", 0, 0)                        # 초기 상태에서 시작
        return answer                              # 모든 조합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 백트래킹 조건을 올바르게 구현하여 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 특별한 오류 없음. 다만 변수명 open/close는 예약어와 혼동될 수 있어 다른 이름 사용 권장.
#
# 📚 사용된/필수 개념(최소):
# - 백트래킹(backtracking)으로 모든 경우의 수 탐색
# - 괄호 짝 조건(open ≤ n, close ≤ open) 유지
# - 시간복잡도: O(C_n * n), C_n은 n번째 카탈란 수
