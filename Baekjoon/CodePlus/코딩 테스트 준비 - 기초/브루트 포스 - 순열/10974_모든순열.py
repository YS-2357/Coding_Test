# 백준 10974번: 모든 순열
# 문제 설명:
# 1부터 N까지의 모든 숫자로 만들 수 있는 순열을 사전순으로 출력하는 문제.
# - 중복 없이 N개의 숫자를 선택해야 한다.
# - 출력은 오름차순으로 정렬된 순서로 나타나야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 8)

# 출력 형식:
# - N개의 숫자로 이루어진 모든 순열을 한 줄에 하나씩 출력한다.

# 예제 입력 1:
# 3
# 예제 출력 1:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

import sys  # 빠른 입력 처리를 위한 sys 모듈 사용

# ✅ 입력 처리
N = int(sys.stdin.readline())  # N 입력 받기
visited = [False] * (N + 1)  # 방문 여부를 확인하는 리스트 (1~N까지 사용)
nums = []  # 현재 선택된 숫자를 저장할 리스트

# ✅ 백트래킹을 이용한 순열 생성 함수
def all_permutations():
    if len(nums) == N:  # ✅ 기저 조건: N개의 숫자가 모두 선택되었을 때 출력
        print(*nums)  # ✅ 리스트 내용을 공백으로 구분하여 출력
        return  # ✅ 함수 종료

    for i in range(1, N+1):  # ✅ 1부터 N까지의 숫자를 차례대로 탐색
        if not visited[i]:  # ✅ 아직 사용되지 않은 숫자인 경우
            nums.append(i)  # ✅ 숫자 선택
            visited[i] = True  # ✅ 선택한 숫자는 사용 처리
            all_permutations()  # ✅ 재귀 호출로 다음 숫자 선택 진행
            nums.pop()  # ✅ 선택한 숫자 제거 (백트래킹)
            visited[i] = False  # ✅ 숫자를 다시 사용 가능하게 변경

# ✅ 실행
all_permutations()


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `start` 매개변수가 불필요하게 증가함
#    - 기존 코드: `def all_permutations(start):`
#    - ❌ 문제점: start 변수를 증가시키면서 순열을 생성하는 것은 올바르지 않음.
#    - ✅ 수정: `start`를 제거하고 `for i in range(1, N+1):`로 모든 숫자를 탐색.

# 2. ✅ `for i in range(start, N+1):`에서 `start` 사용 오류
#    - 기존 코드: `for i in range(start, N+1):`
#    - ❌ 문제점: start가 증가하면서 탐색 범위를 제한함.
#    - ✅ 수정: `for i in range(1, N+1):`로 고정하여 모든 숫자를 탐색.

# 3. ✅ `all_permutations(start + 1)`에서 매개변수 전달 오류
#    - 기존 코드: `all_permutations(start + 1)`
#    - ❌ 문제점: start 변수를 증가시키는 것이 불필요함.
#    - ✅ 수정: `all_permutations()`로 변경하여 순열을 완전히 탐색.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
