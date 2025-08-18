# 미로_탈출_레버_먼저.py
# -----------------------------------------------------
# ✅ 제목: 미로 탈출 — 레버를 당긴 뒤 출구까지 최단 시간
# ✅ 문제 설명(요약):
# - 'S'(시작)에서 'L'(레버)까지, 그 다음 'L'에서 'E'(출구)까지 각각 최단 시간을 더한 값을 구한다.
# - 통로: 'O' / 벽: 'X' / 'S','L','E'는 모두 통로처럼 지나갈 수 있다(단, 레버는 반드시 먼저 당김).
#
# ✅ 입력 형식(요지):
# - maps: 길이 N(5~100)의 문자열 배열, 각 문자열 길이 M(5~100), 문자 집합 {S,E,L,O,X}
#
# ✅ 규칙 요약:
# - 격자에서 상하좌우로 한 칸 이동에 1초.
# - S→L, L→E를 각각 BFS로 최단 거리 계산. 둘 중 하나라도 도달 불가면 -1.
#
# ✅ 입출력 예시(1개):
# - maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"] → 16

def solution(maps):                                           # 함수 시작
    answer = 0                                               # 최종 답(두 구간 합) 저장용
    n, m = len(maps), len(maps[0])                           # 행(N), 열(M) 크기
    dx = [0, 0, 1, -1]                                       # 상하좌우 이동 x증분
    dy = [1, -1, 0, 0]                                       # 상하좌우 이동 y증분

    # 시작(S), 레버(L), 출구(E) 좌표 찾기
    for i in range(n):                                       # 모든 행 순회
        for j in range(m):                                   # 모든 열 순회 (※ m이어야 함)
            if maps[i][j] == 'S':                            # 시작 지점이면
                s = (i, j)                                   # S 좌표 저장
            elif maps[i][j] == 'L':                          # 레버 지점이면
                l = (i, j)                                   # L 좌표 저장
            elif maps[i][j] == 'E':                          # 출구 지점이면
                e = (i, j)                                   # E 좌표 저장

    from collections import deque                            # BFS용 큐

    def bfs(start, goal):                                    # start에서 goal까지 최단거리 BFS
        sx, sy = start                                       # 시작 좌표 언패킹
        gx, gy = goal                                        # 목표 좌표 언패킹
        visited = [[False]*m for _ in range(n)]              # 방문 여부 행렬
        dist = [[-1]*m for _ in range(n)]                    # 거리(초) 행렬
        q = deque()                                          # 큐 생성
        visited[sx][sy] = True                               # 시작 방문 표시
        dist[sx][sy] = 0                                     # 시작까지의 거리는 0
        q.append((sx, sy))                                   # 큐에 시작 좌표 삽입

        while q:                                             # 큐가 빌 때까지
            x, y = q.popleft()                               # 현재 좌표 꺼내기
            if (x, y) == (gx, gy):                           # 목표 도달 시
                return dist[x][y]                            # 최단 거리 반환
            for k in range(4):                               # 4방향 이웃 확인 (※ 4여야 함)
                nx, ny = x + dx[k], y + dy[k]                # 이웃 좌표
                if 0 <= nx < n and 0 <= ny < m:              # 격자 범위 안이고
                    if not visited[nx][ny] and maps[nx][ny] != 'X':  # 미방문 & 벽이 아니면
                        visited[nx][ny] = True               # 방문 표시
                        dist[nx][ny] = dist[x][y] + 1        # 거리 갱신(1초 증가)
                        q.append((nx, ny))                   # 큐에 삽입
        return -1                                            # 도달 불가 시 -1

    # 1) S → L 최단거리
    to_lever = bfs(s, l)                                     # S에서 L까지
    if to_lever == -1:                                       # 도달 불가면
        return -1                                            # 바로 -1 반환

    # 2) L → E 최단거리
    to_exit = bfs(l, e)                                      # L에서 E까지
    if to_exit == -1:                                        # 도달 불가면
        return -1                                            # -1 반환

    answer = to_lever + to_exit                              # 두 구간 최단거리 합
    return answer                                            # 정답 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **미도달** (부분 구현/오류로 실패)
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# 1) 열 루프 범위 오류: `for j in range(n)` → **`range(m)`**로 수정 (가로 길이 사용).
# 2) BFS 내부 방향 루프 오류: `for i in range(n)`처럼 돌리려던 흔적 → **4방향만 순회**.
# 3) BFS 미완성: 방문/거리/큐 로직 부재 → **표준 BFS**(visited, dist, deque)로 완성.
# 4) 두 단계 경로 요구: S→L만(혹은 L→E만) 보던 흐름 → **S→L, L→E 각각 BFS 후 합산**.
# 5) 도달 불가 처리: 경로가 없을 때 리턴값 미정 → **각 BFS -1이면 전체 -1 반환**으로 보완.
#
# 📚 사용된 개념(필수만):
# - 격자 최단 경로: **BFS(큐, 방문표시, 거리배열)** 
# - 문제 분해: **S→L**, **L→E** 두 구간의 최단거리 합

