# 백준 7562번: 나이트의 이동 (BFS - 최단 경로 탐색)
# -----------------------------------------------------
# ✅ 문제 설명:
# - 체스판 위에서 나이트가 (start_x, start_y) → (end_x, end_y)까지 이동하는 최소 이동 횟수를 구하는 문제.
# - 나이트는 특정한 8가지 방향으로만 이동 가능.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 테스트 케이스 개수 N이 주어진다. (1 ≤ N ≤ 100)
# - 각 테스트 케이스마다:
#   - 체스판 크기 M (4 ≤ M ≤ 300)
#   - 나이트의 현재 위치 (start_x, start_y)
#   - 목표 위치 (end_x, end_y)
#
# ✅ 출력 형식:
# - 각 테스트 케이스마다 나이트가 목표 위치로 이동하는 최소 횟수를 출력.
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   3
#   8
#   0 0
#   7 0
#   100
#   0 0
#   30 50
#   10
#   1 1
#   1 1
# 🔹 예제 출력:
#   5
#   28
#   0
# -----------------------------------------------------

import sys
from collections import deque

# ✅ 나이트가 이동할 수 있는 8가지 방향 정의
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, 2, 1, -1, -2]

def bfs(M, start_x, start_y, end_x, end_y):
    """BFS를 활용하여 최단 경로 탐색"""
    # ✅ 예외 처리: 시작 위치와 목표 위치가 같다면 0 반환
    if start_x == end_x and start_y == end_y:
        return 0

    queue = deque([(start_x, start_y, 0)])  # (현재 x좌표, 현재 y좌표, 이동 횟수)
    visited = [[False] * M for _ in range(M)]  # ✅ 방문 여부 체크 배열
    visited[start_x][start_y] = True  # ✅ 시작 위치 방문 처리

    while queue:
        x, y, moves = queue.popleft()  # ✅ 현재 좌표와 이동 횟수
        
        for direction in range(8):  # ✅ 8가지 이동 가능 방향 탐색
            nx = x + dx[direction]
            ny = y + dy[direction]

            # ✅ 체스판 범위 내에 있고, 방문하지 않은 위치라면 이동
            if 0 <= nx < M and 0 <= ny < M and not visited[nx][ny]:
                # ✅ 도착점에 도달하면 이동 횟수 반환
                if nx == end_x and ny == end_y:
                    return moves + 1  
                
                queue.append((nx, ny, moves + 1))  # ✅ 이동 횟수 증가하여 큐에 추가
                visited[nx][ny] = True  # ✅ 방문 처리
    
    return -1  # ✅ 이론적으로 도달할 수 없는 경우는 없음.

# ✅ 입력 처리 및 BFS 실행
N = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

for _ in range(N):
    M = int(sys.stdin.readline().strip())  # 체스판 크기
    start_x, start_y = map(int, sys.stdin.readline().split())  # 시작 위치
    end_x, end_y = map(int, sys.stdin.readline().split())  # 목표 위치
    
    # ✅ BFS 실행 및 결과 출력
    print(bfs(M, start_x, start_y, end_x, end_y))

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드 🚀
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리.
# - `visited` 배열을 사용하여 BFS 탐색을 최적화.
# - `moves` 변수를 사용하여 이동 횟수를 기록.
# - `queue.popleft()`를 사용하여 BFS 탐색을 수행 (FIFO).
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **`grid` 변수를 사용하여 전역 범위 오류 발생**
#    - 기존 코드에서 `grid`가 전역 변수로 선언되지 않아 `NameError` 발생.
#    - 해결 방법: `grid`를 함수 내부에서 `visited`로 변경하여 명확하게 처리.
#
# 2️⃣ **BFS에서 `count`를 증가시키는 방식이 잘못됨**
#    - 기존 코드에서는 `count` 변수를 사용하여 이동 횟수를 직접 증가시켰음.
#    - 해결 방법: `queue`에 `(x, y, moves + 1)`을 삽입하여 이동 횟수를 명확하게 추적.
#
# 3️⃣ **도착점 검사 오류 (`end_x - 1`, `end_y - 1` 계산 오류)**
#    - 기존 코드에서 `if nx == (end_x - 1) and ny == (end_y -1):` 조건으로 검사하여 좌표 오류 발생.
#    - 해결 방법: `if nx == end_x and ny == end_y:`로 수정하여 올바른 도착점 판별.
#
# ✅ 요청한 BFS 힌트:
# 🔹 **BFS를 활용한 최단 거리 탐색 개념**
#    - BFS는 "가장 먼저 도달하는 경로가 최단 거리"를 보장.
#    - 모든 이동을 `queue`에 저장하고, 가장 먼저 도착한 경우를 최단 거리로 반환.
#
# 🔹 **BFS 탐색 과정 예제 (`M=8` 체스판에서 `start_x=0, start_y=0` → `end_x=7, end_y=0`)**
#    ```
#    1️⃣ (0,0)에서 BFS 시작 → (2,1), (1,2) 탐색
#    2️⃣ (2,1)에서 (3,3), (4,2) 탐색
#    3️⃣ ...
#    4️⃣ (7,0)에 도착하면 이동 횟수 5 반환
#    ```
#
# ✅ 최종 코드에서 수정한 점:
# - `visited`를 사용하여 중복 탐색 방지.
# - BFS를 활용하여 최단 경로를 찾도록 `queue.popleft()` 방식 사용.
# - 도착 지점에 대한 검사를 `if nx == end_x and ny == end_y:`로 수정.
# - `moves` 변수를 활용하여 이동 횟수를 추적하여 정확한 BFS 구현.
# -----------------------------------------------------
