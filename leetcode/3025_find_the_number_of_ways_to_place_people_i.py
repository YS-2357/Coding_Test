# 3025_find_the_number_of_ways_to_place_people_i.py
# -----------------------------------------------------
# ✅ 제목: Find the Number of Ways to Place People I
# ✅ 문제 설명(요약):
# - 2차원 평면에 n개의 점이 주어진다.
# - 두 점 (xi, yi), (xj, yj)을 선택했을 때 xi ≤ xj, yi ≥ yj 이면
#   좌상단(A), 우하단(B)로 사람을 배치할 수 있다.
# - 단, 그 직사각형 내부(경계 포함)에 다른 점이 없어야 한다.
# - 이러한 (A, B) 쌍의 개수를 구한다.
#
# ✅ 입력 형식(요지):
# - points: List[List[int]], 길이 n (2 ≤ n ≤ 1000)
#
# ✅ 규칙 요약:
# 1) (xA ≤ xB, yA ≥ yB)인 점 쌍만 후보.
# 2) 사이에 제3의 점이 없어야 유효.
# 3) 정렬 후 스캔하면서 직사각형 조건을 만족하고
#    y좌표가 지금까지 본 최대 y보다 큰 경우만 카운트.
#
# ✅ 입출력 예시(1개):
# - points = [[1,3],[2,2],[3,1]]
#   가능한 쌍: (1,3)-(2,2), (1,3)-(3,1) → 총 2
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))           # x 오름차순, y 내림차순 정렬
        n = len(points)
        answer = 0

        for i in range(n):                                 # i: 좌상단 후보
            maxY = -1
            yi = points[i][1]
            for j in range(i+1, n):                        # j: 우하단 후보
                yj = points[j][1]
                if yj <= yi and yj > maxY:                 # 새로운 '가장 높은' 우하단 후보만 카운트
                    answer += 1
                    maxY = yj
        return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 정렬 후 이중 루프, maxY 갱신 로직으로 모든 쌍 올바르게 카운트.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 조건을 yj >= maxY로 작성 → 같은 y값 중복 카운트 발생.
#   → yj > maxY로 고쳐야 직사각형 내부 점이 없는 경우만 카운트됨.
#
# 📚 사용된/필수 개념(최소):
# - 정렬: (x 오름차순, y 내림차순)으로 후보 순서 보장
# - 스캔 시 maxY 업데이트로 내부 점 배제
# - 시간복잡도: O(n^2), 공간복잡도: O(1)
