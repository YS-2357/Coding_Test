# 0085_Maximal Rectangle.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 85. Maximal Rectangle
# 🏷️ 유형: 스택 / 히스토그램 / DP(누적 높이)
#
# ✅ 문제 설명(요약):
#   - 0/1로 이루어진 이진 행렬에서, '1'로만 구성된 직사각형의 최대 넓이를 구한다.
#   - 각 행을 기준으로 "히스토그램 높이"를 누적하고, 히스토그램 최대 직사각형을 계산해 최댓값을 갱신한다.
#
# ✅ 입력 형식(요지):
#   - matrix: List[List[str]]  (각 원소는 '0' 또는 '1')
#
# ✅ 규칙 요약:
#   - 직사각형은 행/열에 평행한 축 정렬 직사각형이다.
#   - 비어있는 행렬이면 0을 반환한다.
#
# 🧠 핵심 불변식(Invariant):
#   - heights[i]는 현재 행까지 연속된 '1'의 누적 높이(히스토그램의 높이)이다.
#   - stack은 heights 인덱스를 "높이가 증가하는 순"으로 유지하는 단조 증가 스택이다.
#   - heights에 끝 처리용 0을 추가하면, 각 행마다 스택을 완전히 비울 수 있다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                        # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def maximalRectangle(self, matrix: List[List[str]]) -> int:         # 행렬에서 만들 수 있는 최대 직사각형 넓이를 반환하는 함수
        if not matrix:                                                  # 행렬이 비어있는 경우를 확인
            return 0                                                    # 직사각형을 만들 수 없으므로 0 반환
        
        rows, cols = len(matrix), len(matrix[0])                        # 행과 열의 크기를 각각 rows, cols로 저장
        heights = [0] * (cols + 1)                                      # 각 열의 히스토그램 높이를 저장하며 마지막에 센티넬 0을 둠
        max_area = 0                                                    # 최대 직사각형 넓이를 저장할 변수 초기화
        
        for row in matrix:                                              # 행렬의 각 행을 위에서 아래로 순회
            for i in range(cols):                                       # 현재 행의 각 열 인덱스를 순회
                heights[i] = heights[i] + 1 if row[i] == '1' else 0     # '1'이면 높이를 1 증가, '0'이면 높이를 0으로 리셋
            
            stack = []                                                  # 단조 증가 스택을 각 행마다 새로 초기화
            for i in range(len(heights)):                               # 센티넬을 포함한 heights 전체를 순회
                while stack and heights[i] < heights[stack[-1]]:        # 현재 높이가 스택 top 높이보다 작으면 직사각형 계산 시작
                    h = heights[stack.pop()]                            # 팝된 막대의 높이를 h로 저장
                    w = i if not stack else i - stack[-1] - 1           # 팝 이후의 스택 상태로 폭 w를 계산
                    max_area = max(max_area, h * w)                     # 높이 h와 폭 w로 넓이를 계산해 최대값 갱신
                stack.append(i)                                         # 현재 인덱스를 스택에 푸시하여 단조 증가 조건 유지
        
        return max_area                                                 # 전체 행을 처리한 뒤의 최대 넓이를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 행별 히스토그램 누적 + 단조 스택을 이용한 히스토그램 최대 직사각형 계산.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(rows * cols)  (각 행마다 각 인덱스가 스택에 1회 push/pop)
#   - 공간: O(cols)         (heights와 stack)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - left/right 경계를 유지하는 DP 방식(각 행마다 연속 '1'의 좌우 경계 갱신)도 가능하나,
#     단조 스택 방식이 구현과 증명이 더 직관적인 편이다.
