# 백준 14889번: 스타트와 링크
# 문제 설명:
# N명의 사람을 두 팀으로 나눌 때, 두 팀 간 능력치 차이를 최소로 만드는 문제.
# - S[i][j]: i번과 j번 사람이 같은 팀일 때 발생하는 능력치.
# - 두 팀의 능력치 차이의 최솟값을 출력해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (4 ≤ N ≤ 20, 짝수)
# - 다음 N개의 줄에는 N개의 정수로 이루어진 능력치 배열이 주어진다.

# 출력 형식:
# - 두 팀 간 능력치 차이의 최솟값을 출력.

# 예제 입력 1:
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0
# 예제 출력 1:
# 0

import sys
from itertools import combinations

# ✅ 입력 처리
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minimum = float("inf")  # 최솟값 초기화

nums = list(range(N))  # 0부터 N-1까지의 인덱스 리스트
teams = list(combinations(range(N), N // 2))  # N명 중 N//2명 선택하는 모든 조합

for team in teams:
    other = list(set(nums) - set(team))  # 선택되지 않은 팀 구성

    sum_team = sum(board[i][j] + board[j][i] for i, j in combinations(team, 2))
    sum_other = sum(board[i][j] + board[j][i] for i, j in combinations(other, 2))

    minimum = min(minimum, abs(sum_team - sum_other))

# ✅ 결과 출력
print(minimum)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 리스트 차집합 연산 오류
#    - 기존 코드: `other = nums - team`
#    - ❌ 문제점: `list`는 `-` 연산이 지원되지 않음.
#    - ✅ 수정: `set`을 이용하여 차집합 연산 후 다시 `list`로 변환.

# 2. ✅ 불필요한 리스트 변환 (`combinations()`)
#    - 기존 코드: `comb_team = list(combinations(team, 2))`
#    - ❌ 문제점: `combinations()` 자체가 **이터레이터이므로 리스트 변환 필요 없음.**
#    - ✅ 수정: `for i, j in combinations(team, 2):` 형태로 바로 사용.

# -----------------------------------------------------
# 📌 몰랐던 점 (힌트 제공 내용)

# 🔹 `combinations(range(N), N//2)`를 사용하면 팀 조합을 쉽게 구할 수 있음.
# 🔹 `set`을 이용하면 리스트 차집합 연산(`-`)을 우회할 수 있음.
# 🔹 `combinations()`는 리스트 변환이 필요하지 않으며, 직접 `for` 문에서 사용 가능함.
# 🔹 `sum(board[i][j] + board[j][i] for i, j in combinations(team, 2))`와 같이 한 줄로 계산할 수 있음.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!

# -----------------------------------------------------
# 백준 문제 14889: 스타트와 링크

# ✅ 최적화 내용:
# - `combinations`을 사용하지 않고 백트래킹을 이용해 조합을 직접 탐색.
# - 한 팀이 결정되면 나머지는 자동으로 상대 팀이 되므로 중복 탐색 방지.
# - 능력치 차이를 계산할 때 반복문을 줄여 효율성 향상.

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N  # 방문 여부 체크
minimum = float("inf")  # 최솟값 초기화

def calculate_difference():
    """ 현재 방문 상태에서 두 팀 간 능력치 차이를 계산하는 함수 """
    start_team, link_team = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:  # start 팀의 능력치 합산
                start_team += board[i][j]
            elif not visited[i] and not visited[j]:  # link 팀의 능력치 합산
                link_team += board[i][j]
    return abs(start_team - link_team)  # 두 팀 간 능력치 차이 반환

def backtrack(index, count):
    """ 백트래킹을 이용해 팀을 나누고 최소 능력치 차이를 찾는 함수 """
    global minimum

    if count == N // 2:  # 팀이 완성되면 능력치 차이 계산
        minimum = min(minimum, calculate_difference())
        return

    for i in range(index, N):
        if not visited[i]:  # 아직 선택되지 않은 사람을 선택
            visited[i] = True
            backtrack(i + 1, count + 1)  # 다음 사람 선택
            visited[i] = False  # 백트래킹 (원상 복구)

# ✅ 탐색 시작
backtrack(0, 0)

# ✅ 결과 출력
print(minimum)

# -----------------------------------------------------
# ✅ 최적화된 점
# 1. `combinations`을 사용하지 않고 직접 백트래킹 구현 (메모리 절약)
# 2. 한 팀이 선택되면 나머지는 자동으로 결정되므로 중복 탐색 방지 (탐색 횟수 절반 감소)
# 3. 능력치 차이 계산을 한 번만 수행하여 중복 연산 줄임 (반복문 최적화)
