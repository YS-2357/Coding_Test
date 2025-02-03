# 백준 3085번: 사탕 게임
# 문제 설명:
# N x N 크기의 보드에서 인접한 두 칸의 사탕을 교환하여 가장 긴 연속된 사탕 개수를 찾는 문제.

# 입력 형식:
# 첫째 줄에 보드 크기 N이 주어진다. (3 ≤ N ≤ 50)
# 다음 N개의 줄에 N개의 문자가 주어진다. ('C', 'P', 'Z', 'Y' 중 하나)

# 출력 형식:
# 먹을 수 있는 사탕의 가장 긴 연속 개수를 출력.

# 예제 입력 1:
# 3
# CCP
# CCP
# PPC
# 예제 출력 1:
# 3

import sys

# 🛑 [❌ 사용자가 작성한 코드] (틀린 코드)
"""
N = int(input())
array = []
for i in range(N):
    array.append(list(input().strip()))

maximum = 0

# 가로 검사
for i in range(N):
    count = 1
    for j in range(N-1):
        if array[i][j] == array[i][j+1]:
            count += 1
            if count >= maximum:
                maximum = count
        else:
            count = 1

# 세로 검사
for j in range(N):
    count = 1
    for i in range(N-1):
        if array[i][j] == array[i+1][j]:
            count += 1
            if count >= maximum:
                maximum = count
        else:
            count = 1

print(maximum)
"""

# 📌 [❌ 사용자의 코드에서 부족한 점]
# 1. **사탕을 교환하는 로직이 없음**
#    - 주어진 배열에서 최댓값을 찾는 로직만 구현됨.
#    - 사탕을 바꾼 후 최대 연속 개수를 확인하는 과정이 필요함.
# 2. **모든 행과 열에서 인접한 두 사탕을 바꾼 후 검사해야 함**
#    - 한 번의 검사로 끝나는 것이 아니라, 바꾼 후 다시 검사해야 함.
# 3. **바꾼 후 원래 상태로 되돌리는 과정이 필요함**
#    - 탐색 후 다시 원상복구해야 함.

---

# ✅ [✔ 모범 답안: 올바르게 수정된 코드]
# - "가장 긴 연속된 사탕 개수"를 찾는 함수 `check_candies()` 구현
# - "사탕 교환 후 다시 검사"하는 로직 추가
# - 탐색 후 원래 상태로 복구

def check_candies(board, N):
    """
    현재 상태에서 가로 및 세로 방향으로 가장 긴 연속된 사탕 개수를 찾는 함수.
    """
    max_count = 0
    
    # 가로 방향 검사
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:  # 이전 사탕과 같다면 카운트 증가
                count += 1
            else:
                count = 1  # 연속이 끊기면 다시 1로 초기화
            max_count = max(max_count, count)  # 최대값 갱신
    
    # 세로 방향 검사
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:  # 위쪽 사탕과 같다면 카운트 증가
                count += 1
            else:
                count = 1  # 연속이 끊기면 다시 1로 초기화
            max_count = max(max_count, count)  # 최대값 갱신
    
    return max_count


def solve():
    # 입력 처리
    N = int(sys.stdin.readline().strip())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]

    max_candies = 0  # 최댓값 저장 변수

    # 모든 행과 열에 대해 인접한 두 칸을 교환하고 최댓값 검사
    for i in range(N):
        for j in range(N-1):
            # 가로로 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_candies = max(max_candies, check_candies(board, N))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 원상 복구

    for i in range(N-1):
        for j in range(N):
            # 세로로 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            max_candies = max(max_candies, check_candies(board, N))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원상 복구

    # 최종 결과 출력
    print(max_candies)

# 함수 실행
solve()
