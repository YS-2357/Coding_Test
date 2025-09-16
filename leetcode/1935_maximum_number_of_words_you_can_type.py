# 1935_maximum_number_of_words_you_can_type.py
# -----------------------------------------------------
# ✅ 제목: Maximum Number of Words You Can Type (LeetCode 1935)
# ✅ 문제 설명(요약):
# - 문자열 text(공백으로 구분된 단어들)와 문자열 brokenLetters(고장난 키)가 주어진다.
# - 고장난 키에 해당하는 문자가 포함되지 않은 단어만 타이핑 가능.
# - text에서 타이핑 가능한 단어의 개수를 반환.
#
# ✅ 입력 형식(요지):
# - text: str (1 ≤ |text| ≤ 10^4, 소문자와 공백으로만 구성)
# - brokenLetters: str (소문자 알파벳, 길이 ≤ 26)
#
# ✅ 규칙 요약:
# 1) text를 공백으로 분리해 단어 단위로 처리.
# 2) 각 단어에 brokenLetters 중 하나라도 포함되면 불가능.
# 3) 고장난 문자가 전혀 없으면 전체 단어 수가 답.
#
# ✅ 입출력 예시(1개):
# - 입력: text = "hello world", brokenLetters = "ad"
# - "hello", "world" 모두 'a','d' 없음 → 2
# - 출력: 2
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenLetters = set(brokenLetters)             # 고장난 문자 집합
        text = text.split()                            # 단어 단위로 분리
        answer = 0
        for word in text:
            word = set(word)                           # 단어 내 문자 집합
            if word.isdisjoint(brokenLetters):         # 교집합 없으면 가능
                answer += 1
        return answer                                  # 가능한 단어 개수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 테스트 케이스 모두 통과. Accepted.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 처음엔 `if word and brokenLetters:`로 교집합을 확인하려 했지만,
#   이는 단순 불리언 평가일 뿐 교집합 검증이 아님.
# - 교집합 없는지 확인하려면 `isdisjoint` 또는 `if not (word & brokenLetters)`를 사용해야 함.
#
# 📚 사용된/필수 개념(최소):
# - 문자열 split으로 단어 분리
# - 집합(set)과 `isdisjoint`를 이용한 교집합 판정
# - 시간복잡도: O(|text| + |brokenLetters|), 공간복잡도: O(26)
