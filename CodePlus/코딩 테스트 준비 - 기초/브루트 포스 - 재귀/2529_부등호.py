# 백준 2529번: 부등호
# 문제 설명:
# - `k`개의 부등호 (`<`, `>`)가 주어질 때, 0~9 사이의 숫자 중 중복 없이 `k+1`개의 숫자를 선택하여 부등호 관계를 만족하는 최댓값과 최솟값을 찾아야 한다.

# 입력 형식:
# - 첫 번째 줄에 `k`가 주어진다. (1 ≤ `k` ≤ 9)
# - 두 번째 줄에는 `k`개의 부등호가 공백을 사이에 두고 주어진다.

# 출력 형식:
# - 첫째 줄에 부등호 관계를 만족하는 최댓값을 출력한다.
# - 둘째 줄에 부등호 관계를 만족하는 최솟값을 출력한다.

# 예제 입력 1:
# 2
# < >
# 예제 출력 1:
# 897
# 021

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline().strip())  # 부등호 개수
ineq_signs = sys.stdin.readline().split()  # 부등호 리스트
results = []  # 결과를 저장할 리스트
visited = [False] * 10  # 숫자 사용 여부 체크

def backtrack(count, num_list):
    """ 백트래킹을 이용해 부등호 관계를 만족하는 숫자 조합을 찾는 함수 """
    if count == N + 1:  # ✅ 숫자 (N+1)개를 선택한 경우
        results.append("".join(map(str, num_list)))  # 리스트를 문자열로 변환 후 저장
        return

    for i in range(10):  # 0~9 숫자 선택
        if not visited[i]:  # 중복 숫자 방지
            if count == 0 or (ineq_signs[count - 1] == '<' and num_list[-1] < i) or (ineq_signs[count - 1] == '>' and num_list[-1] > i):
                visited[i] = True
                backtrack(count + 1, num_list + [i])
                visited[i] = False  # 백트래킹 (원상 복구)

# ✅ 최댓값 찾기 (큰 숫자부터 탐색)
backtrack(0, [])
max_result = results[-1]  # 가장 마지막에 추가된 값이 최댓값

# ✅ 최솟값 찾기 (작은 숫자부터 탐색)
results.clear()  # 리스트 초기화
backtrack(0, [])
min_result = results[0]  # 가장 먼저 추가된 값이 최솟값

# ✅ 결과 출력
print(max_result)
print(min_result)

# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 부등호 비교 시 인덱스 오류 발생 (`ineq_signs[count]`)
#    - 기존 코드: `ineq_signs[count] == '<'`
#    - ❌ 문제점: `count == N`일 때 `ineq_signs[count]`에 접근하면 IndexError 발생.
#    - ✅ 해결: `if count == 0 or (ineq_signs[count - 1] == '<' and num_list[-1] < i)` 조건 추가.

# 2. ✅ 최댓값과 최솟값을 구하는 방법이 비효율적
#    - 기존 코드: 최댓값과 최솟값을 찾기 위해 두 개의 리스트(`plusle`, `minun`)를 유지.
#    - ❌ 문제점: 중복된 코드가 많아 비효율적.
#    - ✅ 해결: `backtrack()`을 두 번 실행하여 최댓값과 최솟값을 각각 구함.

# 3. ✅ 숫자 리스트 변환 시 `IndexError` 발생 가능
#    - 기존 코드: `' '.join(num + ' ' + sign for num, sign in zip(plusle, ineq_signs)) + ' ' + plusle[-1]`
#    - ❌ 문제점: `plusle[-1]`이 존재하지 않을 경우 `IndexError` 발생 가능.
#    - ✅ 해결: 백트래킹이 끝난 후 `''.join(map(str, plusle))` 방식으로 변환.

# -----------------------------------------------------
# 📌 몰랐던 점 (힌트 제공 내용)

# 🔹 최댓값을 찾을 때는 **큰 숫자부터 탐색** (`9~0` 순서로 선택)
# 🔹 최솟값을 찾을 때는 **작은 숫자부터 탐색** (`0~9` 순서로 선택)
# 🔹 `backtrack()` 함수를 재사용하여 중복된 코드 최소화
# 🔹 `num_list + [i]` 방식으로 리스트를 새롭게 만들어 백트래킹을 수행

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
