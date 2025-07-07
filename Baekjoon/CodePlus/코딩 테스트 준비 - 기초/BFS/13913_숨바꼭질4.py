import sys
from collections import deque

# ✅ 입력 받기
N, K = map(int, sys.stdin.readline().split())

# ✅ 방문 체크 배열 & 이전 위치 배열
visited = [False] * 100001  
previous = [-1] * 100001  

# ✅ BFS 탐색 함수
def bfs(start, end):
    queue = deque([(start, 0)])  # (현재 위치, 이동 횟수)
    visited[start] = True
    
    while queue:
        x, count = queue.popleft()
        
        # ✅ 도착하면 종료
        if x == end:
            return count
        
        # ✅ 3가지 이동 방법 적용
        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx < 100001 and not visited[nx]: 
                queue.append((nx, count + 1))  # 다음 탐색 위치 큐에 추가
                visited[nx] = True
                previous[nx] = x  # ✅ 이전 위치 기록
                
    return -1  # 실패할 일은 없음

# ✅ BFS 실행하여 최단 이동 횟수 계산
min_moves = bfs(N, K)

# ✅ 최단 경로 역추적 (이전 위치를 따라가면서 경로 복원)
path = []
current = K
while current != -1:
    path.append(current)
    current = previous[current]  # 이전 위치로 이동
path.reverse()  # 시작점 → 도착점 순서로 변경

# ✅ 결과 출력
print(min_moves)
print(*path)

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드 🚀
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리.
# - `visited` 배열을 사용하여 BFS 탐색을 최적화.
# - `previous` 배열을 사용하여 최단 경로를 역추적.
# - `queue.popleft()`를 사용하여 BFS 탐색을 수행 (FIFO 방식).
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ **`previous` 배열을 활용하지 않고, 경로를 올바르게 추적하지 못함**
#    - 기존 코드에서는 `history.append(nx)` 방식으로 경로를 저장했음.
#    - 해결 방법: `previous[nx] = x`를 사용하여 각 위치의 이전 위치를 저장.
#
# 2️⃣ **BFS에서 `current` 값을 역추적하는 과정에서 오류 발생**
#    - 기존 코드에서는 `history` 리스트를 사용하여 직접 BFS 경로를 저장.
#    - 해결 방법: `current = previous[current]`를 따라가면서 `path`를 역추적.
#
# 3️⃣ **최단 이동 횟수를 올바르게 출력하지 않음**
#    - 기존 코드에서는 BFS 탐색이 끝난 후, 이동 횟수를 따로 저장하지 않음.
#    - 해결 방법: `bfs()` 함수에서 `return count` 값을 저장하여 활용.
#
# ✅ 요청한 BFS 힌트:
# 🔹 **BFS를 활용한 최단 거리 탐색 개념**
#    - BFS는 "가장 먼저 도달하는 경로가 최단 거리"를 보장.
#    - 모든 이동을 `queue`에 저장하고, 가장 먼저 도착한 경우를 최단 거리로 반환.
#
# 🔹 **BFS 탐색 과정 예제 (`N=5`, `K=17` 인 경우)**
#    ```plaintext
#    5 → 10 → 9 → 18 → 17 (최단 경로 4)
#    ```
#    ✅ `previous` 배열을 활용하여 역추적한 결과:
#    ```plaintext
#    5 10 9 18 17
#    ```
#
# ✅ 최종 코드에서 수정한 점:
# - `previous` 배열을 활용하여 경로를 올바르게 추적.
# - BFS 탐색 중에 `visited` 배열을 사용하여 중복 탐색을 방지.
# - `queue.popleft()`를 사용하여 최단 거리 탐색을 보장.
# - `path.reverse()`를 사용하여 올바른 순서로 최단 경로 출력.
# -----------------------------------------------------
