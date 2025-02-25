# 백준 7576번: 토마토 (그래프 탐색 - BFS)
# -----------------------------------------------------
# ✅ 문제 설명:
# - M×N 크기의 상자에서 모든 토마토가 익는 최소 일수를 구하는 문제.
# - 1: 익은 토마토, 0: 안 익은 토마토, -1: 토마토가 없는 칸.
# - 모든 토마토가 익을 수 없는 경우 -1을 출력.

# ✅ 입력 형식:
# - 첫째 줄: M(가로), N(세로) (2 ≤ M, N ≤ 1,000)
# - 둘째 줄~: N개의 줄에 M개의 정수 (1, 0, -1)

# ✅ 출력 형식:
# - 모든 토마토가 익는 최소 일수를 출력.
# - 만약 모두 익을 수 없다면 -1을 출력.
# -----------------------------------------------------
import sys
from collections import deque

# ✅ 입력 처리
M, N = map(int, sys.stdin.readline().split())  
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # ✅ 토마토 정보 저장

# ✅ 방향 벡터 (상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# ✅ BFS를 위한 큐 초기화 (익은 토마토 위치 삽입)
queue = deque([(i, j) for i in range(N) for j in range(M) if grid[i][j] == 1])

# ✅ BFS 탐색 함수 (최소 일수 계산)
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for direction in range(4):  # ✅ 4방향 탐색
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:  # ✅ 안 익은 토마토만 처리
                grid[nx][ny] = grid[x][y] + 1  # ✅ 이전 일수 + 1로 설정
                queue.append((nx, ny))

# ✅ BFS 실행
bfs()

# ✅ 최종 결과 계산
max_days = 0
for row in grid:
    for value in row:
        if value == 0:  # ✅ BFS 종료 후에도 익지 않은 토마토가 남아 있으면 -1 출력
            print(-1)
            exit()
    max_days = max(max_days, max(row))

# ✅ 최소 일수 계산 후 출력 (초기 값 1 포함이므로 -1 처리)
print(max_days - 1)

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1️⃣ **`days` 증가 위치 오류:**
#    - 기존 코드: `days += 1`이 불필요하게 증가함.
#    - ✅ 해결: `grid[nx][ny] = grid[x][y] + 1` 방식으로 정확한 일수 계산.

# 2️⃣ **`queue` 초기화 방식 오류:**
#    - 기존 코드: `for` 반복문을 사용해 직접 `queue.append()`
#    - ✅ 해결: `queue = deque([...])` 방식으로 초기화하여 불필요한 반복 제거.

# 3️⃣ **BFS 종료 후 0이 남아있는지 검사 필요:**
#    - 기존 코드: `if any(0 in row for row in grid):` 검사가 없음.
#    - ✅ 해결: `for` 루프 내에서 0을 발견하면 `-1` 출력 후 `exit()`.

# ✅ 요청한 BFS 힌트:
# 🔹 **BFS를 활용한 `grid` 탐색 개념**
#    - 모든 `1`을 찾아 BFS 실행하여 최소 일수를 계산.
#    - BFS 탐색 중 `1`을 `이전 일수 +1`로 변경하여 방문을 처리함.
#    - 목표 지점 `(N-1, M-1)`에 도착하면 현재 `grid` 값이 최소 일수.

# 🔹 **BFS 탐색 과정 예제**
#    ```
#    6 4
#    0 0 0 0 0 0
#    0 0 0 0 0 0
#    0 0 0 0 0 0
#    0 0 0 1 0 0
#    ```
#    1️⃣ 모든 `1`(익은 토마토)에서 BFS 시작 → (N,M)까지 탐색 진행
#    2️⃣ BFS 수행 후 `grid`에서 `max(grid) - 1` 값을 출력
#    🔹 결과: `6`
#
# ✅ 최종 코드에서 수정한 점:
# - `grid` 변환 방식을 `sys.stdin.readline()`을 활용하여 빠르게 변환.
# - BFS 탐색 중 방문한 위치를 `grid[nx][ny] = grid[x][y] + 1`로 변경하여 일수 정보 유지.
# - 최단 일수를 구하는 방식이 올바르게 동작하도록 코드 수정.
# -----------------------------------------------------
