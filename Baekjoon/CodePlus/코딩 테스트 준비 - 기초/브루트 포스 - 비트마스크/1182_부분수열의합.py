# 백준 1182번: 부분수열의 합
# 문제 설명:
# 주어진 정수 배열에서 부분 수열을 선택하여 합이 S가 되는 경우의 수를 구하는 문제.
# - 공집합은 제외해야 함.
# - 완전 탐색(백트래킹)으로 해결 가능.

# 입력 형식:
# - 첫 번째 줄에 두 정수 N, S가 주어진다. (1 ≤ N ≤ 20, -1,000,000 ≤ S ≤ 1,000,000)
# - 두 번째 줄에 N개의 정수가 공백으로 구분되어 주어진다.

# 출력 형식:
# - 합이 S가 되는 부분 수열의 개수를 출력한다.

# 예제 입력 1:
# 5 0
# -7 -3 -2 5 8
# 예제 출력 1:
# 1

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N, S = map(int, sys.stdin.readline().split())  # ✅ N: 원소 개수, S: 목표 합
nums = list(map(int, sys.stdin.readline().split()))  # ✅ N개의 정수 입력

# ✅ 부분 수열의 개수를 저장할 변수
count = 0  

# ✅ 백트래킹 함수 정의
def backtrack(sub_sum, index):
    """
    현재까지 선택한 숫자의 합(sub_sum)과 현재 탐색 중인 인덱스(index)를 기준으로 부분 수열을 탐색하는 백트래킹 함수.
    """
    global count
    if sub_sum == S and index != 0:  # ✅ 공집합 제외 후 합이 S가 되면 count 증가
        count += 1  

    # ✅ 현재 인덱스 이후의 숫자만 탐색
    for i in range(index, N):  
        backtrack(sub_sum + nums[i], i + 1)  # ✅ 현재 숫자를 더한 새로운 합으로 재귀 호출

# ✅ 탐색 시작
backtrack(0, 0)

# ✅ 결과 출력
print(count)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `sub_sum == 0` 조건 오류
#    - 기존 코드: `if sub_sum == 0 and index > 0:`
#    - ❌ 문제점: `S`가 0이 아닐 경우 정답이 잘못 나옴.
#    - ✅ 수정: `if sub_sum == S and index != 0:`로 변경하여 정확한 부분 수열만 카운트.

# 2. ✅ `count` 증가 후 `return` 사용 오류
#    - 기존 코드:
#      ```python
#      if sub_sum == S and index != 0:
#          count += 1
#          return
#      ```
#    - ❌ 문제점: `return`을 사용하면 더 깊은 탐색을 하지 않음.
#    - ✅ 수정: `return` 제거하여 더 깊이 탐색하도록 변경.

# 3. ✅ 백트래킹 방식 오류 (중복 탐색 발생)
#    - 기존 코드에서 `for i in range(len(nums)):` 사용 → 중복된 부분 수열 탐색 발생 가능.
#    - ✅ 수정: `for i in range(index, N):`로 변경하여 현재 인덱스 이후의 숫자만 탐색.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 

# -----------------------------------------------------

# 비트마스크를 이용한 풀이법
import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N, S = map(int, sys.stdin.readline().split())  # ✅ N: 원소 개수, S: 목표 합
nums = list(map(int, sys.stdin.readline().split()))  # ✅ N개의 정수 입력

# ✅ 부분 수열의 개수를 저장할 변수
count = 0  

# ✅ 비트마스크를 이용하여 모든 부분 수열 탐색
for bitmask in range(1, 1 << N):  # ✅ 1부터 (2^N - 1)까지 (공집합 제외)
    sub_sum = 0  # ✅ 부분 수열의 합

    for i in range(N):  # ✅ 각 비트를 확인하여 해당 원소 포함 여부 결정
        if bitmask & (1 << i):  # ✅ i번째 비트가 1이면 해당 원소 포함
            sub_sum += nums[i]  

    if sub_sum == S:  # ✅ 합이 S인 경우 count 증가
        count += 1  

# ✅ 결과 출력
print(count)
