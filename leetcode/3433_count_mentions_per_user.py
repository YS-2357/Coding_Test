# 3433_count_mentions_per_user.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3433 - Count Mentions Per User
# ✅ 문제 설명(요약):
#   - numberOfUsers명의 유저가 있고, events 로그가 주어진다.
#   - 이벤트는 MESSAGE 또는 OFFLINE 이며, 시간(timestamp)이 함께 주어진다.
#   - OFFLINE된 유저는 60초가 지나면 자동으로 ONLINE으로 복귀한다.
#   - MESSAGE는 ALL / HERE / 개별 멘션(idX ...) 형태이며, 각 유저가 멘션된 횟수를 계산한다.
#
# ✅ 입력 형식(요지):
#   - numberOfUsers: 유저 수 n
#   - events: ["TYPE", "time", "payload"] 형태의 문자열 리스트
#     - TYPE: "MESSAGE" 또는 "OFFLINE"
#     - time: 문자열이지만 정수로 해석
#     - payload:
#       - MESSAGE: "ALL" / "HERE" / "id0 id1 ..." (공백 구분)
#       - OFFLINE: "userId" (문자열이지만 정수로 해석)
#
# ✅ 규칙 요약:
#   - 이벤트는 시간 오름차순으로 처리해야 하며, 같은 시간에서는 OFFLINE을 MESSAGE보다 먼저 처리한다.
#   - OFFLINE된 유저는 그 시각부터 60초 후 온라인으로 복귀한다.
#   - MESSAGE:
#       - ALL: 모든 유저가 1회 멘션된 것으로 카운트
#       - HERE: 현재 online인 유저만 1회 멘션된 것으로 카운트
#       - idX ...: 명시된 유저를 1회 멘션된 것으로 카운트
#
# -----------------------------------------------------
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - 아래는 사용자가 제출/채택한 최종 정답 코드이며,
#     이 단계에서는 코드 내용을 변경하지 않고,
#     각 줄마다 설명 주석만 추가한다.

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n = numberOfUsers                           # 유저 수
        priority = {"OFFLINE": 0, "MESSAGE": 1}     # 동일 timestamp에서 OFFLINE을 먼저 처리하기 위한 우선순위
        events.sort(key=lambda x: (int(x[1]), priority[x[0]]))  # (시간, 타입우선순위)로 정렬

        online = set(i for i in range(n))           # 현재 online인 유저 집합 (초기에는 모두 online)
        offline = set()                              # 현재 offline인 유저 집합 (추적용)
        cnt = defaultdict(int)                       # cnt[id] = 해당 유저가 마지막으로 OFFLINE된 시각

        ans = [0] * n                                # 유저별 멘션 카운트 결과 배열

        # 정렬된 이벤트를 순차적으로 처리
        for e in events:
            # 현재 이벤트 시각을 기준으로, 60초 이상 지난 OFFLINE 유저들을 online으로 복귀시키는 로직
            for k, v in cnt.items():                 # k: 유저 id, v: 마지막 OFFLINE 시각
                if int(e[1]) - v >= 60:              # 현재시간 - OFFLINE시각 >= 60 이면 복귀 조건 만족
                    online.add(k)                    # online 집합에 추가 (이미 있어도 set이라 안전)
                    if k in offline:                 # offline 집합에 실제로 있으면
                        offline.remove(k)            # offline 집합에서 제거 (없으면 예외 방지)

            # 이벤트 타입에 따라 처리 분기
            if e[0] == "MESSAGE":
                if e[2] == "ALL":
                    # ALL: 모든 유저가 멘션됨 → ans 전체를 +1
                    ans = [x + 1 for x in ans]
                elif e[2] == "HERE":
                    # HERE: 현재 online인 유저만 멘션됨
                    for id in online:
                        ans[id] += 1
                else:
                    # 개별 멘션: "id0 id1 ..." 형태
                    ids = e[2].split(" ")
                    for id in ids:
                        id = int(id[2:])             # "id" 접두사 제거 후 정수 변환
                        ans[id] += 1                 # 해당 유저 멘션 카운트 +1
            else:
                # OFFLINE 이벤트 처리
                id = int(e[2])                       # OFFLINE 대상 유저 id
                online.remove(id)                    # online 집합에서 제거 (현재 online이라고 가정)
                offline.add(id)                      # offline 집합에 추가
                cnt[id] = int(e[1])                  # 마지막 OFFLINE 시각 기록

        return ans                                   # 최종 유저별 멘션 횟수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정렬 전 입력 순서로 처리하면 시간 역행이 발생해 오답이 나올 수 있음.
#   - (시간, OFFLINE우선) 정렬을 추가하여 이벤트 처리 순서를 맞추는 방향으로 개선.
#   - KeyError(offline.remove) 문제는 존재 여부 체크로 회피.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 핵심 개념:
#       - 시뮬레이션 문제에서 이벤트 로그는 시간 순으로 처리해야 함.
#       - 동일 시간에서는 OFFLINE을 먼저 반영한 후 MESSAGE를 처리해야 HERE가 정확해짐.
#   - 실수/리스크 포인트:
#       - cnt.items()를 매 이벤트마다 전수 순회하므로 성능이 악화될 수 있음 (offline 유저가 많으면 비효율).
#       - 복귀 처리 후에도 cnt에서 해당 유저를 제거하지 않아, 이후 이벤트에서도 같은 유저를 계속 검사함.
#       - online.remove(id)는 id가 이미 online에 없으면 KeyError가 날 수 있는 구조.
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도:
#       - 정렬: O(m log m)  (m = len(events))
#       - 이벤트 처리: 각 이벤트마다 cnt 전수 순회 → 최악 O(m * u) (u = cnt에 남아있는 유저 수, 최대 n)
#       - 전체 최악: O(m log m + m*n)
#   - 공간 복잡도:
#       - online/offline/cnt/ans: O(n)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 복귀 예정 시각을 (time+60, user)로 저장하는 min-heap을 사용하면,
#     매 이벤트마다 모든 offline 유저를 전수 순회하지 않고,
#     현재 시각까지 복귀해야 하는 유저만 while-pop으로 처리 가능해짐.
#   - 또한 복귀 처리 시 cnt에서 제거/상태를 정리하면 불필요한 반복 검사와 예외 가능성을 줄일 수 있음.
