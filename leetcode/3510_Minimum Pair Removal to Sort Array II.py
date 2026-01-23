# 3510_Minimum Pair Removal to Sort Array II.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3510. Minimum Pair Removal to Sort Array II
# 🏷️ 유형: 우선순위 큐(힙) / 연결 리스트 / 시뮬레이션 / 그리디(최소 인접합 선택)
#
# ✅ 문제 설명(요약):
#   - 배열에서 인접한 두 원소를 선택해 제거하고 그 합을 하나의 원소로 대체하는 연산을 반복한다.
#   - 배열이 오름차순(비내림차순)이 되면 중단하며, 그때까지의 연산 횟수를 반환한다.
#   - I 버전은 단순 시뮬레이션으로 가능하지만, II 버전은 효율화를 위해 자료구조가 필요하다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]
#
# ✅ 규칙 요약:
#   - 한 연산은 인접 원소 2개를 1개로 합치는 것이며 길이가 1 줄어든다.
#   - “최소 인접합” 쌍을 반복적으로 합치는 흐름을 빠르게 구현한다.
#   - 배열이 오름차순이 되면 더 이상 합치지 않는다.
#
# 🧠 핵심 불변식(Invariant):
#   - 연결 리스트에서 인접 관계(prev/next)를 유지하면 “현재 인접쌍”만 갱신하면 된다.
#   - pq(힙)에는 (인접한 두 노드, 그 합 cost)를 넣어 두고, 항상 최소 cost 후보를 먼저 꺼낸다.
#   - 이미 병합된 노드이거나(cost가 바뀐 stale 항목) 더 이상 인접하지 않은 쌍은 무시한다.
#   - decrease_count는 “현재 배열에서 nums[i] > nums[i+1] 인 인접 역전(inversion) 개수”를 추적하며,
#     이 값이 0이 되면 오름차순이므로 종료한다.
#
# ✅ 정답 코드(제공된 풀이; 수정 금지)

class Node:                                                                # 연결 리스트 노드를 표현하는 클래스 정의
    def __init__(self, value, left):                                       # 노드 초기화 함수 정의
        self.value = value                                                 # 현재 노드의 값(원소 값 또는 병합된 합)을 저장
        self.left = left                                                   # 원래 배열에서의 왼쪽 인덱스(타이브레이커/병합 추적용)
        self.prev = None                                                   # 이전 노드를 가리키는 포인터 초기화
        self.next = None                                                   # 다음 노드를 가리키는 포인터 초기화


