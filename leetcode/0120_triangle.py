# 0120_triangle.py
# -----------------------------------------------------
# ✅ 제목: Triangle (LeetCode 120)
# ✅ 문제 설명(요약):
# - 위에서 시작해 매 행에서 인접한 두 칸 중 하나로만 내려간다.
# - 경로 합의 최솟값을 구한다.
#
# ✅ 입력 형식(요지):
# - triangle: List[List[int]], i번째 행의 길이는 i+1
#
# ✅ 규칙 요약:
# 1) (i, j)에서 (i+1, j) 또는 (i+1, j+1)로만 이동 가능
# 2) 음수 포함 가능 → 그리디 금지, DP 필요
# 3) 경계 칸(j=0, j=i)은 한 방향만 존재
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * (i+1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
            for j in range(1, len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[len(triangle)-1])

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 모든 테스트 통과. DP 테이블로 누적 최소합 계산 성공.
#
# 🔧 오답 이유 및 실수(있다면) / 점검 포인트:
# - 경계 처리(j=0, j=i) 분기 적용함. 내부 칸은 상단 두 칸의 최소값 사용.
# - 공간을 O(n^2)로 사용함(정답 가능). 면접에선 O(1) 추가 공간 최적화 권장.
#
# 📚 사용된 알고리즘 개념:
# - 하향식 경로의 최소합을 위한 하향식→상향식 DP
#   f[i][j] = triangle[i][j] + min(f[i-1][j-1], f[i-1][j])  (경계는 단일 부모)
# - 시간복잡도: O(n^2), 공간복잡도: O(n^2)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이 제안:
# - Bottom-up 제자리 갱신(O(1) 추가 공간):
#   마지막 행을 시작값으로 두고 위로 올라오며
#   triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]).
#   최종적으로 triangle[0][0]이 답.
# - 또는 1차원 DP(길이 = 마지막 행)로 아래에서 위로 갱신해도 O(n) 공간 달성 가능.
