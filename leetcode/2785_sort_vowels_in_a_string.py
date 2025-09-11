# 2785_sort_vowels_in_a_string.py
# -----------------------------------------------------
# ✅ 제목: Sort Vowels in a String
# ✅ 문제 설명(요약):
# - 문자열 s에서 자음은 그대로 두고, 모음만 사전순으로 정렬해 다시 배치.
# - 모음: a, e, i, o, u, A, E, I, O, U.
#
# ✅ 입력 형식(요지):
# - s: str (길이 1 이상, 알파벳 대소문자)
#
# ✅ 규칙 요약:
# 1) 문자열 내 모든 모음을 수집.
# 2) 모음을 정렬.
# 3) 원래 위치에 정렬된 모음을 다시 채워 넣음.
#
# ✅ 입출력 예시(1개):
# - s = "lEetcOde"
#   모음 = [E, e, O, e] → 정렬 = [E, O, e, e]
#   결과 = "lEOtcede"
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels, nums = [], []                        # 모음 목록, 모음 인덱스 목록
        for idx, char in enumerate(s):
            if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                vowels.append(char)                  # 모음만 수집
                nums.append(idx)                     # 모음 위치 기록
        vowels.sort()                                # 모음 정렬
        
        if not vowels:                               # 모음 없으면 그대로 반환
            return s
        
        s = list(s)                                  # 문자열을 리스트로 변환(수정 가능)
        for i, num in enumerate(nums):               # 기록된 위치에 정렬된 모음 채움
            s[num] = vowels[i]
        return "".join(s)                            # 리스트 → 문자열

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 문자열 직접 수정하려다 TypeError 발생.
# - list로 변환 후 join으로 해결.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (오류) s[num] = ... (문자열은 immutable).
# - (수정) list(s)로 변환 후 join으로 마무리.
#
# 📚 사용된/필수 개념(최소):
# - 문자열 불변성 처리(list 변환)
# - 인덱스 추적 후 재배치
# - 시간복잡도: O(n log n) (모음 정렬), 공간복잡도: O(n)

# -----------------------------------------------------
# 다른 풀이
# class Solution:
#     def sortVowels(self, s: str) -> str:
#         vowels_set = set("AEIOUaeiou")
#         vowels = [c for c in s if c in vowels_set]
#         vowels.sort()

#         it = iter(vowels)

#         answer = ''.join(next(it) if c in vowels_set else c for c in s)

#         return answer
