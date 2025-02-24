# 백준 1260번: DFS와 BFS (그래프 탐색 - DFS, BFS)
# -----------------------------------------------------
# ✅ 문제 설명:
# - N개의 정점(1번 ~ N번)과 M개의 간선이 주어진다.
# - DFS와 BFS를 수행한 결과를 출력하는 문제.
# - DFS 결과를 먼저 출력하고, BFS 결과를 출력해야 한다.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 정수 N, M, V (1 ≤ N ≤ 1,000, 1 ≤ M ≤ 10,000, 1 ≤ V ≤ N) 가 주어진다.
# - 이후 M개의 줄에 두 정수 A, B가 주어진다. (1 ≤ A, B ≤ N)
# - 간선은 무방향이며, 같은 간선이 여러 번 주어지지 않음.
#
# ✅ 출력 형식:
# - 첫 번째 줄에 DFS 탐색 결과 출력 (공백으로 구분)
# - 두 번째 줄에 BFS 탐색 결과 출력 (공백으로 구분)
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   4 5 1
#   1 2
#   1 3
#   1 4
#   2 4
#   3 4
# 🔹 예제 출력:
#   1 2 4 3
#   1 2 3 4
# -----------------------------------------------------

import sys
from collections import deque

# ✅ 입력 처리
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]  # 그래프 인접 리스트 초기화

# ✅ 그래프 입력 (무방향 그래프)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())  # `.split()` 추가하여 정수 변환
    graph[A].append(B)
    graph[B].append(A)

# ✅ 탐색 순서 보장을 위해 각 정점의 인접 리스트를 정렬
for i in range(1, N+1):
    graph[i].sort()

# ✅ DFS 탐색 함수 (재귀 방식)
def dfs(node, lst):
    visited[node] = True  # 현재 노드 방문 체크
    lst.append(node)  # 방문한 노드 추가

    for neighbor in graph[node]:  # 인접 노드 탐색
        if not visited[neighbor]:  # 방문하지 않은 노드만 탐색
            dfs(neighbor, lst)

# ✅ BFS 탐색 함수 (큐 방식)
def bfs(start):
    queue = deque([start])  # 큐 초기화 (시작 노드 삽입)
    visited[start] = True  # 시작 노드 방문 처리
    result = []  # 방문 순서 저장 리스트

    while queue:
        node = queue.popleft()  # 큐에서 노드 꺼내기
        result.append(node)  # 방문한 노드 기록

        for neighbor in graph[node]:  # 현재 노드의 인접 노드 탐색
            if not visited[neighbor]:  # 방문하지 않은 노드만 추가
                queue.append(neighbor)
                visited[neighbor] = True  # 방문 체크

    print(*result)  # ✅ BFS 탐색 결과 한 번만 출력

# ✅ DFS 실행
visited = [False] * (N+1)  # DFS 방문 배열 초기화
dfs_result = []
dfs(V, dfs_result)
print(*dfs_result)  # ✅ DFS 탐색 결과 출력

# ✅ BFS 실행
visited = [False] * (N+1)  # BFS 방문 배열 초기화
bfs(V)  # ✅ BFS 탐색 결과 출력

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리
# - `graph`를 인접 리스트로 구현하여 탐색 최적화
# - DFS는 재귀를 사용하여 구현, BFS는 큐를 사용하여 구현
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **DFS 중간 출력 문제**
#    - 기존 코드에서 `print(*lst)`를 DFS 내부에서 실행하여 재귀 호출될 때마다 출력됨.
#    - 해결 방법: DFS가 끝난 후 `print(*dfs_result)`로 한 번만 출력.
#
# 2️⃣ **BFS 탐색에서 방문 배열(`visited`) 문제**
#    - 기존 코드에서 DFS 실행 후 BFS 실행 시 `visited` 배열이 공유됨.
#    - 해결 방법: BFS 실행 전에 `visited` 배열을 새로 초기화하여 독립적으로 탐색 가능하도록 변경.
#
# ✅ 요청한 DFS & BFS 추가 힌트:
# 🔹 **DFS (깊이 우선 탐색) 동작 방식**
#    - 현재 노드에서 **가능한 모든 경로를 탐색**하며, 더 깊이 이동할 수 있는 경로를 우선적으로 탐색.
#    - **스택(LIFO) 방식처럼 작동**하며, 백트래킹을 사용하여 되돌아감.
#    - **예제 탐색 과정 (입력: 4 5 1)**:
#      ```
#      1 → 2 → 4 (백트래킹) → 3
#      결과: 1 2 4 3
#      ```
#
# 🔹 **BFS (너비 우선 탐색) 동작 방식**
#    - 현재 노드에서 **가까운 노드를 먼저 탐색**하며, 한 단계씩 탐색을 확장.
#    - **큐(FIFO) 방식처럼 작동**하며, `deque`를 활용하여 탐색.
#    - **예제 탐색 과정 (입력: 4 5 1)**:
#      ```
#      1 → 2, 3, 4
#      2 → 4 (이미 방문)
#      3 → 4 (이미 방문)
#      결과: 1 2 3 4
#      ```
#
# ✅ 최종 코드에서 수정한 점:
# - DFS 탐색 결과는 `print(*dfs_result)`로 한 번만 출력.
# - BFS 실행 전에 `visited` 배열을 재설정하여 탐색이 독립적으로 실행됨.
# - 입력을 빠르게 처리하기 위해 `sys.stdin.readline()`을 사용함.
# -----------------------------------------------------
