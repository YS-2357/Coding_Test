# 0017_letter_combinations_of_a_phone_number.py
# -----------------------------------------------------
# ✅ 제목: Letter Combinations of a Phone Number
# ✅ 문제 설명(요약):
# - 숫자 문자열 digits(2~9)로 만들 수 있는 모든 문자 조합을 반환한다.
# - 전화 키패드 매핑을 사용한다.
#
# ✅ 입력 형식(요지):
# - digits: str (길이 0 이상, '2'~'9'만 포함)
#
# ✅ 규칙 요약:
# 1) 각 자리의 숫자를 키패드 문자 셋으로 치환하여 모든 조합 생성.
# 2) 빈 입력("")이면 빈 리스트 반환.
# 3) BFS(큐)로 길이=단계 인덱스 원리를 사용해 층별로 확장.
#
# ✅ 입출력 예시(1개):
# - digits = "23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:                               # 빈 입력 처리
            return []

        letter_map = {                               # 숫자→문자 매핑
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        answer = []                                  # 최종 결과 리스트
        queue = deque([""])                          # 시작은 빈 조합 하나

        while queue:                                 # BFS로 층별 확장
            comb = queue.popleft()                   # 현재 조합을 꺼내고
            # print(comb)                            # (디버깅) 진행 상황 확인
            if len(comb) == len(digits):             # 길이가 digits와 같으면
                answer.append(comb)                  # 완성된 조합 → 결과
            else:
                next_digit = digits[len(comb)]       # 다음에 붙일 자리의 숫자
                for letter in letter_map[next_digit]:
                    queue.append(comb + letter)      # 문자 하나 붙여 큐에 재삽입

        return answer                                # 모든 조합 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - for-중첩 확장에서 “언제 다시 큐에서 꺼내 확장할지”가 애매했음.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 자릿수 진행과 큐 확장 타이밍이 분리되어 혼란.
#   → (수정) comb의 길이(len(comb))를 현재 단계 인덱스로 사용,
#     next_digit = digits[len(comb)]로 정확히 그 단계만 확장하여 BFS 구현.
#
# 📚 사용된/필수 개념(최소):
# - BFS(큐)로 층별 확장, 길이=단계 인덱스 매핑
# - 문자열 누적 빌드
# - 시간복잡도: O(3^n ~ 4^n), 공간복잡도: 출력 크기와 동일(+큐)
