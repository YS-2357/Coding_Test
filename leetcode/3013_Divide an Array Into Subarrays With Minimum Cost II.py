# 3013_Divide an Array Into Subarrays With Minimum Cost II.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3013. Divide an Array Into Subarrays With Minimum Cost II
# 🏷️ 유형: 슬라이딩 윈도우 / 정렬 멀티셋(두 SortedList) / k-최소합 유지
#
# ✅ 문제 설명(요약):
#   - nums에서 특정 규칙으로 원소들을 선택해 비용을 최소화한다.
#   - 첫 원소 nums[0]은 항상 비용에 포함된다.
#   - 윈도우(거리 dist 제약) 안에서 필요한 개수만큼의 “최소 원소 합”을 빠르게 유지하며,
#     후보 끝점(i)을 움직여 최소 비용을 갱신한다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]
#   - k: int
#   - dist: int
#
# ✅ 규칙 요약:
#   - 매 후보 i에 대해, i를 마지막 선택으로 포함하고(코드에서는 nums[i]),
#     그 이전 구간에서 조건을 만족하는 k-2개의 최소 원소 합을 더한다.
#   - 마지막에 nums[0]을 더해 전체 최소 비용을 만든다.
#
# 🧠 핵심 불변식(Invariant):
#   - Container는 “현재 활성 원소들” 중 k개(여기서는 k-2개)의 최솟값만 st1에 유지한다.
#   - st1에는 항상 k개(또는 가능한 만큼)의 가장 작은 원소가 들어가며, sm은 st1 원소 합이다.
#   - st2에는 나머지 원소가 들어가며, st2[0]은 st2의 최소값(= st1로 옮겨야 할 후보)이다.
#   - 슬라이딩 윈도우가 이동할 때, 제거(erase)와 추가(add)를 수행한 뒤 adjust()로 균형을 맞춘다.
#
# ✅ 정답 코드(제공된 풀이; 절대 수정 금지)

class Container:                                                        # k개의 최소 원소 합을 유지하기 위한 컨테이너 클래스 정의
    def __init__(self, k: int):                                         # 컨테이너 초기화 함수 정의
        self.k = k                                                      # st1에 유지할 “최소 원소 개수” k를 저장
        self.st1 = SortedList()                                         # 작은 원소 k개를 저장할 SortedList(멀티셋)
        self.st2 = SortedList()                                         # 나머지 원소를 저장할 SortedList(멀티셋)
        self.sm = 0                                                     # st1에 들어있는 원소들의 합을 저장

    def adjust(self):                                                   # st1과 st2의 균형을 맞추는 함수 정의
        while len(self.st1) < self.k and len(self.st2) > 0:             # st1이 부족하고 st2에 원소가 남아있다면
            x = self.st2[0]                                             # st2의 최소 원소를 가져오고
            self.st1.add(x)                                             # 그 원소를 st1에 넣어 최소 집합을 보강
            self.st2.remove(x)                                          # st2에서 해당 원소를 제거
            self.sm += x                                                # st1 합(sm)에 x를 더해 반영

        while len(self.st1) > self.k:                                   # st1이 k개를 초과하면
            x = self.st1[-1]                                            # st1의 최대 원소를 가져와
            self.st2.add(x)                                             # st2로 보내고(나머지 집합으로 이동)
            self.st1.remove(x)                                          # st1에서 제거
            self.sm -= x                                                # st1 합(sm)에서 x를 빼서 반영

    def add(self, x: int):                                              # 원소 x를 컨테이너에 삽입하는 함수 정의
        if len(self.st2) > 0 and x >= self.st2[0]:                      # x가 st2의 최소값 이상이면(큰 편이면)
            self.st2.add(x)                                             # st2에 넣어도 최소 k집합에 들 가능성이 낮다고 보고 st2에 추가
        else:                                                           # 그렇지 않으면(작은 편이면)
            self.st1.add(x)                                             # st1에 우선 넣고
            self.sm += x                                                # sm에도 즉시 반영
        self.adjust()                                                   # 삽입 후 st1이 정확히 k개의 최소를 갖도록 조정

    def erase(self, x: int):                                            # 원소 x를 컨테이너에서 삭제하는 함수 정의
        if x in self.st1:                                               # x가 st1에 존재하면
            self.st1.remove(x)                                          # st1에서 제거하고
            self.sm -= x                                                # sm에서도 제거분을 반영
        elif x in self.st2:                                             # x가 st2에 존재하면
            self.st2.remove(x)                                          # st2에서 제거
        self.adjust()                                                   # 삭제 후에도 균형을 맞추어 st1을 k개 최소로 유지

    def sum(self) -> int:                                               # st1의 원소 합(=k개 최소 합)을 반환하는 함수 정의
        return self.sm                                                  # 누적합 sm을 그대로 반환


class Solution:                                                         # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:    # 최소 비용을 반환하는 함수
        n = len(nums)                                                   # 배열 길이를 저장
        cnt = Container(k - 2)                                          # k-2개의 최소 원소 합을 유지할 컨테이너 생성
        for i in range(1, k - 1):                                       # 초기 구간에서 컨테이너에 넣을 원소들을 순회
            cnt.add(nums[i])                                            # nums[1..k-2]를 컨테이너에 삽입하여 초기 상태 구성

        ans = cnt.sum() + nums[k - 1]                                   # 초기 후보 비용(최소합 + 특정 끝 원소)을 계산
        for i in range(k, n):                                           # i를 k부터 n-1까지 이동시키며 후보를 갱신
            j = i - dist - 1                                            # 윈도우에서 빠져야 할 인덱스를 계산
            if j > 0:                                                   # 제거 인덱스가 유효한 범위(0은 고정 처리이므로 제외)면
                cnt.erase(nums[j])                                      # 윈도우 밖으로 나간 nums[j]를 컨테이너에서 제거
            cnt.add(nums[i - 1])                                        # 새로 활성화되는 nums[i-1]를 컨테이너에 추가
            ans = min(ans, cnt.sum() + nums[i])                         # 현재 i를 끝으로 하는 비용 후보로 ans를 갱신

        return ans + nums[0]                                            # 마지막에 항상 포함되는 nums[0]을 더해 최종 최소 비용 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 제출 코드 기준: 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 슬라이딩 윈도우 + (k-2)개 최소 원소 합 유지(두 멀티셋 분리) + 매 끝점 후보 비교.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n) 수준(SortedList 삽입/삭제가 로그 시간으로 동작)
#   - 공간: O(n) (컨테이너 내부 원소 저장)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - Python 표준 라이브러리만으로는 SortedList가 없어, 두 힙 + lazy deletion로 유사 구조를 구현하는 방식도 가능하다(개념만).
