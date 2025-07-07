# 87946_피로도.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 유저는 최대 피로도 k를 가지고 있고, 여러 개의 던전이 주어진다.
# - 각 던전은 [최소 필요 피로도, 소모 피로도]로 구성된다.
# - 던전은 한 번만 입장할 수 있으며, 입장 조건을 만족해야만 들어갈 수 있다.
# - 던전 순서를 바꿔가며 탐험했을 때, 유저가 **탐험할 수 있는 최대 던전 수**를 구하는 문제이다.

# ✅ 입력 형식:
# - k: 1 이상 5000 이하인 정수 (초기 피로도)
# - dungeons: 최대 8개, 각 던전은 [최소 필요 피로도, 소모 피로도]

# ✅ 출력 형식:
# - 탐험 가능한 최대 던전 수 (정수)

# ✅ 입출력 예제:
# 예제 1:
#   입력: k = 80, dungeons = [[80, 20], [50, 40], [30, 10]]
#   출력: 3

# -----------------------------------------------------

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    candidates = permutations(dungeons)

    for candidate in candidates:
        start = k        # 매 시도마다 초기 피로도 복원
        count = 0        # 현재 조합에서 탐험한 던전 수 초기화

        for dungeon in candidate:
            if start >= dungeon[0]:       # 입장 가능 여부 확인
                start -= dungeon[1]       # 소모 피로도 차감
                count += 1
        answer = max(answer, count)       # 최대 탐험 수 갱신

    return answer

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 조건 비교를 `dungeon[0] >= k`로 잘못 설정하여 입장이 반대로 되었음
# ❌ `k`를 순열 루프 바깥에서 유지해, 피로도가 누적되어 계산됨

# ✅ GPT가 준 힌트 요약:
# - `permutations()`를 사용해 던전 순서 모든 경우 생성
# - 각 순열마다 `start = k`로 피로도 복원 필요
# - 조건: 현재 피로도 `>=` 최소 필요 피로도

# ✅ 사용된 개념 요약:
# - 완전탐색 (순열, permutations)
# - 조건문 기반 시뮬레이션
# - 최대값 갱신 (max)

# ✅ 결과:
# ✅ 처음엔 조건 방향과 피로도 초기화에서 오류 있었으나 수정 후 정답 도출
# -----------------------------------------------------
# 다른 사람의 풀이
# answer = 0  # 최대 탐험 던전 수를 저장할 전역 변수
# N = 0       # 던전 개수 (전역 변수로 저장)
# visited = []  # 각 던전의 방문 여부를 저장하는 리스트

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:          # 현재 탐험한 던전 수가 기존 최대값보다 크면 갱신
#         answer = cnt

#     for j in range(N):        # 모든 던전에 대해 탐색 시도
#         # 현재 피로도가 해당 던전의 최소 필요 피로도 이상이고, 아직 방문하지 않았다면
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1                              # 해당 던전 방문 표시
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)  # 피로도 차감하고 다음 탐색
#             visited[j] = 0                              # 백트래킹: 방문 여부 초기화

# def solution(k, dungeons):
#     global N, visited
#     N = len(dungeons)        # 전체 던전 수 저장
#     visited = [0] * N        # 방문 여부 리스트 초기화
#     dfs(k, 0, dungeons)      # DFS 시작: 초기 피로도 k, 탐험 수 0부터
#     return answer            # 최대로 탐험한 던전 수 반환
# -----------------------------------------------------
