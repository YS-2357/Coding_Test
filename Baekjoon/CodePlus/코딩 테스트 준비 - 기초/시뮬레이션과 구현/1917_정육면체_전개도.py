# 1917_정육면체_전개도.py
# -------------------------------------------------------------
# ✅ 문제 설명:
# - 6x6 격자 안에 주사위 전개도가 주어짐 (1이 6개 있음).
# - 이를 실제 정육면체로 접을 수 있는지 판단하는 문제.
# - 총 3개의 전개도가 주어지며, 각각에 대해 'yes' 또는 'no'를 출력.

# ✅ 입력 형식:
# - 각 테스트 케이스는 6줄씩 총 18줄.
# - 각 줄에는 0 또는 1이 6개씩 주어짐.
# - 입력은 총 3개의 전개도로 구성됨 (6x6 x 3).

# ✅ 출력 형식:
# - 각 전개도에 대해 접을 수 있으면 "yes", 불가능하면 "no"를 출력.

# ✅ 예제 입력:
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 0 1 1 1 1 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# ...
# ✅ 예제 출력:
# yes
# no
# yes
# -------------------------------------------------------------

import sys
sys.setrecursionlimit(10000)  # DFS 재귀 깊이 제한 해제

# ✅ 네 방향 (상, 하, 좌, 우) 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# ✅ 주사위를 굴렸을 때의 면 변화 정의 함수
def roll(dice, dir):
    # 0, 1, 2, 3, 4, 5
    top, bottom, front, back, left, right = dice
    if dir == 0:  # 위쪽으로 굴림
        return [front, back, bottom, top, left, right]
    elif dir == 1:  # 아래쪽으로 굴림
        return [back, front, top, bottom, left, right]
    elif dir == 2:  # 왼쪽으로 굴림
        return [right, left, front, back, top, bottom]
    elif dir == 3:  # 오른쪽으로 굴림
        return [left, right, front, back, bottom, top]

# ✅ DFS로 전개도에서 주사위를 굴리며 바닥면을 기록
def dfs(x, y, dice):
    visited[x][y] = True
    face_map[(x, y)] = dice[1]  # 현재 위치의 바닥면 기록

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < 6 and 0 <= ny < 6:
            if not visited[nx][ny] and board[nx][ny] == 1:
                ndice = roll(dice, dir)  # 주사위 상태 갱신
                dfs(nx, ny, ndice)  # 다음 위치 탐색

# ✅ 테스트 케이스 3개 반복
for _ in range(3):
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]
    visited = [[False] * 6 for _ in range(6)]  # 방문 체크 배열
    face_map = {}  # 위치별 주사위 면 기록

    # ✅ 시작점 (1이 있는 첫 좌표) 찾기
    found = False
    for i in range(6):
        for j in range(6):
            if board[i][j] == 1:
                dfs(i, j, [0, 1, 2, 3, 4, 5])  # DFS 시작
                found = True
                break
        if found:
            break

    # ✅ 전개도가 유효한 정육면체인지 판별
    if len(set(face_map.values())) == 6 and len(face_map) == 6:
        print("yes")  # 주사위 6면이 중복 없이 모두 사용됨
    else:
        print("no")  # 중복되거나 6면이 아님

# -------------------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드 🚀
# - DFS + 주사위 굴리기 시뮬레이션 기반.
# - 주사위의 6면이 정확히 한 번씩 사용되는지 확인.
# - DFS 깊이 제한 해제를 통해 모든 가능한 전개도를 탐색 가능.
# - 방향별 roll 함수로 주사위 면 위치 추적.
#
# ✅ 2단계에서 틀렸던 점:
# 1️⃣ 단순히 6개의 1이 있다고 해서 전개도가 유효하다고 판단할 수 없음.
# 2️⃣ 주사위의 면이 중복되거나 누락될 수 있음 → DFS로 6면 추적 필요.
#
# ✅ 요청 힌트 기반 구현:
# - "11가지 전개도 외우지 않고도 해결하는 방법" → DFS + roll 시뮬레이션.
# - 전개도를 따라 굴리면서 주사위 면이 모두 한 번씩 쓰이는지 체크.
# -------------------------------------------------------------
