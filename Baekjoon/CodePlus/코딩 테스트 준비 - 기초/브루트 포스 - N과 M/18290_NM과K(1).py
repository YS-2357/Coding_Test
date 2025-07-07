# 백준 18290번: NM과 K (1)
# 문제 설명:
# N×M 크기의 격자에서 서로 인접하지 않은 K개의 수를 선택해 합의 최댓값을 구하는 문제.
# - 상하좌우로 인접한 수는 선택할 수 없다.
# - 완전 탐색(브루트포스)을 이용해 모든 가능한 조합을 찾고 최댓값을 구해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N, M, K가 주어진다. (1 ≤ N, M ≤ 10, 1 ≤ K ≤ min(4, N×M))
# - 두 번째 줄부터 N개의 줄에 걸쳐 M개의 정수가 주어진다. (-10,000 ≤ A_ij ≤ 10,000)

# 출력 형식:
# - 선택한 K개의 수의 합의 최댓값을 출력한다.

# 예제 입력 1:
# 2 3 2
# 1 2 3
# 4 5 6
# 예제 출력 1:
# 10

import sys

# ✅ 입력 처리
N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cannot = [[False] * M for _ in range(N)]  # 방문 체크용 배열
neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상하좌우 이동

max_sum = -50000  # 문제에서 주어진 수의 최솟값보다 작은 값으로 초기화

def select_numbers(count, total, start_x, start_y):
    """K개의 숫자를 선택하여 최대합을 구하는 브루트포스 탐색"""
    global max_sum

    if count == K:  # K개의 숫자를 모두 선택한 경우
        max_sum = max(max_sum, total)
        return

    for i in range(start_x, N):  # 이전보다 큰 인덱스에서 탐색
        for j in range(start_y if i == start_x else 0, M):  # 같은 행에서는 이전 열부터 탐색
            if not cannot[i][j]:  # 선택 가능하면
                # 현재 숫자 선택
                cannot[i][j] = True
                temp = []  # 인접한 칸을 비활성화하기 위한 리스트

                # 상하좌우 위치를 선택 불가능하게 설정
                for dx, dy in neighbors:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and not cannot[nx][ny]:
                        cannot[nx][ny] = True
                        temp.append((nx, ny))  # 나중에 원상복구할 위치 저장

                # 다음 숫자 선택 (완전 탐색)
                select_numbers(count + 1, total + board[i][j], i, j)

                # 원상 복구 (백트래킹)
                cannot[i][j] = False
                for nx, ny in temp:  # 원래 선택 불가능했던 곳을 다시 되돌림
                    cannot[nx][ny] = False

# 탐색 시작
select_numbers(0, 0, 0, 0)
print(max_sum)

# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ GPT `K`개의 숫자를 선택하는 과정에서 중복된 탐색을 했음.
#    - 기존 코드에서는 `(i, j)`를 선택한 후에도 **처음부터 다시 탐색**했음.
#    - ❌ 문제점: **이미 탐색한 숫자를 다시 선택할 가능성이 있음.**
#    - ✅ 수정: `(i, j)`를 선택한 후, 다음 탐색을 `i, j` 이후부터 진행하도록 변경.

# 2. ✅ GPT 백트래킹을 잘못 구현했음.
#    - 기존 코드에서는 `cannot[i][j]`를 원상복구할 때 **모든 상하좌우를 다시 `False`로 변경**했음.
#    - ❌ 문제점: **원래 선택할 수 없었던 위치까지 선택 가능해지는 오류 발생.**
#    - ✅ 수정: `temp` 리스트를 만들어 **새롭게 비활성화한 위치만 되돌리는 방식으로 변경.**

# 3. ✅ `if count = K:` 문법 오류를 냈음 (`=` → `==`).
#    - ❌ 문제점: `=`는 할당 연산자로 사용되며, 조건문에서 비교 연산을 할 때는 `==`을 사용해야 함.
#    - ✅ 수정: `if count == K:`로 변경.

# 4. ✅ `K`개의 숫자를 선택하기 전에 최댓값을 비교하는 논리를 잘못 짰음.
#    - ❌ 문제점: `count == K`이기 전에 `max_sum`을 비교하고 업데이트함.
#    - ✅ 수정: **`K`개의 숫자를 선택한 후** 최댓값을 갱신하는 구조로 변경.

# 5. ✅ 백트래킹에서 원상복구를 정확하게 하지 않았음.
#    - ❌ 문제점: `cannot[i][j]`를 `False`로 돌리는 과정에서 인접한 칸도 `False`로 변경했음.
#    - ✅ 수정: **인접한 칸을 되돌리기 전, 원래 `False`였던 곳은 그대로 유지하도록 `temp` 리스트 활용.**

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
