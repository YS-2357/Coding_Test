# 백준 10971번: 외판원 순회 2 (Traveling Salesman Problem)
# 문제 설명:
# N개의 도시를 한 번씩 방문하고 다시 출발점으로 돌아오는 최소 비용을 구하는 문제.
# - W[i][j]는 i번 도시에서 j번 도시로 이동하는 비용을 의미.
# - W[i][i] = 0 (자기 자신으로 이동 불가능)
# - 이동이 불가능한 경우 W[i][j] = 0이 주어짐.
# - 가능한 모든 경로를 탐색하여 최소 비용을 구해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (2 ≤ N ≤ 10)
# - 다음 N개의 줄에 N개의 정수로 구성된 도시 간 이동 비용 행렬이 주어진다.

# 출력 형식:
# - 모든 도시를 한 번씩 방문하고 다시 출발점으로 돌아오는 최소 비용을 출력한다.

# 예제 입력 1:
# 4
# 0 10 15 20
# 5 0 9 10
# 6 13 0 12
# 8 8 9 0
# 예제 출력 1:
# 35

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 정수 N 입력 받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # N x N 이동 비용 행렬 저장

# ✅ 방문 여부를 저장할 리스트
visited = [False] * N  

# ✅ 최소 비용 저장 변수 (최대값으로 초기화)
min_value = float('inf')  

# ✅ 백트래킹을 이용한 완전 탐색 (DFS 기반)
def TSP(start, current, cost, count):
    global min_value  

    # ✅ 모든 도시를 방문한 경우 (출발점으로 돌아오는 비용 추가)
    if count == N and board[current][start] > 0:
        min_value = min(min_value, cost + board[current][start])  # ✅ 최소 비용 갱신
        return  

    # ✅ 모든 도시 탐색
    for next_city in range(N):
        if not visited[next_city] and board[current][next_city] > 0:  # ✅ 방문하지 않은 도시이고 이동 가능하면
            visited[next_city] = True  # ✅ 방문 처리
            TSP(start, next_city, cost + board[current][next_city], count + 1)  # ✅ 다음 도시로 이동
            visited[next_city] = False  # ✅ 백트래킹 (원상 복구)

# ✅ 모든 도시를 출발점으로 하여 탐색 시작
for start_city in range(N):
    visited[start_city] = True  # ✅ 출발 도시 방문 처리
    TSP(start_city, start_city, 0, 1)  # ✅ 출발점, 현재 위치, 비용, 방문 개수
    visited[start_city] = False  # ✅ 백트래킹 (출발 도시 원상 복구)

# ✅ 최소 비용 출력
print(min_value)  


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `seq` 리스트에 이동 경로가 아닌 비용을 저장하는 문제
#    - 기존 코드: `seq.append(board[i][j])`
#    - ❌ 문제점: seq에 이동 비용을 저장하면, 올바른 경로를 추적할 수 없음.
#    - ✅ 수정: seq가 아닌 방문한 도시 번호를 저장하도록 변경.

# 2. ✅ 경로의 마지막에서 출발점으로 돌아오는 비용을 고려하지 않음
#    - 기존 코드:
#      ```python
#      if len(seq) == N:
#          value = sum(seq)
#          min_value = min(min_value, value)
#      ```
#    - ❌ 문제점: 마지막 도시에서 출발점으로 돌아가는 비용이 빠져 있음.
#    - ✅ 수정: `board[seq[-1]][seq[0]]`를 추가하여 경로를 완성.

# 3. ✅ `visited` 리스트 크기 설정 오류
#    - 기존 코드: `visited = [False] * (N + 1)`
#    - ❌ 문제점: 도시 개수는 `N`이므로, `N+1` 크기는 불필요.
#    - ✅ 수정: `visited = [False] * N`으로 크기를 조정.

# 4. ✅ 불필요한 중첩 루프 제거 및 DFS 최적화
#    - 기존 코드: `for i in range(N): for j in range(N):`
#    - ❌ 문제점: 불필요한 이중 반복문으로 인해 시간 복잡도가 증가함.
#    - ✅ 수정: `for next_city in range(N):`로 단일 반복문으로 변경.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
