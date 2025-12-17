# 3573_best_time_to_buy_and_sell_stock_v.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3573 - Best Time to Buy and Sell Stock V
#
# ✅ 문제 설명(요약):
#   - 주가 배열 prices와 정수 k가 주어진다.
#   - 최대 k번의 거래(트랜잭션)로 얻을 수 있는 최대 이익을 구한다.
#   - 거래는 매수 후 매도로 종료되며, (문제 정의에 따라) 특정 상태 전이로 최대 이익을 계산한다.
#
# ✅ 입력 형식(요지):
#   - prices: 각 날짜의 주가를 나타내는 정수 배열
#   - k: 허용되는 최대 거래 횟수
#
# ✅ 규칙 요약:
#   - 거래 횟수 제한(k) 하에서, 날짜 순서대로 상태를 갱신하며 최대 이익을 계산한다.
#   - dp[trans]는 특정 거래 횟수(trans)에 대한 여러 상태(0/1/2)를 함께 관리한다.
#
# -----------------------------------------------------
# ✅ 정답 코드(제공된 풀이; 코드 수정 금지)
#   - 사용자가 “나의 풀이 아님”을 명시했으나, 3단계 규칙에 따라
#     아래 코드는 제공된 원문을 그대로 두고 주석으로만 설명한다.

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        first_price = prices[0]  # 0일차 주가 (초기 상태 구성에 사용)

        # dp[trans] = [state0, state1, state2]
        # - state0: 거래 trans번까지 고려했을 때의 "현재 최대 이익" (포지션이 없는 상태로 해석 가능)
        # - state1: 거래 trans번 상태에서의 "매수(롱) 포지션" 관련 최적값 (현금-주식 형태의 보유 상태)
        # - state2: 거래 trans번 상태에서의 "반대 포지션/대체 상태" 관련 최적값 (문제 정의의 상태 전이에 의존)
        #
        # 초기값:
        # - state0 = 0
        # - state1 = -first_price
        # - state2 = first_price
        # 위 초기화는 day=0에서 가능한 상태의 기준값을 세팅하는 역할을 한다.
        dp = [[0, -first_price, first_price] for _ in range(k + 1)]

        n = len(prices)  # 전체 날짜 수
        
        # 1일차부터 마지막 날까지 순회하며 DP 갱신
        for day in range(1, n):
            curr_price = prices[day]  # 현재 날짜의 주가

            # trans를 k -> 1로 역순 갱신:
            # - dp[trans]를 갱신할 때 dp[trans-1]의 "이전 날짜 값"을 안정적으로 참조하기 위함
            for trans in range(k, 0, -1):
                prev_profit = dp[trans - 1][0]  # 바로 이전 거래 횟수 상태의 state0(기준 이익)

                # state0 갱신:
                # - 기존 state0 유지
                # - state1 + curr_price: state1(보유 상태)에서 curr_price로 청산하는 전이
                # - state2 - curr_price: state2 상태에서 curr_price로 전이하는 케이스(문제의 상태 정의에 의존)
                dp[trans][0] = max(
                    dp[trans][0],
                    dp[trans][1] + curr_price,
                    dp[trans][2] - curr_price
                )

                # state1 갱신:
                # - 기존 state1 유지
                # - prev_profit - curr_price: (trans-1)의 이익에서 curr_price로 진입(매수)하는 전이
                dp[trans][1] = max(dp[trans][1], prev_profit - curr_price)

                # state2 갱신:
                # - 기존 state2 유지
                # - prev_profit + curr_price: (trans-1)의 이익에서 curr_price로 진입하는 다른 전이(문제의 상태 정의에 의존)
                dp[trans][2] = max(dp[trans][2], prev_profit + curr_price)
        
        # k번 거래까지 고려했을 때의 최종 최대 이익(state0)을 반환
        return dp[k][0]

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - (사용자 풀이 아님) k차원 거래 제한에서, 날짜를 순회하며 3상태 DP로 최대 이익을 갱신하는 방식.
#   - 거래 횟수를 역순으로 도는 이유는 dp[trans-1]의 값이 같은 day에서 덮어써지는 것을 방지하기 위함.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념:
#       - DP(거래 횟수 제한) + 상태 전이(3개 상태)
#       - In-place 갱신을 위한 trans 역순 루프
#   - 주의 포인트:
#       - 이 풀이의 state2는 일반적인 "k번 거래" 표준 템플릿(hold/cash)과 형태가 다르므로,
#         문제의 정의(추가 제약/대체 거래 모델)에 맞는 상태 의미를 정확히 이해해야 한다.
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(n * k)
#   - 공간 복잡도: O(k)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - k가 매우 큰 경우(예: k >= n/2)에는 무제한 거래 형태로 단순화되는 경우가 흔하므로,
#     해당 케이스를 분기 처리하면 시간을 줄일 수 있다(문제 조건에 따라 적용 여부 결정).
#   - 표준 템플릿(2상태: cash/hold) 또는 2k상태(buy/sell 배열)로도 풀이 가능하나,
#     이 문제의 상태 정의가 추가 규칙을 포함한다면 현재 3상태 구조가 더 직접적일 수 있다.
