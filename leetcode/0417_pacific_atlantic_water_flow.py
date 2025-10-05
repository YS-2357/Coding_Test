# 0417_pacific_atlantic_water_flow.py
# -----------------------------------------------------
# ✅ 제목: Pacific Atlantic Water Flow (LeetCode 417)
# ✅ 문제 설명(요약):
# - 높이 격자에서 각 칸의 물이 태평양(상/좌 경계)과 대서양(하/우 경계) 모두로 흘러갈 수 있는 좌표를 구한다.
#
# ✅ 입력 형식(요지):
# - heights: List[List[int]] 크기 m×n, 각 원소는 고도
#
# ✅ 규칙 요약:
# 1) 물은 네 방향으로만 흐르며, 높은 곳→낮은 곳 또는 같은 높이로만 이동 가능(등고선 포함).
# 2) 태평양은 상단 행과 좌측 열과 접함, 대서양은 하단 행과 우측 열과 접함.
# 3) 두 바다 모두에 도달 가능한 칸을 반환.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지) — 한 줄 주석 포함
from collections import deque                                         # BFS용 큐

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])                          # 격자 크기
        pacific = deque()                                             # 태평양 시작점 큐
        atlantic = deque()                                            # 대서양 시작점 큐

        pacific_visited = [[False]*n for _ in range(m)]               # 태평양 도달 가능 표시
        atlantic_visited = [[False]*n for _ in range(m)]              # 대서양 도달 가능 표시

        for i in range(m):                                            # 좌측 열(태평양) 초기화
            pacific.append((i, 0))                                    # (i,0) enqueue
            pacific_visited[i][0] = True                              # 방문 표기
        for j in range(n):                                            # 상단 행(태평양) 초기화
            pacific.append((0, j))                                    # (0,j) enqueue
            pacific_visited[0][j] = True                              # 방문 표기

        for i in range(m):                                            # 우측 열(대서양) 초기화
            atlantic.append((i, n-1))                                 # (i,n-1) enqueue
            atlantic_visited[i][n-1] = True                           # 방문 표기
        for j in range(n):                                            # 하단 행(대서양) 초기화
            atlantic.append((m-1, j))                                 # (m-1,j) enqueue
            atlantic_visited[m-1][j] = True                           # 방문 표기

        def bfs(q, visited):                                          # 경계에서 역방향으로 퍼지는 BFS
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]                        # 4방향 이동
            while q:                                                  # 큐 빌 때까지
                x, y = q.popleft()                                    # 현재 칸
                for dx, dy in dirs:                                   # 이웃 검사
                    nx, ny = x+dx, y+dy                               # 이웃 좌표
                    if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:   # 범위 내, 미방문
                        if heights[nx][ny] >= heights[x][y]:          # 역방향 확장: 높거나 같은 곳만
                            visited[nx][ny] = True                     # 방문 확정
                            q.append((nx, ny))                         # 큐에 추가

        bfs(pacific, pacific_visited)                                  # 태평양에서 도달 가능한 칸들
        bfs(atlantic, atlantic_visited)                                # 대서양에서 도달 가능한 칸들

        result = []                                                    # 교집합 결과
        for i in range(m):                                             # 모든 칸 순회
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:   # 두 바다 모두에 도달하면
                    result.append([i, j])                               # 결과에 추가

        return result                                                  # 정답 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 두 경계에서 BFS 역확장으로 교집합 좌표 계산 성공.
#
# 🔧 오답 이유 및 실수, 사용한 알고리즘 개념:
# - 개념: 경계에서 시작해 "높거나 같은 고도"로만 이동하는 BFS를 각각 수행.
# - 실수 가능 지점:
#   1) 방문 배열을 하나로 합치면 안 됨(바다별로 분리 필요).
#   2) 조건을 반대로 두면 안 됨(정방향 흐름이 아니라 역방향 확장).
# - 시간복잡도: O(mn) (각 칸을 최대 2회 방문)
# - 공간복잡도: O(mn) (visited 2개, 큐)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - DFS로도 동일하게 가능. 단, 파이썬은 재귀 깊이 주의.
# - 미세 최적화: dirs 상수화, 비트 방문표시로 메모리 절약 가능.
