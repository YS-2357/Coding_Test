# 백준 15651번: N과 M (3)
# 문제 설명:
# 1부터 N까지 자연수 중에서 길이가 M인 중복 순열을 출력하는 문제.
# - 같은 숫자를 여러 번 선택할 수 있으며, 순서가 다르면 다른 경우로 취급한다.

# 입력 형식:
# - 두 정수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

# 출력 형식:
# - 한 줄에 하나씩 길이가 M인 순열을 출력한다.

# 예제 입력 1:
# 3 1
# 예제 출력 1:
# 1
# 2
# 3

import sys

# ✅ 입력 처리
N, M = map(int, sys.stdin.readline().split())

# ✅ 현재 순열을 저장할 리스트
seq = []

# ✅ 백트래킹을 활용한 중복 순열 생성 함수
def backtrack():
    if len(seq) == M:  # 길이가 M이면 출력
        print(*seq)
        return
    
    for num in range(1, N + 1):  # 1부터 N까지 탐색 (중복 가능)
        seq.append(num)  # 숫자 추가
        backtrack()  # 다음 숫자 탐색
        seq.pop()  # 원상 복구 (백트래킹)

# ✅ 중복 순열 생성 실행
backtrack()
