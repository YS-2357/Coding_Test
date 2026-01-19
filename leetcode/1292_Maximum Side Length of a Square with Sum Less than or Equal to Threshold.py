# 1292_Maximum Side Length of a Square with Sum Less than or Equal to Threshold.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# 🏷️ 유형: 2D 누적합 / 이분탐색
#
# ✅ 문제 설명(요약):
#   - 양의 정수 행렬 mat에서, 합이 threshold 이하인 정사각형(축 정렬)의 최대 한 변 길이를 구한다.
#   - 가능한 가장 큰 변 길이를 반환한다.
#
# ✅ 입력 형식(요지):
#   - mat: List[List[int]]  (m×n 양의 정수)
#   - threshold: int
#
# ✅ 규칙 요약:
#   - 정사각형의 원소 합이 threshold 이하이면 “유효”하다.
#   - 유효한 정사각형 중 최대 변 길이를 찾는다.
#
# 🧠 핵심 불변식(Invariant):
#   - 2D prefix sum으로 임의의 k×k 정사각형 합을 O(1)에 계산할 수 있다.
#   - “길이 k가 가능하면 k보다 작은 길이도 가능”이라는 단조성이 성립하므로 이분탐색이 가능하다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#
# -----------------------------------------------------
# ✅ 정답 1 (2D Prefix Sum + Binary Search)

class Solution:                                                         # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:# threshold 이하 합을 갖는 최대 정사각형 변 길이를 구하는 함수
        m, n = len(mat), len(mat[0])                                     # 행렬의 행(m)과 열(n) 크기를 저장

        prefix = [[0] * (n + 1) for _ in range(m + 1)]                   # 2D 누적합(prefix) 배열을 0으로 초기화

        for i in range(m):                                               # mat의 각 행 i를 순회
            for j in range(n):                                           # mat의 각 열 j를 순회
                prefix[i + 1][j + 1] = (                                 # (i, j)까지의 누적합을 점화식으로 계산
                    prefix[i][j + 1]                                     # 위쪽 영역 누적합
                    + prefix[i + 1][j]                                   # 왼쪽 영역 누적합
                    - prefix[i][j]                                       # 중복된 좌상단 영역 누적합을 제거
                    + mat[i][j]                                          # 현재 칸 값을 더해 최종 누적합 완성
                )

        left, right = 1, min(m, n)                                       # 이분탐색 범위를 가능한 변 길이 1..min(m,n)로 설정
        ans = 0                                                          # 가능한 최대 변 길이를 저장할 변수 초기화

        while left <= right:                                             # 이분탐색 범위가 유효한 동안 반복
            mid = (left + right) // 2                                    # 현재 검사할 변 길이 mid를 선택
            isValid = False                                              # 길이 mid의 유효한 정사각형 존재 여부 플래그 초기화

            for i in range(mid, m + 1):                                  # prefix 좌표에서 정사각형의 아래 경계 i를 순회
                for j in range(mid, n + 1):                              # prefix 좌표에서 정사각형의 오른쪽 경계 j를 순회
                    total = (                                            # (i-mid, j-mid)~(i-1, j-1) 정사각형 합을 O(1)로 계산
                        prefix[i][j]                                     # 전체 영역 누적합
                        - prefix[i - mid][j]                             # 위쪽 영역을 빼고
                        - prefix[i][j - mid]                             # 왼쪽 영역을 빼고
                        + prefix[i - mid][j - mid]                       # 두 번 빠진 좌상단 영역을 다시 더함
                    )
                    if total <= threshold:                               # 정사각형 합이 threshold 이하라면
                        isValid = True                                   # 길이 mid가 가능하므로 플래그를 True로 설정
                        break                                            # 더 볼 필요 없이 내부 루프 종료
                if isValid:                                              # 이미 가능함을 확인한 경우
                    break                                                # 외부 루프도 종료

            if isValid:                                                  # 길이 mid가 가능하면
                ans = mid                                                # 정답 후보를 mid로 갱신
                left = mid + 1                                           # 더 큰 길이를 탐색하기 위해 left를 올림
            else:                                                        # 길이 mid가 불가능하면
                right = mid - 1                                          # 더 작은 길이를 탐색하기 위해 right를 내림

        return ans                                                       # 최종적으로 가능한 최대 변 길이를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답 1: Accepted.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 2D prefix sum + 길이 단조성 기반 이분탐색.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(m * n * log(min(m, n)))  (각 mid마다 모든 k×k 후보를 스캔)
#   - 공간: O(m * n)                   (prefix 저장)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 이분탐색 대신 k를 증가시키며 가능한 범위를 좁히는 방식도 있으나, 단조성이 명확해 이분탐색이 보편적이다.

# -----------------------------------------------------
# ✅ 정답 2 (2D Prefix Sum + Decreasing Scan)

class Solution:                                                         # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:# threshold 이하 정사각형의 최대 변 길이를 구하는 함수
        n, m = len(mat), len(mat[0])                                     # 행렬 크기를 n(행), m(열)로 저장

        prefix = [[0] * (m + 1) for _ in range(n + 1)]                   # 2D 누적합(prefix) 배열을 0으로 초기화

        for j in range(n + 1):                                           # prefix의 행 인덱스 j를 0..n까지 순회
            for i in range(m + 1):                                       # prefix의 열 인덱스 i를 0..m까지 순회
                prefix[j][i] = mat[j - 1][i - 1] + prefix[j - 1][i] + prefix[j][i - 1] - prefix[j - 1][i - 1]  # 2D 누적합 점화식으로 갱신

        max_side = min(n, m)                                             # 가능한 최대 변 길이를 min(n, m)으로 초기화

        while max_side > 0:                                              # 변 길이를 큰 값부터 1까지 감소시키며 검사
            for j in range(n - max_side + 1):                            # 정사각형의 좌상단 행 j의 가능한 범위를 순회
                for i in range(m - max_side + 1):                        # 정사각형의 좌상단 열 i의 가능한 범위를 순회
                    side = prefix[j + max_side][i + max_side] - prefix[j][i + max_side] - prefix[j + max_side][i] + prefix[j][i]  # 현재 정사각형 합을 O(1)로 계산
                    if side <= threshold:                                # 합이 threshold 이하라면
                        return max_side                                  # 현재 max_side가 최대이므로 즉시 반환
            max_side -= 1                                                # 현재 길이가 불가능하면 변 길이를 1 감소
        
        return 0                                                         # 어떤 정사각형도 불가능한 경우 0 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답 2: Accepted.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 2D prefix sum + 큰 길이부터 내려가며 조기 종료.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(m * n * min(m, n))  (길이를 하나씩 줄이며 전수 검사)
#   - 공간: O(m * n)              (prefix 저장)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - prefix 구축 루프에서 j=0 또는 i=0일 때 mat[-1][-1] 접근이 발생할 수 있어,
#     일반적으로는 1..n, 1..m 범위로 구축하는 구현이 더 안전하다(코드 수정은 금지이므로 경고만).
