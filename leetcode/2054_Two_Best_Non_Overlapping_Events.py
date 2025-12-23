# 2054_Two_Best_Non_Overlapping_Events.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2054. Two Best Non-Overlapping Events
# ✅ 문제 설명(요약):
#   - events = [start, end, value]가 주어질 때, 서로 겹치지 않는(시간이 겹치지 않는) 이벤트를 최대 2개까지 선택한다.
#   - 두 이벤트는 time overlap이 없어야 하며, 보통 "다음 이벤트 start > 이전 이벤트 end" 조건을 사용한다.
#   - 선택한 이벤트 value 합의 최댓값을 반환한다.
#
# ✅ 입력 형식(요지):
#   - events: List[List[int]], 각 원소는 [start, end, value]
#
# ✅ 규칙 요약:
#   - 최대 2개 선택 가능.
#   - 겹치지 않음의 기준: 다음 이벤트의 시작 시간이 이전 이벤트의 종료 시간보다 엄격히 커야 함(start > end).
#   - 목표: value 합 최대화.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - 주의: 아래 코드는 "사용자가 작성한 풀이가 아니라" 참고/차용한 풀이로 표시한다.
#   - 이 단계에서는 코드 내용을 변경하지 않고, 각 줄마다 설명 주석만 추가한다.

class Solution:
    def maxTwoEvents(self, events):
        events.sort()                                      # (start, end, value) 기준으로 기본 정렬: start 우선, 동률이면 end/value 순
        dp = [[-1] * 3 for _ in range(len(events))]        # dp[idx][cnt]: idx부터 탐색, 이미 cnt개 선택했을 때의 최대 합(메모이제이션)
        return self.find_events(events, 0, 0, dp)          # 0번 인덱스부터, 0개 선택 상태로 시작

    def find_events(self, events, idx, cnt, dp):
        if cnt == 2 or idx >= len(events):                 # 2개를 이미 골랐거나, 끝까지 탐색했으면 더 이상 얻을 가치 없음
            return 0

        if dp[idx][cnt] == -1:                             # 아직 계산하지 않은 상태라면 계산 수행
            end = events[idx][1]                           # 현재 이벤트의 종료 시간
            lo, hi = idx + 1, len(events) - 1              # 다음 후보 범위: idx+1 ~ 마지막

            # 이진 탐색: start > end인 "다음 이벤트"의 시작 인덱스 후보를 찾으려는 의도
            # - 목표는 lower_bound(start > end)에 해당하는 위치를 찾는 것
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)                # 중간 인덱스(오른쪽 편향 아님)
                if events[mid][0] > end:                   # mid의 시작이 end보다 크면, 더 왼쪽에도 조건 만족이 있을 수 있어 hi를 줄임
                    hi = mid
                else:                                      # start <= end면 겹치므로, 더 오른쪽으로 이동
                    lo = mid + 1

            # include: 현재 idx 이벤트를 선택하는 경우의 가치
            # - 다음으로는 (겹치지 않는) start > end인 이벤트부터 재귀 탐색
            # - 조건을 만족하지 못하면(또는 범위를 벗어나면) 추가 이득은 0
            include = events[idx][2] + (
                self.find_events(events, lo, cnt + 1, dp)
                if lo < len(events) and events[lo][0] > end
                else 0
            )

            # exclude: 현재 idx 이벤트를 건너뛰고 다음 idx+1로 진행
            exclude = self.find_events(events, idx + 1, cnt, dp)

            dp[idx][cnt] = max(include, exclude)           # 선택/비선택 중 최댓값 저장

        return dp[idx][cnt]                                # 메모된 결과 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 본 코드는 "사용자 본인 풀이 아님(차용/참고 풀이)".
#   - 재귀 + 메모이제이션 + 이진 탐색으로 최대 2개 이벤트 선택을 계산한다.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용한 핵심 개념:
#     - 정렬: start 기준으로 정렬하여, 다음 이벤트 후보를 이진 탐색으로 찾을 수 있게 함
#     - DP(Top-Down Memoization):
#       - 상태: (idx, cnt) = 현재 인덱스 idx부터 보며 이미 cnt개 선택한 상태
#       - 전이: 현재 이벤트를 선택(include)하거나 건너뜀(exclude)
#     - 이진 탐색:
#       - 현재 이벤트 종료 end 이후 시작(start > end)하는 다음 이벤트 인덱스를 찾음
#   - 주의(잠재 리스크를 “주석으로만” 명시):
#     - 이진 탐색이 "조건을 만족하는 최소 인덱스"를 찾는 의도이지만,
#       구현 형태에 따라 경계 케이스에서 lo가 마지막 인덱스로 멈추고 조건 미만일 수 있어,
#       이후 (events[lo][0] > end)로 한 번 더 검증하는 구조를 사용하고 있다.
#     - 이 문제는 통상적으로 (start, end) 기준 경계가 중요하며, 조건이 start > end임을 확실히 유지해야 한다.
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(N log N)
#     - 정렬 O(N log N)
#     - dp 상태는 (idx: N) * (cnt: 2) 수준이므로 O(N)
#     - 각 상태에서 이진 탐색 O(log N) → 전체 O(N log N)
#   - 공간 복잡도: O(N)
#     - dp 테이블 O(N * 3)
#     - 재귀 호출 스택 O(N) (최악)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 대표 대안: 이벤트를 시작 시간으로 정렬한 뒤,
#     종료 시간 기준으로 "이전 이벤트들 중 최대 value"를 prefix 형태로 관리하며
#     각 이벤트에 대해 "겹치지 않는 최적 1개 + 현재 1개"를 계산하는 스위핑/이진탐색 풀이가 널리 사용된다(코드 X).
