# 백준 15649번: N과 M (1)
# 문제 설명:
# 1부터 N까지 자연수 중에서 길이가 M인 모든 순열을 출력하는 문제.
# - 같은 숫자는 한 번만 사용 가능하며, 순서가 다르면 다른 경우로 취급한다.

# 입력 형식:
# - 두 정수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력 형식:
# - 한 줄에 하나씩 길이가 M인 순열을 출력한다.

# 예제 입력 1:
# 3 1
# 예제 출력 1:
# 1
# 2
# 3

# 예제 입력 2:
# 4 2
# 예제 출력 2:
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3

import sys

# ✅ 입력 처리
N, M = map(int, sys.stdin.readline().split())

# ✅ 방문 체크 리스트 (사용 여부 확인)
visited = [False] * (N + 1)

# ✅ 현재 순열을 저장할 리스트
sequence = []

# ✅ 백트래킹을 활용한 순열 생성 함수
def backtrack():
    if len(sequence) == M:  # 길이가 M이면 출력
        print(*sequence)
        return

    for num in range(1, N + 1):  # 1부터 N까지 탐색
        if not visited[num]:  # 방문하지 않은 숫자라면
            visited[num] = True  # 방문 표시
            sequence.append(num)  # 현재 숫자를 추가
            backtrack()  # 재귀 호출
            sequence.pop()  # 원상복구 (백트래킹)
            visited[num] = False  # 방문 표시 해제

# ✅ 순열 생성 실행
backtrack()


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. `itertools.permutations()`을 사용하지 않고 순열을 직접 구현해야 했음.
#    - ✅ 백트래킹을 활용하여 순열을 생성하는 방식을 적용.

# 2. `visited` 리스트 없이 중복 검사하려다 오류 발생.
#    - 기존: `if num not in sequence:` 조건으로 중복 검사.
#    - ❌ 리스트 검색 연산이 비효율적이고, 시간이 오래 걸림.
#    - ✅ 수정: `visited[num]` 리스트를 사용하여 O(1)로 중복 검사.

# 3. 백트래킹에서 `sequence.append(num)` 후 `backtrack()` 실행한 뒤 원상복구 과정이 필요했음.
#    - ✅ `sequence.pop()`을 호출하여 탐색이 끝난 후 상태를 복구.

# 4. `visited[num]` 체크를 하지 않아, 중복된 숫자가 포함될 가능성이 있었음.
#    - ✅ `visited[num] = True` → `backtrack()` 실행 → `visited[num] = False`로 원상 복구.

# 5. `print(sequence)`를 그대로 출력하면 리스트 형태로 출력되어 틀림.
#    - ✅ `print(*sequence)`를 사용하여 공백 구분 출력.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
