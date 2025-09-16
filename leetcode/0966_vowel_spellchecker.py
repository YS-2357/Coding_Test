# 0966_vowel_spellchecker.py
# -----------------------------------------------------
# ✅ 제목: Vowel Spellchecker (LeetCode 966)
# ✅ 문제 설명(요약):
# - 주어진 단어 리스트 wordlist와 질의 queries가 있다.
# - 각 query를 wordlist와 매칭하는 규칙:
#   1) 정확히 일치하면 그대로 반환.
#   2) 대소문자 무시(case-insensitive)로 일치하면 wordlist의 첫 등장 단어 반환.
#   3) 모음(a,e,i,o,u)을 모두 동일 취급(vowel-error)하여 일치하면 wordlist의 첫 등장 단어 반환.
#   4) 위 경우 모두 아니면 "" 반환.
#
# ✅ 입력 형식(요지):
# - wordlist: List[str], queries: List[str]
#
# ✅ 규칙 요약:
# - 우선순위: Exact > Case-insensitive > Vowel-error > "".
# - 첫 등장 단어 우선 선택.
#
# ✅ 입출력 예시(1개):
# - wordlist = ["KiTe","kite","hare","Hare"]
# - queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# - 출력 = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            word = word.lower()                  # 대소문자 무시
            aeiou = "aeiou"
            for v in aeiou:
                word = word.replace(v, "*")      # 모든 모음을 "*"로 치환
            return word

        answer = []
        exact_set = set(wordlist)                # 정확 일치 확인용
        case_map = {}                            # 소문자 기준 첫 등장 단어 매핑
        vowel_map = {}                           # devowel 기준 첫 등장 단어 매핑
        for w in wordlist:
            k1 = w.lower()
            if k1 not in case_map:               # 첫 등장 단어만 저장
                case_map[k1] = w
            k2 = devowel(w)
            if k2 not in vowel_map:              # 첫 등장 단어만 저장
                vowel_map[k2] = w

        for query in queries:
            ql = query.lower()                   # query 소문자화
            qd = devowel(query)                  # query devowel 처리
            if query in exact_set:               # 1) Exact
                answer.append(query)
            elif ql in case_map:                 # 2) Case-insensitive
                answer.append(case_map[ql])
            elif qd in vowel_map:                # 3) Vowel-error
                answer.append(vowel_map[qd])
            else:                                # 4) 매칭 실패
                answer.append("")
        
        return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 초기 코드에서 case_map, vowel_map이 마지막 단어로 덮여 우선순위 규칙 위반.
# - devowel 함수에서 대문자 모음 처리가 누락되어 매칭 실패.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - dict comprehension 대신 for-loop 사용, 첫 등장 단어만 저장하도록 수정.
# - devowel 내부에서 소문자화 후 모음을 일괄 치환하도록 개선.
#
# 📚 사용된/필수 개념(최소):
# - 문자열 처리: 소문자화, 모음 치환(devowel)
# - 해시맵 기반 매핑(case_map, vowel_map) → 빠른 조회
# - 우선순위 조건문: Exact > Case-insensitive > Vowel-error > "".
# - 시간복잡도: O(L + Q·m), L=wordlist 길이 합, Q=queries 개수, m=평균 길이
