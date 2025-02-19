# 백준 1309번: 동물원 (다이나믹 프로그래밍 - DP)
# -----------------------------------------------------
# ✅ 문제 설명:
# - 2×N 크기의 동물원 우리에 사자를 배치하는 방법의 수를 구하는 문제.
# - 조건: 사자는 서로 가로로 인접하지 않도록 배치해야 함.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 정수 N (1 ≤ N ≤ 100,000)이 주어진다.
#
# ✅ 출력 형식:
# - 가능한 사자 배치 방법의 수를 9901로 나눈 나머지를 출력한다.
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   4
#
# 🔹 예제 출력 1:
#   41
# -----------------------------------------------------

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 동물원 우리의 세로 크기 입력
MOD = 9901  # 문제에서 주어진 MOD 값

# ✅ DP 테이블 초기화
dp = [[0] * 3 for _ in range(N)]  # dp[i][0]: i번째 줄에 사자를 배치하지 않는 경우
                                  # dp[i][1]: i번째 줄에 왼쪽 칸에 사자를 배치하는 경우
                                  # dp[i][2]: i번째 줄에 오른쪽 칸에 사자를 배치하는 경우

# ✅ 첫 번째 줄 초기값 설정
dp[0][0] = 1  # 사자를 배치하지 않는 경우
dp[0][1] = 1  # 왼쪽 칸에 사자를 배치하는 경우
dp[0][2] = 1  # 오른쪽 칸에 사자를 배치하는 경우

# ✅ DP 테이블 채우기 (Bottom-Up 방식)
for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD  # 사자를 배치하지 않는 경우
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD  # 왼쪽 칸에 사자를 배치하는 경우
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD  # 오른쪽 칸에 사자를 배치하는 경우

# ✅ 정답 출력 (마지막 줄의 모든 배치 경우의 합)
print(sum(dp[N-1]) % MOD)

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `print(sum(dp[N-1]))` → `print(sum(dp[N-1]) % MOD)`로 수정 (MOD 연산 적용).
# 2. ✅ DP 배열에서 각 줄의 사자 배치 경우를 개별적으로 저장하도록 유지.
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
