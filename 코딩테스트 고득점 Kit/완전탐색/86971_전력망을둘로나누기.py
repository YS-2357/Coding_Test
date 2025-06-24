# 86971_전력망을둘로나누기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 송전탑 n개가 트리 구조(사이클 없음)로 연결되어 있고,
#   각 전선(wires)을 하나 끊어서 두 개의 송전망으로 나누려고 한다.
# - 두 전력망에 속한 송전탑의 개수 차이가 **가장 작아지도록** 끊는 경우를 찾아,
#   그 **최솟값을 반환**하는 문제.

# ✅ 입력 형식:
# - n: 송전탑의 개수 (2 ≤ n ≤ 100)
# - wires: [a, b] 형태의 n-1개 전선 연결 정보

# ✅ 출력 형식:
# - 전선을 하나 끊었을 때 생기는 두 송전망 송전탑 개수 차이의 **최솟값**

# ✅ 입출력 예제:
# 예제 1:
#   입력: n = 9, wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
#   출력: 3

# -----------------------------------------------------

def solution(n, wires):
    answer = n  # 최대 차이는 n이므로, 초기값은 n으로 설정

    # wires에서 하나의 전선을 끊고 나머지로 그래프 구성
    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]  # 인접 리스트 초기화

        for j in range(len(wires)):
            if i == j:
                continue  # i번째 전선은 끊음 (그래프에 포함하지 않음)
            a, b = wires[j]
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)

        # DFS로 한 쪽 전력망의 송전탑 수 세기
        def dfs(node):
            visited[node] = True
            count = 1  # 자기 자신 포함
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    count += dfs(neighbor)
            return count

        one_comp = dfs(1)           # 한쪽 전력망 송전탑 수
        other_comp = n - one_comp   # 나머지 송전탑 수
        diff = abs(one_comp - other_comp)
        answer = min(answer, diff)  # 최소 차이 갱신

    return answer

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 처음에는 간선을 끊지 않고 DFS만 반복함 → 의미 없는 탐색
# ❌ `graph[a].append(a)` 등 잘못된 간선 연결
# ❌ `visitied` 오타로 IndexError 발생

# ✅ GPT가 준 힌트 요약:
# - `for i in range(len(wires))`로 간선 하나씩 제거하며 탐색
# - 제거 후 인접 리스트로 그래프 구성
# - DFS를 통해 컴포넌트 크기(송전탑 수)를 계산
# - 두 컴포넌트 차이의 최솟값을 `answer`로 관리

# ✅ 사용된 개념 요약:
# - 그래프 탐색(DFS)
# - 간선 제거 시뮬레이션
# - 트리 분할 후 각 연결 요소 크기 계산
# - 차이의 최솟값 갱신

# ✅ 결과:
# ✅ 정답 도출, 실수 수정 후 최종 성공
# -----------------------------------------------------
# 다른 사람의 풀이
# def solution(n, wires):
#     ans = n  # 초기값: 최악의 경우 차이 n으로 설정

#     for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):  
#         # wires에서 i번째 간선을 제거한 경우의 리스트를 sub로 순회

#         s = set(sub[0])  
#         # 첫 간선의 두 노드를 집합 s에 넣고 시작 (연결된 컴포넌트 초기화)

#         [s.update(v) for _ in sub for v in sub if set(v) & s]
#         # 연결된 노드들이 있는 간선을 계속 추가함
#         # 즉, s에 포함된 노드와 겹치는 간선이 있다면 s에 그 노드들도 추가
#         # 모든 연결된 노드를 s에 누적

#         ans = min(ans, abs(2 * len(s) - n))  
#         # s에는 한쪽 컴포넌트의 노드들이 들어있음 → 다른 쪽은 n - len(s)
#         # 두 집합 차이 = |len(s) - (n - len(s))| = |2*len(s) - n|
#         # 최솟값으로 갱신

#     return ans  # 최솟값 반환
