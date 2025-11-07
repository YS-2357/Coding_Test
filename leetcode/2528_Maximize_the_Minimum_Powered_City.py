# 2528_Maximize_the_Minimum_Powered_City.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2528. Maximize the Minimum Powered City
# ✅ 문제 설명(요약):
#   - n개의 도시가 일렬로 있고, 각 도시는 stations[i]개의 발전소를 가진다.
#   - 도시 i의 실제 전력은 반경 r 내의 발전소 총합이다.
#   - k개의 발전소를 추가로 어디든 설치할 수 있다.
#   - 모든 도시 전력의 최소값을 최대화하는 것이 목표이다.
#
# ✅ 입력 형식(요지):
#   stations: List[int] — 각 도시의 발전소 수
#   r: int — 발전소 영향 반경
#   k: int — 추가로 설치할 수 있는 발전소 개수
#
# ✅ 규칙 요약:
#   - “모든 도시 전력 ≥ X”가 가능한지 여부를 판별(check 함수).
#   - 가능한 X의 최대값을 이분 탐색으로 찾는다.
#   - check 함수 내부는 차분 배열(Difference Array)과 그리디 보충으로 구현.
#
# ✅ 정답 코드(⚠️ 나의 풀이 아님)
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        cnt = [0] * (n + 1)

        # 초기 전력 분포를 차분 배열 형태로 계산
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            cnt[left] += stations[i]
            cnt[right] -= stations[i]

        # 주어진 목표 전력 val 이상을 만족할 수 있는지 확인
        def check(val: int) -> bool:
            diff = cnt.copy()            # 차분 복제 (현재 전력 상태)
            total = 0                    # 현재 도시의 누적 전력
            remaining = k                # 남은 추가 발전소 수

            for i in range(n):
                total += diff[i]          # 현재 위치까지의 누적 전력
                if total < val:           # 부족할 경우
                    add = val - total     # 필요한 발전소 수
                    if remaining < add:   # 여분이 부족하면 불가능
                        return False
                    remaining -= add
                    end = min(n, i + 2 * r + 1)  # 영향 구간 끝 지점
                    diff[end] -= add              # 이후 구간 영향 제거
                    total += add                  # 즉시 보충
            return True

        lo, hi = min(stations), sum(stations) + k
        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):                # mid 전력을 만족할 수 있으면
                res = mid
                lo = mid + 1              # 더 큰 값 탐색
            else:
                hi = mid - 1              # 불가능하면 감소
        return res
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 이분 탐색과 차분 배열을 통한 효율적 검증 구조.
#   - check(val) 한 번당 O(n), 전체 O(n log U)로 통과.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 나의 풀이가 아닌 참고 풀이.
#   - 핵심 개념:
#       1. **Binary Search on Answer** — 가능한 최소 전력을 탐색.
#       2. **Difference Array** — 발전소 추가의 범위 효과를 O(1)에 반영.
#       3. **Greedy Left-to-Right Fill** — 부족한 도시를 만날 때 즉시 보충.
#
# 📚 시간·공간 복잡도:
#   - check 함수: O(n)
#   - 전체 이분 탐색: O(n log(sum(stations) + k))
#   - 공간복잡도: O(n)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 세그먼트 트리나 누적합을 이용해 “현재 전력 합”을 관리할 수도 있으나,
#     차분 배열 방식이 가장 단순하고 빠르다.
# -----------------------------------------------------
# ⚠️ 본 코드는 “참고 풀이”이며, 나의 직접 풀이가 아님을 명시함.
