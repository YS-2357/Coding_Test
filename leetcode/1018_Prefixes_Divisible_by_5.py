# 1018_Prefixes_Divisible_by_5.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1018. Binary Prefix Divisible By 5
# ✅ 문제 설명(요약):
#   - 이진수 배열 nums가 주어진다. nums[0..i] 구간을 이진수로 보았을 때,
#     그 값이 5로 나누어떨어지는지 여부를 각 i마다 판단해야 한다.
#   - 예: nums = [1,0,1]이면,
#       - prefix "1"   → 1
#       - prefix "10"  → 2
#       - prefix "101" → 5
#     각각이 5로 나누어지는지 True/False로 기록한다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int], 각 원소는 0 또는 1
#
# ✅ 규칙 요약:
#   - prefix 이진수는 매 단계마다 이전 값에 대해:
#         cur = cur*2 + nums[i]
#     로 갱신된다.
#   - overflow 걱정 없이 5로 나누어떨어짐만 확인하려면
#     cur % 5 값을 계속 유지하면 충분하다.
#   - 매 prefix마다 cur % 5 == 0 여부를 결과 리스트에 push한다.

# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - prefix를 10진수 전체로 만들 필요 없이 "mod 5 값"만 계속 관리한다.
#   - cur = (cur*2 + num) % 5 공식으로 누적.
#   - 매 prefix마다 cur == 0이면 True를 결과에 추가한다.

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)                     # nums 배열 길이 (정보 목적)
        cur = 0                           # 현재 prefix의 (10진수 % 5) 값을 저장
        ans = list()                      # 각 prefix가 5로 나누어떨어지는지 여부 저장
        
        for num in nums:                  # nums 원소를 왼쪽→오른쪽 순회
            cur = (cur * 2 + num) % 5     # prefix 값을 업데이트하되 5로 모듈러 연산 유지
            ans.append(cur == 0)          # 현재 prefix가 5로 나누어떨어지면 True
        
        return ans                        # 모든 prefix에 대한 검사 결과 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - prefix를 매번 실제 정수로 변환하면 overflow 및 O(n^2) 위험이 있어,
#     누적 모듈러 방식(cur % 5)
