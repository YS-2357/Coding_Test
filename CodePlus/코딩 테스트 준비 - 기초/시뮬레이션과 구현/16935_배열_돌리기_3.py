# 16935_배열_돌리기_3.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - N×M 크기의 배열을 주어지고, 특정 연산을 수행해야 한다.
# - 6개의 연산 (상하반전, 좌우반전, 시계90도 회전, 반시계90도 회전, 
#   4분면 시계방향 이동, 4분면 반시계방향 이동)을 구현해야 한다.
# - R개의 연산이 주어졌을 때, 최종 배열 상태를 출력해야 한다.
#
# ✅ 입력 형식:
# - 첫 번째 줄: N, M, R (2 ≤ N, M ≤ 100, 1 ≤ R ≤ 1000)
# - 이후 N개의 줄: 배열 원소 (0 ≤ 원소 ≤ 100)
# - 마지막 줄: R개의 연산 (1 ≤ 연산 ≤ 6)
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

def rotate_right(matrix, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[n - 1 - j][i]
    return temp, m, n

def rotate_left(matrix, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[j][m - 1 - i]
    return temp, m, n

def move_clockwise(matrix, n, m):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 1 -> 2
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i + n // 2][j] = matrix[i][j]  # 2 -> 3
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 3 -> 4
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i - n // 2][j] = matrix[i][j]  # 4 -> 1
    return temp

def move_counter_clockwise(matrix, n, m):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i + n // 2][j] = matrix[i][j]  # 1 -> 4
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 4 -> 3
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i - n // 2][j] = matrix[i][j]  # 3 -> 2
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 2 -> 1
    return temp

n, m, r = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
operations = list(map(int, sys.stdin.readline().split()))

for op in operations:
    if op == 1:
        board.reverse()
    elif op == 2:
        board = [row[::-1] for row in board]
    elif op == 3:
        board, n, m = rotate_right(board, n, m)
    elif op == 4:
        board, n, m = rotate_left(board, n, m)
    elif op == 5:
        board = move_clockwise(board, n, m)
    elif op == 6:
        board = move_counter_clockwise(board, n, m)

for row in board:
    print(*row)
