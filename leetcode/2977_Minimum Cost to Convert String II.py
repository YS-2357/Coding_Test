# 2977_Minimum Cost to Convert String II.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2977. Minimum Cost to Convert String II
# 🏷️ 유형: 그래프 최단경로(Floyd-Warshall) / 문자열 DP / 해시 매핑
#
# ✅ 문제 설명(요약):
#   - source 문자열을 target 문자열로 변환하려고 한다.
#   - 단일 문자뿐 아니라 “문자열 조각(original -> changed)” 변환 규칙과 비용(cost)이 주어진다.
#   - 여러 번의 변환을 연쇄적으로 적용할 수 있으며, 전체 최소 비용을 구한다.
#   - 불가능하면 -1을 반환한다.
#
# ✅ 입력 형식(요지):
#   - source: str
#   - target: str
#   - original: List[str]
#   - changed: List[str]
#   - cost: List[int]
#
# ✅ 규칙 요약:
#   - 변환은 같은 길이의 문자열 조각끼리 대응되는 것으로 취급되며, 규칙의 비용을 더한다.
#   - 규칙 간 연쇄 변환이 가능하므로, 조각 A->B, B->C가 있으면 A->C도 가능하며 비용은 합으로 계산된다.
#   - 최종적으로 source 전체를 target 전체로 만들기 위한 최소 비용을 구한다.
#
# 🧠 핵심 불변식(Invariant):
#   - id는 변환 규칙에 등장하는 문자열 조각을 정점으로 압축 매핑한다.
#   - dist[u][v]는 조각 u를 v로 바꾸는 최소 비용이며, Floyd-Warshall로 모든 쌍 최단비용을 전처리한다.
#   - dp[i]는 source[0:i]를 target[0:i]로 변환하는 최소 비용이며, i에서 가능한 길이 L 조각 변환을 시도해 dp[i+L]를 완화한다.
#   - lens는 변환 규칙에 등장하는 조각 길이 집합으로, dp 전이에서 검사할 길이를 제한한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                             # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def minimumCost(self, source, target, original, changed, cost):         # 최소 변환 비용을 반환하는 함수
        INF = 10**30                                                        # 충분히 큰 수로 무한대(INF)를 설정
        id = {}                                                             # 문자열 조각을 정점 인덱스로 매핑할 딕셔너리 초기화
        lens = set()                                                        # 변환 규칙에 등장하는 문자열 길이 집합을 저장할 set 초기화
        sz = 0                                                              # 현재까지 등록된 정점(문자열 조각) 개수를 저장할 변수

        dist = [[INF]*201 for _ in range(201)]                              # dist 행렬을 INF로 초기화(최대 201 정점 가정)

        for s, t, c in zip(original, changed, cost):                        # 주어진 변환 규칙들을 순회
            if s not in id:                                                 # 시작 조각 s가 아직 등록되지 않았다면
                id[s] = sz                                                  # s에 새 인덱스를 할당
                lens.add(len(s))                                            # dp 전이를 위해 s의 길이를 lens에 추가
                sz += 1                                                     # 정점 개수를 증가
            if t not in id:                                                 # 도착 조각 t가 아직 등록되지 않았다면
                id[t] = sz                                                  # t에 새 인덱스를 할당
                sz += 1                                                     # 정점 개수를 증가
            dist[id[s]][id[t]] = min(dist[id[s]][id[t]], c)                 # 직접 변환 비용은 중복 규칙 중 최소 비용으로 저장

        for i in range(sz):                                                 # 등록된 모든 정점 i에 대해
            dist[i][i] = 0                                                  # 자기 자신으로의 변환 비용은 0으로 설정

        for k in range(sz):                                                 # Floyd-Warshall의 중간 정점 k를 순회
            for i in range(sz):                                             # 시작 정점 i를 순회
                if dist[i][k] < INF:                                        # i->k가 가능하면
                    for j in range(sz):                                     # 도착 정점 j를 순회
                        if dist[k][j] < INF:                                # k->j가 가능하면
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])  # i->k->j 경로로 최단비용을 완화

        n = len(source)                                                     # source의 길이를 저장
        dp = [INF] * (n + 1)                                                # dp[i] = prefix 길이 i까지의 최소 비용을 INF로 초기화
        dp[0] = 0                                                           # 길이 0(빈 접두사)의 비용은 0으로 설정

        for i in range(n):                                                  # 접두사 끝 위치 i를 0..n-1까지 순회
            if dp[i] == INF:                                                # i까지 도달 불가능한 상태면
                continue                                                    # 전이를 시도하지 않고 건너뜀

            if source[i] == target[i]:                                      # 현재 문자 1개가 이미 동일하면
                dp[i + 1] = min(dp[i + 1], dp[i])                           # 비용 증가 없이 dp를 한 칸 전진 가능

            for L in lens:                                                  # 가능한 조각 길이 L을 모두 시도
                if i + L > n:                                               # 범위를 벗어나면
                    continue                                                # 해당 길이는 건너뜀
                s = source[i:i+L]                                           # source에서 길이 L 조각을 추출
                t = target[i:i+L]                                           # target에서 길이 L 조각을 추출
                if s in id and t in id:                                     # 두 조각이 모두 그래프 정점으로 존재하면
                    dp[i + L] = min(dp[i + L], dp[i] + dist[id[s]][id[t]])  # i->i+L로 변환 비용을 더해 dp를 완화

        return -1 if dp[n] == INF else dp[n]                                # 끝까지 불가능하면 -1, 가능하면 최소 비용 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 규칙 조각을 정점으로 하는 최단경로 전처리(Floyd-Warshall) + 문자열 접두사 DP로 최소 비용 합성.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(sz^3 + n * |lens|)  (sz는 규칙에서 등장한 고유 조각 수; dp 전이는 길이 후보만 검사)
#   - 공간: O(sz^2 + n)           (dist 행렬 + dp 배열)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 조각 길이/종류가 커지는 변형에서는 트라이/해시 롤링으로 가능한 매칭을 빠르게 열거하는 방식도 고려할 수 있다(개념만).
