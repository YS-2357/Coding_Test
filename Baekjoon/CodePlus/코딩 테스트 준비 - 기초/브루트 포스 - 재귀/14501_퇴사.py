# 백준 14501번: 퇴사
# 문제 설명:
# N일 동안 상담을 진행하면서 최대한 많은 수익을 얻을 수 있도록 상담 일정을 정하는 문제.
# - 상담을 시작하면 T[i]일 동안 진행되며, P[i]만큼의 수익을 얻는다.
# - 상담이 N+1일을 넘어가면 할 수 없다.
# - 가능한 최대 수익을 구해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 15)
# - 다음 N개의 줄에 T[i]와 P[i]가 주어진다.

# 출력 형식:
# - 퇴사 전까지 얻을 수 있는 최대 수익을 출력한다.

# 예제 입력 1:
# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200
# 예제 출력 1:
# 45

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
T = []
P = []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

max_revenue = 0  # 최대 수익 초기화

def maximize_revenue(day, revenue):
    """ 퇴사 전까지 최대 수익을 구하는 백트래킹 함수 """
    global max_revenue

    if day >= N:  # ✅ 종료 조건
        max_revenue = max(max_revenue, revenue)
        return 

    # ✅ 상담을 선택하는 경우
    if day + T[day] <= N:  # 퇴사 전에 상담이 끝나는 경우만 가능
        maximize_revenue(day + T[day], revenue + P[day])

    # ✅ 상담을 선택하지 않는 경우 (다음 날짜로 이동)
    maximize_revenue(day + 1, revenue)

# ✅ 탐색 시작
maximize_revenue(0, 0)
print(max_revenue)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 함수 호출을 하지 않음
#    - 기존 코드: `maximize_revenue` 변수를 그냥 사용함.
#    - ❌ 문제점: 실행이 되지 않음.
#    - ✅ 수정: `maximize_revenue(0, 0)`을 호출하여 탐색을 시작.

# 2. ✅ 상담을 선택하지 않는 경우 `if` 조건 안에 넣음
#    - 기존 코드: `maximize_revenue(day + 1, revenue)`가 `if` 조건 안에 존재.
#    - ❌ 문제점: 상담을 건너뛰는 경우가 발생하지 않음.
#    - ✅ 수정: `maximize_revenue(day + 1, revenue)`를 `if` 블록 밖으로 이동.

# 3. ✅ 잘못된 종료 조건 (`if day == N:`)
#    - 기존 코드: `if day == N:`
#    - ❌ 문제점: `day > N`이 되는 경우 탐색이 계속 진행됨.
#    - ✅ 수정: `day >= N`으로 조건을 수정해야, **퇴사일을 넘어가면 종료 가능**.

# 4. ✅ `elif day + T[day] > N:` 불필요한 검사
#    - 기존 코드: `elif day + T[day] > N: return`
#    - ❌ 문제점: 이 조건이 필요 없음. 이미 `if day >= N:`에서 탐색 종료가 보장됨.
#    - ✅ 해결: 이 부분을 제거하고, 상담이 가능한 경우만 `maximize_revenue()` 실행.

# 5. ✅ `maximize_revenue(day + T[day], revenue + P[day])` 잘못된 호출
#    - 기존 코드: `maximize(day + T[day], revenue + P[day])`
#    - ❌ 문제점: `maximize`라는 잘못된 함수명을 사용했음. (함수명이 다름)
#    - ✅ 수정: `maximize_revenue(day + T[day], revenue + P[day])`으로 변경.

# -----------------------------------------------------
# 📌 몰랐던 점 (힌트 제공 내용)

# 🔹 `maximize_revenue(0, 0)`을 실행하지 않으면 탐색이 시작되지 않음.
# 🔹 퇴사일 이후에 상담이 진행되지 않도록 `if day >= N:`에서 종료해야 함.
# 🔹 `maximize_revenue(day + 1, revenue)`는 모든 경우에 실행해야 함.
# 🔹 상담을 건너뛰는 경우도 고려해야 한다.
# 🔹 `elif day + T[day] > N:` 조건은 필요 없음.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
