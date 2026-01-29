# 2976_Minimum Cost to Convert String I.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2976. Minimum Cost to Convert String I
# 🏷️ 유형: 그래프 최단경로 / Floyd-Warshall / 전처리(26자)
#
# ✅ 문제 설명(요약):
#   - source 문자열을 target 문자열로 변환하려고 한다.
#   - 각 위치의 문자 source[i]를 target[i]로 바꾸기 위해, 주어진 문자 변환 규칙(original -> changed)과 비용(cost)을 사용할 수 있다.
#   - 여러 번의 변환을 연쇄적으로 적용할 수 있으며, 전체 변환 비용의 최솟값을 구한다.
#   - 어떤 문자는 목표 문자로 변환이 불가능하면 -1을 반환한다.
#
# ✅ 입력 형식(요지):
#   - source: str
#   - target: str
#   - original: list[str]  (변환 시작 문자들)
#   - changed: list[str]   (변환 도착 문자들)
#   - cost: list[int]      (각 변환 비용)
#
# ✅ 규칙 요약:
#   - 문자 집합은 소문자 26개('a'~'z')로 제한된다.
#   - 직접 변환뿐 아니라 중간 문자를 거치는 연쇄 변환도 허용된다.
#   - 각 위치별 최소 변환 비용을 합산한 값이 정답이다.
#
# 🧠 핵심 불변식(Invariant):
#   - dist[u][v]는 문자 u를 v로 바꾸는 최소 비용(최단거리)을 의미한다.
#   - 초기 dist는 직접 변환 규칙의 최소 비용으로 채우고, dist[i][i]=0으로 둔다.
#   - Floyd-Warshall로 모든 문자쌍 최단비용을 구하면, 각 위치 변환 비용은 dist[u][v]로 즉시 조회 가능하다.
#   - 어떤 위치에서 dist[u][v]가 inf이면 변환 불가능이므로 -1을 반환한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                                 # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:  # 최소 변환 비용을 반환하는 함수
        inf = float('inf')                                                      # 도달 불가능을 표현할 무한대 값을 설정
        dist = [[inf] * 26 for _ in range(26)]                                  # 26×26 최단비용 행렬을 inf로 초기화

        for i in range(26):                                                     # 모든 문자 i에 대해
            dist[i][i] = 0                                                      # 자기 자신으로의 변환 비용은 0으로 설정

        for o, c, z in zip(original, changed, cost):                             # 주어진 직접 변환 규칙들을 순회하며
            u = ord(o) - 97                                                     # 시작 문자를 0..25 인덱스로 변환
            v = ord(c) - 97                                                     # 도착 문자를 0..25 인덱스로 변환
            dist[u][v] = min(dist[u][v], z)                                     # 동일 변환이 여러 번 주어지면 최소 비용만 유지

        for k in range(26):                                                     # Floyd-Warshall의 중간 노드 k를 순회
            for i in range(26):                                                 # 시작 노드 i를 순회
                if dist[i][k] == inf:                                           # i->k가 불가능하면
                    continue                                                    # k를 거치는 경로는 의미 없으므로 건너뜀
                for j in range(26):                                             # 도착 노드 j를 순회
                    if dist[k][j] != inf:                                       # k->j가 가능하면
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])   # i->k->j 경로로 최단비용을 완화

        total_cost = 0                                                          # 전체 변환 비용 누적 변수를 0으로 초기화
        for s_char, t_char in zip(source, target):                              # source와 target을 같은 위치끼리 순회
            u = ord(s_char) - 97                                                # source 문자를 인덱스로 변환
            v = ord(t_char) - 97                                                # target 문자를 인덱스로 변환
            if u == v:                                                          # 이미 같은 문자면
                continue                                                        # 변환 비용이 0이므로 건너뜀
            if dist[u][v] == inf:                                               # u->v 변환이 불가능하면
                return -1                                                       # 전체 변환이 불가능하므로 -1 반환
            total_cost += dist[u][v]                                            # 해당 위치의 최소 변환 비용을 누적

        return total_cost                                                       # 누적된 최소 총 비용을 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 26자 알파벳 그래프의 모든 쌍 최단경로(Floyd-Warshall) 후 위치별 비용 합산.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(26^3 + |source|)  (문자 수가 고정이라 Floyd-Warshall이 충분히 작음)
#   - 공간: O(26^2)             (dist 행렬)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 변환 규칙이 희소하고 문자 종류가 커지는 일반화 문제라면, 각 시작 문자에서 다익스트라를 돌리는 방식도 가능하다(개념만).
