# 0006_zigzag_conversion.py
# -----------------------------------------------------
# ✅ 제목: Zigzag Conversion
# ✅ 문제 설명(요약):
# - 문자열 s와 행 수 numRows가 주어진다.
# - 문자열을 지그재그 형태로 행렬에 배치한 후, 행 단위로 읽어 새로운 문자열을 반환한다.
#
# ✅ 입력 형식(요지):
# - s: str (1 ≤ len(s) ≤ 1000)
# - numRows: int (1 ≤ numRows ≤ len(s))
#
# ✅ 규칙 요약:
# 1) 행은 0 ~ numRows-1까지 존재.
# 2) row=0부터 row=numRows-1까지 아래로 내려가며 문자 채움.
# 3) 맨 아래에 도달하면 대각선 위로 올라가며 채움.
# 4) 끝까지 반복 후, 각 행을 이어붙여 결과 생성.
#
# ✅ 입출력 예시(1개):
# - s = "PAYPALISHIRING", numRows = 3
#   배치:
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
#   결과 → "PAHNAPLSIIGYIR"
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):  # 행이 1이거나 문자열 길이보다 크면 변환 불필요
            return s

        rows = [""] * numRows                  # 각 행에 문자를 모을 리스트
        row = 0                                # 현재 행 위치
        step = 1                               # 이동 방향 (아래=+1, 위=-1)
        i = 0                                  # 문자열 인덱스

        while i < len(s):                      # 문자열 끝까지 순회
            rows[row] += s[i]                  # 현재 행에 문자 추가

            if row == 0:                       # 맨 위에 도달하면 아래로 이동
                step = 1
            elif row == numRows - 1:           # 맨 아래에 도달하면 위로 이동
                step = -1

            row += step                        # 행 갱신
            i += 1                             # 다음 문자로 이동

        return "".join(rows)                   # 각 행을 합쳐서 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - step을 단순히 토글(step *= -1)해서 시작 시 바로 음수가 되어 IndexError 발생.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 방향 전환을 단순 토글 → 시작점(row=0)에서도 잘못된 방향 전환 발생.
#   → (수정) 경계 조건에서만 step을 명시적으로 설정:
#      row==0 → step=1, row==numRows-1 → step=-1.
#
# 📚 사용된/필수 개념(최소):
# - 문자열 시뮬레이션, while 반복문 제어
# - 조건 분기(경계에서 방향 전환)
# - 시간복잡도: O(n), 공간복잡도: O(n)
