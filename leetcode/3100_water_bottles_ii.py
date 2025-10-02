# 3100_water_bottles_ii.py
# -----------------------------------------------------
# ✅ 제목: Water Bottles II (LeetCode 3100)
# ✅ 문제 설명(요약):
# - 처음에 numBottles개의 물병을 갖고 있다.
# - 빈 병을 numExchange개 모으면 새 물병 1개와 교환할 수 있다.
# - 단, 교환할 때마다 다음 교환에는 1개 더 많은 빈 병이 필요하다.
# - 최종적으로 마실 수 있는 물병 수의 최대치를 구한다.
#
# ✅ 입력 형식(요지):
# - numBottles: int (초기 물병 수)
# - numExchange: int (첫 교환 시 필요한 빈 병 수)
#
# ✅ 규칙 요약:
# 1) 초기 병은 모두 마실 수 있다.
# 2) 교환할 때마다 필요한 빈 병 수가 1씩 증가한다.
# 3) 더 이상 교환할 수 없을 때 종료한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        answer = 0
        while numBottles > 0:
            if numBottles >= numExchange:
                numBottles -= numExchange - 1
                answer += numExchange
                numExchange += 1
            else:
                answer += numBottles
                numBottles = 0
        return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 제출 코드에서 답은 맞게 나온다.
#
# 🔧 오답 이유 및 실수(있다면):
# - 로직상 빈 병을 줄였다가 다시 더하는 과정(`numBottles -= numExchange - 1`)으로
#   상태를 유지. 동작은 맞지만 직관적이지 않고 경계 조건에서 헷갈릴 수 있음.
# - 더 명확하게는 "빈병 개수"와 "필요 교환량"을 별도 변수로 두는 방식이 직관적이다.
#
# 📚 사용된 알고리즘 개념:
# - 단순 시뮬레이션
# - 매 교환마다 필요 교환량 증가
# - 시간복잡도: O(교환 횟수), 공간복잡도: O(1)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이:
# - 등차수열 합을 이용해 한 번에 여러 번 교환 가능한 횟수 t를 계산해 갱신할 수 있다.
#   이 경우 시간복잡도를 O(log n) 수준으로 줄일 수 있다.
