# 백준 15661번: 링크와 스타트
# 문제 설명:
# N명의 사람을 두 팀으로 나눌 때, 두 팀 간 능력치 차이를 최소로 만드는 문제.
# - S[i][j]: i번과 j번 사람이 같은 팀일 때 발생하는 능력치.
# - 두 팀의 능력치 차이의 최솟값을 출력해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (2 ≤ N ≤ 20)
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
    
    if count == N:  # 전체 인원을 한 팀으로 구성하는 경우 제외
        return
    
    if 0 < count < N:  # 한 팀이 최소 1명 이상일 때 능력치 차이 계산
        minimum = min(minimum, calculate_difference())

    for i in range(index, N):  # 팀 구성 탐색
        if not visited[i]:  # 아직 선택되지 않은 사람을 선택
            visited[i] = True
            backtrack(i + 1, count + 1)  # 다음 사람 선택
            visited[i] = False  # 백트래킹 (원상 복구)

# ✅ 탐색 시작
backtrack(0, 0)

# ✅ 결과 출력
print(minimum)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 팀이 완성되었을 때 `return` 문제
#    - 기존 코드: `if 0 < count < N: return`
#    - ❌ 문제점: 팀이 한 번이라도 만들어지면 탐색이 중단됨.
#    - ✅ 수정: `return`을 제거하고 계속 탐색하도록 변경.

# 2. ✅ 모든 경우의 수 탐색 문제
#    - 기존 코드: 조기 종료 조건(`count == N`)이 있어 탐색이 중단됨.
#    - ❌ 문제점: 일부 경우를 탐색하지 않음.
#    - ✅ 수정: `if count == N:`에서는 종료만 하고, 다른 경우도 탐색하도록 변경.

# 3. ✅ `calculate_difference()` 호출 문제
#    - 기존 코드: `if 0 < count < N:` 내에서만 최소값 업데이트.
#    - ❌ 문제점: 모든 경우를 검사하지 않음.
#    - ✅ 해결: `calculate_difference()`를 호출한 후에도 탐색을 계속 진행.

# -----------------------------------------------------
# 📌 몰랐던 점 (힌트 제공 내용)

# 🔹 팀을 자유롭게 나누는 경우에는 **조합(combinations)**보다 **백트래킹이 유용**.
# 🔹 한 팀이 최소 1명 이상이어야 하므로 `count == N`이 되면 탐색 종료해야 함.
# 🔹 `visited` 배열을 이용하면 특정 인원을 쉽게 체크할 수 있음.
# 🔹 `calculate_difference()`를 실행할 때 **중복 계산을 피하기 위해 두 중첩 루프를 활용**.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
