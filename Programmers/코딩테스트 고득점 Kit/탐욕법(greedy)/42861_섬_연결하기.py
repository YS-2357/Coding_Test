# 42861_섬 연결하기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - n개의 섬과, 각 섬을 연결하는 다리의 정보가 주어진다.
# - 각 다리에는 연결 비용이 있으며, 모든 섬을 연결하는 최소 비용을 구해야 한다.
# - 모든 섬은 연결되어야 하며, 사이클은 없어야 한다 → MST(최소 신장 트리) 문제.

# ✅ 입력 형식:
# - n: 섬의 개수 (1 ≤ n ≤ 100)
# - costs: [a, b, cost] 형태의 리스트 (0 ≤ a,b < n, 1 ≤ cost ≤ 1,000)
#          a, b: 연결할 섬의 번호 / cost: 연결 비용
# - len(costs): 최대 10,000

# ✅ 출력 형식:
# - 모든 섬을 연결하는 최소 비용 (정수)

# ✅ 입출력 예제:
#   입력: n = 4, costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
#   출력: 4
# -----------------------------------------------------

def solution(n, costs):
    answer = 0  # MST(최소 신장 트리)의 총 비용을 저장할 변수

    # 1. 각 노드(섬)의 부모를 자기 자신으로 초기화 → Union-Find용 배열
    parent = [i for i in range(n)]

    # 2. 간선 리스트를 비용 기준으로 오름차순 정렬 → 크루스칼 알고리즘 핵심
    costs.sort(key=lambda x: x[2])

    # 3. Find 함수: 노드의 루트(대표자)를 찾는 함수 (경로 압축 적용)
    #    → 경로 압축으로 시간복잡도 거의 O(1) 수준
    def find(x):
        while parent[x] != x:            # 루트가 아닐 때까지 반복
            parent[x] = parent[parent[x]]  # 경로 압축 (한 단계 건너뛰기)
            x = parent[x]                  # 부모 갱신
        return x  # 루트 반환

    # 4. Union 함수: 두 노드를 하나의 집합으로 합침
    #    → 루트가 다르면 병합하고 True 반환 / 같으면 False (사이클 방지)
    def union(a, b):
        root_a = find(a)  # a의 루트 찾기
        root_b = find(b)  # b의 루트 찾기
        if root_a != root_b:  # 다른 그룹일 경우에만 합침
            if root_a < root_b:  # 번호가 작은 쪽을 루트로 (규칙)
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
            return True  # 연결 성공 → MST에 추가 가능
        return False  # 이미 같은 그룹 → 사이클 발생 → 추가 X

    # 5. 크루스칼 알고리즘 실행
    #    → 비용이 작은 간선부터 순회, 사이클이 없으면 연결
    for a, b, cost in costs:
        if union(a, b):        # 두 섬이 연결 가능한 경우
            answer += cost     # MST에 간선 추가 → 비용 누적

    # 6. 모든 섬이 연결된 후 최소 비용 반환
    return answer

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ visited[] 배열만으로는 사이클 판별 불가 → 잘못된 MST 생성
# ❌ 따라서 Union-Find를 반드시 사용해야 함

# ✅ GPT가 준 힌트 요약:
# - MST는 사이클 방지가 핵심 → Union-Find로 그룹 관리
# - 크루스칼 알고리즘:
#   1) 간선 정렬
#   2) find로 루트 비교
#   3) 다르면 union → 비용 추가

# ✅ 사용된 개념 요약:
# - MST(최소 신장 트리): n개의 노드를 최소 비용으로 연결 (사이클 없음)
# - 크루스칼 알고리즘: 간선 중심 → 비용 정렬 + Union-Find
# - Union-Find:
#   - find(x): 루트 탐색 (경로 압축)
#   - union(a,b): 두 집합 합치기
# - 시간 복잡도: O(E log E) (간선 정렬) + O(E α(N)) ≈ O(E log E)
#   → E = len(costs), α(N) = 아커만 함수 (거의 상수)

# -----------------------------------------------------
# 다른 풀이 1
# def solution(n, costs):
#     # 1) 간선 비용 오름차순 정렬: (w, u, v) 형태로 다루면 편함
#     edges = sorted([(w, u, v) for u, v, w in costs])

#     # 2) Union-Find 준비
#     parent = list(range(n))    # parent[x] = x의 대표(루트)
#     size = [1] * n             # 루트 트리의 크기(랭크 대신 size 사용)

#     def find(x):
#         # 경로 압축: 루트를 바로 가리키도록 갱신 (재귀 or 반복형 모두 OK)
#         while parent[x] != x:
#             parent[x] = parent[parent[x]]
#             x = parent[x]
#         return x

#     def union(a, b):
#         ra, rb = find(a), find(b)
#         if ra == rb:
#             return False  # 같은 집합 → 이 간선 채택하면 사이클
#         # 사이즈 기준으로 합치기(작은 트리를 큰 트리에 붙임)
#         if size[ra] < size[rb]:
#             ra, rb = rb, ra
#         parent[rb] = ra
#         size[ra] += size[rb]
#         return True

#     # 3) 간선 선택
#     total = 0
#     taken = 0
#     for w, u, v in edges:
#         if union(u, v):        # 사이클이 아니면 채택
#             total += w
#             taken += 1
#             if taken == n - 1: # MST 완성
#                 break
#     return total

# -----------------------------------------------------
# 다른 풀이 2
# import heapq

# def solution(n, costs):
#     # 1) 인접리스트 구성: 각 정점에서 (비용, 이웃) 형태로 저장
#     adj = [[] for _ in range(n)]
#     for u, v, w in costs:
#         adj[u].append((w, v))
#         adj[v].append((w, u))

#     # 2) Prim: 임의의 정점(0)에서 시작
#     visited = [False] * n
#     pq = [(0, 0)]          # (간선비용, 정점) — 시작 비용 0
#     total = 0
#     picked = 0

#     while pq and picked < n:
#         w, u = heapq.heappop(pq)
#         if visited[u]:
#             continue
#         # 새 정점 u 채택
#         visited[u] = True
#         total += w
#         picked += 1
#         # u에서 뻗는 간선들을 힙에 추가
#         for nw, nv in adj[u]:
#             if not visited[nv]:
#                 heapq.heappush(pq, (nw, nv))

#     # 연결 불가능 입력은 없다고 가정(문제 보장). 그래도 안전하게 확인하려면:
#     # if picked < n: return ??? (문제 보장으로 불필요)
#     return total
