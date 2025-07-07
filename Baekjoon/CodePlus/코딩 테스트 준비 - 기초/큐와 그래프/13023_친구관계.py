# 백준 13023번: 친구 관계 (그래프 탐색 - DFS)
# -----------------------------------------------------
# ✅ 문제 설명:
# - N명의 사람(0번 ~ N-1번)이 있으며, M개의 친구 관계(무방향 간선)가 주어진다.
# - 다섯 명이 연속해서 친구 관계를 맺고 있는지 확인하는 문제.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 정수 N, M (5 ≤ N ≤ 2000, 1 ≤ M ≤ 2000)이 주어진다.
# - 이후 M개의 줄에 두 정수 A, B가 주어진다. (0 ≤ A, B < N)
#
# ✅ 출력 형식:
# - 다섯 명이 연속해서 친구 관계를 이루는 경우 1 출력.
# - 그렇지 않다면 0 출력.
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   5 4
#   0 1
#   1 2
#   2 3
#   3 4
# 🔹 예제 출력:
#   1
# -----------------------------------------------------

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

# ✅ 그래프 입력 (무방향 그래프)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

# ✅ DFS 탐색 함수
def dfs(node, depth):
    if depth == 5:  # 깊이가 5이면 조건 충족
        print(1)
        exit()
    
    visited[node] = True  # 현재 노드 방문 처리
    
    for neighbor in graph[node]:  # 인접 노드 탐색
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
    
    visited[node] = False  # 백트래킹 (방문 취소)

# ✅ 모든 노드를 시작점으로 DFS 실행
visited = [False] * N  # 방문 배열 초기화
for start in range(N):
    dfs(start, 1)

# ✅ 끝까지 탐색해도 depth=5가 없으면 0 출력
print(0)

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리
# - `graph`를 인접 리스트로 구현하여 탐색 최적화
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **DFS 실행 시 `visited` 배열을 초기화하지 않음**
#    - 기존 코드: `visited = [False] * N`이 한 번만 설정됨.
#    - 문제점: 한 번 방문한 노드가 모든 DFS에서 공유됨.
#    - 해결 방법: `dfs()`를 호출할 때 `visited`를 초기화하거나, 백트래킹을 올바르게 유지해야 함.
#
# 2️⃣ **DFS 탐색 중 중복 방문 방지**
#    - 기존 코드에서는 `visited[node]`를 `True`로 설정한 후 백트래킹 과정에서 `False`로 재설정했음.
#    - DFS 탐색에서 불필요한 경로를 탐색하지 않도록 방문 관리가 필요함.
#
# ✅ 최종 코드에서 수정한 점:
# - `dfs()` 내부에서 방문 체크 후 백트래킹을 올바르게 수행함.
# - `exit()`를 활용하여 깊이가 5 이상이 되는 순간 즉시 프로그램 종료.
# - 입력을 빠르게 처리하기 위해 `sys.stdin.readline()`을 사용함.
# -----------------------------------------------------
