# 42748_K번째수.py
# ------------------------------------------------------
# ✅ 문제 설명:
# - 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때,
#   k번째에 있는 수를 구하는 문제.
#
# ✅ 입력 형식:
# - array: (1 ≤ array의 길이 ≤ 100)
# - commands: (1 ≤ commands의 길이 ≤ 50)
#   - commands[i] = [i, j, k] (1-based 인덱스)
#
# ✅ 출력 형식:
# - 각 command에 대해 결과를 배열로 반환
#
# ✅ 입출력 예제:
# 🔹 입력:
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#
# 🔹 출력:
# [5, 6, 3]
# ------------------------------------------------------

def solution(array, commands):
    answer = []
    for lst in commands:
        start = lst[0]  # 시작 인덱스 (1-based)
        end = lst[1]    # 끝 인덱스 (1-based)
        want = lst[2]   # 원하는 값의 위치 (1-based)

        # ✅ 1. start-1부터 end까지 슬라이싱 후 정렬
        sub_array = sorted(array[start-1:end])

        # ✅ 2. 정렬된 배열에서 want번째 값 추가
        answer.append(sub_array[want-1])  # 1-based이므로 인덱스 조정

    return answer

# ------------------------------------------------------
# ✅ 핵심 요약:
# - 슬라이싱: array[start-1:end]
# - 정렬: sorted(sub_array)
# - 1-based index 조정 필요: sub_array[want-1]
# - 결과를 answer 리스트에 순서대로 저장
# ------------------------------------------------------
