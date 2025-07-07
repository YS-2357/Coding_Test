# 백준 1248번: 맞춰봐
# 문제 설명:
# N개의 숫자로 이루어진 수열에서 특정 구간의 합이 주어진 부호 조건을 만족하도록 숫자를 배치하는 문제.
# - 부호 행렬이 주어지며, 특정 구간의 합이 양수(+), 음수(-), 0(0)인지 결정해야 한다.
# - -10부터 10까지의 숫자를 중복 없이 배치하여 조건을 만족하는 수열을 찾아야 한다.
# - 사전순으로 가장 빠른 정답을 출력해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 10)
# - 두 번째 줄에 N * (N + 1) / 2 개의 부호가 공백 없이 주어진다.

# 출력 형식:
# - 조건을 만족하는 하나의 수열을 출력한다. (정답이 여러 개일 경우 사전순으로 가장 빠른 것을 출력)

# 예제 입력 1:
# 4
# -+0++++--+
# 예제 출력 1:
# -2 1 0 2

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
signs = list(sys.stdin.readline().strip())

# ✅ 부호 행렬 초기화
board = [[''] * N for _ in range(N)]
index = 0
for i in range(N):
    for j in range(i, N):
        board[i][j] = signs[index]
        index += 1

# ✅ 결과를 저장할 리스트
seq = []

# ✅ 부호 조건 검증 함수
def is_valid(count):
    sub_sum = 0
    for i in range(count, -1, -1):
        sub_sum += seq[i]
        if board[i][count] == '+' and sub_sum <= 0:
            return False
        if board[i][count] == '-' and sub_sum >= 0:
            return False
        if board[i][count] == '0' and sub_sum != 0:
            return False
    return True

# ✅ 백트래킹 함수 정의
def backtrack(count):
    if count == N:
        print(*seq)
        exit(0)
        
    for i in range(-10, 11):
        seq.append(i)
        if is_valid(count):
            backtrack(count + 1)
        seq.pop()

# ✅ 탐색 시작
backtrack(0)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `board` 초기화 방식 오류
#    - 기존 코드: `board = [[''] * N] * N`
#    - ❌ 문제점: 모든 행이 동일한 리스트를 참조하여 의도치 않은 값 변경 발생.
#    - ✅ 수정: `board = [[''] * N for _ in range(N)]`으로 변경하여 각 행을 독립적으로 생성.

# 2. ✅ `is_valid(count)`에서 부분합 계산 오류
#    - 기존 코드: `total = sum(seq[i:count+1])`
#    - ❌ 문제점: `sum()`을 사용할 경우 매번 슬라이싱이 발생하여 비효율적.
#    - ✅ 수정: `sub_sum` 변수를 사용하여 부분합을 누적하여 계산.

# 3. ✅ `is_valid(count)`에서 `board[i][depth]` 잘못된 참조
#    - 기존 코드: `if board[i][depth] == '+' and sub_sum <= 0:`
#    - ❌ 문제점: `depth`는 정의되지 않은 변수이며, `count`가 사용되어야 함.
#    - ✅ 수정: `if board[i][count] == '+' and sub_sum <= 0:`으로 변경.

# 4. ✅ `is_valid(seq)` 잘못된 함수 호출
#    - 기존 코드: `if is_valid(seq):`
#    - ❌ 문제점: `is_valid()`는 `seq`가 아니라 `count`를 인자로 받아야 함.
#    - ✅ 수정: `if is_valid(count):`으로 변경.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀
