# 백준 2667번: 단지번호붙이기 (BFS - 그래프 탐색)
# -----------------------------------------------------
# ✅ 문제 설명:
# - N×N 크기의 지도에서 0(빈 공간)과 1(집)이 주어진다.
# - 상하좌우로 연결된 1의 집들이 하나의 단지를 형성한다.
# - 각 단지의 크기를 오름차순으로 정렬하여 출력하는 문제.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 지도 크기 N (5 ≤ N ≤ 25)
# - 이후 N개의 줄에 N개의 0 또는 1이 주어진다.
#
# ✅ 출력 형식:
# - 첫 줄에 단지의 개수 출력.
# - 이후 각 단지에 속한 집의 수를 오름차순 정렬하여 출력.
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   7
#   0110100
#   0110101
#   1110101
#   0000111
#   0100000
#   0111110
#   0111000
# 🔹 예제 출력:
#   3
#   7
#   8
#   9
# -----------------------------------------------------

import sys
from collections import deque

# ✅ 입력 처리
N = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]  # ✅ 문자열 입력을 리스트로 변환

# ✅ BFS를 위한 방향 벡터 (좌, 우, 상, 하)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# ✅ BFS 탐색 함수 (단지 크기 계산)
def bfs(x, y):
    queue = deque([(x, y)])  # ✅ 시작 좌표 추가
    grid[x][y] = 0  # ✅ 방문 처리
    count = 1  # ✅ 단지 내 집 개수

    while queue:
        x, y = queue.popleft()

        for direction in range(4):  # ✅ 4방향 탐색
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                queue.append((nx, ny))  # ✅ 다음 방문 위치 추가
                grid[nx][ny] = 0  # ✅ 방문 처리
                count += 1  # ✅ 단지 크기 증가

    return count  # ✅ 단지 크기 반환

# ✅ 단지 개수 및 크기 저장 리스트
complex_sizes = []

# ✅ 모든 좌표 탐색하여 BFS 실행
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1:  # ✅ 집(1)을 발견하면 BFS 실행
            complex_sizes.append(bfs(i, j))  # ✅ 단지 크기 추가

# ✅ 단지 크기 정렬 후 출력
complex_sizes.sort()  # ✅ 오름차순 정렬
print(len(complex_sizes))  # ✅ 총 단지 개수 출력
for size in complex_sizes:
    print(size)  # ✅ 각 단지 크기 출력

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리.
# - `grid`를 2D 리스트로 변환하여 관리.
# - BFS를 사용하여 모든 단지를 탐색하며 크기를 계산.
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **입력 변환 오류 (`sys.stdin.readline().split()` → `strip()` 없이 사용)**
#    - 기존 코드에서 `sys.stdin.readline()`만 사용하여 한 줄 전체를 리스트로 변환하지 못함.
#    - 해결 방법: `.strip()`을 추가하여 공백 제거 후 `list(map(int, ...))`로 변환.
#
# 2️⃣ **방문 처리 오류**
#    - 기존 코드에서 방문한 `1`을 다시 탐색하는 경우가 발생할 가능성이 있었음.
#    - 해결 방법: BFS 실행 시 `grid[x][y] = 0`을 즉시 처리하여 방문한 집을 다시 탐색하지 않도록 수정.
#
# ✅ 요청한 BFS 힌트:
# 🔹 **BFS를 활용한 `grid` 탐색 개념**
#    - 모든 `1`을 찾아 BFS 실행하여 단지 크기를 계산.
#    - BFS 탐색 중 `1`을 `0`으로 바꾸어 중복 방문을 방지.
#    - 모든 탐색이 끝난 후, 단지 크기를 정렬하여 출력.
#
# 🔹 **BFS 탐색 과정 예제**
#    ```
#    0110100
#    0110101
#    1110101
#    0000111
#    0100000
#    0111110
#    0111000
#    ```
#    1️⃣ (0,1)에서 BFS 시작 → 단지 크기 7
#    2️⃣ (2,0)에서 BFS 시작 → 단지 크기 8
#    3️⃣ (3,4)에서 BFS 시작 → 단지 크기 9
#    🔹 결과: `3` (단지 개수), `[7, 8, 9]` (오름차순 정렬 후 출력)
#
# ✅ 최종 코드에서 수정한 점:
# - `grid` 변환 방식을 `strip()`을 활용하여 올바르게 변환.
# - BFS 탐색 중 방문한 위치를 즉시 `0`으로 변경하여 중복 방문 방지.
# - 모든 단지를 탐색한 후, 크기를 오름차순 정렬하여 출력.
# -----------------------------------------------------
