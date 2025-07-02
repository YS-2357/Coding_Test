# 43163_단어 변환.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - begin 단어에서 target 단어로 변환하려고 합니다.
# - 한 번에 한 글자씩만 바꿀 수 있고, 변환된 단어는 words에 포함되어야 합니다.
# - 최소 몇 단계의 변환이 필요한지 구하세요.

# ✅ 입력 형식:
# - begin: 시작 단어 (소문자, 길이 1~10)
# - target: 목표 단어
# - words: 단어 리스트 (최대 50개)

# ✅ 출력 형식:
# - 최소 단계 수 (정수), 변환이 불가능하면 0

# ✅ 입출력 예제:
# 예제 1:
#   입력: begin = "hit", target = "cog", words = ["hot","dot","dog","lot","log","cog"]
#   출력: 4
#   설명: hit → hot → dot → dog → cog

# -----------------------------------------------------

from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n  # 각 단어 방문 여부
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수) 큐에 삽입
    
    def word_diff(a, b):
        # 두 단어가 한 글자만 다른지 여부 확인
        return sum(c1 != c2 for c1, c2 in zip(a, b)) == 1

    while queue:
        word, count = queue.popleft()
        for i in range(n):
            if word_diff(words[i], word) and not visited[i]:
                if words[i] == target:
                    return count + 1  # target에 도달하면 즉시 반환
                visited[i] = True
                queue.append((words[i], count + 1))  # 다음 단어와 함께 큐에 추가
                
    return 0  # target에 도달하지 못한 경우

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ count를 마지막 값으로 반환해버림 → target에 도달하지 않아도 반환될 수 있음
# ❌ 큐 초기화를 잘못한 적 있음: deque((begin, 0)) → deque([(begin, 0)])

# ✅ GPT가 준 힌트 요약:
# - BFS는 target에 가장 먼저 도달하는 경로가 최단 거리이므로, 도달한 순간 return
# - 탐색 도중 target을 만나면 즉시 종료해야 함

# ✅ 사용된 개념 요약:
# - BFS(너비 우선 탐색): 최단 거리 탐색에 적합
# - zip() + sum(): 두 단어 간 글자 차이 계산
# - visited[] 배열로 중복 탐색 방지

# -----------------------------------------------------
