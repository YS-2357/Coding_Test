# 백준 15654번: N과 M (5)
# 문제 설명:
# N개의 자연수가 주어지고, 이 중에서 길이가 M인 순열을 출력하는 문제.
# - 같은 숫자는 한 번만 선택할 수 있으며, 순서가 다르면 다른 경우로 취급한다.
# - 입력받은 숫자들을 오름차순 정렬한 후 순열을 생성해야 한다.

# 입력 형식:
# - 첫 번째 줄에 두 정수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# - 두 번째 줄에 N개의 자연수가 주어진다. (서로 다른 정수, 1 ≤ 숫자 ≤ 10,000)

# 출력 형식:
# - 한 줄에 하나씩 길이가 M인 순열을 출력한다.

# 예제 입력 1:
# 3 2
# 4 2 5
# 예제 출력 1:
# 2 4
# 2 5
# 4 2
# 4 5
# 5 2
# 5 4

import sys

# ✅ 입력 처리
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()  # 숫자들을 오름차순으로 정렬

# ✅ 방문 체크 리스트 (사용 여부 확인)
visited = [False] * N

# ✅ 현재 순열을 저장할 리스트
seq = []

# ✅ 백트래킹을 활용한 순열 생성 함수
def backtrack():
    if len(seq) == M:  # 길이가 M이면 출력
        print(*seq)
        return
    
    for i in range(N):  # 주어진 숫자 중에서 선택
        if not visited[i]:  # 방문하지 않은 숫자라면
            visited[i] = True  # 방문 표시
            seq.append(nums[i])  # 현재 숫자를 추가
            backtrack()  # 재귀 호출
            seq.pop()  # 원상 복구 (백트래킹)
            visited[i] = False  # 방문 표시 해제

# ✅ 순열 생성 실행
backtrack()

# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. 입력을 집합(set)으로 받아서 순서가 유지되지 않음.
#    - 기존 코드: `nums = list({int(sys.stdin.readline()) for _ in range(N)})`
#    - ❌ 문제점: 집합(set)은 순서를 보장하지 않으므로, 입력된 숫자의 순서가 바뀔 수 있음.
#    - ✅ 수정: `nums = list(map(int, sys.stdin.readline().split()))`으로 변경.

# 2. `nums.sort()`를 사용하지 않아서 순열이 정렬되지 않음.
#    - 기존 코드에서는 입력된 순서를 그대로 사용했음.
#    - ❌ 문제점: 문제에서 "입력받은 숫자를 정렬한 후 순열을 생성해야 한다"고 명시되어 있음.
#    - ✅ 수정: `nums.sort()`를 추가하여 입력된 숫자를 오름차순 정렬.

# 3. `visited` 리스트의 변수명을 잘못 입력하여 오류 발생.
#    - 기존 코드: `visted[i] = False` (오타)
#    - ❌ 문제점: `visited`가 아니라 `visted`라고 오타가 있어서 백트래킹이 정상적으로 작동하지 않음.
#    - ✅ 수정: `visited[i] = False`로 변경.

# 4. 잘못된 입력 방식으로 인해 여러 줄 입력을 받을 수 있도록 반복문을 사용했음.
#    - 기존 코드: `nums = list(map(int, sys.stdin.readline().split() for _ in range(N)))`
#    - ❌ 문제점: `sys.stdin.readline().split()`은 한 줄의 입력을 처리하는 것이므로, 반복문이 불필요함.
#    - ✅ 수정: `nums = list(map(int, sys.stdin.readline().split()))`로 변경.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
