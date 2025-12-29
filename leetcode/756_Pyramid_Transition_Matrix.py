# 756_Pyramid_Transition_Matrix.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 756. Pyramid Transition Matrix
# ✅ 문제 설명(요약):
#   - 바닥 문자열 bottom이 주어지고, 길이 3의 문자열 allowed가 주어진다.
#   - allowed의 각 항목 "UVW"는 아래층의 인접한 두 블록(U,V) 위에 W를 올릴 수 있음을 의미한다.
#   - bottom에서 시작하여 한 층씩 위로 쌓아 최종적으로 꼭대기(길이 1)에 도달할 수 있는지 여부를 반환한다.
#
# ✅ 입력 형식(요지):
#   - bottom: str (초기 바닥층)
#   - allowed: List[str] (각 원소 길이 3, "UVW" 형태)
#
# ✅ 규칙 요약:
#   - 한 층의 문자열 node가 길이 L이면, 다음 층은 길이 L-1의 문자열이 된다.
#   - 다음 층의 i번째 문자는 현재 층의 (i, i+1) 인접 쌍에 의해 결정되며,
#     (node[i], node[i+1])에 대응하는 가능한 upper 문자들의 조합을 선택해 만들 수 있다.
#   - 가능한 다음 층이 여러 개면, 그 중 하나라도 꼭대기까지 도달하면 True.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - 아래는 사용자가 제출/채택한 최종 정답 코드이며,
#     이 단계에서는 코드 내용을 변경하지 않고,
#     각 줄마다 설명 주석만 추가한다.

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        candidate = defaultdict(set)                         # (아래 2칸) -> (위에 올릴 수 있는 문자들) 매핑

        for u, v, w in allowed:                              # allowed의 각 문자열 "UVW"를 (U,V)->W로 해석
            candidate[u, v].add(w)                           # 동일 (U,V)에 대해 여러 W가 가능하므로 set에 저장
        
        def add_neighbor(node):
            res = ['']                                       # 다음 층 문자열 후보들을 누적 생성(초기에는 빈 문자열 1개)
            for i in range(1, len(node)):                    # 인접쌍 (node[i-1], node[i])를 순회
                uppers = candidate[(node[i-1], node[i])]     # 해당 인접쌍 위에 올릴 수 있는 문자 집합
                if uppers:                                   # 가능 문자가 존재하면
                    res = [r + u for u in uppers for r in res]
                                                             # 기존 후보 r들에 대해 u를 뒤에 붙여 후보 확장(데카르트 곱)
                else:                                        # 어떤 위치에서라도 가능한 문자가 없으면
                    return []                                # 해당 node에서 다음 층을 만들 수 없으므로 빈 리스트 반환
            return res                                       # 가능한 다음 층 문자열 후보들 반환

        visited = set()                                      # 실패가 확정된 층 문자열(node)을 메모(가지치기)

        def dfs(node):
            if len(node) == 1:                               # 꼭대기(길이 1)에 도달하면 성공
                return True
            if node in visited:                              # 이미 이 node에서 실패했음을 알면 재탐색 불필요
                return False

            for nxt in add_neighbor(node):                   # 가능한 다음 층 후보들을 모두 시도
                if dfs(nxt):                                 # 하나라도 성공하면
                    return True                               # 즉시 True 반환
            
            visited.add(node)                                # 모든 후보가 실패했으면 이 node는 실패 상태로 기록
            return False                                     # 실패 반환

        return dfs(bottom)                                   # 바닥층에서 DFS 시작

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - (기록 없음) DFS + 후보 생성 + 방문(실패) 메모로 정답 판정.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용한 핵심 알고리즘/개념:
#     - 백트래킹/DFS: 각 층에서 가능한 다음 층 문자열을 생성하며 탐색
#     - 해시 맵(딕셔너리): (아래 2칸) -> 가능한 위 문자 집합 매핑
#     - 가지치기(메모이제이션): 특정 node(층 문자열)에서 실패가 확정되면 visited에 저장해 중복 탐색 방지
#   - 주의 포인트:
#     - add_neighbor에서 후보 수가 폭발할 수 있어, visited 가지치기가 실질적인 성능을 좌우할 수 있다.
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도: 최악의 경우 지수적(각 위치의 후보 문자 조합에 의해 분기 폭발 가능)
#     - 다만 visited로 동일 node 재탐색을 막아 평균적으로 완화된다.
#   - 공간 복잡도: O(S)
#     - S는 visited에 저장되는 층 문자열 수(상태 수)에 비례
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 다음 층 문자열을 “한 번에 전부 생성”하기보다,
#     한 글자씩 위층을 만들며 중간에 불가능해지면 즉시 백트래킹하는 방식으로
#     후보 폭발을 줄일 수 있다(개념만, 코드 X).
#   - allowed를 비트마스크로 압축해 전이를 빠르게 하는 최적화도 가능하다(개념만, 코드 X).
