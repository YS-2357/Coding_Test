# 120812_최빈값_구하기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 배열에서 가장 많이 등장하는 값(최빈값)을 구한다.
# - 최빈값이 여러 개면 -1을 반환한다.
#
# ✅ 입력:
# - array: 길이 1 이상 100 이하의 정수 배열 (0 ≤ 원소 ≤ 100)
#
# ✅ 출력:
# - 최빈값 (단, 여러 개면 -1)
#
# ✅ 예시:
#   입력: [1, 2, 3, 3, 3, 4] → 출력: 3
#   입력: [1, 1, 2, 2] → 출력: -1
# -----------------------------------------------------

def solution(array):
    # ✅ 1. 각 숫자의 등장 횟수를 저장할 딕셔너리 초기화
    counts = {}

    # ✅ 2. 배열 순회하며 빈도 계산
    for number in array:
        # counts.get(number, 0): number가 없으면 0, 있으면 기존 값
        counts[number] = counts.get(number, 0) + 1

    # ✅ 3. 최빈값과 최대 빈도 초기화
    max_count = 0         # 최대 등장 횟수
    mode = -1             # 최빈값 (결과)
    multiple_modes = False # 최빈값이 여러 개인지 여부

    # ✅ 4. 딕셔너리 순회하며 최빈값 결정
    for number, count in counts.items():
        if count > max_count:
            # 새로운 최댓값 발견 → 갱신
            max_count = count
            mode = number
            multiple_modes = False  # 새로운 최댓값이므로 중복 아님
        elif count == max_count:
            # 동일한 최대 등장 횟수가 또 나오면 중복 플래그 설정
            multiple_modes = True

    # ✅ 5. 결과 반환
    if multiple_modes:
        return -1   # 최빈값이 여러 개면 -1
    else:
        return mode # 그렇지 않으면 mode 반환

# -----------------------------------------------------
# ✅ 사용된 개념 요약:
# - 딕셔너리를 활용한 **빈도 계산**
#   - counts[number] = counts.get(number, 0) + 1
# - 최대 빈도와 최빈값 비교 갱신
#   - count > max_count → 새로운 최빈값
#   - count == max_count → 중복 여부 체크
#
# ✅ 시간 복잡도:
# - O(n): 배열 순회 후 딕셔너리 순회 (n은 array 길이)
# ✅ 공간 복잡도:
# - O(k): k는 서로 다른 값의 개수 (최대 101)
# -----------------------------------------------------

# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1
