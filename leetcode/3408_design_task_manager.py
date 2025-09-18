# 3408_design_task_manager.py
# -----------------------------------------------------
# ✅ 제목: Design Task Manager (LeetCode 3408)
# ✅ 문제 설명(요약):
# - 작업(tasks)은 (userId, taskId, priority)로 정의.
# - 연산:
#   add(u, t, p): 작업 추가
#   edit(t, p'): 작업 우선순위 변경
#   rmv(t): 작업 제거
#   execTop(): 전 시스템에서 우선순위 최댓값, 동률이면 taskId 최댓값인 작업을 실행하고 제거. 해당 userId 반환. 없으면 -1
#
# ✅ 입력 형식(요지):
# - 생성자: TaskManager(tasks: List[List[int]])
# - 메서드: add, edit, rmv, execTop
#
# ✅ 규칙 요약:
# 1) taskId는 전역 유일
# 2) execTop은 (priority 내림차순, 동률 시 taskId 내림차순)
# 3) 효율을 위해 힙 + 지연 삭제 사용 가능
#
# ✅ 입출력 예시(1개):
# - 초기: tasks = [[1,101,8],[2,102,20],[3,103,5]]
# - add(4,104,5)
# - edit(102, 9)
# - execTop() → 2 (priority 20의 userId)
# - rmv(101)
# - add(50,101,8)
# - execTop() → 50  (동일 taskId 재등록, 최신 owner=50)
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
import heapq as hq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []                                # (-priority, -taskId, userId) 저장
        self.taskPriority = {}                        # taskId → 최신 priority
        self.taskOwner = {}                           # taskId → 최신 userId

        for userId, taskId, priority in tasks:
            hq.heappush(self.heap, (-priority, -taskId, userId))
            self.taskPriority[taskId] = priority
            self.taskOwner[taskId] = userId

    def add(self, userId: int, taskId: int, priority: int) -> None:
        hq.heappush(self.heap, (-priority, -taskId, userId))   # 새 상태 push
        self.taskPriority[taskId] = priority                   # 최신 상태 기록
        self.taskOwner[taskId] = userId 

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.taskPriority: return            # 존재 가정이지만 방어적으로
        self.taskPriority[taskId] = newPriority               # 최신 priority 갱신
        userId = self.taskOwner[taskId]                       # 기존 owner 유지
        hq.heappush(self.heap, (-newPriority, -taskId, userId))  # 지연 삭제 방식

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskPriority:
            del self.taskPriority[taskId]                     # 최신 상태 무효화
        if taskId in self.taskOwner:
            del self.taskOwner[taskId]                        # owner도 무효화

    def execTop(self) -> int:
        while self.heap:
            negp, negTid, uid = hq.heappop(self.heap)
            tid, p = -negTid, -negp
            # 최신 priority와 owner가 모두 일치해야 유효(지연 삭제의 검증 단계)
            if tid in self.taskPriority and self.taskPriority[tid] == p \
            and self.taskOwner.get(tid) == uid:
                del self.taskPriority[tid]                    # 실행과 동시에 제거
                del self.taskOwner[tid]
                return uid
        return -1                                              # 작업이 없으면 -1

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 힙에서 오래된 항목을 execTop 시점에 제거하는 지연 삭제로 기대 동작 충족.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - edit에서 힙을 순회하며 임의 삭제 시도 → 불필요하며 O(n). 지연 삭제로 단순화.
# - rmv 후 동일 taskId 재등록 시, 예전 owner가 반환되는 버그 → execTop 검증에 owner까지 일치 확인 추가.
#
# 📚 사용된/필수 개념(최소):
# - 최대 힙(음수 키)로 (priority↓, taskId↓) 정렬
# - 해시맵 두 개로 최신 상태 추적(taskPriority, taskOwner)
# - 지연 삭제(lazy deletion)로 임의 원소 삭제 없이 정합성 보장
# - 시간복잡도: add/edit/execTop 평균 O(log n), rmv O(1) + 청소는 execTop에서 처리
