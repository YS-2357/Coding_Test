# 161990_바탕화면_정리.py
# -----------------------------------------------------
# ✅ 제목: 바탕화면 정리 — 아이콘(#)을 모두 포함하는 최소 사각형 좌표 찾기
# ✅ 문제 설명(요약):
# - wallpaper: '.'(빈칸), '#'(아이콘)로 이루어진 문자열 배열.
# - 모든 '#'을 완전히 포함하는 가장 작은 축 정렬 사각형의
#   좌상단 (lux, luy), 우하단 (rdx, rdy) 좌표를 반환하되,
#   우하단은 한 칸 바깥까지(반열림)여야 함.
#
# ✅ 입력 형식(요지):
# - wallpaper: List[str]
#
# ✅ 규칙 요약:
# - 한 번의 스캔으로 '#'의 (행, 열) 최소/최대 인덱스를 갱신.
# - 반환은 [min_row, min_col, max_row+1, max_col+1].
#
# ✅ 입출력 예시(간단):
# - ["..#.", ".##.", "...."] → [0,2,2,4]

def solution(wallpaper):
    answer = []
    lux, luy = len(wallpaper), len(wallpaper[0])  # 좌상단을 크게 시작(최솟값 갱신용)
    rdx, rdy = 0, 0                               # 우하단을 작게 시작(최댓값 갱신용)
    # print(lux, luy, rdx, rdy)
    for i, row in enumerate(wallpaper):
        for j, r in enumerate(row):
            if r == "#":
                lux, luy = min(lux, i), min(luy, j)
                rdx, rdy = max(rdx, i), max(rdy, j)
                # print(lux, luy, rdx, rdy)
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx+1)
    answer.append(rdy+1)
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - 단일 스캔 O(HW)으로 '#'의 행/열 최소·최대 인덱스 갱신
# - 우하단 좌표는 반열림을 위해 +1 보정
