# 0407_trapping_rain_water_ii.py
# -----------------------------------------------------
# ✅ 제목: Trapping Rain Water II (LeetCode 407)
# ✅ 문제 설명(요약):
# - m×n 고도 지도에서 빗물이 고일 수 있는 총량을 구한다.
# - 경계에서 물이 새지 않는 조건 하에 내부 칸 위로 고일 수 있는 물의 양을 합산한다.
#
# ✅ 입력 형식(요지):
# - heightMap: List[List[int]], 크기 m×n (m,n ≥ 1)
#
# ✅ 규칙 요약:
# 1) 물은 네 방향으로만 흘러간다.
# 2) 경계는 외부로 열려 있으므로 “가장 낮은 경계 높이”가 수위를 결정한다.
# 3) 각 칸의 물 높이 = max(0, 경계수위 − 고도).
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
import heapq as hq  # 최소 힙 사용을 위한 모듈 별칭

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])                 # 격자 크기 계산
        if m < 3 or n < 3:                                       # 3x3 미만이면 물이 고일 수 없음
            return 0

        boundary = []                                            # 경계 셀들을 담을 힙 컨테이너
        visited = [[False] * n for _ in range(m)]               # 방문(수위 확정) 여부

        for i in range(m):
            boundary.append((heightMap[i][0], i, 0))            # 왼쪽 열 경계 삽입
            boundary.append((heightMap[i][-1], i, n-1))         # 오른쪽 열 경계 삽입
            visited[i][0] = True                                # 경계 방문 처리
            visited[i][-1] = True

        for j in range(1, n-1):
            boundary.append((heightMap[0][j], 0, j))            # 위쪽 행 경계(모서리 제외) 삽입
            boundary.append((heightMap[-1][j], m-1, j))         # 아래쪽 행 경계(모서리 제외) 삽입
            visited[0][j] = True                                # 경계 방문 처리
            visited[-1][j] = True
        
        hq.heapify(boundary)                                     # 경계들을 최소 힙으로 구성
        answer = 0                                               # 누적 물의 양
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]                    # 4방향 이동 벡터
        
        while boundary:                                          # 힙이 빌 때까지 반복
            h, x, y = hq.heappop(boundary)                       # 가장 낮은 경계 수위 꺼냄

            for dx, dy in dirs:                                  # 이웃 4칸 순회
                nx, ny = x + dx, y + dy                          # 이웃 좌표
                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]:  # 범위 밖/이미 확정이면 스킵
                    continue
                nh = heightMap[nx][ny]                           # 이웃 고도
                level = max(h, nh)                               # 이웃의 새 경계 수위(물이 차면 h, 아니면 nh)
                if nh < h:                                       # 경계보다 이웃이 낮다면
                    answer += h - nh                             # 고인 물 양을 누적
                visited[nx][ny] = True                           # 이웃 수위 확정
                hq.heappush(boundary, (level, nx, ny))           # 새 경계로 힙에 삽입

        return answer                                            # 총 물의 양 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 최소 힙 + BFS 확장으로 정답 통과.
#
# 🔧 오답 이유 및 실수, 사용한 알고리즘 개념:
# - 핵심 개념: 경계에서 안쪽으로 퍼지는 **우선순위 큐(최소 힙) 기반 탐색**.
#   - 힙에서 꺼낸 높이 h가 해당 칸의 **확정 경계 수위**.
#   - 이웃 nh < h면 물 h−nh를 채우고, 새 경계는 level=max(h,nh).
# - 실수 포인트(수정 완료):
#   1) 이웃 방문 표시(visited)는 **푸시 직전**에 해야 중복 푸시 방지.
#   2) 이웃은 **항상 푸시**해야 탐색이 이어짐. 물 더하기는 조건부.
#
# 📚 시간·공간 복잡도:
# - 시간: O(mn log(mn))  (각 칸이 힙에 최대 1회 삽입/삭제)
# - 공간: O(mn)          (visited, 힙)
#
# -----------------------------------------------------
# (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 동일 로직의 바텀업 구현만 존재. 복잡도 근본 개선은 불가.
# - 메모리 절약: visited를 비트세트로 대체 가능(언어별).
