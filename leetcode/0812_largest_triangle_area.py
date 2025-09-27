# 0812_largest_triangle_area.py
# -----------------------------------------------------
# ✅ 제목: Largest Triangle Area
# ✅ 문제 설명(요약):
# - 평면 위 점들의 집합이 주어진다.
# - 세 점을 선택해 만들 수 있는 삼각형 중 최대 면적을 구하라.
# - 면적은 실수(float)로 반환한다.
#
# ✅ 입력 형식(요지):
# - points: List[List[int]], 각 원소는 [x, y] 좌표
#
# ✅ 규칙 요약:
# 1) 세 점 (a, b, c)을 선택해 삼각형 면적 공식 적용:
#    area = |x_a(y_b - y_c) + x_b(y_c - y_a) + x_c(y_a - y_b)| / 2
# 2) 모든 조합 중 최대값을 갱신
# 3) n ≤ 50 이므로 O(n³) 완전탐색 가능
#
# ✅ 입출력 예시(1개):
# - points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
#   → 최대 면적은 2.0
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        answer = 0
        for i in range(len(points)):                       # 첫 번째 점 선택
            a1, a2 = points[i]
            for j in range(i+1, len(points)):              # 두 번째 점 선택
                b1, b2 = points[j]
                for k in range(j+1, len(points)):          # 세 번째 점 선택
                    c1, c2 = points[k]
                    # 외적 기반 공식으로 면적 계산
                    area = abs(a1*(b2-c2) + b1*(c2-a2) + c1*(a2-b2)) / 2
                    # 최대값 갱신
                    answer = max(answer, area)
        return answer                                      # 최대 면적 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 공식 및 완전탐색 구현으로 정답 반환.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 조건문으로 `area > answer` 비교 후 대입 대신 `max()` 사용해 가독성 개선.
# - 나머지 로직은 올바르게 동작.
#
# 📚 사용된/필수 개념(최소):
# - 삼각형 면적 공식 (외적/슈레이스 공식)
# - 삼중 루프 완전탐색
# - 시간복잡도: O(n³), n ≤ 50이라 충분히 가능

# -----------------------------------------------------
# 다른 풀이
# from typing import List

# class Solution:
#     def largestTriangleArea(self, points: List[List[int]]) -> float:
#         # ---------- 1) 볼록껍질: Andrew monotonic chain ----------
#         pts = sorted(set(map(tuple, points)))
#         if len(pts) < 3:
#             return 0.0

#         def cross(o, a, b):
#             return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

#         # collinear 보존: '< 0'만 팝하여 경계 극점 손실 방지
#         lower = []
#         for p in pts:
#             while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
#                 lower.pop()
#             lower.append(p)

#         upper = []
#         for p in reversed(pts):
#             while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
#                 upper.pop()
#             upper.append(p)

#         hull = lower[:-1] + upper[:-1]   # CCW, 마지막 중복 제거
#         h = len(hull)
#         if h < 3:
#             return 0.0

#         # ---------- 2) 회전 캘리퍼스: O(h^2) ----------
#         def area2(a, b, c):
#             return abs(cross(a, b, c))  # 두 배 면적

#         best2 = 0  # 두 배 면적의 최대값
#         for i in range(h):
#             k = i + 2  # 각 i마다 k 초기화
#             # j를 원형으로 i+1 .. i+h-1 까지 순회(삼각형은 i<j<k 원형 인덱싱으로 표현)
#             for j in range(i + 1, i + h - 1):
#                 j2 = j % h
#                 # k는 최소 j+1 이상이어야 함
#                 if k < j + 1:
#                     k = j + 1
#                 # 면적이 증가/동일(평탄)하는 동안 k 전진
#                 while k + 1 < i + h and \
#                       area2(hull[i], hull[j2], hull[(k + 1) % h]) >= area2(hull[i], hull[j2], hull[k % h]):
#                     k += 1
#                 best2 = max(best2, area2(hull[i], hull[j2], hull[k % h]))

#         return best2 / 2.0
