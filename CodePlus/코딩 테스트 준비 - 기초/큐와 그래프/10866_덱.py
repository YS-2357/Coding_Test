# 백준 10866번: 덱 (자료구조 - Double-ended Queue)
# -----------------------------------------------------
# ✅ 문제 설명:
# - 덱(Deque)은 앞과 뒤에서 삽입 및 삭제가 가능한 자료구조이다.
# - 주어진 명령어를 처리하여 덱을 구현하는 문제이다.
#
# ✅ 입력 형식:
# - 첫 번째 줄에 정수 N (1 ≤ N ≤ 10,000)이 주어진다.
# - 이후 N개의 줄에 명령어가 주어진다.
#
# ✅ 출력 형식:
# - 각 명령어에 대한 결과를 출력한다.
#
# ✅ 입출력 예제:
# 🔹 예제 입력:
#   15
#   push_back 1
#   push_front 2
#   front
#   back
#   size
#   empty
#   pop_front
#   pop_back
#   pop_front
#   size
#   empty
#   pop_back
#   push_front 3
#   empty
#   front
# 🔹 예제 출력:
#   2
#   1
#   2
#   0
#   2
#   1
#   -1
#   0
#   1
#   -1
#   0
#   3
# -----------------------------------------------------

import sys
from collections import deque

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 명령어 개수 입력
queue = deque()  # 덱 생성

# ✅ 명령어 처리
for _ in range(N):
    command = sys.stdin.readline().strip().split()

    if command[0] == "push_front":
        queue.appendleft(int(command[1]))  # 덱 앞에 값 추가
    elif command[0] == "push_back":
        queue.append(int(command[1]))  # 덱 뒤에 값 추가
    elif command[0] == "pop_front":
        print(queue.popleft() if queue else -1)  # 덱 앞에서 값 제거
    elif command[0] == "pop_back":
        print(queue.pop() if queue else -1)  # 덱 뒤에서 값 제거
    elif command[0] == "size":
        print(len(queue))  # 덱 크기 출력
    elif command[0] == "empty":
        print(1 if not queue else 0)  # 덱이 비어있는지 확인
    elif command[0] == "front":
        print(queue[0] if queue else -1)  # 덱의 앞 원소 출력
    elif command[0] == "back":
        print(queue[-1] if queue else -1)  # 덱의 뒤 원소 출력

# -----------------------------------------------------
# ✅ 백준 제출용 최종 정답 코드
# - `sys.stdin.readline()`을 활용하여 빠르게 입력 처리
# - `collections.deque`를 사용하여 O(1) 연산을 유지
# -----------------------------------------------------
