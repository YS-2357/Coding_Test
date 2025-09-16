# 92341_주차요금계산.py
# -----------------------------------------------------
# ✅ 제목: 주차 요금 계산
# ✅ 문제 설명(요약):
# - 입출차 기록이 주어졌을 때 각 차량의 누적 주차 시간을 계산한 후,
#   주어진 요금 정책에 따라 차량별 요금을 산출하는 문제.
#
# ✅ 입력 형식(요지):
# - fees = [기본시간, 기본요금, 단위시간, 단위요금]
# - records = ["HH:MM 차량번호 IN/OUT", ...]
#
# ✅ 규칙 요약:
# 1) 출차 기록이 없는 차량은 23:59에 자동 출차한 것으로 간주.
# 2) 누적 주차시간 ≤ 기본시간 → 기본요금만 청구.
# 3) 초과시간 → 올림(ceil) 단위 계산:
#    기본요금 + ⌈(누적시간-기본시간)/단위시간⌉ × 단위요금.
# 4) 결과는 차량번호 오름차순으로 정렬하여 반환.
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
def solution(fees, records):
    answer = []
    in_time = {}                        # 입차 중인 차량의 입차시각 기록
    total = {}                          # 차량별 누적 주차 시간(분)

    for record in records:              # 모든 입출차 기록 순회
        time, num, status = record.split()
        if status == "IN":              # 입차일 경우
            in_time[num] = time
        else:                           # 출차일 경우
            in_h, in_m = in_time[num].split(":")
            out_h, out_m = time.split(":")
            # 출차시각 - 입차시각 = 이번 구간의 주차시간
            total[num] = total.get(num, 0) + ((int(out_h)*60 + int(out_m)) - (int(in_h)*60 + int(in_m)))
            in_time[num] = 0            # 입차 기록 소멸

    for key, value in in_time.items():  # 하루 끝(23:59)까지 출차되지 않은 차량 처리
        if value != 0:
            in_h, in_m = value.split(":")
            total[key] = total.get(key, 0) + (23*60 + 59) - (int(in_h)*60 + int(in_m))
            in_time[key] = 0

    for key, value in sorted(total.items()):   # 차량번호 기준 정렬
        if value > fees[0]:                    # 기본시간 초과 시
            # 초과시간을 단위시간으로 나눠 올림한 뒤 단위요금 곱
            fee = fees[1] + ((value - fees[0] + fees[2] - 1) // fees[2]) * fees[3]
        else:                                  # 기본시간 이내면 기본요금
            fee = fees[1]
        answer.append(fee)                     # 결과 리스트에 추가
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 차량별 IN/OUT 시각을 정확히 누적하고, 출차 없는 차량도 23:59 처리.
# - 차량번호 정렬 후 요금 계산까지 구현되어 정답을 만족.

# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기에는 total을 단일 변수로 두어 누적 불가 → 차량별 dict(total[num])로 수정.
# - 출차 없는 차량을 고려하지 않아 누락 → 23:59 처리 루프 추가.
# - 초과시간 요금을 단순 나눗셈으로 처리 → 올림(ceil) 연산으로 보정.

# 📚 사용된/필수 개념(최소):
# - 딕셔너리(dict) 활용: 차량별 입차 기록과 누적 시간 관리
# - 시간 파싱: "HH:MM" → 분 단위 환산
# - 올림 나눗셈 구현: (a+b-1)//b
# - 정렬: 차량번호 오름차순 보장
# - 시간복잡도: O(N + K log K) (N=기록 수, K=차량 수)

# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - `defaultdict(int)`로 total 초기화 시 get() 호출 생략 가능.
# - in_time 딕셔너리 대신, 출차 시 바로 누적하고 제거하는 방식으로 관리 단순화 가능.
