# 3562_maximum_profit_from_trading_stocks_with_discounts.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
#
# ✅ 문제 설명(요약):
#   - 각 직원 i는 주식 1개를 살 수 있고, 현재 가격(present[i])과 미래 가치(future[i])가 주어진다.
#   - 예산(budget) 내에서 일부 주식을 구매하여 총 이익(미래 가치 - 구매 비용)의 최대값을 구한다.
#   - 계층(hierarchy)은 트리/유향 구조로 주어지며, 특정 조건에서 자식에게 할인(has_discount)이 적용될 수 있다.
#   - 노드별로 "구매/스킵"을 선택하고, 자식들의 선택을 예산 제한 하에 조합하여 최적 이익을 계산한다.
#
# ✅ 입력 형식(요지):
#   - n: 직원 수
#   - present: 각 직원의 현재 주식 가격
#   - future: 각 직원의 미래 주식 가치
#   - hierarchy: [u, v] 리스트(1-indexed)로 u가 v의 상위(부모) 관계를 의미
#   - budget: 총 구매 예산 상한
#
# ✅ 규칙 요약:
#   - 각 노드(직원)에서 주식을 "구매"하면 비용을 지출하고 이익을 얻는다.
#   - has_discount가 True면 present[i]가 절반 비용(present[i]//2)로 적용된다.
#   - 부모의 선택 등에 따라 자식에게 할인 상태(True/False)가 전달될 수 있다.
#   - 전체 구조는 트리 DP(서브트리 결합) + 배낭(예산) 형태로 합성된다.
#
# -----------------------------------------------------
# ✅ 정답 코드(제공된 풀이; 코드 수정 금지)
#   - 사용자가 “나의 풀이 아님”을 명시했으나, 3단계 규칙에 따라
#     아래 코드는 제공된 원문을 그대로 두고 주석으로만 설명한다.

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj_list = defaultdict(list)  # 부모 -> 자식 인접 리스트
        for h in hierarchy:
            adj_list[h[0] - 1].append(h[1] - 1)  # 입력은 1-indexed이므로 0-indexed로 변환
        
        @lru_cache(None)
        def dfs(employee, has_discount):
            # employee 노드에서 시작해 서브트리 내에서 가능한 (spent -> profit) 최적값 맵을 반환
            # has_discount가 True이면 현재 노드 구매 비용을 절반으로 적용
            cost = present[employee] // 2 if has_discount else present[employee]  # 현재 노드 구매 비용
            profit = future[employee] - cost  # 현재 노드 1개를 구매했을 때의 순이익
            
            # buy_current: 현재 노드를 "구매"하는 경우의 (지출 -> 이익) 맵
            # - cost <= budget일 때만 구매 가능
            buy_current = {cost: profit} if cost <= budget else {}
            # skip_current: 현재 노드를 "구매하지 않음"의 (지출 -> 이익) 맵 (항상 0:0으로 시작)
            skip_current = {0: 0}
            
            # 자식 서브트리들을 하나씩 결합(배낭식 컨볼루션)하여 경우의 수를 확장
            for child in adj_list[employee]:
                # 현재 노드를 구매하는 경우: 자식은 할인(True)을 받는 케이스의 dfs 결과를 결합
                child_with_discount = dfs(child, True)  # Do something
                # 현재 노드를 스킵하는 경우: 자식은 할인(False)을 받지 않는 케이스의 dfs 결과를 결합
                child_no_discount = dfs(child, False) # Do nothing
                
                # buy_current(현재 구매) ⊗ child_with_discount(자식 할인) 결합
                new_buy = {}
                for spent, prof in buy_current.items(): # Do something, but the current stock
                    for child_spent, child_prof in child_with_discount.items():
                        total_spent = spent + child_spent  # 합산 지출
                        if total_spent <= budget:          # 예산 이내만 유지
                            total_prof = prof + child_prof # 합산 이익
                            # 동일 지출(total_spent)에 대해 최대 이익을 유지
                            if total_spent not in new_buy or new_buy[total_spent] < total_prof:
                                new_buy[total_spent] = total_prof
                buy_current = new_buy # This is mandatory because you need to check 
                                      # all possible combinations of picking children results. 
                                      # For example if the given graph is 1 -> 2, and 1 -> 3, 
                                      # it might be correct to either pick the path from 1 to 2, 
                                      # the path 1 to 3, or both paths if there is still budget left. 
                                      # Same goes for a skipping action.
                
                # skip_current(현재 스킵) ⊗ child_no_discount(자식 할인 없음) 결합
                new_skip = {}
                for spent, prof in skip_current.items(): # Do nothing, skip the current stock
                    for child_spent, child_prof in child_no_discount.items():
                        total_spent = spent + child_spent  # 합산 지출
                        if total_spent <= budget:          # 예산 이내만 유지
                            total_prof = prof + child_prof # 합산 이익
                            # 동일 지출(total_spent)에 대해 최대 이익을 유지
                            if total_spent not in new_skip or new_skip[total_spent] < total_prof:
                                new_skip[total_spent] = total_prof
                skip_current = new_skip
            
            # 현재 노드에서의 최종 결과: "구매"와 "스킵" 두 맵을 합쳐 지출별 최대 이익을 유지
            result = {} # Merge the results of doing something and doing nothing at node employee
            for spent, prof in buy_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            for spent, prof in skip_current.items():
                if spent not in result or result[spent] < prof:
                    result[spent] = prof
            
            return result
        
        # 루트(0번 직원)에서 시작, 루트는 할인 없이(False) 시작
        result = dfs(0, False)
        # 가능한 지출들 중 최대 이익을 반환 (없으면 0)
        return max(result.values()) if result else 0

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - (사용자 풀이 아님) 트리 DP + 예산(배낭) 결합으로 서브트리 조합을 모두 탐색하는 형태.
#   - 각 노드에서 "구매/스킵" 두 상태를 만들고, 자식 결과를 지출 합산으로 결합한다.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념:
#       - 트리 DP: 서브트리 단위로 최적해를 계산한 뒤 부모에서 결합
#       - Knapsack-style merge: (spent -> profit) 맵의 컨볼루션 방식 결합
#       - Memoization(lru_cache): (employee, has_discount) 상태 캐싱으로 중복 계산 절감
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도(개략):
#       - 노드별로 (spent -> profit) 맵을 자식들과 결합하며,
#         맵 크기를 B(=budget) 수준으로 보면 결합은 최악 O(B^2)까지 커질 수 있음.
#       - 트리 전체에서 자식 결합이 누적되므로, 최악은 대략 O(n * B^2) 급으로 커질 수 있음(입력 제약에 따라 달라짐).
#   - 공간 복잡도(개략):
#       - 상태별 맵 저장: (node, discount)별로 O(B) 수준 가능 → 대략 O(n * B)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 맵을 "지출별 최대 이익"으로 유지하면서,
#     불필요한 지출 상태(지배(dominated)되는 상태)를 가지치기하면 실전 성능을 개선할 수 있음.
#   - 예산이 큰 경우, 리스트 DP(길이 budget+1)로 전환해 결합을 최적화하는 변형도 고려 가능.

