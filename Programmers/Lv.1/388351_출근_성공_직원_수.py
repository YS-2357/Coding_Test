# 388351_출근_성공_직원_수.py
# -----------------------------------------------------
# ✅ 제목: 일주일 출근 기록에서 지각 없는 직원 수 구하기
# ✅ 문제 설명(요약):
# - 직원별 희망 출근 시각(schedules)과 실제 출근 기록(timelogs, 1주 7일)이 주어진다.
# - 희망 시각 + 10분 이내에 들어오면 그 날은 성공으로 본다.
# - 주말(토/일)은 제외하며, startday에 따라 한 주의 요일 인덱스가 달라진다.
# - 일주일 동안(평일만) 단 하루도 지각이 없는 직원의 수를 구한다.
#
# ✅ 입력 형식(요지):
# - schedules: List[int]  # 예: 930(=09:30), 1015(=10:15)
# - timelogs : List[List[int]]  # 직원별 7일 도착 시각 HHMM 정수
# - startday : int  # 시작 요일 인덱스(문제 정의에 따름)
#
# ✅ 규칙 요약:
# - 허용 기준: 도착시간 ≤ (희망시간 + 10분)
# - 주말(토/일)은 건너뛴다(요일 계산은 startday 기준으로 순서 매핑).
# - 한 주(평일) 동안 모두 기준 이하면 그 직원은 ‘지각 없음’으로 카운트.
#
# ✅ 입출력 예시(간단):
# - schedules = [930, 1000]
# - timelogs  = [[930, 932, 941, 900, 1000, 959, 930],
#                [1005, 1012, 1009, 1000, 1008, 1200, 1111]]
# - startday = 1
#   → 결과: 1  (첫 번째 직원만 평일 전부 기준 만족이라고 가정한 예)
#
# ✅ 정답 코드(너의 원본 코드; 그대로 유지)
def solution(schedules, timelogs, startday):
    answer = 0
    
    hash = {}
    for idx, schedule in enumerate(schedules):
        hour, min = schedule // 100, schedule % 100
        min += 10
        if min >= 60:
            hour += 1
            min -= 60
        hash[idx] = [hour * 100 + min, True]
    
    for idx, timelog in enumerate(timelogs):
        for i in range(len(timelog)):
            day = (i + startday) % 7
            if day == 6 or day == 0:
                continue
            if hash[idx][1] and hash[idx][0] < timelog[i]:
                hash[idx][1] = False
    # print(hash)
    answer = sum([1 for key, value in hash.items() if value[1]])
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - HHMM 정수를 시간/분으로 분리 후 **+10분 보정**(분 올림 처리)
# - 요일 인덱싱: `(i + startday) % 7`로 해당 날짜의 요일 계산, 주말 제외
# - 직원별로 평일 전부 통과했는지 플래그로 추적해 최종 합산
