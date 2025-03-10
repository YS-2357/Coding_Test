# 14499_주사위_굴리기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - N×M 크기의 지도 위에서 주사위를 이동시키는 문제.
# - 주어진 이동 명령에 따라 주사위를 굴리고, 주사위 바닥과 지도 값을 변경해야 함.
# - 지도 범위를 벗어나면 해당 이동은 무시됨.
#
# ✅ 입력 형식:
# - 첫 번째 줄: N, M, x, y, K (지도 크기, 시작 좌표, 이동 횟수)
# - N줄: 지도 정보 (0 또는 숫자)
# - 한 줄: K개의 이동 명령 (1: 동, 2: 서, 3: 북, 4: 남)
#
# ✅ 출력 형식:
# - 각 이동 후 주사위 윗면의 숫자 출력 (지도 범위 벗어나면 출력 없음)
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   4 2 0 0 8
#   0 2
#   3 4
#   5 6
#   7 8
#   4 4 4 1 3 3 3 2
# 🔹 예제 출력:
#   0
#   0
#   3
#   0
#   0
#   8
#   6
# -----------------------------------------------------

import sys

# ✅ 입력 처리
N, M, start_x, start_y, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = list(map(int, sys.stdin.readline().split()))

# ✅ 주사위 초기 상태 (윗면, 북, 동, 서, 남, 바닥면)
dice = [0, 0, 0, 0, 0, 0]

# ✅ 이동 방향 (동, 서, 북, 남)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# ✅ 주사위 굴리기 함수
def move_dice(command):
    """ 주사위를 특정 방향으로 굴리는 함수 """
    if command == 1:  # 동쪽
        dice[0], dice[2], dice[5], dice[4] = dice[4], dice[0], dice[2], dice[5]
    elif command == 2:  # 서쪽
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
    elif command == 3:  # 북쪽
        dice[0], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[0]
    elif command == 4:  # 남쪽
        dice[0], dice[1], dice[5], dice[3] = dice[3], dice[0], dice[1], dice[5]

# ✅ 이동 명령 처리
for command in commands:
    nx, ny = start_x + dx[command - 1], start_y + dy[command - 1]

    # 🚨 이동 가능 여부 체크
    if 0 <= nx < N and 0 <= ny < M:
        start_x, start_y = nx, ny  # 좌표 업데이트
        move_dice(command)  # 주사위 굴리기

        # 🚨 지도와 주사위 바닥면 값 교환
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]  # 주사위 바닥면 값 복사
        else:
            dice[5] = board[nx][ny]  # 지도 값을 주사위 바닥면에 저장
            board[nx][ny] = 0  # 지도 값을 0으로 초기화

        # ✅ 주사위 윗면 값 출력
        print(dice[0])

# -----------------------------------------------------
# ✅ 2단계에서 틀렸던 점 및 수정 사항:
# 1️⃣ **주사위 회전 로직 오류**
#    - 기존 코드에서 `up, north, east, south, west, down`을 미리 선언했으나, 
#      새로운 값이 올바르게 반영되지 않았음.
#    - 해결: `dice` 리스트를 직접 갱신하는 방식으로 수정하여 주사위 상태가 유지되도록 변경.
#
# 2️⃣ **윗면 값 출력 오류**
#    - 기존 코드에서 `print(dice[1])`을 사용했지만, 윗면은 `dice[0]`이므로 수정.
#
# 3️⃣ **이동 불가능한 경우 체크**
#    - 기존 코드에서 `nx, ny`를 계산 후 이동이 불가능한 경우에도 `move_dice()`를 호출함.
#    - 해결: `if 0 <= nx < N and 0 <= ny < M:` 조건을 먼저 검사하여 불필요한 함수 호출 방지.
# -----------------------------------------------------
