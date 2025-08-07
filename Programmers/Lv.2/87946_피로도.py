# 87946_피로도.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 초기 피로도 k와 각 던전의 [최소 필요 피로도, 소모 피로도] 리스트 dungeons가 주어집니다.
# - 현재 피로도 ≥ 최소 필요 피로도일 때만 던전을 탐험할 수 있고, 탐험 후에는 소모 피로도만큼 피로도가 감소.
# - 각 던전은 한 번만 탐험 가능하며, 탐험한 던전 수의 최댓값을 구해 반환합니다.
#
# ✅ 입력:
# - k: 초기 피로도 (1 ≤ k ≤ 5,000)
# - dungeons: 길이 1~8의 2차원 리스트, 각 원소는 [minimum, consume]
#
# ✅ 출력:
# - 탐험할 수 있는 던전의 최대 개수 (정수)
#
# ✅ 예시:
#   k = 80
#   dungeons = [[80,20],[50,40],[30,10]]
#   → 80→(80,20)→60→(50,40)→20→마지막 던전 탐험 불가
#   → 탐험 개수 = 2
# -----------------------------------------------------

def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)  # 던전별 방문 여부

    def dfs(current_k, count):
        nonlocal answer
        # ✅ 지금까지 탐험한 count를 최댓값과 비교
        answer = max(answer, count)
        # ✅ 아직 탐험하지 않은 던전 중 가능한 던전을 모두 시도
        for idx, (minimum, consume) in enumerate(dungeons):
            if not visited[idx] and current_k >= minimum:
                visited[idx] = True
                dfs(current_k - consume, count + 1)
                visited[idx] = False  # 백트래킹: 상태 복원

    dfs(k, 0)  # 초기 호출: 남은 피로도 k, 탐험 수 0
    return answer

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# - 처음에는 dfs 내부에서 answer를 수정하면서도, 
#   dfs의 반환값을 answer에 할당하려고 하여 None이 할당되는 오류 발생
# - `answer`가 함수 solution의 지역 변수임에도 `global`을 사용해 참조하려 해 NameError 발생
#
# ✅ GPT가 준 힌트 요약:
# - `answer`는 반환값이 아니라 `nonlocal`로 선언해 nested 함수 내에서 직접 갱신
# - `dfs` 호출 결과를 변수에 할당하지 말고, 호출 후 그대로 `return answer`
# - 백트래킹 구조: 방문 전후에 `visited[idx]`를 `True`↔`False`로 설정
#
# ✅ 사용된 개념 요약:
# - DFS(백트래킹): 순열 탐색을 통해 가능한 모든 던전 탐험 순서 시도
# - `nonlocal answer`: 중첩 함수에서 외부 변수 갱신
# - `visited` 배열: 던전 중복 탐험 방지
# - early update: 재귀 진입 시마다 `answer` 갱신으로 최댓값 유지
#
# ✅ 시간 복잡도:
# - 던전 개수 ≤ 8 → 최악의 순열 수 8! = 40,320번 호출
# - 각 호출에서 최대 8회 루프 → 총합 ≲ 320,000 연산 → 충분히 빠름
# -----------------------------------------------------
