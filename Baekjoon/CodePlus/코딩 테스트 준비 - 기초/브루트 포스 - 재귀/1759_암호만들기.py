# 백준 1759번: 암호 만들기
# 문제 설명:
# 주어진 C개의 문자 중 L개의 알파벳을 선택해 암호를 만든다.
# - 최소 한 개의 모음 (a, e, i, o, u)을 포함해야 한다.
# - 최소 두 개의 자음이 포함되어야 한다.
# - 알파벳이 오름차순 정렬된 순서여야 한다.

# 입력 형식:
# - 첫 번째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15)
# - 두 번째 줄에 C개의 서로 다른 소문자 알파벳이 주어진다.

# 출력 형식:
# - 조건을 만족하는 암호를 한 줄에 하나씩 사전순으로 출력한다.

# 예제 입력 1:
# 4 6
# a t c i s w
# 예제 출력 1:
# acis
# acit
# aciw
# actw
# aist
# aisw
# aitw
# cist
# cisw
# citw
# istw

import sys

# ✅ 입력 처리 (알파벳 정렬)
L, C = map(int, sys.stdin.readline().split())
alphabets = sorted(sys.stdin.readline().split())  # 사전순 정렬

# ✅ 모음 리스트
aeiou = {'a', 'e', 'i', 'o', 'u'}

# ✅ 백트래킹 함수 정의
def find_code(index, current_code):
    if len(current_code) == L:  # 길이가 L이면 조건 검사 후 출력
        vowel_count = sum(1 for char in current_code if char in aeiou)
        consonant_count = L - vowel_count  # 전체 길이 - 모음 개수 = 자음 개수
        if vowel_count >= 1 and consonant_count >= 2:
            print("".join(current_code))
        return

    for i in range(index, C):  # 현재 인덱스 이후의 문자만 선택
        find_code(i + 1, current_code + [alphabets[i]])  # 다음 문자 선택

# ✅ 암호 찾기 시작
find_code(0, [])

# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 리스트 입력 처리 오류
#    - 기존 코드: `alphabets = sorted(sys.stdin.readline().split)`
#    - ❌ 문제점: `split`이 실행되지 않음 (메서드 객체가 됨).
#    - ✅ 수정: `sorted(sys.stdin.readline().split())`로 변경하여 정렬된 리스트 저장.

# 2. ✅ `for` 루프에서 `i` 변수 정의 오류
#    - 기존 코드: `for i in range(i, C):`
#    - ❌ 문제점: `i`가 정의되지 않은 상태에서 `range(i, C)` 사용.
#    - ✅ 수정: `for i in range(index, C):`로 변경.

# 3. ✅ `find_code(0, [])` 호출 오류
#    - 기존 코드: `print(0, [])`
#    - ❌ 문제점: 백트래킹 탐색을 시작하지 않고 `print(0, [])`를 출력.
#    - ✅ 수정: `find_code(0, [])`를 호출하여 암호 찾기 시작.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
