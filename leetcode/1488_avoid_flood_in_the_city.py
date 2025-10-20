# 1488_avoid_flood_in_the_city.py
# -----------------------------------------------------
# ✅ 제목: Avoid Flood in The City (LeetCode 1488)
# ✅ 문제 설명(요약):
# - rains[i]는 i번째 날에 비가 오는 호수 번호이다.
# - rains[i] == 0이면 맑은 날로, 그날은 임의의 호수를 비울 수 있다.
# - 같은 호수에 두 번 비가 오기 전에 반드시 그 사이 맑은 날 중 하나에서 비워야 한다.
# - 불가능하면 []를, 가능하면 일정을 배열로 반환하라.
#   (비 오는 날은 -1, 맑은 날은 비운 호수 번호를 기입)
#
# ✅ 입력 형식(요지):
# - rains: List[int], 0 ≤ rains[i] ≤ 10⁹, 길이 n
#
# ✅ 규칙 요약:
# 1) 같은 호수에 두 번 비가 오면, 두 번째 오기 전 반드시 비워야 함.
# 2) 맑은 날마다 "다음에 비가 가장 빨리 올 호수"를 우선적으로 비운다.
# 3) 불가능한 경우(맑은 날이 부족한 경우)는 즉시 빈 리스트 반환.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지) — 한 줄 주석 포함
import heapq as hq                                                # 최소 힙 사용

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        answer = [-1] * n                                         # 결과 배열 초기화
        full = set()                                              # 현재 물이 찬 호수 집합
        heap = []                                                 # (다음 비 오는 날, 호수) 최소 힙
        next_rain = {}                                            # (미사용) 향후 예측용
        rain_days = {}                                            # 각 호수의 비 오는 날 목록

        for i, lake in enumerate(rains):                          # 1단계: 호수별 비 오는 인덱스 저장
            if lake > 0:
                rain_days.setdefault(lake, []).append(i)

        for i, lake in enumerate(rains):                          # 2단계: 하루씩 순회
            if lake > 0:                                          # 비 오는 날
                if lake in full:                                  # 이미 찬 호수에 또 비 → 불가능
                    return []
                full.add(lake)                                    # 현재 호수에 물이 참
                rain_days[lake].pop(0)                            # 오늘 날짜 소비
                if rain_days[lake]:                               # 다음 비 오는 날이 있다면
                    hq.heappush(heap, (rain_days[lake][0], lake)) # (다음날, 호수)로 힙에 삽입
                answer[i] = -1                                    # 비 오는 날은 -1로 기록
            else:                                                 # 맑은 날
                if heap:                                          # 비워야 할 호수가 있다면
                    _, to_drain = hq.heappop(heap)                # 다음 비가 가장 임박한 호수 선택
                    full.remove(to_drain)                         # 해당 호수 비우기
                    answer[i] = to_drain                          # 결과에 비운 호수 번호 기록
                else:
                    answer[i] = 1                                 # 임의의 호수 비우기(문제 허용)

        return answer                                             # 전체 일정 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 그리디 + 최소 힙 조합으로 정답 통과.
#
# 🔧 오답 이유 및 실수, 사용된 알고리즘 개념:
# - 핵심 개념:
#   * 비 오는 날마다 “다음에 비가 다시 오는 호수”를 힙에 저장.
#   * 맑은 날에는 “가장 빨리 다시 비가 올 호수”를 우선 비운다.
#   * 힙이 비었으면 아무 호수나 비워도 됨.
# - 실수 가능 포인트:
#   1) 비 오는 호수가 이미 full에 있을 때 검사 누락 시 실패.
#   2) rain_days.pop(0)로 날짜를 즉시 제거하지 않으면 다음 비 시점 추적 불가.
#
# 📚 시간·공간 복잡도:
# - 시간복잡도: O(n log n) (힙 연산 포함)
# - 공간복잡도: O(n) (rain_days, heap, full)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 동일 로직을 SortedList 기반으로 구현 가능 (O(log n) bisect).
# - 단, 힙 방식이 더 직관적이며 구현이 간단하다.
