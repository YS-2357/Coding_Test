# 1518_water_bottles.py
# -----------------------------------------------------
# ✅ 제목: Water Bottles (LeetCode 1518)
# ✅ 문제 설명(요약):
# - numBottles개의 물병이 있다.
# - 빈 병 numExchange개를 가져가면 새 물병 1개와 교환할 수 있다.
# - 최종적으로 마실 수 있는 물병 수의 총합을 구하라.
#
# ✅ 입력 형식(요지):
# - numBottles: int (초기 물병 수)
# - numExchange: int (교환에 필요한 빈 병 수)
#
# ✅ 규칙 요약:
# 1) 초기 물병은 모두 마신다.
# 2) 빈 병을 모아 numExchange개가 되면 1개 새 물병으로 교환.
# 3) 새 물병도 마신 후 빈 병에 합산 → 반복.
# 4) 더 이상 교환 불가할 때 종료.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        answer = numBottles
        a, b = divmod(numBottles, numExchange)
        while a > 0:
            # print(a, b, answer)
            answer += a
            now = a + b
            a, b = divmod(now, numExchange)
        return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 시뮬레이션을 통해 정답이 정확히 나옴.
#
# 🔧 오답 이유 및 실수(있다면):
# - 없음. while 루프 조건과 빈 병 업데이트가 올바르게 구현됨.
#
# 📚 사용된 알고리즘 개념:
# - 단순 시뮬레이션
# - 매번 교환 가능한 물병 수(a)와 나머지 빈 병 수(b)를 divmod로 갱신
# - 시간복잡도: O(log_{numExchange}(numBottles))
# - 공간복잡도: O(1)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이:
# - 수학적 공식: 총합 = numBottles + (numBottles - 1) // (numExchange - 1)
#   단, numExchange > 1일 때만 적용 가능.
