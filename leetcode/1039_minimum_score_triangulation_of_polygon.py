# 1039_minimum_score_triangulation_of_polygon.py
# -----------------------------------------------------
# ✅ 제목: Minimum Score Triangulation of Polygon (LeetCode 1039)
# ✅ 문제 설명(요약):
# - 볼록 n각형의 각 정점 i에 값 values[i]가 주어진다.
# - 교차하지 않는 대각선들로 n−2개의 삼각형으로 분할(삼각분할)할 때,
#   각 삼각형 (a,b,c)의 점수 values[a]*values[b]*values[c] 합의 최솟값을 구한다.
#
# ✅ 입력 형식(요지):
# - values: List[int], 정점 값을 시계방향으로 나열
#
# ✅ 규칙 요약:
# 1) 삼각분할은 대각선이 서로 교차하지 않아야 함.
# 2) 전체 점수 = 모든 삼각형 점수의 합.
# 3) n ≤ 50, 값 범위 제한 내 최대곱 가능.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            return min(
                (values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 문제 포기 후 레퍼런스 코드를 확인.
# - 제출 기준 통과(정답 코드) 형태.
#
# 🔧 오답 이유 및 실수 / 학습 포인트:
# - 핵심은 "구간 DP" 설계와 전이식 도출의 감.
#   dp(i,j) = min_{i<k<j} [ dp(i,k) + dp(k,j) + values[i]*values[k]*values[j] ].
# - 기저조건 누락·인덱스 범위 착오가 빈번: i+2>j → 0, i+2==j → 한 개 삼각형의 곱.
# - "마지막으로 붙이는 삼각형" 관점이 직관을 만든다. (i,j)를 변으로 고정하고 k만 순회.
#
# 📚 사용된 알고리즘 개념:
# - 구간 DP(Interval DP), 최적 부분구조, 중복 부분문제.
# - 탑다운 메모이제이션(@lru_cache)로 상태 수 O(n^2), 상태 전이 O(n) → 시간 O(n^3), 공간 O(n^2).
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이 또는 제안:
# - 바텀업 DP: 길이 len=2..n-1, for i, j=i+len, k in (i+1..j-1)로 테이블 채움.
#   동일한 복잡도(O(n^3)/O(n^2))지만 재귀 스택이 없어 안정적.
# - 디버깅 팁: 작은 예시로 dp 테이블을 손으로 채워 전이 확인
#   예) [2,1,4,4] → dp[0][2]=8, dp[1][3]=16, dp[0][3]=min(24,40)=24.
