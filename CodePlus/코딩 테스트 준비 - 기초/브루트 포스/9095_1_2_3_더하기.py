# 백준 9095번: 1, 2, 3 더하기
# 문제 설명:
# 정수 N을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 문제.
# 예를 들어 N=4라면 가능한 경우의 수는 다음과 같다.
# (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2), (1+3), (3+1) → 총 7가지.

# 입력 형식:
# - 첫째 줄에 테스트 케이스 개수 T가 주어진다. (1 ≤ T ≤ 10)
# - 이후 T개의 줄에 정수 N이 주어진다. (1 ≤ N ≤ 10)

# 출력 형식:
# - 각 테스트 케이스마다 N을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

# 예제 입력 1:
# 3
# 4
# 7
# 10

# 예제 출력 1:
# 7
# 44
# 274

import sys

# ✅ 입력 처리
n = int(sys.stdin.readline())
arrays = [int(sys.stdin.readline()) for _ in range(n)]

# ✅ 메모이제이션을 위한 딕셔너리
memo = {0: 1, 1: 1, 2: 2, 3: 4}

# ✅ 재귀 + 메모이제이션을 활용한 DP 함수
def trimino(n):
    if n in memo:
        return memo[n]
    memo[n] = trimino(n-1) + trimino(n-2) + trimino(n-3)
    return memo[n]

# ✅ 각 테스트 케이스 결과 출력
for arr in arrays:
    print(trimino(arr))


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드와 틀린 점
# 1. **리스트 입력 방식 오류**
#    ```python
#    arrays = list.append(int(sys.stdin.readline()) for _ in range(n))
#    ```
#    - `list.append()`는 반환값이 `None`이므로 `arrays`에 값이 저장되지 않았음.
#    - ✅ 수정: `arrays = [int(sys.stdin.readline()) for _ in range(n)]`로 변경.

# 2. **변수명 오타 (`memmo`, `meno`, `tetrimino`)**
#    ```python
#    if n in memo:
#        return memmo[n]  # ❌ 오타 (memo → memmo)
#    memo[n] = tetrimino(n-1) + tetrimino(n-2) + tetrimino(n-3)  # ❌ 오타 (trimino → tetrimino)
#    return meno[n]  # ❌ 오타 (memo[n] 반환해야 함)
#    ```
#    - ✅ 수정: `memo[n]`, `trimino(n-1)`, `trimino(n-2)`, `trimino(n-3)`로 올바르게 변경.

# 3. **출력 시 `memo(arr)` 호출 오류**
#    ```python
#    print(memo(arr))  # ❌ `memo`는 딕셔너리이므로 함수처럼 호출할 수 없음
#    ```
#    - `memo[arr]`을 직접 출력하면 값이 없을 경우 `KeyError` 발생 가능.
#    - ✅ 수정: `trimino(arr)`을 먼저 호출해서 값이 존재하도록 한 후 `print(trimino(arr))`로 변경.

# 4. **재귀 함수의 반환값 처리 오류**
#    ```python
#    return meno[n]  # ❌ 오타
#    ```
#    - `memo[n]`을 반환해야 하는데, `meno[n]`으로 잘못 호출됨.
#    - ✅ 수정: `return memo[n]`으로 변경.

# 5. **메모이제이션 초기값 오류**
#    ```python
#    memo = {}  # ❌ 비어 있는 딕셔너리로 시작하면 기본값이 없어 오류 발생
#    ```
#    - 기본적인 초기값을 포함해야 `N=1, 2, 3`일 때 바로 반환 가능.
#    - ✅ 수정: `memo = {0: 1, 1: 1, 2: 2, 3: 4}`로 변경.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