# 더 효율적인 풀이
# from collections import deque

# def solution(maps):
#     """
#     더 효율적인 풀이 (시간/공간 O(N*M)):
#     - 격자 크기 최대 100x100이므로 BFS 2회(S->L, L->E)가 최적입니다.
#     - 불필요한 자료구조를 최소화하고, 조기 종료(목표 도달 시 즉시 반환)로 시간을 줄입니다.
#     """
#     n, m = len(maps), len(maps[0])

#     # S, L, E 위치 1회 스캔으로 찾기
#     sx = sy = lx = ly = ex = ey = -1
#     for i, row in enumerate(maps):
#         # 문자열이므로 row[j] 인덱싱만 사용 (리스트 변환 불필요)
#         for j, ch in enumerate(row):
#             if ch == 'S':
#                 sx, sy = i, j
#             elif ch == 'L':
#                 lx, ly = i, j
#             elif ch == 'E':
#                 ex, ey = i, j

#     # 4방향 이동 상수 (반복문 내부 바인딩 비용 최소화를 위해 상수로 정의)
#     DIRS = ((1,0), (-1,0), (0,1), (0,-1))

#     def bfs(ax, ay, bx, by):
#         """(ax,ay) -> (bx,by) 최단거리. 도달 불가 시 -1."""
#         # 방문 배열을 매 호출마다 새로 생성 (중복 방문 방지)
#         visited = [[False]*m for _ in range(n)]
#         dq = deque()
#         dq.append((ax, ay, 0))            # (x, y, dist)
#         visited[ax][ay] = True
#         grid = maps                       # 로컬 바인딩으로 속도 미세 향상

#         while dq:
#             x, y, d = dq.popleft()
#             if x == bx and y == by:       # 목표 도달 시 즉시 반환 (조기 종료)
#                 return d
#             # 4방향 탐색
#             nx0 = x + 1; ny0 = y
#             nx1 = x - 1; ny1 = y
#             nx2 = x;     ny2 = y + 1
#             nx3 = x;     ny3 = y - 1
#             # if 블록 4개로 분기(파이썬 루프/언패킹 오버헤드 약간 감소)
#             if 0 <= nx0 < n and 0 <= ny0 < m and not visited[nx0][ny0] and grid[nx0][ny0] != 'X':
#                 visited[nx0][ny0] = True
#                 dq.append((nx0, ny0, d+1))
#             if 0 <= nx1 < n and 0 <= ny1 < m and not visited[nx1][ny1] and grid[nx1][ny1] != 'X':
#                 visited[nx1][ny1] = True
#                 dq.append((nx1, ny1, d+1))
#             if 0 <= nx2 < n and 0 <= ny2 < m and not visited[nx2][ny2] and grid[nx2][ny2] != 'X':
#                 visited[nx2][ny2] = True
#                 dq.append((nx2, ny2, d+1))
#             if 0 <= nx3 < n and 0 <= ny3 < m and not visited[nx3][ny3] and grid[nx3][ny3] != 'X':
#                 visited[nx3][ny3] = True
#                 dq.append((nx3, ny3, d+1))
#         return -1

#     # S -> L
#     d1 = bfs(sx, sy, lx, ly)
#     if d1 == -1:
#         return -1

#     # L -> E
#     d2 = bfs(lx, ly, ex, ey)
#     if d2 == -1:
#         return -1

#     return d1 + d2
