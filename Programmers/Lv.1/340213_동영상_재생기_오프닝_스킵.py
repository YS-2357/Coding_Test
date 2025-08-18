# 340213_동영상_재생기_오프닝_스킵.py
# -----------------------------------------------------
# ✅ 제목: 동영상 재생기 — 오프닝 자동 스킵과 10초 이동
# ✅ 문제 설명(요약):
# - 길이 video_len의 영상에서 시작 위치 pos부터 명령(commands)을 순서대로 수행한다.
# - 명령은 "prev"(10초 뒤로), "next"(10초 앞으로).
# - 현재 위치가 오프닝 구간 [op_start, op_end]에 걸치면 즉시 op_end로 점프한다.
# - 모든 명령 처리 후 위치를 "mm:ss"로 반환한다.
#
# ✅ 입력 형식(요지):
# - video_len, pos, op_start, op_end: "mm:ss" 문자열
# - commands: ["prev" | "next"] 리스트
#
# ✅ 규칙 요약:
# - prev: 10초 감소, 하한 00:00으로 클램프
# - next: 10초 증가, 상한 video_len으로 클램프
# - 오프닝 스킵: 시작 직후 1회 + 각 명령 처리 직후마다 [op_start, op_end] 포함이면 op_end로 점프
#
# ✅ 입출력 예시(일부)
# - 예) video_len="34:33", pos="13:00", op=[00:55, 02:55], commands=["next","prev"] → "13:00"
# - 예) video_len="10:55", pos="00:05", op=[00:15, 06:55], commands=["prev","next","next"] → "06:55"
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(video_len, pos, op_start, op_end, commands):
    v_min, v_sec = map(int, video_len.split(":"))            # 영상 길이 분/초 파싱
    p_min, p_sec = map(int, pos.split(":"))                  # 현재 위치 분/초 파싱
    s_min, s_sec = map(int, op_start.split(":"))             # 오프닝 시작 분/초
    e_min, e_sec = map(int, op_end.split(":"))               # 오프닝 끝 분/초

    def in_opening(pm, ps):                                  # 오프닝 포함 여부(양끝 포함)
        return (s_min, s_sec) <= (pm, ps) <= (e_min, e_sec)  # 튜플 비교로 분·초 일관 판정

    if in_opening(p_min, p_sec):                              # 시작 직후 1회 스킵 적용
        p_min, p_sec = e_min, e_sec

    for cmd in commands:                                      # 명령 순서대로 처리
        if cmd == "prev":                                     # 10초 뒤로
            if p_sec - 10 < 0:                                # 초가 음수면 분 차감
                if p_min == 0:                                # 이미 0분이면 00:00 고정
                    p_min, p_sec = 0, 0
                else:
                    p_min -= 1                                # 분 -1
                    p_sec = 60 - (10 - p_sec)                 # 초 보정(60에서 빼기)
            else:
                p_sec -= 10                                   # 초에서 바로 10초 차감
        else:                                                 # "next": 10초 앞으로
            if p_sec + 10 >= 60:                              # 초가 60 이상이면 분 올림
                p_min += 1                                    # 분 +1
                p_sec = (p_sec + 10) - 60                     # 초 보정(60 넘긴 만큼)
            else:
                p_sec += 10                                   # 초에 10초 가산

        if (p_min, p_sec) < (0, 0):                           # 하한 클램프(안전)
            p_min, p_sec = 0, 0
        if (p_min, p_sec) > (v_min, v_sec):                   # 상한 클램프(영상 길이)
            p_min, p_sec = v_min, v_sec

        if in_opening(p_min, p_sec):                          # 이동 직후 스킵 재적용
            p_min, p_sec = e_min, e_sec

    return f"{p_min:02d}:{p_sec:02d}"                         # 두 자리 0패딩으로 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **미도달** (초기 풀이에서 다수 테스트 실패 → 현재 버전으로 수정)
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# 1) 오프닝 판정식을 분·초를 따로 비교(OR 조합) → 분 경계에서 오판정
#    → (s_min,s_sec) ≤ (p_min,p_sec) ≤ (e_min,e_sec) 형태의 **튜플 비교**로 수정.
# 2) 스킵 타이밍 누락/혼선(시작 직후 미적용, 마지막에만 재확인 등)
#    → **시작 직후 1회** + **각 명령 처리 직후마다** 스킵을 적용하도록 순서 정립.
# 3) 초 경계 처리 오류(≥/</= 혼동)로 59↔60 전환 버그
#    → prev는 `p_sec-10<0`, next는 `p_sec+10>=60` 기준으로 올바르게 분 이동.
# 4) 상한 클램프에서 분·초를 따로 비교
#    → `(p_min,p_sec) > (v_min,v_sec)`로 일관 비교.
# 5) 출력 포맷 0패딩 누락("13:0","6:55")
#    → `f"{p_min:02d}:{p_sec:02d}"`로 두 자리 고정.
#
# 📚 사용한/필요한 개념(최소):
# - 시각 비교의 **튜플(사전식) 비교**
# - 이동 후 **클램프 → 스킵** 순서 보장
# - 분/초 경계에서의 올림·내림 보정
