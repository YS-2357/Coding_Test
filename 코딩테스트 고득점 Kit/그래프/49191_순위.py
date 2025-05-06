# 49191_순위.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - A가 B를 이기면 A의 순위는 B보다 앞선다.
# - 여러 경기 결과가 주어졌을 때, 각 선수의 정확한 순위를 알 수 있는지 판단한다.
# - 정확한 순위를 알 수 있는 선수의 수를 반환해야 한다.

# ✅ 입력 형식:
# - n: 선수의 수 (1 ≤ n ≤ 100)
# - results: 경기 결과 리스트 (A가 B를 이겼다면 [A, B])

# ✅ 출력 형식:
# - 정확한 순위를 알 수 있는 선수의 수 (int)

# ✅ 입출력 예제:
# 🔹 입력:
#   n = 5
#   results = [[4,3],[4,2],[3,2],[1,2],[2,5]]
# 🔹 출력:
#   2
# -----------------------------------------------------

from collections import defaultdict

def solution(n, results):
    answer = 0
    # ✅ 각 선수의 이긴 선수 목록과 진 선수 목록을 저장
    win_graph = defaultdict(set)   # A가 B를 이김 → win_graph[A].add(B)
    lose_graph = defaultdict(set)  # A가 B를 이김 → lose_graph[B].add(A)

    for winner, loser in results:
        win_graph[winner].add(loser)
        lose_graph[loser].add(winner)

    # ✅ DFS로 전파 관계 추적
    def dfs(graph, start, visited):
        for next in graph[start]:
            if next not in visited:
                visited.add(next)
                dfs(graph, next, visited)

    # ✅ 각 선수에 대해 정확한 순위를 알 수 있는지 판단
    for i in range(1, n+1):
        win_visited = set()   # i가 이긴 모든 선수들
        lose_visited = set()  # i가 진 모든 선수들

        dfs(win_graph, i, win_visited)
        dfs(lose_graph, i, lose_visited)

        # ✅ 전파된 win/lose의 수가 n-1이면 순위를 알 수 있음
        if len(win_visited) + len(lose_visited) == n - 1:
            answer += 1

    return answer

# -----------------------------------------------------
# ✅ 내가 이전에 틀렸던 점 정리:
# 1. 이긴 선수와 진 선수를 한 방향으로만 저장함 → 전파 관계 파악 불가
# 2. 순위 확정 조건을 잘못 이해했음 → "연결된 선수 수 = n - 1"로 판단해야 함
# 3. DFS로 전파 관계를 확장하지 않아 직접 연결된 관계만 고려함

# ✅ ChatGPT가 제공한 힌트 목록:
# - defaultdict(set)을 활용해 win/lose 그래프 구축
# - 각 선수에 대해 DFS 수행하여 모든 전파 가능한 승/패 관계 추적
# - 정확한 순위는 "이긴 선수 수 + 진 선수 수 == n - 1" 조건으로 확인
# - DFS 템플릿: `for next in graph[start]` → 재귀 호출로 전파
# -----------------------------------------------------
