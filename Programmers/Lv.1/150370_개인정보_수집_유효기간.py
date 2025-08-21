# 150370_개인정보_수집_유효기간.py
# -----------------------------------------------------
# ✅ 제목: 개인정보 수집 유효기간 — 28일 달력으로 만료 판정
# ✅ 문제 설명(요약):
# - today, terms(약관종류→개월), privacies(수집일 + 약관종류)가 주어진다.
# - 모든 달은 28일로 계산하며, "수집일 + 약관개월"이 되는 날 0시에 만료가 시작된다.
# - 오늘(today) 기준 만료된 항목의 인덱스를 오름차순으로 반환한다.
#
# ✅ 입력 형식(요지):
# - today: "YYYY.MM.DD"
# - terms: ["A 6", "B 12", ...]
# - privacies: ["YYYY.MM.DD A", ...]
#
# ✅ 규칙 요약:
# - 일수 환산: to_days(y,m,d) = y*12*28 + m*28 + d
# - 만료 시작일 = 수집일(일수) + 약관개월*28
# - today_days ≥ 만료 시작일이면 만료된 것으로 본다.
#
# ✅ 입출력 예시(간단):
# - today = "2022.05.19"
# - terms = ["A 6", "B 12", "C 3"]
# - privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
#   → 반환: [1, 3]
#
# ✅ 정답 코드
def to_days(y, m, d):
    return int(y)*12*28 + int(m)*28 + int(d)

def solution(today, terms, privacies):
    answer = []
    yy, mm, dd = today.split(".")
    todays = to_days(yy, mm, dd)
    # print(todays)
    
    hash = {}
    for term in terms:
        tp, tt = term.split()
        hash[tp] = int(tt)*28
    # print(hash)
    
    for idx, privacy in enumerate(privacies):
        p_date, p_type = privacy.split()
        y, m, d = p_date.split(".")
        p_days = to_days(y, m, d)
        if todays - p_days >= hash[p_type]:
            answer.append(idx+1)
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - 28일 달력 기준으로 날짜를 정수 일수로 환산
# - 약관 종류→개월을 일수로 미리 변환해 O(1) 비교
# - 만료 조건: today_days ≥ (수집일_days + term_months*28) ↔ (today_days - 수집일_days) ≥ term_days
