# 87694_아이템 줍기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 캐릭터는 여러 사각형의 테두리만 따라 이동할 수 있음
# - 사각형 내부는 이동 불가하며, 여러 사각형이 겹칠 수 있음
# - 캐릭터가 시작 좌표에서 아이템 좌표까지 도달하는 최소 거리를 구하라

# ✅ 입력 형식:
# - rectangle: [[x1, y1, x2, y2], ...] 형태의 사각형 리스트
# - characterX, characterY: 캐릭터 시작 위치
# - itemX, itemY: 아이템 위치

# ✅ 출력 형식:
# - 캐릭터가 아이템까지 도달하는 최소 거리 (정수)

# ✅ 입출력 예제:
#   입력: [[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8
#   출력: 17

# -----------------------------------------------------

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표계를 2배로 확장하여 반쪽 칸 문제 방지
    for i in range(len(rectangle)):
        rectangle[i] = [x * 2 for x in rectangle[i]]

    # 전체 보드 초기화 (102x102 크기, 좌표는 최대 100이므로 여유분 포함)
    board = [[0] * 102 for _ in range(102)]

    # 각 사각형마다 테두리는 1, 내부는 -1로 마킹
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 테두리(외곽선) 처리
                if x == x1 or x == x2 or y == y1 or y == y2:
                    if board[y][x] != -1:  # 내부보다 우선순위 낮음
                        board[y][x] = 1
                else:
                    board[y][x] = -1  # 내부는 이동 불가이므로 -1로 차단

    # BFS 초기화: 시작 위치 (좌표도 2배), 이동 횟수 0
    queue = deque([(characterX * 2, characterY * 2, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterY * 2][characterX * 2] = True  # 시작 지점 방문 처리

    # 상하좌우 이동 벡터
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y, count = queue.popleft()

        # 아이템 위치에 도달했으면 거리 반환 (2배 좌표이므로 //2)
        if (x, y) == (itemX * 2, itemY * 2):
            return count // 2

        # 4방향 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 좌표 유효성 검사 및 테두리인지 확인
            if 0 <= nx < 102 and 0 <= ny < 102:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True  # 방문 처리
                    queue.append((nx, ny, count + 1))  # 이동 거리 증가

    return 0  # 아이템에 도달하지 못한 경우 (문제 조건상 발생 X)

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 내부를 0으로만 처리해서 경계 구분이 모호했음
# ❌ 테두리와 내부 구분이 제대로 되지 않아 경로 단축 현상 발생
# ❌ 좌표 2배 확장 후 visited 처리 누락

# ✅ GPT가 준 힌트 요약:
# - 내부(사각형 내부)는 무조건 -1로 막고, 경계는 덮이지 않도록 분리 마킹
# - 2배 좌표 시스템에서 BFS 사용 후 //2로 되돌림

# ✅ 사용된 개념 요약:
# - BFS(최단 거리 탐색)
# - 좌표 스케일링(2배 확장으로 절반 지점 문제 해결)
# - 사각형 테두리 vs 내부 판별 처리
# - visited 배열로 중복 탐색 방지

# -----------------------------------------------------
