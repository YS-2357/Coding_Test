# 42628_이중우선순위큐.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 삽입 연산: "I 숫자" → 숫자를 큐에 삽입
# - 삭제 연산: "D 1"은 최대값 삭제, "D -1"은 최소값 삭제
# - 모든 연산 후 큐에 남아 있는 숫자 중 [최댓값, 최솟값]을 반환
# - 큐가 비었으면 [0, 0] 반환
# - 연산 수는 최대 1,000,000개까지 가능

# ✅ 입력 형식:
# - operations: 문자열 명령어 리스트 (ex: ["I 16", "D 1", ...])

# ✅ 출력 형식:
# - [최댓값, 최솟값] 또는 [0, 0]

# ✅ 입출력 예제:
#   입력: ["I 16", "D 1"]
#   출력: [0, 0]

# -----------------------------------------------------

import heapq as hq  # heap 자료구조를 위한 파이썬 표준 모듈 사용

def solution(operations):
    heap = []  # 파이썬의 heapq는 최소 힙만 지원하므로 min heap으로 초기화

    for op in operations:
        command, value = op.split(' ')  # 명령어와 숫자를 분리 (예: "I 16" → "I", "16")
        value = int(value)  # 문자열을 정수로 변환

        if command == "I":  # 삽입 명령
            hq.heappush(heap, value)  # 최소 힙에 값 삽입 (heap은 자동으로 정렬 유지)
        
        elif command == "D" and heap:  # 삭제 명령이며, 힙이 비어있지 않은 경우만 수행
            if value == 1:
                # 최대값 삭제: heapq는 최대 힙을 지원하지 않기 때문에, 가장 큰 값 직접 찾아 제거
                # 최대값의 인덱스를 찾아 pop으로 제거 (비효율적: O(N))
                heap.pop(heap.index(max(heap)))
            elif value == -1:
                # 최소값 삭제: heap의 루트 원소가 최소값이므로 heappop 사용 (O(log N))
                hq.heappop(heap)

    # 모든 연산이 끝난 후
    if not heap:
        # 힙이 비어있다면 [0, 0] 반환 (문제 조건)
        return [0, 0]
    else:
        # 힙이 남아 있다면, 최대값과 최소값을 각각 구해서 리스트로 반환
        # heapq는 최소 힙만 제공하므로 max는 직접 계산 (O(N))
        return [max(heap), min(heap)]

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 이중 힙 구조를 구현하지 않고 단일 힙만 사용함 → 효율성 낮음
# ❌ 최대값 삭제를 위해 max(heap)를 매번 계산 → O(N)이라 비효율적 (정답은 맞음)
# ❌ "heap.pop(heap.index(max(...)))"은 의도는 맞지만 heapq가 관리하는 정렬 상태를 망가뜨릴 수 있음

# ✅ GPT가 준 힌트 요약:
# - 시간복잡도를 줄이려면 max_heap과 min_heap을 따로 관리해야 함 (이중 힙 구조)
# - 삭제된 값이 두 힙 모두에서 동기화되어야 하므로 유효성 검사도 필요
# - Counter 또는 set 등을 활용해 '정상값만' 유지하면 완전한 해결 가능

# ✅ 사용된 개념 요약:
# - heapq: 최소 힙 (우선순위 큐) 구조 사용
# - 문자열 파싱: split()과 int()로 명령어 구문 분석
# - 리스트 조작: max(), pop(index) 등으로 직접 삭제 구현
# - 조건 분기: heap이 비었는지 여부, 명령어 종류 확인

# -----------------------------------------------------

# import heapq
# from collections import defaultdict

# def solution(operations):
#     min_heap = []
#     max_heap = []
#     entry_count = defaultdict(int)  # 각 숫자의 유효 개수

#     for op in operations:
#         command, value = op.split()
#         value = int(value)

#         if command == 'I':
#             # 삽입: 두 힙에 push, 카운트 증가
#             heapq.heappush(min_heap, value)
#             heapq.heappush(max_heap, -value)
#             entry_count[value] += 1

#         elif command == 'D':
#             # 삭제인데 아무것도 없으면 무시
#             if not entry_count:
#                 continue

#             target_heap = max_heap if value == 1 else min_heap

#             # 유효한 값이 나올 때까지 pop
#             while target_heap:
#                 num = -heapq.heappop(max_heap) if value == 1 else heapq.heappop(min_heap)
#                 if entry_count[num] > 0:
#                     entry_count[num] -= 1
#                     if entry_count[num] == 0:
#                         del entry_count[num]
#                     break

#     # 마지막 결과를 만들기 위해 힙에서 유효한 값 찾아야 함
#     min_val = max_val = None

#     while min_heap:
#         num = heapq.heappop(min_heap)
#         if entry_count[num] > 0:
#             min_val = num
#             break

#     while max_heap:
#         num = -heapq.heappop(max_heap)
#         if entry_count[num] > 0:
#             max_val = num
#             break

#     if min_val is None or max_val is None:
#         return [0, 0]
#     else:
#         return [max_val, min_val]
