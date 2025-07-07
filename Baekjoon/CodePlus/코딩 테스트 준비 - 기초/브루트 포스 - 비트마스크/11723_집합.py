# 백준 11723번: 집합
# 문제 설명:
# 공집합에서 시작하여 특정 연산을 수행하는 문제.
# - 6가지 연산 (add, remove, check, toggle, all, empty)이 주어짐.
# - 비트마스크를 사용하여 빠르게 연산을 처리해야 함.

# 입력 형식:
# - 첫 번째 줄에 연산 개수 M이 주어진다. (1 ≤ M ≤ 3,000,000)
# - 이후 M개의 연산이 한 줄씩 주어진다.

# 출력 형식:
# - "check x" 연산이 주어질 때마다 1 또는 0을 출력한다.

# 예제 입력 1:
# 26
# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 2
# toggle 3
# check 3
# check 1
# toggle 3
# check 3
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# check 2
# 예제 출력 1:
# 1
# 1
# 0
# 0
# 1
# 1
# 0
# 1
# 1
# 0
# 1
# 0

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 연산 개수 입력
M = int(sys.stdin.readline())

# ✅ 비트마스크를 사용하여 집합을 저장할 변수
S = 0  

# ✅ 결과를 한 번에 출력하기 위한 리스트
output = []

# ✅ 연산 처리
for _ in range(M):
    command = sys.stdin.readline().strip().split()  # ✅ 공백으로 분리하여 명령어 읽기
    
    if len(command) == 1:  # ✅ "all" 또는 "empty" 연산 처리
        operation = command[0]
    else:  # ✅ "add x", "remove x", "check x", "toggle x" 연산 처리
        operation, num = command[0], int(command[1])

    if operation == "add":  # ✅ x 추가
        S |= (1 << num)
    elif operation == "remove":  # ✅ x 제거
        S &= ~(1 << num)
    elif operation == "check":  # ✅ x 포함 여부 확인 (1 또는 0 출력)
        check = (S & (1 << num))
        print(1 if check else 0)
        # output.append("1\n" if (S & (1 << num)) else "0\n") # ✅ 여기서 입력만 받고 출력을 나중에 하기
    elif operation == "toggle":  # ✅ x 존재 여부 반전
        S ^= (1 << num)
    elif operation == "all":  # ✅ 1~20 전체 선택
        S = (1 << 21) - 1
    elif operation == "empty":  # ✅ 모든 원소 제거
        S = 0

# ✅ 한 번에 출력하여 시간 단축
# sys.stdout.write("".join(output))  

# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `"all"` 연산에서 `1 << 20`을 사용해야 했음
#    - 기존 코드: `S = (1 << 21) - 1`
#    - ❌ 문제점: 21번째 비트까지 포함됨.
#    - ✅ 수정: `S = (1 << 21) - 1`으로 유지하여 1~20번 비트 포함.

# 2. ✅ `check` 연산에서 `print()` 사용으로 인한 속도 저하
#    - 기존 코드:
#      ```python
#      print(1 if (S & (1 << num)) else 0)
#      ```
#    - ❌ 문제점: `M = 3,000,000`일 때 `print()`를 사용하면 **매 연산마다 출력이 발생**하여 **속도가 느려짐**.
#    - ✅ 수정: `sys.stdout.write()`를 사용하여 **한 번에 출력하여 실행 속도를 개선함**.
#    - ✅ **출력 최적화 이유:** 
#       - `sys.stdout.write()`는 문자열을 **버퍼에 모아서 한 번에 출력**하므로 성능이 향상됨.
#       - `print()`를 사용하면 매 호출마다 **출력 함수가 실행되므로 성능이 저하됨**.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
