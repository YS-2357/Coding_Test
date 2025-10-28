# 3354_Make_Array_Elements_Equal_to_Zero.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3354. Make Array Elements Equal to Zero
# ✅ 문제 설명(요약):
#   배열 nums가 주어진다. 인덱스 i를 시작점으로 선택하고 nums[i]==0일 때만 출발 가능하다.
#   왼쪽 또는 오른쪽 방향으로 이동하며, 0이 아닌 칸을 만나면 그 값을 1 줄이고 방향을 반전한다.
#   모든 원소를 0으로 만들 수 있는 시작점·방향 선택의 총 개수를 구하라.
#
# ✅ 입력 형식(요지):
#   - nums: 정수 리스트 (길이 n)
#
# ✅ 규칙 요약:
#   - 시작점 i는 반드시 nums[i] == 0.
#   - 각 i에서 왼쪽 합(left)과 오른쪽 합(right)을 비교:
#       • left == right  → 양쪽 모두 가능 (기여도 2)
#       • |left - right| == 1 → 큰 합 쪽으로만 가능 (기여도 1)
#       • 그 외 → 불가능 (기여도 0)
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        prefix, total = 0, sum(nums)       # prefix: 왼쪽 누적합, total: 전체 합

        for i in range(n):
            left, right = prefix, total - prefix - nums[i]  # 현재 위치 기준 좌우 합 계산
            if nums[i] == 0:                               # 시작점은 0만 가능
                if left == right:
                    ans += 2                               # 좌우 대칭 → 두 방향 모두 가능
                elif abs(left - right) == 1:
                    ans += 1                               # 한쪽만 가능
            prefix += nums[i]                              # 다음 인덱스용 누적 갱신
        return ans
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 모든 테스트케이스에서 정답 일치.
#   - 불필요한 합 재계산 없이 단일 패스로 해결.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 알고리즘 개념: Prefix Sum (누적합)
#   - 핵심 아이디어: 각 0 위치에서 좌우 합의 균형을 O(1)에 계산.
#   - 초기 시도 시 매번 sum() 호출 시 O(n²) 가능 → prefix로 개선해 O(n) 달성.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n) (배열 1회 순회)
#   - 공간: O(1) (prefix, total, ans만 사용)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - prefix 배열 + suffix 배열로도 가능하지만, 공간만 늘고 동일한 결과.
#   - 균형 조건만 보면 되므로 누적합 1회 스캔이 최적.
