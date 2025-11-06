# 3607_Power_Grid_Maintenance.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3607. Power Grid Maintenance
# ✅ 문제 설명(요약):
#   c개의 노드(1..c)와 무방향 간선 connections로 이루어진 전력망이 주어진다.
#   모든 노드는 초기에는 온라인 상태다.
#   두 종류의 쿼리를 순서대로 처리하여 응답을 반환한다.
#     • [1, x] : 정비 요청. x가 온라인이면 x를 반환.
#                x가 오프라인이면 x가 속한 연결 컴포넌트에서
#                온라인인 노드 중 가장 작은 ID를 반환. 없다면 -1.
#     • [2, x] : 종료 요청. 노드 x를 오프라인으로 표시.
#
# ✅ 입력 형식(요지):
#   c: int — 노드 수 (1..c)
#   connections: List[List[int]] — 무방향 간선 목록
#   queries: List[List[int]] — 각 원소는 [t, x] 형태의 쿼리
#
# ✅ 규칙 요약:
#   - 간선은 고정. 연결 컴포넌트 구조는 변하지 않는다.
#   - 각 컴포넌트에서 "현재 온라인인 노드의 최소 ID"를 빠르게 찾아야 한다.
#   - [2, x]로 x가 오프라인 되면 그 컴포넌트의 최소 온라인 ID를 필요 시 다음으로 갱신한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))                         # 부모 배열(1..c). DSU 초기화

        def find(x):
            while parent[x] != x:                           # 경로 압축의 반복적 구현
                parent[x] = parent[parent[x]]              # 한 단계 건너뛰며 압축
                x = parent[x]
            return x

        for a, b in connections:                            # 모든 간선으로 컴포넌트 병합
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        next_node = [0] * (c + 1)                           # 같은 컴포넌트 내에서 ID 오름차순 단일 연결 리스트의 next 포인터
        comp_min = [0] * (c + 1)                            # 각 컴포넌트 대표(root)별 "현재 최소 온라인 ID"
        last: dict[int, int] = {}                           # 각 컴포넌트에서 마지막으로 연결한 노드 ID 기록

        for i in range(1, c + 1):                           # 각 노드를 컴포넌트별로 오름차순 연결
            r = find(i)
            if comp_min[r] == 0:                            # 아직 첫 노드가 없다면
                comp_min[r] = i                             # 컴포넌트 최소 ID 설정
            else:
                next_node[last[r]] = i                      # 이전 노드의 next를 현재 i로 연결
            last[r] = i                                     # 마지막 노드 갱신

        offline = [False] * (c + 1)                         # 노드 온라인/오프라인 상태
        ans: List[int] = []                                 # 쿼리 결과

        for t, x in queries:
            if t == 1:                                      # 정비 요청
                if not offline[x]:                          # x가 온라인이면
                    ans.append(x)                           # x가 처리
                else:                                       # x가 오프라인이면
                    r = find(x)                             # x의 컴포넌트 루트
                    ans.append(comp_min[r] if comp_min[r] else -1)  # 컴포넌트의 최소 온라인 ID 또는 -1
            else:                                           # 종료 요청
                if not offline[x]:                          # 아직 온라인이라면만 처리
                    offline[x] = True                       # x를 오프라인으로 전환
                    r = find(x)                             # x의 컴포넌트 루트
                    if comp_min[r] == x:                    # 컴포넌트 최소가 x였다면 갱신 필요
                        y = next_node[x]                    # x 다음 후보부터 탐색
                        while y and offline[y]:             # 오프라인인 노드는 건너뛰기
                            y = next_node[y]
                        comp_min[r] = y if y else 0         # 다음 온라인 노드 또는 없음(0)

        return ans                                          # 모든 쿼리 결과 반환
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 연결 컴포넌트를 DSU로 고정한 뒤, 각 컴포넌트의 노드를 ID 오름차순 단일 연결 리스트로 구성.
#   - comp_min[root]에 "현재 최소 온라인 ID"만 유지하고,
#     종료 시 comp_min이 그 노드였을 때만 next 포인터를 따라가며 한 번에 갱신.
#   - 정비 요청은 O(1), 종료 요청은 comp_min이 바뀔 때만 연결 리스트를 전진.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념: DSU(Union-Find)로 컴포넌트 전처리 + 컴포넌트별 오름차순 단일 연결 리스트 + 게으른 전진.
#   - 동작 원리:
#       • 간선이 고정이므로 컴포넌트는 불변 → DSU로 한 번만 계산.
#       • 각 컴포넌트 노드를 오름차순으로 next 연결하여 "다음 후보"를 O(1)로 참조.
#       • 종료 시 comp_min이 종료 노드일 때만 next로 전진하면서 최초 온라인 노드로 업데이트.
#   - 주의점:
#       • comp_min이 아닌 내부 노드를 종료해도 comp_min은 변하지 않으므로 추가 처리 불필요.
#       • 같은 노드가 여러 번 종료되는 입력은 상태 체크로 무시.
#
# 📚 시간·공간 복잡도:
#   - 전처리: DSU 병합 O(c + |E| α(c))
#   - 쿼리 처리:
#       • [1, x]: O(1)
#       • [2, x]: comp_min이 해당 노드일 때만 while로 전진. 각 노드는 comp_min으로 "최대 한 번"만 스킵됨.
#         → 전체 쿼리 동안의 전진 총합 O(c)로 **상암ortized O(1)**.
#   - 총합: O(c + |E| α(c) + |Q|) 상암ortized
#   - 공간: O(c + |E|)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 컴포넌트별 최소 힙(min-heap) + lazy 삭제:
#       • 종료 시 힙에 삭제 마커를 남기고, 정비 요청 시 힙의 꼭대기를 정리.
#       • 구현은 직관적이나 파이썬에서는 삭제 마커 관리가 필요.
#   - 컴포넌트별 정렬 세트(TreeSet/SortedList):
#       • 최소 조회/삭제 O(log n)로 안정적. 다만 외부 자료구조 의존 가능.
#   - 본 풀이(연결 리스트 + comp_min 전진)는 파이썬 표준만으로 상암ortized O(1)을 달성해 코드가 짧고 빠름.
