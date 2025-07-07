# 백준 14889번: 스타트와 링크 (비트마스크 풀이)
# 문제 설명:
# N명의 사람을 두 팀으로 나누어 팀 능력치 차이를 최소화하는 문제.
# - 각 사람의 능력치는 S[i][j] 형태로 주어지며, 같은 팀일 때 능력치 합산.
# - 정확히 N/2명의 선수를 두 팀으로 나눠야 한다.
# - 모든 가능한 팀 조합을 탐색하여 능력치 차이가 최소가 되는 값을 출력한다.
# - 비트마스크를 활용하여 팀을 나누고, 모든 조합을 탐색하여 최솟값을 찾는다.

# 입력 형식:
# - 첫 번째 줄에 정수 N(4 ≤ N ≤ 20)이 주어진다. (N은 짝수)
# - 이후 N개의 줄에 능력치 정보 S[i][j]가 주어진다.

# 출력 형식:
# - 두 팀의 능력치 차이의 최솟값을 출력한다.

# 예제 입력 1:
# 4
# 0 1 2 3
# 4 0 5 6
# 7 1 0 2
# 3 4 5 0
# 예제 출력 1:
# 0

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N = int(sys.stdin.readline())  # ✅ N명 (짝수)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # ✅ 능력치 행렬 입력
min_diff = float("inf")  # ✅ 최소 차이를 저장할 변수 (무한대로 초기화)

# ✅ 특정 팀의 능력치를 계산하는 함수
def calc_diff(team):
    """
    주어진 팀에서 두 명씩 조합하여 능력치 합을 계산하는 함수
    - 능력치 공식: S[i][j] + S[j][i] (i, j가 같은 팀일 경우)
    - 중복을 피하기 위해 i < j 조건을 사용하여 계산
    """
    score = 0
    for i in range(len(team)):  
        for j in range(i + 1, len(team)):  # ✅ i < j 조건으로 중복 계산 방지
            score += board[team[i]][team[j]] + board[team[j]][team[i]]
    return score

# ✅ 비트마스크를 이용하여 가능한 팀 조합을 탐색
for mask in range(1, (1 << N)):  # ✅ 2^N 개의 조합을 생성 (0부터 X, 공집합 제외)
    if bin(mask).count("1") == N // 2:  # ✅ N/2명이 선택된 경우만 유효한 팀 조합
        team_start = [i for i in range(N) if mask & (1 << i)]  # ✅ 선택된 팀원 리스트
        team_link = [i for i in range(N) if not (mask & (1 << i))]  # ✅ 나머지 팀

        # ✅ 두 팀의 능력치를 계산
        score_start = calc_diff(team_start)
        score_link = calc_diff(team_link)

        # ✅ 최소 차이 갱신
        min_diff = min(min_diff, abs(score_start - score_link))

# ✅ 결과 출력
print(min_diff)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `calc_diff()`에서 team 변수를 전달하지 않음
#    - 기존 코드: `def calc_diff():`
#    - ❌ 문제점: `team` 변수를 함수 내에서 정의하지 않고 사용 → `NameError` 발생 가능
#    - ✅ 수정: `def calc_diff(team):`로 변경하여 `team`을 인자로 받음.

# 2. ✅ `abs()` 함수 사용 오류
#    - 기존 코드: `abs(score_start, score_link)`
#    - ❌ 문제점: `abs()`는 하나의 인자만 받을 수 있음 (`TypeError` 발생)
#    - ✅ 수정: `abs(score_start - score_link)`로 변경하여 정확한 차이 계산.

# 3. ✅ 비트마스크를 활용한 팀 생성 방식 개선
#    - 기존 코드에서 `team_start`와 `team_link`를 직접 나누는 과정이 비효율적이었음.
#    - ✅ 수정: `team_start = [i for i in range(N) if mask & (1 << i)]`
#    - ✅ 수정: `team_link = [i for i in range(N) if not (mask & (1 << i))]`

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
