# 1970_Last_Day_Where_You_Can_Still_Cross.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1970. Last Day Where You Can Still Cross
# ✅ 문제 설명(요약):
#   - row x col 격자에서 day가 1씩 증가할 때마다 cells[day-1] 위치가 물(water)로 바뀐다.
#   - 어떤 day에 대해, 맨 윗줄(0행)에서 시작하여 맨 아랫줄(row-1행)까지
#     물을 밟지 않고(land만 밟고) 4방향 이동으로 도달할 수 있으면 "건널 수 있다".
#   - 건널 수 있는 마지막 day(최대 day)를 반환한다.
#
# ✅ 입력 형식(요지):
#   - row: 행 개수
#   - col: 열 개수
#   - cells: 각 day에 물이 되는 좌표 리스트(1-indexed)
#
# ✅ 규칙 요약:
#   - day = d라면, cells[0..d-1]가 물이 되고 나머지는 land로 남는다.
#   - 이동은 상/하/좌/우 4방향만 허용된다.
#   - "건널 수 있음"은 day가 증가할수록 단조 감소(True → False로만 변함)한다.
#   - 따라서 이분탐색으로 마지막 True day를 찾고, 각 mid day에 대해 BFS로 도달 가능 여부를 판정한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - 아래는 사용자가 제출/채택한 최종 정답 코드이며,
#     이 단계에서는 코드 내용을 변경하지 않고,
#     각 줄마다 설명 주석만 추가한다.

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:     
        def bfs(day):
            land = [[True] * col for _ in range(row)]          # True=land, False=water로 사용할 격자 초기화(전부 land)

            for i in range(day):                               # day일 동안 물이 되는 칸을 반영
                r, c = cells[i][0] - 1, cells[i][1] - 1        # 입력이 1-indexed이므로 0-index로 변환
                land[r][c] = False                             # 해당 칸을 water로 변경

            q = deque()                                        # BFS 큐
            visited = [[False] * col for _ in range(row)]      # 방문 체크

            for c in range(col):                               # 0행의 모든 열에서 시작 가능 지점 탐색
                if land[0][c]:                                 # land인 칸만 시작점
                    q.append((0, c))                            # 시작점 큐에 삽입
                    visited[0][c] = True                        # 방문 처리

            dirs = [(1,0), (0,1), (-1,0), (0,-1)]              # 4방향 이동

            while q:
                r, c = q.popleft()                             # 현재 위치 pop

                if r == row - 1:                               # 마지막 행에 도달하면
                    return True                                 # crossing 가능

                for dr, dc in dirs:                             # 4방향 확장
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row and 0 <= nc < col and land[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True                 # 미방문 land면 방문 처리
                        q.append((nr, nc))                     # 큐에 삽입

            return False                                        # BFS 종료까지 마지막 행을 못 갔으면 crossing 불가

        left, right = 1, len(cells)                             # 이분 탐색 범위: day(1..row*col)
        ans = 0                                                 # 마지막으로 가능한 day 기록(초기 0)

        while left <= right:
            mid = (left + right) // 2                           # 현재 검사할 day

            if bfs(mid):                                        # mid day에 crossing 가능하면
                ans = mid                                       # 후보 갱신
                left = mid + 1                                  # 더 큰 day를 탐색(마지막 True 찾기)
            else:                                               # crossing 불가하면
                right = mid - 1                                 # 더 작은 day로 이동

        return ans                                               # 마지막으로 가능했던 day 반환


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col                                     # 전체 셀 개수
        top, bottom = n, n + 1                            # 가상 노드: top(윗줄), bottom(아랫줄)

        parent = list(range(n + 2))                       # Union-Find parent 배열
        rank = [0] * (n + 2)                              # Union-Find rank 배열
        grid = [[False] * col for _ in range(row)]        # 현재 land 여부(False=water, True=land)

        def find(x):
            if parent[x] != x:                            # 경로 압축
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a, b = find(a), find(b)                       # 두 노드의 루트 찾기
            if a == b:
                return                                   # 이미 같은 컴포넌트면 종료
            if rank[a] < rank[b]:                         # rank 기준 union
                parent[a] = b
            else:
                parent[b] = a
                if rank[a] == rank[b]:
                    rank[a] += 1

        dr = [1, -1, 0, 0]                                # 상하좌우 이동 벡터
        dc = [0, 0, 1, -1]

        # day를 역순으로 순회하며 land를 하나씩 "복구"
        for d in range(n - 1, -1, -1):
            r, c = cells[d][0] - 1, cells[d][1] - 1       # 1-indexed → 0-indexed
            grid[r][c] = True                             # 해당 칸을 land로 변경
            idx = r * col + c                             # 2D 좌표를 1D 인덱스로 변환

            if r == 0:                                    # 맨 윗줄이면 top 가상 노드와 연결
                union(idx, top)
            if r == row - 1:                              # 맨 아랫줄이면 bottom 가상 노드와 연결
                union(idx, bottom)

            # 인접한 land들과 union
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]:
                    union(idx, nr * col + nc)

            # top과 bottom이 연결되면 crossing 가능
            if find(top) == find(bottom):
                return d                                  # 역순이므로 d가 정답 day

        return 0                                          # 이론상 도달하지 않음

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - (기록 없음) 이분 탐색 + BFS 판정으로 마지막 가능한 day를 찾는다.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용한 핵심 알고리즘/자료구조:
#     - 단조성 기반 이분 탐색: day가 커질수록 가능 여부가 True→False로만 변하므로 마지막 True를 탐색
#     - BFS: 특정 day의 격자 상태에서 0행 시작점들로부터 row-1행 도달 여부 판정
#   - 흔한 실수 포인트(일반적):
#     - day 인덱스(1-based day)와 cells 리스트 인덱스(0-based)의 대응 실수
#     - BFS 시작점을 0행 전체로 넣지 않고 하나만 넣는 실수
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(log(RC) * (RC))
#     - 각 bfs(mid)에서 격자 생성/수몰 처리/탐색이 O(RC)
#     - 이분 탐색이 O(log(RC))번 호출
#   - 공간 복잡도: O(RC)
#     - land, visited, BFS 큐 사용
#   - 성능 주의:
#     - bfs(day)마다 land를 새로 만들고 day만큼 수몰 반영하므로 상수항이 커질 수 있다.
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - Union-Find를 day 역순으로 적용하면 O(RC α(RC)) 수준으로 풀 수 있다(개념만, 코드 X).
#   - BFS 버전에서도 누적 상태/프리컴퓨트로 land 재구성 비용을 줄이는 최적화 여지가 있다(개념만, 코드 X).
