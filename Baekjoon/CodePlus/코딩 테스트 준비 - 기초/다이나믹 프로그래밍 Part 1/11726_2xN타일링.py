# 백준 11726번: 2×N 타일링 (다이나믹 프로그래밍 - Bottom-Up 방식)
# 문제 설명:
# 2×N 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 문제.
# - 가능한 모든 타일 배치 방법을 구해야 하며, 경우의 수가 매우 커질 수 있음.
# - 결과를 10,007로 나눈 나머지를 출력해야 함.

# 입력 형식:
# - 첫 번째 줄에 정수 N (1 ≤ N ≤ 1,000)이 주어진다.

# 출력 형식:
# - 2×N 크기의 직사각형을 타일로 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1:
# 2
# 예제 출력 1:
# 2  (||, =)

import sys  # ✅ 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N = int(sys.stdin.readline().strip())  # ✅ 정수 N 입력 받기 (1 ≤ N ≤ 1,000)

# ✅ DP 테이블 초기화 (0부터 N까지)
dp = [0] * (N + 1)  # ✅ dp[i] = 2×i 크기의 직사각형을 타일로 채우는 방법의 수

# ✅ 기본값 설정 (점화식 기반)
dp[0] = 1  # ✅ 2×0 크기의 직사각형은 아무것도 채우지 않는 1가지 방법 존재
dp[1] = 1  # ✅ 2×1 크기의 직사각형은 1×2 타일 하나만 사용 가능

# ✅ DP 테이블 채우기 (Bottom-Up 방식)
for i in range(2, N + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007  # ✅ 점화식: dp[i] = dp[i-1] + dp[i-2] (나머지 연산 포함)

# ✅ 결과 출력
print(dp[N])  # ✅ N을 2×N 타일링할 수 있는 방법의 개수 출력


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ N = 1일 때 IndexError 발생 가능
#    - 기존 코드: `dp[1] = 1, dp[2] = 2`
#    - ❌ 문제점: N=1일 경우, dp[2]가 존재하지 않아 IndexError 발생.
#    - ✅ 해결: dp[0]을 초기화하여 예외 방지.

# 2. ✅ 10007로 나누는 연산을 누락하여 값이 너무 커지는 문제
#    - 기존 코드: `dp[i] = dp[i-1] + dp[i-2]`
#    - ❌ 문제점: 값이 커질 경우 메모리 낭비 및 오버플로우 가능성 존재.
#    - ✅ 해결: `dp[i] = (dp[i-1] + dp[i-2]) % 10007`로 변경.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 

'''
# 잘못 푼 풀이(브루트 포스)
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

money = 0

def maximize_money(count, max_money):
    global money
    
    if count == N:
        money = max(money, max_money)
    
    for i in range(N):
        if count + (i + 1) <= N:
            maximize_money(count + (i + 1), max_money + nums[i])

maximize_money(0, 0)
print(money)
'''
