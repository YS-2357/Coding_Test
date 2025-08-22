# 0011_container_with_most_water.py
# -----------------------------------------------------
# ✅ 제목: Container With Most Water
# ✅ 문제 설명(요약):
# - n개의 세로선이 주어지고, 각 선의 길이(height[i])는 양의 정수다.
# - 두 선을 선택하여 x축과 함께 물을 담을 수 있는 컨테이너를 만들 수 있다.
# - 컨테이너에 담을 수 있는 물의 최대 면적을 구하는 문제.
#
# ✅ 입력 형식(요지):
# - height: List[int], 길이 n (n ≥ 2)
#
# ✅ 규칙 요약:
# 1) 용량 계산: (j - i) * min(height[i], height[j])
# 2) 최대 면적을 반환
#
# ✅ 입출력 예시(1개):
# - height = [1,8,6,2,5,4,8,3,7]
#   정답 → 49
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)                           # 배열 길이
        left, right = 0, n - 1                    # 양 끝에서 시작할 두 포인터
        area = 0                                  # 최대 면적 저장 변수

        while left < right:                       # 포인터가 교차하기 전까지 반복
            # 현재 구간의 용량 계산
            area = max(area, (right - left) * min(height[left], height[right]))
            
            # 낮은 쪽 포인터를 이동 (높은 쪽은 그대로 두는 게 유리)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area                               # 최종 최대 면적 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 모든 쌍을 비교하는 O(n^2) 시도를 하면 시간 초과 발생.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 단순 이중 루프 → 비효율적.
#   → (수정) 양 끝 포인터에서 시작해 낮은 쪽을 이동하는 투 포인터 전략으로 변경.
#   → 시간복잡도 O(n)으로 개선.
#
# 📚 사용된/필수 개념(최소):
# - Two Pointers (양 끝에서 좁혀오기)
# - Greedy: 낮은 쪽을 옮겨야 더 큰 용량 가능
# - 시간복잡도: O(n), 공간복잡도: O(1)
