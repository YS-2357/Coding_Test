# 744_Find Smallest Letter Greater Than Target.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 744. Find Smallest Letter Greater Than Target
# 🏷️ 유형: 선형 탐색 / 순환(랩어라운드) 처리
#
# ✅ 문제 설명(요약):
#   - 정렬된 문자 배열 letters와 문자 target이 주어진다.
#   - target보다 사전순으로 “엄격히 큰” 문자 중 가장 작은 문자를 반환한다.
#   - 그런 문자가 없으면 배열이 원형처럼 동작하므로 letters[0]을 반환한다.
#
# ✅ 입력 형식(요지):
#   - letters: List[str]  (정렬된 소문자 리스트)
#   - target: str         (단일 문자)
#
# ✅ 규칙 요약:
#   - letters는 오름차순 정렬되어 있다.
#   - target보다 큰 문자가 존재하면 그중 최소 문자를 반환한다.
#   - 존재하지 않으면 첫 원소로 랩어라운드한다.
#
# 🧠 핵심 불변식(Invariant):
#   - 정렬된 배열에서 왼쪽부터 순회하며 처음 만나는 “target보다 큰 문자”가 곧 최소 후보이다.
#   - 끝까지 없으면 랩어라운드 규칙에 의해 답은 항상 letters[0]이다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:  # target보다 큰 최소 문자를 반환하는 함수
        for letter in letters:                                      # letters를 왼쪽부터 순회
            if ord(letter) > ord(target):                           # 현재 문자가 target보다 엄격히 크면
                return letter                                       # 첫 발견이 최소이므로 즉시 반환

        return letters[0]                                           # 끝까지 없으면 랩어라운드로 첫 문자를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 정렬 배열의 선형 탐색 + 없을 때 랩어라운드 처리.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n)  (최악 한 번 전체 순회)
#   - 공간: O(1)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - letters가 정렬되어 있으므로 이분탐색으로 O(log n)에 개선할 수 있다(개념만).
