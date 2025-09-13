# 3541_find_most_frequent_vowel_and_consonant.py
# -----------------------------------------------------
# ✅ 제목: Find Most Frequent Vowel and Consonant (LeetCode 3541)
# ✅ 문제 설명(요약):
# - 문자열 s에서 가장 많이 등장한 모음의 빈도와 가장 많이 등장한 자음의 빈도를 더해 반환.
# - 모음: a, e, i, o, u
# - 모음이나 자음이 없으면 해당 빈도는 0으로 취급.
#
# ✅ 입력 형식(요지):
# - 문자열 s (영문 소문자, 1 ≤ |s| ≤ 100)
#
# ✅ 규칙 요약:
# 1) 전체 문자열을 스캔하며 각 문자의 빈도를 계산.
# 2) 모음 중 최빈값(max_v), 자음 중 최빈값(max_c) 찾음.
# 3) 결과 = max_v + max_c.
#
# ✅ 입출력 예시(1개):
# - 입력: s = "leetcode"
# - 모음 빈도: e=3, o=1 → max_v = 3
# - 자음 빈도: l=1, t=1, c=1, d=1 → max_c = 1
# - 출력: 3 + 1 = 4
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def maxFreqSum(self, s: str) -> int:
        hash_map = {}                               # 문자 빈도 저장
        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1

        aeiou = "aeiou"                             # 모음 집합
        max_v, max_c = 0, 0
        for key, value in hash_map.items():         # 각 문자에 대해
            if key in aeiou:                        # 모음이면
                max_v = max(max_v, value)           # 모음 최대 갱신
            else:                                   # 자음이면
                max_c = max(max_c, value)           # 자음 최대 갱신
        
        return max_v + max_c                        # 합산 후 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 테스트 케이스 모두 통과. Accepted.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 특별한 오류 없음. 단, 문자열이 모두 모음/자음인 경우도 올바르게 처리됨(빈도 0 처리).
#
# 📚 사용된/필수 개념(최소):
# - 해시맵을 이용한 빈도 카운트
# - 모음/자음 분리 및 최대값 탐색
# - 시간복잡도: O(n), 공간복잡도: O(1) (최대 26문자)
