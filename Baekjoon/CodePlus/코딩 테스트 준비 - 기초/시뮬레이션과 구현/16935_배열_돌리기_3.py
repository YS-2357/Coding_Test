# -----------------------------------------------------
# ✅ 문제 설명:
# - N×M 크기의 배열이 주어지고, 특정 연산을 수행해야 한다.
# - 6개의 연산 (상하반전, 좌우반전, 시계90도 회전, 반시계90도 회전, 
#   좌상/우상/우하/좌하 시계방향 이동, 좌상/좌하/우하/우상 반시계방향 이동)을 구현해야 한다.
# - R개의 연산이 주어졌을 때, 최종 배열 상태를 출력해야 한다.
#
# ✅ 입력 형식:
# - 첫 번째 줄: `N M R` (2 ≤ N, M ≤ 100, 1 ≤ R ≤ 1000)
# - 이후 N개의 줄: 배열 원소 (0 ≤ 원소 ≤ 100)
# - 마지막 줄: `R`개의 연산 (1 ≤ 연산 ≤ 6)
#
# ✅ 출력 형식:
# - 연산을 수행한 후 최종 배열을 출력
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   3 3 1
#   1 2 3
#   4 5 6
#   7 8 9
#   3
# 🔹 예제 출력 1:
#   7 4 1
#   8 5 2
#   9 6 3
# -----------------------------------------------------

import sys

# ✅ 90도 회전 (시계 방향)
def rotate_right(matrix, n, m):
    """ 90도 시계 방향 회전 """
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[n - 1 - j][i]
    return temp, m, n  # 회전 후 크기 변경

# ✅ 90도 회전 (반시계 방향)
def rotate_left(matrix, n, m):
    """ 90도 반시계 방향 회전 """
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[j][m - 1 - i]
    return temp, m, n  # 회전 후 크기 변경

# ✅ 좌상/우상/우하/좌하 시계 방향 이동
def move_clockwise(matrix, n, m):
    """
    4분면을 시계 방향으로 이동하는 함수
    - 좌상 → 우상, 우상 → 우하, 우하 → 좌하, 좌하 → 좌상 이동
    """
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 좌상 → 우상
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i + n // 2][j] = matrix[i][j]  # 우상 → 우하
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 우하 → 좌하
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i - n // 2][j] = matrix[i][j]  # 좌하 → 좌상
    return temp

# ✅ 좌상/좌하/우하/우상 반시계 방향 이동
def move_counter_clockwise(matrix, n, m):
    """
    4분면을 반시계 방향으로 이동하는 함수
    - 좌상 → 좌하, 좌하 → 우하, 우하 → 우상, 우상 → 좌상 이동
    """
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i + n // 2][j] = matrix[i][j]  # 좌상 → 좌하
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 좌하 → 우하
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i - n // 2][j] = matrix[i][j]  # 우하 → 우상
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 우상 → 좌상
    return temp

# ✅ 입력 처리
n, m, r = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
operations = list(map(int, sys.stdin.readline().split()))

# ✅ 연산 수행
for op in operations:
    if op == 1:
        board.reverse()  # 상하반전
    elif op == 2:
        board = [row[::-1] for row in board]  # 좌우반전
    elif op == 3:
        board, n, m = rotate_right(board, n, m)  # 시계방향 회전
    elif op == 4:
        board, n, m = rotate_left(board, n, m)  # 반시계방향 회전
    elif op == 5:
        board = move_clockwise(board, n, m)  # 좌상/우상/우하/좌하 시계방향 이동
    elif op == 6:
        board = move_counter_clockwise(board, n, m)  # 좌상/좌하/우하/우상 반시계방향 이동

# ✅ 최종 결과 출력
for row in board:
    print(*row)

# -----------------------------------------------------
# ✅ 2단계에서 발생한 오류 정리 및 수정:
# 1️⃣ **배열 반전 시 인덱스 오류**
# - 기존 코드: `matrix.reverse()`가 상하반전만 수행하고 좌우반전은 따로 처리하지 않음.
# - ✅ 해결: `board.reverse()`와 `board = [row[::-1] for row in board]`을 분리하여 구현.

# 2️⃣ **시계 및 반시계 회전 시 N, M 값 유지 오류**
# - 기존 코드: `rotate_right()`와 `rotate_left()`에서 N, M 값이 변경되지 않음.
# - ✅ 해결: `return temp, m, n`을 추가하여 회전 후 크기 변경.

# 3️⃣ **4분면 이동 연산에서 잘못된 위치 지정**
# - 기존 코드에서 4분면 이동이 잘못 설정됨.
# - ✅ 해결: `move_clockwise()`와 `move_counter_clockwise()`를 수정하여 올바른 방향 이동.

# ✅ 최종 정리:
# - `sys.stdin.readline()`을 사용하여 빠른 입력 처리.
# - 6가지 연산을 개별 함수로 정의하여 코드 모듈화.
# - N, M이 변경되는 회전 연산을 처리한 후 크기 조정.
# -----------------------------------------------------
