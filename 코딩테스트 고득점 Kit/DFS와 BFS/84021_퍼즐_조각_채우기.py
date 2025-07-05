# 84021_퍼즐 조각 채우기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 게임 보드의 빈 공간(0)과 테이블의 퍼즐 조각(1)을 맞춰 최대한 많이 채우세요.
# - 조각은 90도씩 회전할 수 있고, 정확히 맞는 조각만 사용할 수 있습니다.
# - 한 조각은 한 번만 사용 가능하며, 맞는 경우에만 채워집니다.

# ✅ 입력 형식:
# - game_board: n x n 정사각형 보드 (0은 빈칸, 1은 채워진 부분)
# - table: 퍼즐 조각들이 들어 있는 n x n 보드 (1은 퍼즐, 0은 빈공간)

# ✅ 출력 형식:
# - game_board의 빈 칸에 table의 퍼즐 조각을 정확히 끼워 넣을 수 있는 총 블록 칸 수

# ✅ 입출력 예제:
# 입력:
# game_board = [[1,1,0],[0,1,0],[0,1,1]]
# table = [[1,1,1],[1,0,0],[0,0,0]]
# 출력: 3

# -----------------------------------------------------

from collections import deque

def solution(game_board, table):
    n = len(game_board)  # 보드의 크기 n

    # ✅ 특정 값(0 또는 1)에 대해 연결된 블록들을 추출하는 함수
    def extract_blocks(board, target):
        visited = [[False] * n for _ in range(n)]  # 방문 여부 기록
        blocks = []  # 추출된 블록 리스트

        for i in range(n):
            for j in range(n):
                if board[i][j] == target and not visited[i][j]:  # 타겟 값이고 아직 방문 안 했다면
                    q = deque([(i, j)])  # BFS 시작
                    visited[i][j] = True
                    shape = []  # 현재 블록의 모양 좌표들

                    while q:
                        x, y = q.popleft()
                        shape.append((x, y))  # 블록 좌표 저장

                        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:  # 4방향 탐색
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
                                visited[nx][ny] = True
                                q.append((nx, ny))  # 연결된 블록 탐색

                    # 좌상단 기준으로 정규화
                    min_x = min(p[0] for p in shape)
                    min_y = min(p[1] for p in shape)
                    normalized = sorted([(x - min_x, y - min_y) for x, y in shape])
                    blocks.append(normalized)  # 정규화된 블록 저장
        return blocks

    # ✅ 블록을 90도 회전하는 함수
    def rotate(block):
        return [(y, -x) for x, y in block]  # x, y를 90도 회전 (y, -x)

    # ✅ 회전 후 좌표를 다시 정규화하는 함수
    def normalize(block):
        min_x = min(x for x, y in block)
        min_y = min(y for x, y in block)
        return sorted([(x - min_x, y - min_y) for x, y in block])  # 좌상단 기준으로 이동

    # ✅ game_board에서 빈 공간(0), table에서 퍼즐 조각(1) 추출
    empty_spaces = extract_blocks(game_board, 0)
    puzzle_pieces = extract_blocks(table, 1)

    used = [False] * len(puzzle_pieces)  # 각 퍼즐 조각 사용 여부
    answer = 0  # 최종 채운 퍼즐 칸 수

    # ✅ 빈 공간마다 조각을 맞춰본다
    for empty in empty_spaces:
        for i in range(len(puzzle_pieces)):
            if used[i]:  # 이미 사용한 조각은 패스
                continue
            piece = puzzle_pieces[i]  # 현재 조각

            for _ in range(4):  # 회전 4번까지 시도
                piece = rotate(piece)  # 90도 회전
                piece = normalize(piece)  # 회전 후 정렬

                if piece == empty:  # 퍼즐이 빈 공간과 정확히 맞으면
                    used[i] = True  # 해당 조각 사용 처리
                    answer += len(piece)  # 조각 크기만큼 정답에 더함
                    break
            if used[i]:  # 이미 매칭됐다면 다음 빈칸으로 넘어감
                break

    return answer  # 최종 채운 칸 수 반환

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 블록 정규화 누락 시 회전 후 비교 오류 발생
# ❌ 90도 회전만 해놓고 normalize 안 해서 오답 발생
# ❌ 같은 조각 여러 번 사용하는 오류 발생 → used[] 필요

# ✅ GPT가 준 힌트 요약:
# - 퍼즐 블록을 정규화하고 회전마다 normalize해야 비교 가능
# - 빈칸과 블록은 모두 같은 방식으로 추출하여 비교 대상 통일
# - BFS + 회전 + 정렬 기반의 비교 구조를 사용할 것

# ✅ 사용된 개념 요약:
# - BFS: 블록/빈칸 탐색
# - 회전 및 정규화: 퍼즐 비교를 위한 정규 형태 구성
# - 중복 방지 처리: used 배열
# - 좌표 처리 및 좌상단 기준 이동
# -----------------------------------------------------
