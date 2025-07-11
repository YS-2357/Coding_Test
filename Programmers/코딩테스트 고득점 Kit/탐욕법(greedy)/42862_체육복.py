# 42862_체육복.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 전체 학생 수 n명 중 일부는 체육복을 도난당했고(lost), 일부는 여벌 체육복이 있음(reserve)
# - 도난당한 학생은 양옆 번호 학생에게만 체육복을 빌릴 수 있음
# - 체육 수업을 들을 수 있는 최대 학생 수를 구하라

# ✅ 입력 형식:
# - n: 전체 학생 수 (2 ≤ n ≤ 30)
# - lost: 체육복을 도난당한 학생 번호 리스트
# - reserve: 여벌 체육복이 있는 학생 번호 리스트

# ✅ 출력 형식:
# - 체육 수업을 들을 수 있는 최대 학생 수 (정수)

# ✅ 입출력 예제:
#   입력: n = 5, lost = [2, 4], reserve = [1, 3, 5]
#   출력: 5

# -----------------------------------------------------

def solution(n, lost, reserve):
    # reserve와 lost에 모두 있는 학생은 여벌을 잃어버렸다고 간주 → 제거
    real_lost = [l for l in lost if l not in reserve]
    real_reserve = [r for r in reserve if r not in lost]

    # 그리디 탐색을 위해 정렬
    real_lost.sort()
    real_reserve.sort()

    # 기본적으로는 체육복이 없는 학생 수만큼 수업을 못 들음
    answer = n - len(real_lost)

    # 체육복을 빌릴 수 있는지 체크
    for number in real_lost:
        if number - 1 in real_reserve:
            real_reserve.remove(number - 1)
            answer += 1
        elif number + 1 in real_reserve:
            real_reserve.remove(number + 1)
            answer += 1

    return answer

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ real_lost와 real_reserve를 정렬하지 않아서 탐색 순서가 꼬일 수 있음 → 최적해 보장 안 됨
# ❌ number + 1만 먼저 검사할 경우, 그리디 특성상 순서에 따라 결과 달라질 수 있음
# ✅ 정렬 후 number - 1 먼저 검사 → 문제 조건에 충실한 탐색

# ✅ GPT가 준 힌트 요약:
# - 그리디 알고리즘은 정렬이 선행되어야 가장 가까운 값부터 처리할 수 있음
# - 리스트 제거 시 remove()는 O(N)이지만, 제한 조건(n ≤ 30)이 작아서 무방함
# - 동시에 reserve와 lost에 있는 학생은 사전에 제거해야 정확성 향상

# ✅ 사용된 개념 요약:
# - 그리디 알고리즘: 현재 상황에서 가장 이득이 되는 선택을 반복
# - 정렬: 순차적으로 탐색하기 위해 필요
# - 예외 처리: 여벌이 있는 학생이 도난당한 경우 중복 제거
# - 조건 분기: 앞번호 또는 뒷번호가 여벌을 가진 경우 빌림 처리

# -----------------------------------------------------
