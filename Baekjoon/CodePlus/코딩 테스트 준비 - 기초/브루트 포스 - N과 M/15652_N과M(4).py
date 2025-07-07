# 백준 15652번: N과 M (4)
# 문제 설명:
# 1부터 N까지 자연수 중에서 길이가 M인 오름차순(비내림차순) 조합을 출력하는 문제.
# - 같은 숫자를 여러 번 선택할 수 있으며, 순서는 반드시 오름차순이어야 한다.

# 입력 형식:
# - 두 정수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력 형식:
# - 한 줄에 하나씩 길이가 M인 오름차순 조합을 출력한다.

# 예제 입력 1:
# 4 2
# 예제 출력 1:
# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4

import sys

# ✅ 입력 처리
N, M = map(int, sys.stdin.readline().split())

# ✅ 현재 조합을 저장할 리스트
seq = []

# ✅ 백트래킹을 활용한 중복 조합 생성 함수
def backtrack(start):
    if len(seq) == M:  # 길이가 M이면 출력
        print(*seq)
        return
    
    for num in range(start, N + 1):  # 현재 숫자부터 N까지 탐색 (오름차순 유지)
        seq.append(num)  # 숫자 추가
        backtrack(num)  # 같은 숫자를 선택할 수 있도록 유지
        seq.pop()  # 원상 복구 (백트래킹)

# ✅ 중복 조합 생성 실행
backtrack(1)
