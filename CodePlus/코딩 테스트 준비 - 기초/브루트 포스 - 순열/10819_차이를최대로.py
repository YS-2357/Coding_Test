# 백준 10819번: 차이를 최대로
# 문제 설명:
# N개의 정수로 만들 수 있는 모든 순열 중에서 다음 식의 최댓값을 구하는 문제.
# - 식: |A[1] - A[2]| + |A[2] - A[3]| + ... + |A[N-1] - A[N]|
# - 완전 탐색(Brute Force) 방식으로 해결 가능하며, N! 경우의 수를 탐색해야 한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (3 ≤ N ≤ 8)
# - 두 번째 줄에 N개의 정수가 주어진다. (-100 ≤ Ai ≤ 100)

# 출력 형식:
# - 위의 수식을 최대화하는 순열을 선택했을 때의 최댓값을 출력한다.

# 예제 입력 1:
# 6
# 20 1 15 8 4 10
# 예제 출력 1:
# 62

import sys  # 입력 속도 향상을 위한 sys 모듈 사용

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 정수 N 입력 받기
nums = list(map(int, sys.stdin.readline().split()))  # N개의 정수를 리스트로 저장

# ✅ 백트래킹을 위한 변수 초기화
seq = []  # 현재 선택한 숫자를 저장할 리스트
visited = [False] * N  # 방문 여부를 확인하는 리스트
max_value = 0  # 최댓값 저장 변수

# ✅ 백트래킹을 이용한 완전 탐색 함수
def bruteforce():
    global max_value  # 함수 내부에서 전역 변수 수정

    if len(seq) == N:  # ✅ 기저 조건: N개의 숫자가 모두 선택된 경우
        value = 0
        for i in range(N - 1):  # ✅ |A[i] - A[i+1]|의 합 계산
            value += abs(seq[i] - seq[i+1])
        max_value = max(max_value, value)  # ✅ 최댓값 갱신
        return  # ✅ 백트래킹 종료

    for i in range(N):  # ✅ 0부터 N-1까지 탐색하여 순열 생성
        if not visited[i]:  # ✅ 아직 사용하지 않은 숫자인 경우
            seq.append(nums[i])  # ✅ 숫자 추가
            visited[i] = True  # ✅ 사용한 숫자로 표시
            bruteforce()  # ✅ 재귀 호출로 다음 숫자 선택
            seq.pop()  # ✅ 백트래킹: 숫자 제거
            visited[i] = False  # ✅ 다시 사용 가능하도록 변경

# ✅ 실행
bruteforce()
print(max_value)  # ✅ 최댓값 출력


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ `visited` 리스트 크기 설정 오류
#    - 기존 코드: `visited = [False] * (N + 1)`
#    - ❌ 문제점: 인덱스 범위가 `0`부터 `N-1`까지이므로, `N+1`은 불필요.
#    - ✅ 수정: `visited = [False] * N`으로 크기를 조정.

# 2. ✅ 순열 계산 후 `return` 없음 → 불필요한 탐색 발생
#    - 기존 코드:
#      ```python
#      for i in range(N - 1):
#          value += abs(seq[i] - seq[i+1])
#          max_value = max(max_value, value)
#      ```
#    - ❌ 문제점: 모든 경우의 수를 탐색해야 하지만, 불필요하게 연산이 계속 실행됨.
#    - ✅ 수정: `return`을 추가하여 백트래킹 종료.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
