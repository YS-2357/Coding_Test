# -----------------------------------------------------
# ✅ 문제 설명:
# - N×M 크기의 배열이 주어지고, 반시계 방향으로 R번 회전해야 한다.
# - 배열의 가장 바깥쪽 테두리부터 안쪽으로 여러 개의 "레이어(껍질)"를 나눠서 회전한다.
# - R개의 회전을 수행한 후, 최종 배열을 출력한다.
#
# ✅ 입력 형식:
# - 첫 번째 줄: `N M R` (2 ≤ N, M ≤ 300, 1 ≤ R ≤ 10^9)
# - 이후 N개의 줄: 배열 원소 (1 ≤ 원소 ≤ 1000)
#
# ✅ 출력 형식:
# - R번 회전한 후의 배열을 출력
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   4 4 1
#   1 2 3 4
#   5 6 7 8
#   9 10 11 12
#   13 14 15 16
# 🔹 예제 출력 1:
#   2 3 4 8
#   1 7 11 12
#   5 6 10 16
#   9 13 14 15
# -----------------------------------------------------

import sys

# ✅ 입력 처리 (빠른 입력을 위해 sys.stdin.readline 사용)
N, M, R = map(int, sys.stdin.readline().split())  # 행(N), 열(M), 회전 횟수(R)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 2차원 배열 입력

# ✅ 배열을 레이어(껍질) 단위로 회전하는 함수
def rotate_layers(board, N, M, R):
    num_layers = min(N, M) // 2  # 총 레이어 개수 (가장 바깥쪽부터 안쪽으로)

    for layer in range(num_layers):
        # ✅ 현재 레이어의 경계 좌표 설정
        sx, sy = layer, layer  # 좌상단 좌표
        ex, ey = N - layer - 1, M - layer - 1  # 우하단 좌표

        # ✅ 현재 레이어의 주기 계산 (한 바퀴 도는 길이)
        cycle_length = 2 * ((ex - sx + 1) + (ey - sy + 1) - 2)

        # ✅ 불필요한 회전을 줄이기 위해 R을 주기로 나눔
        rotate_count = R % cycle_length  

        # ✅ 회전할 필요가 없으면 스킵
        if rotate_count == 0:
            continue

        # ✅ 1. 레이어를 리스트로 변환
        elements = []
        
        # 🔹 → (왼쪽 → 오른쪽) (맨 윗줄)
        for j in range(sy, ey + 1):
            elements.append(board[sx][j])  # (sx, j)

        # 🔹 ↓ (위쪽 → 아래쪽) (맨 오른쪽 줄)
        for i in range(sx + 1, ex + 1):
            elements.append(board[i][ey])  # (i, ey)

        # 🔹 ← (오른쪽 → 왼쪽) (맨 아래줄)
        if sx != ex:  
            for j in range(ey - 1, sy - 1, -1):
                elements.append(board[ex][j])  # (ex, j)

        # 🔹 ↑ (아래쪽 → 위쪽) (맨 왼쪽 줄)
        if sy != ey:
            for i in range(ex - 1, sx, -1):
                elements.append(board[i][sy])  # (i, sy)

        # ✅ 2. 리스트를 R % 주기 칸 회전
        rotated = elements[rotate_count:] + elements[:rotate_count]

        # ✅ 3. 회전된 리스트를 다시 원래 배열에 채워넣기
        idx = 0  # rotated 리스트의 인덱스
        
        # 🔹 → (왼쪽 → 오른쪽) (맨 윗줄)
        for j in range(sy, ey + 1):
            board[sx][j] = rotated[idx]  # (sx, j)
            idx += 1

        # 🔹 ↓ (위쪽 → 아래쪽) (맨 오른쪽 줄)
        for i in range(sx + 1, ex + 1):
            board[i][ey] = rotated[idx]  # (i, ey)
            idx += 1

        # 🔹 ← (오른쪽 → 왼쪽) (맨 아래줄)
        if sx != ex:  
            for j in range(ey - 1, sy - 1, -1):
                board[ex][j] = rotated[idx]  # (ex, j)
                idx += 1

        # 🔹 ↑ (아래쪽 → 위쪽) (맨 왼쪽 줄)
        if sy != ey:
            for i in range(ex - 1, sx, -1):
                board[i][sy] = rotated[idx]  # (i, sy)
                idx += 1

# ✅ 배열 회전 수행
rotate_layers(board, N, M, R)

# ✅ 최종 결과 출력
for row in board:
    print(*row)

# -----------------------------------------------------
# 16926_배열_돌리기_1.py과 차이점은 R을 주기로 나눈 것 뿐이다.