class Solution:                                                            # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def minimumPairRemoval(self, nums: List[int]) -> int:                  # 최소 연산 횟수를 반환하는 함수
        class PQItem:                                                      # 힙에 들어갈 아이템 클래스를 내부에 정의
            def __init__(self, first, second, cost):                       # PQItem 초기화 함수 정의
                self.first = first                                         # 인접쌍의 첫 번째 노드 포인터를 저장
                self.second = second                                       # 인접쌍의 두 번째 노드 포인터를 저장
                self.cost = cost                                           # 두 노드 값의 합(cost)을 저장

            def __lt__(self, other):                                       # 힙에서의 정렬 기준을 정의(최소 힙)
                if self.cost == other.cost:                                # cost가 같으면
                    return self.first.left < other.first.left              # 더 왼쪽에 있는 쌍을 우선 처리하도록 타이브레이커 적용
                return self.cost < other.cost                              # 기본적으로 cost가 작은 쌍이 우선

        pq = []                                                            # 인접쌍을 관리하는 최소 힙을 초기화
        head = Node(nums[0], 0)                                            # 연결 리스트의 헤드 노드를 첫 원소로 생성
        current = head                                                     # 현재 노드 포인터를 head로 시작
        merged = [False] * len(nums)                                       # 원본 인덱스 기준으로 “삭제(병합됨)” 여부를 기록하는 배열
        decrease_count = 0                                                 # 인접 역전(nums[i] > nums[i+1]) 개수를 카운트하는 변수
        count = 0                                                          # 실제로 수행한 병합 연산 횟수를 카운트하는 변수

        for i in range(1, len(nums)):                                      # 두 번째 원소부터 끝까지 순회하며 연결 리스트와 힙을 구성
            new_node = Node(nums[i], i)                                    # 새 노드를 생성(값과 원본 인덱스 기록)
            current.next = new_node                                        # 현재 노드의 next를 새 노드로 연결
            new_node.prev = current                                        # 새 노드의 prev를 현재 노드로 연결
            heapq.heappush(                                                # 현재 인접쌍(current, new_node)을 힙에 삽입
                pq, PQItem(current, new_node, current.value + new_node.value)
            )

            if nums[i - 1] > nums[i]:                                      # 원본 배열 기준으로 인접 역전이 있으면
                decrease_count += 1                                        # 역전 개수를 증가

            current = new_node                                             # current를 다음 노드로 이동

        while decrease_count > 0:                                          # 역전이 남아있는 동안 병합을 계속 수행
            item = heapq.heappop(pq)                                       # 힙에서 cost가 가장 작은 인접쌍 후보를 꺼냄
            first, second, cost = item.first, item.second, item.cost       # 후보 쌍 노드와 cost를 로컬 변수로 꺼냄

            if (                                                          # 다음 조건이면 이 PQItem은 더 이상 유효하지 않음
                merged[first.left]                                         # 첫 노드가 이미 병합/삭제되었거나
                or merged[second.left]                                     # 두 번째 노드가 이미 병합/삭제되었거나
                or first.value + second.value != cost                      # 현재 노드 값 합이 cost와 달라 stale 항목인 경우
            ):
                continue                                                   # 무효 항목이므로 다음 후보를 뽑음
            count += 1                                                     # 유효한 병합을 수행하므로 연산 횟수를 증가

            if first.value > second.value:                                 # 병합 대상 쌍 자체가 역전이었다면
                decrease_count -= 1                                        # 해당 역전 1개는 병합으로 사라지므로 감소

            prev_node = first.prev                                         # first의 이전 노드를 저장
            next_node = second.next                                        # second의 다음 노드를 저장
            first.next = next_node                                         # first가 병합 결과 노드가 되므로 next를 second.next로 연결
            if next_node:                                                  # 다음 노드가 존재하면
                next_node.prev = first                                     # next_node의 prev를 first로 갱신

            if prev_node:                                                  # 이전 노드가 존재하면(왼쪽 경계가 아니면)
                if prev_node.value > first.value and prev_node.value <= cost:  # (prev, first) 역전이 병합 후 해소되는 경우
                    decrease_count -= 1                                    # 역전 개수를 1 감소
                elif prev_node.value <= first.value and prev_node.value > cost: # (prev, first)가 병합 후 새로 역전이 되는 경우
                    decrease_count += 1                                    # 역전 개수를 1 증가

                heapq.heappush(                                            # 병합 후 새 인접쌍(prev_node, first)을 힙에 삽입
                    pq, PQItem(prev_node, first, prev_node.value + cost)
                )

            if next_node:                                                  # 다음 노드가 존재하면(오른쪽 경계가 아니면)
                if second.value > next_node.value and cost <= next_node.value: # (second, next) 역전이 병합 후 해소되는 경우
                    decrease_count -= 1                                    # 역전 개수를 1 감소
                elif second.value <= next_node.value and cost > next_node.value: # (second, next)가 병합 후 새로 역전이 되는 경우
                    decrease_count += 1                                    # 역전 개수를 1 증가
                heapq.heappush(                                            # 병합 후 새 인접쌍(first, next_node)을 힙에 삽입
                    pq, PQItem(first, next_node, cost + next_node.value)
                )

            first.value = cost                                             # first 노드 값을 병합 결과(cost)로 업데이트
            merged[second.left] = True                                     # second 노드는 제거되었음을 표시(병합됨)

        return count                                                       # 모든 역전이 해소될 때까지의 병합 횟수를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 제출 코드 기준: 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 연결 리스트로 인접 관계 유지 + 최소 힙으로 최소 인접합 쌍 선택 + 역전 개수(decrease_count)로 종료 조건 관리.
#
# 📚 시간·공간 복잡도:
#   - 시간: O((n + k) log n) 수준(힙 연산 중심; k는 병합 횟수)으로 동작하도록 설계된 시뮬레이션.
#   - 공간: O(n) (노드/힙/merged 배열)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 활성 구간을 인덱스로 관리하며 lazy deletion을 더 엄격히 처리하는 자료구조(예: union-find로 다음 유효 인덱스 점프)도 가능하다(개념만).
