# 20327_배열_회전하기_6.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 2^n x 2^n 크기의 배열이 주어지고, r개의 연산이 주어진다.
# - 연산은 1번부터 8번까지 총 8가지가 존재하며, 각 연산은 정해진 방식대로
#   배열을 회전하거나 반전시킨다.
# - 연산의 대상은 2^l x 2^l 블록 단위이다.
# - 각 연산은 블록 내부를 회전하거나, 블록의 위치를 이동시킨다.
#
# ✅ 입력 형식:
# - 첫 줄: n r (1 ≤ n ≤ 6, 1 ≤ r ≤ 1000)
# - 다음 2^n 줄: 배열의 각 행
# - 다음 r줄: 연산 정보 k l (1 ≤ k ≤ 8, 0 ≤ l ≤ n)
#
# ✅ 출력 형식:
# - 연산을 모두 수행한 후의 배열을 출력한다.
#
# ✅ 예제 입력:
# 3 1
# 1 2 3 4 5 6 7 8
# ...
# 2 2
#
# ✅ 예제 출력:
# ...
# -----------------------------------------------------

import sys
input = sys.stdin.readline

n, r = map(int, input().split())  # n은 배열의 크기를 위한 지수, r은 연산 수
arr = [list(map(int, input().split())) for _ in range(2 ** n)]  # 2^n x 2^n 배열 입력

for _ in range(r):  # 연산 수만큼 반복
    op_type, l = map(int, input().split())  # op_type: 연산 종류, l: 블록 크기를 결정하는 지수

    block_size = 2 ** l  # 현재 블록의 크기
    temp_block = []  # 블록 내 값을 저장할 임시 리스트
    new_arr = [[0] * (2 ** n) for _ in range(2 ** n)]  # 결과를 저장할 새로운 배열

    if op_type == 1:
        # 1번 연산: 각 블록을 상하 반전
        for i in range(0, 2 ** n, block_size):
            for j in range(0, 2 ** n, block_size):
                for row in arr[i:i + block_size]:
                    temp_block.append(row[j:j + block_size])  # 블록 추출
                for idx in range(len(temp_block) // 2):
                    temp_block[idx], temp_block[-idx - 1] = temp_block[-idx - 1], temp_block[idx]  # 상하 반전
                for x in range(i, i + block_size):
                    for y in range(j, j + block_size):
                        new_arr[x][y] = temp_block[x - i][y - j]  # 새로운 배열에 반영
                temp_block = []

    elif op_type == 2:
        # 2번 연산: 각 블록을 좌우 반전
        for i in range(0, 2 ** n, block_size):
            for j in range(0, 2 ** n, block_size):
                for row in arr[i:i + block_size]:
                    temp_block.append(row[j:j + block_size])  # 블록 추출
                mirrored = [row[::-1] for row in temp_block]  # 각 행을 좌우 반전
                for x in range(i, i + block_size):
                    for y in range(j, j + block_size):
                        new_arr[x][y] = mirrored[x - i][y - j]  # 새로운 배열에 반영
                temp_block = []

    elif op_type == 3:
        # 3번 연산: 각 블록을 시계 방향 90도 회전
        for i in range(0, 2 ** n, block_size):
            for j in range(0, 2 ** n, block_size):
                for row in arr[i:i + block_size]:
                    temp_block.append(row[j:j + block_size])  # 블록 추출
                rotated = [[0] * block_size for _ in range(block_size)]  # 회전 결과 저장용
                for x in range(block_size):
                    for y in range(block_size):
                        rotated[x][y] = temp_block[block_size - y - 1][x]  # 시계 방향 회전 공식
                for x in range(i, i + block_size):
                    for y in range(j, j + block_size):
                        new_arr[x][y] = rotated[x - i][y - j]  # 새로운 배열에 반영
                temp_block = []

    elif op_type == 4:
        # 4번 연산: 각 블록을 반시계 방향 90도 회전
        for i in range(0, 2 ** n, block_size):
            for j in range(0, 2 ** n, block_size):
                for row in arr[i:i + block_size]:
                    temp_block.append(row[j:j + block_size])  # 블록 추출
                rotated = [[0] * block_size for _ in range(block_size)]
                for x in range(block_size):
                    for y in range(block_size):
                        rotated[x][y] = temp_block[y][block_size - x - 1]  # 반시계 방향 회전 공식
                for x in range(i, i + block_size):
                    for y in range(j, j + block_size):
                        new_arr[x][y] = rotated[x - i][y - j]  # 새로운 배열에 반영
                temp_block = []

    elif op_type in (5, 6, 7, 8):
        # 5~8번 연산: 블록 위치 자체를 이동
        from collections import defaultdict

        block_dict = {}  # 블록 정보를 저장할 딕셔너리
        cnt = -1
        for i in range(0, 2 ** n, block_size):
            cnt += 1
            for j in range(0, 2 ** n, block_size):
                for row in arr[i:i + block_size]:
                    temp_block.append(row[j:j + block_size])  # 블록 추출
                block_dict[(i // block_size, j // block_size)] = temp_block  # 블록 위치에 저장
                temp_block = []

        size = (2 ** n) // block_size  # 블록 수
        if op_type == 5:
            # 5번 연산: 블록 전체 상하 반전
            for i in range(size // 2):
                for j in range(size):
                    block_dict[(i, j)], block_dict[(size - 1 - i, j)] = block_dict[(size - 1 - i, j)], block_dict[(i, j)]

        elif op_type == 6:
            # 6번 연산: 블록 전체 좌우 반전
            for i in range(size):
                for j in range(size // 2):
                    block_dict[(i, j)], block_dict[(i, size - 1 - j)] = block_dict[(i, size - 1 - j)], block_dict[(i, j)]

        elif op_type == 7:
            # 7번 연산: 블록 시계 방향 이동
            rotated_blocks = {}
            for i in range(size):
                for j in range(size):
                    rotated_blocks[(i, j)] = block_dict[(size - 1 - j, i)]
            block_dict = rotated_blocks

        elif op_type == 8:
            # 8번 연산: 블록 반시계 방향 이동
            rotated_blocks = {}
            for i in range(size):
                for j in range(size):
                    rotated_blocks[(i, j)] = block_dict[(j, size - 1 - i)]
            block_dict = rotated_blocks

        # 블록 정보를 새로운 배열에 반영
        for i in range(size):
            for j in range(size):
                block = block_dict[(i, j)]
                for x in range(i * block_size, (i + 1) * block_size):
                    for y in range(j * block_size, (j + 1) * block_size):
                        new_arr[x][y] = block[x - (i * block_size)][y - (j * block_size)]

    arr = new_arr  # 원본 배열 갱신

# 결과 출력
for row in arr:
    print(" ".join(map(str, row)))

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드 🚀
# - 연산 종류에 따라 블록 내부 또는 블록 위치 자체를 처리.
# - 1~4번은 블록 내부 처리, 5~8번은 블록 위치 조작.
# - 모든 연산은 딕셔너리 또는 슬라이싱을 활용해 처리 효율성 확보.
# - 문제 요구사항과 조건을 충실히 반영한 정답 코드.
# -----------------------------------------------------
