# 2327_number_of_people_aware_of_a_secret.py
# -----------------------------------------------------
# ✅ 제목: Number of People Aware of a Secret
# ✅ 문제 설명(요약):
# - Day1에 1명이 비밀을 앎.
# - 배운 지 delay일째부터 전파 가능, forget일째 되는 날 잊어서 제외.
# - n일째 "여전히 알고 있는" 인원 수(mod 1e9+7)를 구한다.
#
# ✅ 입력 형식(요지):
# - n, delay, forget: int
#
# ✅ 규칙 요약(점화식):
# - dp[i][j]: i일(0-index) 시점에, 배운 지 j+1일째인 사람 수(0 ≤ j < forget)
# - 이동: j>0 → dp[i][j] = dp[i-1][j-1]
# - 신규: dp[i][0] = Σ dp[i-1][j] for j ∈ [delay-1 .. forget-2]  (전파 가능 구간)
# - 정답: Σ dp[n-1][j] for j ∈ [0 .. forget-2]  (forget-1은 오늘 잊음 → 제외)
#
# ✅ 입출력 예시(1개):
# - n=6, delay=2, forget=4 → 정답 1
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * forget for _ in range(n)]     # dp[i][j]: i일 시점, j+1일차 그룹
        dp[0][0] = 1                               # Day1(인덱스0)에 1명이 막 앎

        for i in range(1, n):                      # Day2..Day n
            # 1) 그룹 이동: 어제 j-1일차 → 오늘 j일차
            for j in range(1, forget):
                dp[i][j] = dp[i-1][j-1]

            # 2) 신규 생성: 어제 전파 가능자들의 합이 오늘 0일차로 유입
            for j in range(delay - 1, forget - 1): # [delay-1 .. forget-2]
                dp[i][0] = (dp[i][0] + dp[i-1][j]) % MOD

        # 오늘(n일째) 여전히 기억 중인 사람: j=0..forget-1만 합산
        return sum(dp[n-1][j] for j in range(forget)) % MOD

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 전이/신규 생성 로직은 올바름.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 최종 합산 시 j=forget-1(오늘 잊는 그룹)까지 포함 → 과계산.
#   → j ∈ [0 .. forget-2]까지만 합산하도록 수정.
#
# 📚 사용된/필수 개념(최소):
# - 2차원 DP로 “배운 뒤 경과 일수” 상태 분리
# - 전파 가능 구간: [delay-1 .. forget-2]
# - 시간복잡도: O(n·forget), 공간복잡도: O(n·forget)

# -----------------------------------------------------
# # 다른 풀이
# class Solution:
#     def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
#         aware, spread, total = [0] * n, 0, 1
#         aware[0] = 1

#         for day in range(1, n):
#             if day >= delay:
#                 spread += aware[day - delay]
#             if day >= forget:
#                 forgot = aware[day - forget]
#                 total -= forgot
#                 spread -= forgot
            
#             aware[day] = spread
#             total += spread
        
#         return total % (10 ** 9 + 7)
