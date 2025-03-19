#############################################
# ✅ [문제 1]
# 문제 설명:
# - 주어진 정수 배열에서 중복을 제거하고 정렬하여 출력하는 문제입니다.
# - 입력:
#   첫 번째 줄에 N (정수의 개수)
#   두 번째 줄에 N개의 정수
# - 출력:
#   중복을 제거하고 정렬한 수열을 출력합니다.
#
# 입출력 예시:
# 입력:
# 5
# 3 5 3 2 5
# 출력:
# 2 3 5
#
# 풀이:
# - set() 으로 중복 제거
# - sorted() 함수로 정렬
# - map() + join()으로 출력
#############################################

import sys

# N 입력 받기
n = int(sys.stdin.readline().strip())  # 배열의 크기 입력

# 정수 배열 입력, 중복 제거
arr = set(map(int, sys.stdin.readline().strip().split()))  # set으로 중복 제거

# 정렬
arr = sorted(arr)  # 정렬된 리스트

# 출력
print(' '.join(map(str, arr)))  # 문자열로 변환 후 출력

#############################################
# ✅ [문제 2]
# 문제 설명:
# - 미로 탈출 최단 거리 문제입니다.
# - 미로는 NxM 크기이며, 
#   'S'가 시작점, 'E'가 도착점, '.'은 이동 가능, '#'은 벽입니다.
# - 4방향(상, 하, 좌, 우)으로 이동 가능하며 최단 거리를 구합니다.
#
# 입출력 예시:
# 입력:
# 5 5
# S.#..
# .#.#.
# ..#.#
# ..#.E
# .....
#
# 출력:
# 7
#
# 풀이:
# - BFS를 사용해 최단 거리 탐색
# - queue 사용, visited 체크
# - 출구를 만나면 즉시 거리 반환
#############################################

from collections import deque

# 미로 크기 입력
n, m = map(int, sys.stdin.readline().split())

# 보드 입력 받기
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 방향 벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':  # 시작점 발견
            start = (i, j)

# BFS 함수 정의
def bfs(start):
    queue = deque([(*start, 0)])  # 큐 초기화 (x, y, 거리)
    visited = [[False]*m for _ in range(n)]  # 방문 배열
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()  # 큐 pop
        if board[x][y] == 'E':  # 도착 시 거리 반환
            return dist

        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            # 범위 내이며, 벽이 아니고, 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny, dist + 1))  # 다음 지점 추가
    return -1  # 경로 없을 시 -1 반환

# 최단 거리 출력
print(bfs(start))

#############################################
# ✅ [문제 3]
# 문제 설명:
# - 문자열 압축 문제입니다.
# - 문자열을 1~len(s)//2까지 자른 블록 단위로 반복 압축합니다.
# - 같은 문자열이 반복될 경우 "횟수[문자]" 형식으로 압축
# - 가능한 모든 압축 시도 중 가장 짧은 압축 길이를 구합니다.
#
# 입출력 예시:
# 입력:
# abcabcabcabc
# 출력:
# 6   (4[abc])
#
# 풀이:
# - step 크기를 1부터 N//2까지 늘리며 탐색
# - prev 블록과 비교하며 반복 횟수 count
# - count > 1일 때 압축 문자열 추가
# - 마지막 블록 처리
# - 모든 시도 중 최소 길이 출력
#############################################

# 문자열 입력
s = sys.stdin.readline().strip()
n = len(s)
answer = n  # 초기값은 압축 없이 전체 길이

# step 길이마다 탐색
for step in range(1, n // 2 + 1):
    compressed = ''  # 압축 결과
    prev = s[0:step]  # 초기 블록
    count = 1  # 반복 횟수

    # 문자열을 step 단위로 슬라이스
    for i in range(step, n, step):
        # 이전 블록과 같으면 count 증가
        if prev == s[i:i + step]:
            count += 1
        else:
            # 반복 끝났을 때 압축 문자열 붙이기
            if count > 1:
                compressed += f"{count}[{prev}]"
            else:
                compressed += prev

            # 새로운 블록 시작
            prev = s[i:i + step]
            count = 1

    # 마지막 블록 처리
    if count > 1:
        compressed += f"{count}[{prev}]"
    else:
        compressed += prev

    # 최소 길이 비교
    answer = min(answer, len(compressed))

# 최종 결과 출력
print(answer)

#############################################
# ✅ 최종 정리:
# - 이 파일에는 각 문제에 대한 문제 설명, 입출력 예시, 한줄 한줄 주석, 풀이 방법을 모두 포함.
# - 깃허브에 올릴 때 README 없이도 코드 자체로 설명이 충분히 되도록 구성됨.
#############################################
