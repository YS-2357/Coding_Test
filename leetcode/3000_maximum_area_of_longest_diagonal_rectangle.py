# 3000_maximum_area_of_longest_diagonal_rectangle.py
# -----------------------------------------------------
# ✅ 제목: Maximum Area of Longest Diagonal Rectangle
# ✅ 문제 설명(요약):
# - 여러 직사각형의 가로·세로 길이가 주어진다.
# - 각 직사각형의 대각선 길이 √(w²+h²)를 비교하여 가장 긴 대각선을 찾는다.
# - 대각선 길이가 같은 경우에는 넓이가 가장 큰 직사각형을 선택한다.
# - 해당 직사각형의 넓이를 반환한다.
#
# ✅ 입력 형식(요지):
# - dimensions: List[List[int]], 각 원소는 [w, h] 형태의 직사각형 크기
#
# ✅ 규칙 요약:
# 1) 대각선 비교 시 √ 대신 w²+h² 사용 (실수 오차 방지).
# 2) 더 큰 대각선 제곱 → 후보 갱신.
# 3) 대각선 제곱이 같으면 넓이 비교 → 더 큰 넓이로 갱신.
#
# ✅ 입출력 예시(1개):
# - dimensions = [[3,4],[6,8],[5,12]]
#   → 대각선 제곱: 25, 100, 169
#   → 가장 큰 대각선: (5,12), 넓이=60
#   → 정답 = 60
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = [0, 0, [0, 0]]                      # [인덱스, 대각선 제곱, (w,h)]

        for i, dim in enumerate(dimensions):
            s = dim[0] * dim[0] + dim[1] * dim[1]      # 대각선 제곱
            if s > max_area[1]:                        # 더 긴 대각선이면 갱신
                max_area[0] = i
                max_area[1] = s
                max_area[2] = [dim[0], dim[1]]
            elif s == max_area[1]:                     # 대각선 길이가 같으면
                if dim[0] * dim[1] > max_area[2][0] * max_area[2][1]:  # 넓이 비교
                    max_area[0] = i
                    max_area[2] = [dim[0], dim[1]]
        
        x, y = dimensions[max_area[0]]                 # 최종 선택된 직사각형
        return x * y                                   # 넓이 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 올바르게 동작했지만 구조를 리스트로 관리해 조금 복잡함.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 대각선 비교만 하고 넓이 비교 조건을 빠뜨릴 수 있었음.
#   → (수정) elif s == max_area[1]일 때 넓이 비교 조건 추가.
#
# 📚 사용된/필수 개념(최소):
# - 정수 연산으로 대각선 비교 (sqrt 불필요)
# - 조건 분기: 대각선 크기 >, == 시 처리
# - 시간복잡도: O(n), 공간복잡도: O(1)
