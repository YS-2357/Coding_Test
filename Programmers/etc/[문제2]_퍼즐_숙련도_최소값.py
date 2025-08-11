# [문제2]_퍼즐_숙련도_최소값.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 퍼즐 n개, 각 난이도 diffs[i], 시간 times[i]
# - 숙련도 level에 따라 diff > level이면 (diff - level)번 틀리고
#   틀릴 때마다 현재+이전 퍼즐 시간 소모, 마지막에 한 번 더 현재 퍼즐 시간 소모
# - 제한 시간 limit 내에 모두 풀 수 있는 최소 level 구하기.

# ✅ 입력 형식:
# - diffs, times: 길이 n(1 ≤ n ≤ 300,000)
# - diffs[0] = 1, 1 ≤ diffs[i] ≤ 100,000
# - 1 ≤ times[i] ≤ 10,000
# - 1 ≤ limit ≤ 10^15
# - 항상 해가 존재

# ✅ 출력 형식:
# - 최소 숙련도 level (정수)

# ✅ 입출력 예시:
# diffs=[1,5,3], times=[2,4,7], limit=30 → 3

# ✅ 정답 코드:
def solution(diffs, times, limit):
    n = len(diffs)

    # 주어진 level에서 소요 시간 계산
    def total_time(level):
        total = times[0]                 # 첫 퍼즐은 난이도 1, 무조건 한 번에 해결
        for i in range(1, n):
            if level >= diffs[i]:
                total += times[i]
            else:
                fails = diffs[i] - level
                total += fails * (times[i] + times[i-1]) + times[i]
        return total

    # 이진 탐색으로 최소 level 찾기
    lo, hi = 1, max(diffs)
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if total_time(mid) <= limit:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 도출 (힌트 사용 안 함)

# 📚 사용된 개념 요약:
# - level → 시간 함수가 단조 감소함을 이용해 이진 탐색
# - 각 퍼즐 시간 계산: diff ≤ level → 단순합, diff > level → 실패 횟수 계산
# - 시간복잡도: O(n log max_diff)
