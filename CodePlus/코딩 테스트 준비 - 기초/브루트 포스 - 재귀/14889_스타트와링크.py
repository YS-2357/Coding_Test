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

# 표준 입력을 사용하기 위한 sys 모듈 임포트
import sys
input = sys.stdin.read

# 입력을 한 번에 읽어오기
data = input().strip().split()

# 주어진 숫자 N
N = int(data[0])

# 능력치 표 초기화
abilities = []
index = 1
for i in range(N):
    row = list(map(int, data[index:index + N]))
    abilities.append(row)
    index += N

# 팀 나누기 백트래킹 함수 정의
def backtrack(start, team):
    # 팀이 절반으로 나누어진 경우
    if len(team) == N // 2:
        other_team = [i for i in range(N) if i not in team]
        team_score = sum(abilities[i][j] for i in team for j in team)
        other_team_score = sum(abilities[i][j] for i in other_team for j in other_team)
        global min_diff
        min_diff = min(min_diff, abs(team_score - other_team_score))
        return
    
    # 가능한 팀 조합을 찾기 위한 백트래킹
    for i in range(start, N):
        if i not in team:
            team.append(i)
            backtrack(i + 1, team)
            team.pop()

# 초기값 설정
min_diff = float('inf')

# 백트래킹 함수 호출
backtrack(0, [])

# 결과 출력
print(min_diff)
