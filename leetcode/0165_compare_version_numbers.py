# 0165_compare_version_numbers.py
# -----------------------------------------------------
# ✅ 제목: Compare Version Numbers
# ✅ 문제 설명(요약):
# - 두 버전 문자열(version1, version2)을 비교한다.
# - 각 버전은 '.'으로 구분된 정수 시퀀스로 표현된다.
# - 각 세그먼트를 앞에서부터 순차적으로 비교하며:
#   - version1 > version2 → 1 반환
#   - version1 < version2 → -1 반환
#   - 같으면 0 반환
#
# ✅ 입력 형식(요지):
# - version1, version2: 문자열 (버전 번호)
#
# ✅ 규칙 요약:
# 1) '.' 단위로 split 후 정수로 비교
# 2) 길이가 다르면 부족한 부분은 0으로 취급
# 3) 모든 비교가 끝나면 동일
#
# ✅ 입출력 예시(1개):
# - version1 = "1.01", version2 = "1.001" → 0
# - version1 = "1.0", version2 = "1.0.0" → 0
# - version1 = "0.1", version2 = "1.1" → -1
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1 = version1.split(".")                   # '.' 기준으로 분리
        num2 = version2.split(".")
        for n1, n2 in zip_longest(num1, num2, fillvalue=0):  # 길이 맞춰서 순회
            n1, n2 = int(n1), int(n2)                # 정수로 변환
            if n1 > n2:                              # 더 큰 버전 발견
                return 1
            elif n1 < n2:                            # 더 작은 버전 발견
                return -1
        return 0                                     # 끝까지 동일하면 0 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - zip_longest로 길이 맞춰 처리하여 모든 예제 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기엔 zip만 사용 → 짧은 리스트까지만 비교 → "1.0" vs "1.0.0" 케이스 실패
# - zip_longest(fillvalue=0)로 보완하여 해결.
#
# 📚 사용된/필수 개념(최소):
# - 문자열 split 후 정수 변환
# - zip_longest로 다른 길이 버전 보정
# - 비교 연산자 활용
# - 시간복잡도: O(max(n, m)), n, m은 version1, version2의 길이
