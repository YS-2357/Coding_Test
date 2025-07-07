# 백준 1107번: 리모컨
# 문제 설명:
# 현재 채널 100에서 시작하여 목표 채널 N으로 이동하는 최소 버튼 클릭 횟수를 찾는 문제.
# - 숫자 버튼(0~9)과 `+`, `-` 버튼을 이용해 이동 가능.
# - 고장난 버튼이 있을 수 있음.

# 입력 형식:
# 첫째 줄에 이동하려는 채널 N이 주어진다. (0 ≤ N ≤ 500,000)
# 둘째 줄에 고장난 버튼 개수 M이 주어진다. (0 ≤ M ≤ 10)
# 셋째 줄에 고장난 버튼 M개가 공백으로 구분되어 주어진다. (없을 경우 입력 없음)

# 출력 형식:
# 최소한의 버튼 클릭 횟수를 출력한다.

# 예제 입력 1:
# 5457
# 3
# 6 7 8
# 예제 출력 1:
# 6

from itertools import product

# 🛑 [❌ 사용자가 작성한 코드] (틀린 코드)
"""
from itertools import product

initial = 100
channel = int(input())
n = int(input())
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for _ in range(n):
    nums.remove(int(input()))

minimum = 499900
candidates = list(product(nums, repeat=len(str(channel))))
for i in range(len(candidates)):
    candidate = "".join(candidates[i])  # ❌ 문자열 조합에서 튜플을 join하려는 오류
    candidate = int(candidate)  # ✅ 올바르게 정수 변환
    value = abs(channel - candidate)
    if value < minimum:
        minimum = value
        
print(minimum + len(str(channel)))  # ❌ 최소 클릭 횟수 계산이 올바르지 않음
"""

# 📌 [❌ 사용자의 코드에서 틀린 점]
# 1. **문자열 조합 오류**
#    - `candidates`는 튜플의 리스트 형태이므로 `"".join(candidates[i])`가 올바르게 동작하지 않음.
#    - **수정 방법:** `"".join(map(str, candidates[i]))` 사용하여 숫자를 문자열로 변환 후 결합.
# 2. **최소 클릭 횟수 계산이 올바르지 않음**
#    - `+` 또는 `-` 버튼을 사용하는 경우를 고려하지 않음.
#    - 목표 채널과 가장 가까운 숫자를 찾고, **이 숫자로부터 `+` 또는 `-`를 이용해 목표 채널까지 이동해야 함**.

---

# ✅ [✔ 모범 답안: 올바르게 수정된 코드]
# - `product()`를 사용하여 목표 채널과 같은 자릿수의 가능한 모든 조합을 생성.
# - 가장 가까운 숫자를 찾은 후 `+`, `-` 버튼을 고려하여 최소 버튼 클릭 횟수를 계산.

def get_closest_channel(N, usable_buttons):
    """
    목표 채널 N과 가장 가까운 숫자를 찾아서 반환하는 함수.
    """
    min_clicks = abs(N - 100)  # + / - 버튼만 이용할 경우

    # 숫자 버튼이 고장나지 않았다면, 가능한 모든 숫자 조합을 생성하여 탐색
    for length in range(1, len(str(N)) + 2):  # 목표 채널의 자릿수 ±1까지 탐색
        for candidate in product(usable_buttons, repeat=length):
            candidate_number = int("".join(map(str, candidate)))
            clicks = len(str(candidate_number)) + abs(candidate_number - N)
            min_clicks = min(min_clicks, clicks)

    return min_clicks

# 입력 처리
N = int(input())  # 목표 채널
M = int(input())  # 고장난 버튼 개수
if M > 0:
    broken_buttons = set(map(int, input().split()))
else:
    broken_buttons = set()

# 사용 가능한 버튼 리스트 생성
usable_buttons = [i for i in range(10) if i not in broken_buttons]

# 최소 클릭 횟수 계산
result = get_closest_channel(N, usable_buttons)
print(result)


# 또는
# 백준 문제 1107: 리모컨

# 표준 입력을 사용하기 위해 sys 모듈을 임포트
import sys

# 목표 채널과 고장난 버튼의 개수와 리스트를 입력받음
target = int(sys.stdin.readline().strip())  # 목표 채널을 입력받음
n = int(sys.stdin.readline().strip())  # 고장난 버튼의 개수를 입력받음
broken_buttons = set(sys.stdin.readline().split()) if n > 0 else set()  # 고장난 버튼의 리스트를 입력받아 집합으로 변환

# 현재 채널에서 목표 채널까지 이동하기 위한 최솟값을 초기화 (현재 채널은 100번)
min_presses = abs(target - 100)

# 모든 가능한 채널(0부터 999999까지)에 대해 브루트포스 탐색
for num in range(1000000):
    num_str = str(num)  # 숫자를 문자열로 변환하여 각 자리를 검사
    for digit in num_str:
        if digit in broken_buttons:  # 만약 숫자가 고장난 버튼에 포함되면
            break  # 더 이상 검사할 필요 없이 루프를 탈출
    else:
        # 고장난 버튼이 없는 경우
        presses = len(num_str) + abs(num - target)  # 숫자를 누르는 횟수 + 목표 채널까지 이동하는 횟수
        min_presses = min(min_presses, presses)  # 최솟값을 업데이트

# 결과 출력
print(min_presses)
