# 3453_Separate Squares I.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3453. Separate Squares I
# 🏷️ 유형: 이분탐색 / 기하 / 면적 누적
#
# ✅ 문제 설명(요약):
#   - 여러 정사각형이 주어질 때, 어떤 수평선 y = t로 잘라서
#   - 선 아래(또는 왼쪽 정의에 따라 “아래 부분”)에 포함되는 전체 면적이
#   - 전체 면적의 절반이 되도록 하는 t를 찾는다.
#   - 해당 t를 실수로 반환한다.
#
# ✅ 입력 형식(요지):
#   - squares: List[List[int]] 형태의 [x, y, l] 리스트
#     - (x, y)는 정사각형의 좌하단 좌표
#     - l은 한 변의 길이
#
# ✅ 규칙 요약:
#   - 각 정사각형의 전체 면적은 l*l이다.
#   - 수평선 y = t 아래에 포함되는 면적은 “겹치는 높이”에 비례해 l * overlap_height 로 계산된다.
#   - 해는 실수이며, 수치적으로 근사한다.
#
# 🧠 핵심 불변식(Invariant):
#   - t가 커질수록 (선 아래로 포함되는) 면적 curr_area는 단조 증가한다.
#   - 단조성을 이용하면 이분탐색으로 target_area = total_area/2 를 만족하는 t를 찾을 수 있다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                         # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def separateSquares(self, squares: List[List[int]]) -> float:        # 전체 면적을 절반으로 나누는 y값을 찾는 함수
        low, high, total_area = float('inf'), float('-inf'), 0           # low/high는 탐색 범위, total_area는 전체 면적 합 초기화

        for x, y, l in squares:                                          # 각 정사각형 [x, y, l]을 순회
            total_area += l * l                                          # 현재 정사각형의 전체 면적(l*l)을 누적
            low = min(low, y)                                            # 가능한 최저 y 경계를 갱신
            high = max(high, y + l)                                      # 가능한 최고 y 경계를 갱신
        
        target_area = total_area / 2.0                                   # 목표 면적을 전체 면적의 절반으로 설정

        for i in range(60):                                              # 충분한 정밀도를 위해 고정 횟수(60)만큼 이분탐색 반복
            mid = (low + high) / 2.0                                     # 현재 탐색 구간의 중간 y값을 계산

            curr_area = 0                                                # mid 아래에 포함되는 면적을 누적할 변수 초기화
            for _, y, l in squares:                                      # 각 정사각형의 y와 l만 사용하여 계산
                curr_y = max(0, min(l, mid - y))                         # mid와 정사각형의 수직 겹침 높이를 0~l로 클램프
                curr_area += l * curr_y                                  # 겹침 면적(가로 l * 겹침높이 curr_y)을 누적
            
            if curr_area < target_area:                                  # mid 아래 면적이 목표보다 작으면
                low = mid                                                # 더 큰 y에서 면적이 늘어나므로 low를 올림
            else:                                                        # mid 아래 면적이 목표 이상이면
                high = mid                                               # 더 작은 y에서도 가능하므로 high를 내림

        return mid                                                       # 마지막 반복의 mid를 근사 해답으로 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 단조 함수(누적 면적) 위에서의 실수 이분탐색.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(60 * n)  (n은 정사각형 개수, 반복 횟수는 상수)
#   - 공간: O(1)       (상수 변수만 사용)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 겹침 높이 함수가 구간별 선형이므로, 이벤트(y, y+l)를 모아 구간별 면적 기울기를 누적하는 방식(스위프 라인)으로도 풀 수 있다 (개념만).
