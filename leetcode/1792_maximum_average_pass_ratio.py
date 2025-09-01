# 1792_maximum_average_pass_ratio.py
# -----------------------------------------------------
# ✅ 제목: Maximum Average Pass Ratio
# ✅ 문제 설명(요약):
# - 각 반에 대해 합격자 수 a, 총 학생 수 b가 주어진다.
# - 추가 학생 extraStudents명을 임의로 배치할 수 있다.
# - 학생을 배치하면 (a+1)/(b+1)로 갱신된다(즉, 합격자로 추가됨).
# - 전체 평균 합격률(모든 반의 합격률 평균)을 최대로 하는 값을 반환한다.
#
# ✅ 입력 형식(요지):
# - classes: List[List[int]] (각 원소는 [a, b], 1 ≤ a ≤ b)
# - extraStudents: int (추가 학생 수)
#
# ✅ 규칙 요약:
# 1) 학생은 한 번에 1명씩, 반드시 어떤 반에 배정.
# 2) 각 배정에서 “이득”이 가장 큰 반에 우선 배치해야 평균이 최대.
#    - 이득 Δ = (a+1)/(b+1) - a/b = (b-a) / (b*(b+1))
#
# ✅ 입출력 예시(1개):
# - classes = [[1,2],[3,5],[2,2]], extraStudents=2
#   → 최적 배치 후 평균 합격률 ≈ 0.78333
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)

        def gain(a, b):
            # (a+1)/(b+1) - a/b = (b - a) / (b*(b+1))
            return (b - a) / (b * (b + 1))

        heap = []
        for a, b in classes:
            heapq.heappush(heap, (-gain(a, b), a, b))        # 최대 이득 기준 힙(음수로 저장)

        for _ in range(extraStudents):                      # k명 배치
            g, a, b = heapq.heappop(heap)                   # 가장 이득 큰 반 꺼냄
            a, b = a + 1, b + 1                             # 학생 1명 배정
            heapq.heappush(heap, (-gain(a, b), a, b))       # 갱신 후 다시 푸시

        total = 0.0
        while heap:                                         # 최종 합격률 계산
            _, a, b = heapq.heappop(heap)
            total += a / b

        answer = total / n                                  # 전체 평균 반환
        return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 힙 기반 탐욕적 배치로 문제 조건 충족, 정답 도출 성공.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (없음) 다만 gain 계산식 오타 주의 필요. (b-a)/(b*(b+1))가 정확)
# - float 오차는 파이썬 double precision으로 충분.
#
# 📚 사용된/필수 개념(최소):
# - 탐욕법(Greedy): 매번 평균 증가량 최대 반에 배정
# - 최대 힙(heapq에 음수 push)
# - 시간복잡도: O((n+k) log n), 공간복잡도: O(n)
