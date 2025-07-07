# 백준 1707번: 이분 그래프 (Bipartite Graph) 판별
# -----------------------------------------------------
# ✅ 문제 설명:
# - 주어진 무방향 그래프가 "이분 그래프(Bipartite Graph)"인지 판별하는 문제.
# - "이분 그래프"란 그래프의 정점을 두 그룹으로 나눌 수 있으며, 같은 그룹 내에서는 간선이 존재하지 않아야 한다.
# - 즉, "서로 연결된 정점이 항상 다른 그룹에 속해야 함."
#
# ✅ 입력 형식:
# - 첫 번째 줄에 테스트 케이스 개수 K (1 ≤ K ≤ 5)
# - 각 테스트 케이스마다:
#   - 정점 개수 V, 간선 개수 E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 200,000)
#   - 이후 E개의 줄에 간선 정보 (A, B) 주어짐 (1 ≤ A, B ≤ V)
#
# ✅ 출력 형식:
# - 각 테스트 케이스마다 "YES" 또는 "NO" 출력.
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   2
#   3 2
#   1 3
#   2 3
#   4 4
#   1 2
#   2 3
#   3 4
#   4 2
# 🔹 예제 출력:
#   YES
#   NO
# -----------------------------------------------------

import sys
from collections import deque

# ✅ 테스트 케이스 개수 입력
K = int(sys.stdin.readline())

# ✅ BFS 탐색 함수 (이분 그래프 판별)
def bfs(start):
    global color
    queue = deque([start])
    color[start] = 0  # ✅ 시작 노드는 0번 색상으로 지정

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:  # ✅ 인접한 노드 탐색
            if color[neighbor] == -1:  # ✅ 아직 색칠되지 않은 노드
                color[neighbor] = 1 - color[node]  # ✅ 현재 노드와 반대 색으로 색칠
                queue.append(neighbor)  # ✅ 큐에 추가하여 탐색 지속
            elif color[neighbor] == color[node]:  # ✅ 인접 노드와 같은 색이면 이분 그래프 아님
                return False

    return True  # ✅ 이분 그래프 판별 완료

# ✅ 각 테스트 케이스 실행
for _ in range(K):
    N, M = map(int, sys.stdin.readline().split())  # ✅ 정점 개수 N, 간선 개수 M 입력
    graph = [[] for _ in range(N+1)]  # ✅ 인접 리스트 초기화
    color = [-1] * (N+1)  # ✅ 색상 배열 (-1: 미방문)

    # ✅ 그래프 입력 (무방향 그래프)
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    is_bipartite = True  # ✅ 이분 그래프 여부 체크

    # ✅ 모든 연결 요소 탐색
    for i in range(1, N+1):
        if color[i] == -1:  # ✅ 방문하지 않은 노드에서 BFS 실행
            if not bfs(i):  # ✅ 이분 그래프가 아니라면 즉시 종료
                is_bipartite = False
                break

    # ✅ 결과 출력
    print("YES" if is_bipartite else "NO")  # ✅ 이분 그래프 여부 출력

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리
# - `graph`를 인접 리스트로 구현하여 탐색 최적화
# - BFS를 사용하여 이분 그래프 판별
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **입력에서 `sys.stdin.readline().split()` 누락**
#    - 기존 코드에서 `sys.stdin.readline()`만 사용하여 `split()`이 없었음.
#    - 해결 방법: `.split()`을 추가하여 올바르게 정수 변환 수행.
#
# 2️⃣ **BFS 실행 시 `color` 배열이 전역 변수로 선언되지 않아 오류 발생**
#    - 기존 코드에서는 `color`를 함수 내부에서 직접 접근할 수 없었음.
#    - 해결 방법: `global color`를 선언하여 전역 변수로 접근 가능하도록 수정.
#
# 3️⃣ **`graph[B].append(A)`가 호출되기 전에 B가 존재하지 않는 경우 발생 가능**
#    - `graph`의 크기를 `N+1`로 설정하여 범위를 초과하지 않도록 보장.
#
# ✅ 요청한 "이분 그래프 판별 논리" 힌트:
# 🔹 **BFS를 활용한 이분 그래프 판별 (색칠법)**
#    - **각 노드를 두 가지 색(0, 1) 중 하나로 색칠하면서 탐색.**
#    - **현재 노드가 속한 그룹과 다른 색을 다음 노드에 부여.**
#    - **BFS 탐색 중, 현재 노드와 인접한 노드가 같은 색이면 이분 그래프가 아님 (`NO`).**
#    - **모든 노드를 탐색하면서, 모든 연결 요소에 대해 독립적으로 BFS 실행.**
#    - **모든 탐색이 끝났을 때 모순이 발생하지 않았다면 `YES` 출력.**
#
# 🔹 **BFS 탐색 과정 예제**
#    ```
#    1 → 2 → 3 → 4
#    색상: 0 → 1 → 0 → 1
#    결과: YES
#
#    1 → 2 → 3 → 4 → 2
#    색상: 0 → 1 → 0 → 1 → (충돌 발생)
#    결과: NO
#    ```
#
# ✅ 최종 코드에서 수정한 점:
# - `bfs()`에서 `global color` 선언을 추가하여 전역 변수 접근 가능하도록 변경.
# - 입력을 빠르게 처리하기 위해 `sys.stdin.readline()`을 사용함.
# - 모든 연결 요소를 탐색하면서 BFS를 실행하여 이분 그래프 여부를 판별.
# -----------------------------------------------------
