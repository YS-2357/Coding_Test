# 43105_정수_삼각형.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 주어진 삼각형에서 위에서 아래로 내려오면서 선택할 수 있는 경로 중
#   숫자의 합이 가장 큰 경로를 찾는 문제.
# - 아래로 내려갈 때는 바로 아래 칸 또는 아래 오른쪽 칸으로만 이동할 수 있다.

# ✅ 입력 형식:
# - triangle: 2차원 리스트, 삼각형 형태 (높이 1 이상 500 이하)
# - 각 숫자: 0 이상 9,999 이하

# ✅ 출력 형식:
# - 맨 아래층까지 이동하면서 얻을 수 있는 최대 합을 정수로 반환
# -----------------------------------------------------

def solution(triangle):
    # ✅ DP 테이블 생성 (삼각형과 같은 크기, 모든 값을 0으로 초기화)
    DP = [[0] * len(triangle) for _ in range(len(triangle))]
    
    # ✅ 시작점 초기화 (삼각형 꼭대기)
    DP[0][0] = triangle[0][0]

    # ✅ 삼각형을 위에서부터 한 줄씩 내려가며 DP 테이블 채우기
    for width in range(1, len(triangle)):
        for col in range(width + 1):
            # 왼쪽 위에서 오는 경우
            if col - 1 >= 0:
                DP[width][col] = DP[width-1][col-1] + triangle[width][col]
            
            # 바로 위에서 오는 경우 (두 경우 중 최대값 선택)
            if DP[width-1][col]:
                DP[width][col] = max(DP[width][col], DP[width-1][col] + triangle[width][col])

    # ✅ 맨 마지막 줄에서 최댓값 반환
    return max(DP[-1])

# -----------------------------------------------------
# ✅ 주요 구현 전략:
# - DP[i][j]: i번째 줄의 j번째 칸까지 내려오는 최대 합을 저장
# - 이전 줄의 왼쪽 대각선과 바로 위에서 오는 경우를 비교하여 최대값 저장
# - 마지막 줄(DP[-1])에서 가장 큰 값을 결과로 반환

# ✅ 2단계에서의 주요 실수 및 수정 사항:
# 1️⃣ DP 초기화 시 삼각형 크기만큼 정확히 할당했는지 확인 필요
# 2️⃣ col-1 인덱스 체크: 음수 인덱스 방지를 위해 조건문 추가
# 3️⃣ 두 경로(왼쪽 대각선/바로 위) 중 최대값을 선택하는 로직을 명확히 작성

# -----------------------------------------------------
# ✅ 프로그래머스 제출용 최종 정답 코드. 테스트케이스 통과 가능.
# -----------------------------------------------------
