# 백준 14391번: 종이 조각 (비트마스크 풀이)
# 문제 설명:
# N x M 크기의 종이를 조각내어 각 조각의 숫자를 합한 값이 최대가 되도록 하는 문제.
# - 각 칸을 "가로 조각" 또는 "세로 조각"으로 나누어 숫자로 변환 가능.
# - "가로 조각"이면 같은 행에서 연속된 숫자를 하나의 수로 간주.
# - "세로 조각"이면 같은 열에서 연속된 숫자를 하나의 수로 간주.
# - 비트마스크를 활용하여 가능한 모든 조합을 탐색해 최댓값을 구함.

# 입력 형식:
# - 첫 번째 줄에 두 정수 N(1 ≤ N ≤ 4), M(1 ≤ M ≤ 4)이 주어진다.
# - 이후 N개의 줄에 M자리의 숫자가 주어진다.

# 출력 형식:
# - 모든 조각을 합한 최댓값을 출력한다.

# 예제 입력 1:
# 2 3
# 123
# 312
# 예제 출력 1:
# 435

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N, M = map(int, sys.stdin.readline().split())  # ✅ N x M 크기 입력
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]  # ✅ 숫자로 이루어진 종이 조각 입력
max_sum = 0  # ✅ 최댓값 저장 변수

# ✅ 비트마스크를 이용하여 모든 조각 나누는 경우 탐색
for mask in range((1 << (N * M))):  # ✅ 2^(N*M) 개의 조합을 생성 (모든 경우 탐색)
    total_sum = 0  # ✅ 현재 조합에서 숫자 합

    # ✅ "가로 조각" 탐색 (mask에서 0인 경우)
    for r in range(N):  
        c = 0
        while c < M:
            if not (mask & (1 << (r * M + c))):  # ✅ 비트가 0이면 "가로 조각"
                num = 0  # ✅ 하나의 숫자로 변환
                while c < M and not (mask & (1 << (r * M + c))):  # ✅ 연속된 가로 숫자 처리
                    num = num * 10 + board[r][c]
                    c += 1
                total_sum += num  # ✅ 가로 조각 합산
            else:
                c += 1  # ✅ 다음 칸 탐색

    # ✅ "세로 조각" 탐색 (mask에서 1인 경우)
    for c in range(M):
        r = 0
        while r < N:
            if mask & (1 << (r * M + c)):  # ✅ 비트가 1이면 "세로 조각"
                num = 0  # ✅ 하나의 숫자로 변환
                while r < N and (mask & (1 << (r * M + c))):  # ✅ 연속된 세로 숫자 처리
                    num = num * 10 + board[r][c]
                    r += 1
                total_sum += num  # ✅ 세로 조각 합산
            else:
                r += 1  # ✅ 다음 칸 탐색

    # ✅ 최대 합 갱신
    max_sum = max(max_sum, total_sum)

# ✅ 결과 출력
print(max_sum)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `mask = 0`을 고려해야 함
#    - 기존 코드: `for mask in range(1, (1 << (N * M)))`
#    - ❌ 문제점: `mask = 0`을 제외하여 **모든 조합을 고려하지 않음**
#    - ✅ 수정: `for mask in range((1 << (N * M))):`로 변경하여 공집합 포함 탐색.

# 2. ✅ 괄호 우선순위 오류
#    - 기존 코드: `if mask & (1 << r * M + c):`
#    - ❌ 문제점: `r * M + c`의 연산이 올바르게 수행되지 않을 가능성이 있음.
#    - ✅ 수정: `if mask & (1 << (r * M + c)):`로 괄호를 추가하여 연산 순서 명확화.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
