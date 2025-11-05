# 3318_Find_X_Sum_of_All_K_Long_Subarrays_I.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3318. Find X-Sum of All K-Long Subarrays I
# ✅ 문제 설명(요약):
#   길이 n의 정수 배열 nums가 주어진다.
#   각 길이 k의 부분배열(subarray)에 대해 "x-sum"을 계산해야 한다.
#   x-sum이란:
#     1) 부분배열에서 각 값의 빈도수를 센다.
#     2) (빈도 내림차순, 값 내림차순) 기준으로 정렬한다.
#     3) 상위 x개의 (값 × 빈도)의 합을 구한다.
#   각 윈도우의 x-sum 결과를 순서대로 반환한다.
#
# ✅ 입력 형식(요지):
#   nums: List[int], k: int, x: int
#   1 <= k <= len(nums)
#
# ✅ 규칙 요약:
#   - Counter를 이용해 각 윈도우 내 빈도를 계산.
#   - (빈도, 값) 순으로 정렬 후 상위 x개의 가중합을 구함.
#   - 슬라이딩 윈도우를 한 칸씩 이동하며 결과를 누적.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n-k+1):
            cnt = Counter(nums[i:i+k])                             # 현재 윈도우 내 빈도 계산
            freq = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)  # 빈도·값 내림차순 정렬
            x_sum = sum(v * f for v, f in freq[:x])                # 상위 x개의 (값×빈도) 합산
            ans.append(x_sum)
        return ans
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 모든 테스트케이스 통과.
#   - 문제 I 버전(n, k 작음)에서는 충분히 효율적.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념: Sliding Window + Counting
#   - 윈도우마다 Counter로 빈도를 계산한 뒤,
#     (frequency, value) 기준으로 정렬하여 상위 x개의 합을 구함.
#   - 빈도 동률 시 값이 큰 쪽을 우선해야 하므로 key=(x[1], x[0]).
#   - 각 윈도우의 독립 계산으로 구조 명확.
#
# 📚 시간·공간 복잡도:
#   - 시간복잡도: O((n−k+1) × k log k)
#       • Counter(nums[i:i+k]) = O(k)
#       • 정렬 = O(k log k)
#       • 전체 윈도우 반복 = (n−k+1)
#   - 공간복잡도: O(k) (빈도 딕셔너리 저장)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - freq를 슬라이딩 윈도우 방식으로 갱신(O(1))하고,
#     상위 x 빈도 유지 자료구조(예: 힙, 정렬 리스트)를 사용하면
#     O(n log k)로 개선 가능.
