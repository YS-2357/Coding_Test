# 42587_프린터.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 인쇄 대기 목록에 있는 문서들마다 중요도(priority)가 있으며,
#   중요도가 높은 문서가 먼저 인쇄됩니다.
# - 내가 요청한 문서(location)가 **몇 번째로 인쇄되는지** 구하는 문제입니다.

# ✅ 입력 형식:
# - priorities: 문서들의 중요도 리스트 (길이 1 이상 100 이하)
# - location: 내가 요청한 문서의 현재 위치 (0 ≤ location < len(priorities))

# ✅ 출력 형식:
# - 해당 문서가 몇 번째로 인쇄되는지를 나타내는 정수 (1-based)

# ✅ 입출력 예제:
# 예제 1:
#   입력: priorities = [2, 1, 3, 2], location = 2
#   출력: 1
# 예제 2:
#   입력: priorities = [1, 1, 9, 1, 1, 1], location = 0
#   출력: 5
# -----------------------------------------------------

from collections import deque

def solution(priorities, location):
    # 인덱스와 함께 큐에 넣음: (문서 번호, 중요도)
    queue = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    count = 0  # 인쇄 순서를 기록할 변수

    while queue:
        idx, priority = queue.popleft()  # 큐의 맨 앞 문서를 꺼냄

        # 남은 문서 중 더 높은 우선순위가 있는지 검사
        if any(priority < other_priority for _, other_priority in queue):
            queue.append((idx, priority))  # 우선순위 낮으면 다시 큐 뒤로
        else:
            count += 1  # 인쇄됨
            if idx == location:
                return count  # 요청한 문서의 인쇄 순서를 반환

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 처음에 `from collection import queue`라고 잘못 입력하여 ImportError 발생
# ❌ `return` 없이 함수 종료됨 (초기 코드에서 while 내부 비워둠)
# ❌ 우선순위 비교를 직접 구현하지 않음

# ✅ GPT가 준 힌트 요약:
# - `from collections import deque` 사용 필요
# - `any(priority < other for _, other in queue)`로 우선순위 비교
# - `enumerate()`를 이용해 문서 인덱스를 함께 관리

# ✅ 사용된 개념 요약:
# - 큐 (deque) 사용: FIFO 구조에 맞게 문서 처리
# - any(): 우선순위 비교를 위한 조건 검색
# - enumerate(): 인덱스와 값을 함께 추적

# -----------------------------------------------------
