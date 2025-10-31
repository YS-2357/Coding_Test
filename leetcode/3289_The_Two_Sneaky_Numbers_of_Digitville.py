# 3289_The_Two_Sneaky_Numbers_of_Digitville.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3289. The Two Sneaky Numbers of Digitville
# ✅ 문제 설명(요약):
#   Digitville에는 모든 숫자가 한 번씩만 등장해야 하지만,
#   “교활한(sneaky)” 두 숫자가 두 번 등장했다.
#   주어진 배열 nums에서 정확히 두 번 등장한 숫자들을 찾아
#   오름차순으로 반환하라.
#
# ✅ 입력 형식(요지):
#   - nums: 정수 리스트 (길이 n)
#   - 각 숫자는 0 이상 100 이하 (중복 존재 가능)
#
# ✅ 규칙 요약:
#   - 모든 숫자 중 등장 횟수가 2인 원소를 찾는다.
#   - 그 두 값을 정렬하여 반환한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        detective = dict()                    # 각 숫자의 등장 횟수를 기록할 딕셔너리
        ans = []                              # 두 번 등장한 숫자만 저장할 리스트

        for n in nums:                        # 모든 숫자 순회
            detective[n] = detective.get(n, 0) + 1  # 등장 횟수 1 증가
            if detective[n] == 2:             # 정확히 두 번째 등장 시
                ans.append(n)                 # 결과 리스트에 추가

        ans.sort()                            # 오름차순 정렬
        return ans                            # 교활한 숫자 2개 반환
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 모든 테스트케이스 정답 일치.
#   - 두 번 등장한 숫자만 실시간으로 추출해 두 번째 루프 불필요.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념: 해시맵(딕셔너리) 기반 빈도수 카운팅.
#   - 핵심 아이디어: 등장 시점에 바로 카운트 증가 및 필터링.
#   - 기존 두 번 순회(O(2n)) 구조를 한 번의 순회(O(n))로 축소.
#
# 📚 시간·공간 복잡도:
#   - 시간복잡도: O(n) (리스트 한 번 순회 + 정렬 O(k log k), k=2 → 상수)
#   - 공간복잡도: O(n) (등장 횟수 저장용 딕셔너리)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - collections.Counter 활용 시 한 줄 풀이 가능:
#       from collections import Counter
#       return sorted([num for num, c in Counter(nums).items() if c == 2])
#   - 하지만 현재 풀이가 이미 O(n) 최적이며, 실시간 필터링 구조가 가장 효율적이다.
