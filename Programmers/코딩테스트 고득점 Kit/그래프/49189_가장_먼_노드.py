# 📁 파일명: 49189_가장_먼_노드.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - n개의 노드가 있는 무방향 그래프에서 1번 노드로부터 가장 멀리 떨어진 노드의 개수를 구하는 문제
# - 간선(edge)은 양방향이며, 하나의 노드에서 다른 노드로 최단 거리로 이동할 수 있다.

# ✅ 입출력 예제:
# 입력:
#   n = 6
#   edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# 출력:
#   3
# 설명: 1번 노드에서 가장 멀리 떨어진 노드(6, 4, 5)가 총 3개

# -----------------------------------------------------
from collections import deque

def solution(n, edge):
    # ✅ 인접 리스트 초기화
    graph = [[] for _ in range(n + 1)]

    # ✅ 양방향 그래프 구성
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # ✅ 방문 여부를 체크하는 배열
    visited = [False] * (n + 1)

    # ✅ 거리 저장 배열 (1번 노드에서 각 노드까지의 거리)
    distance = [0] * (n + 1)

    # ✅ BFS 시작: (노드 번호, 거리)
    queue = deque()
    queue.append((1, 0))         # 1번 노드부터 시작, 거리 0
    visited[1] = True            # 시작 노드 방문 처리

    # ✅ BFS 탐색
    while queue:
        current, dist = queue.popleft()         # 현재 노드, 거리 추출
        for neighbor in graph[current]:         # 현재 노드의 이웃 노드 탐색
            if not visited[neighbor]:           # 방문하지 않은 경우만 진행
                visited[neighbor] = True        # 방문 처리
                distance[neighbor] = dist + 1   # 거리 저장
                queue.append((neighbor, dist + 1))  # 큐에 다음 노드 추가

    # ✅ 가장 멀리 떨어진 거리 계산
    max_dist = max(distance)

    # ✅ 가장 멀리 떨어진 노드의 수 세기
    return distance.count(max_dist)

# -----------------------------------------------------
# 🧩 내가 처음에 틀린 부분과 실수 목록:
# 1️⃣ `queue.append(neighbor, dist + 1)`에서 괄호 없이 튜플을 넣어 오류 발생
#    - ❌ append(neighbor, dist + 1)
#    - ✅ append((neighbor, dist + 1))

# 2️⃣ 문제에서 요구한 건 "가장 멀리 있는 노드의 수"인데, 나는 max 거리까지만 구하고 끝냄
#    - ❌ return max(distance)
#    - ✅ return distance.count(max(distance))

# 3️⃣ 1번 노드 기준으로 거리 저장이 누락되어 결과가 정확하지 않았음

# -----------------------------------------------------
# 🧠 힌트 목록 (ChatGPT가 제공한 것):
# 🔹 BFS는 최단 거리 탐색에 적합 → 큐에 (노드, 거리)를 함께 넣자
# 🔹 거리 정보는 distance 배열에 저장
# 🔹 가장 멀리 떨어진 거리 = max(distance)
# 🔹 그 거리의 개수를 count()로 세면 정답

# ----------------------------------------------------
