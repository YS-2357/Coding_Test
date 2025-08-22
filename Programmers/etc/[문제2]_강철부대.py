# 문제2_강철부대(레벨3).py
# -----------------------------------------------------
# ✅ 제목: 강철부대 — 여러 출발지에서 목적지까지의 최단 시간
# ✅ 문제 설명(요약):
# - 무향 그래프(간선 가중치=1)에서 여러 sources가 destination으로 복귀하는 최단시간.
# - 복귀 불가능하면 -1.
#
# ✅ 입력 형식(요지):
# - n: 정점 수 (1..n)
# - roads: List[List[int]] (양방향 간선)
# - sources: List[int] (여러 출발 노드)
# - destination: int
#
# ✅ 규칙 요약(핵심 아이디어):
# - 간선 가중치가 전부 1 → **단일 BFS**를 destination에서 역방향으로 한 번만 수행.
# - 그 결과 거리 배열 dist로 모든 source의 답을 O(1) 조회.
#
# ✅ 입출력 예시(간단):
# - n=3, roads=[[1,2],[2,3]], sources=[2,3], destination=1 → [1,2]
# - n=5, roads=[[1,2],[1,4],[2,4],[2,5],[4,5]], sources=[1,3,5], destination=5 → [2,-1,0]

from collections import deque

def solution(n, roads, sources, destination):
    adj = [[] for _ in range(n+1)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)
    INF = 10**9
    dist = [INF]*(n+1)
    # 목적지에서 역으로 BFS
    q = deque([destination])
    dist[destination] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                q.append(v)
    # 조회
    return [(-1 if dist[s] == INF else dist[s]) for s in sources]

# -----------------------------------------------------
# 📚 꼭 필요한 개념 & 사용 개념(최소):
# - 무가중치 그래프 최단거리: 단일 **BFS**
# - “여러 출발지 → 하나의 목적지”는 **목적지에서 역방향 BFS 한 번**으로 전체 커버
