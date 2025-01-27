# 백준 6588번: 골드바흐의 추측
# 문제 설명:
# 6 이상의 짝수를 두 개의 소수의 합으로 나타내는 문제.
# 가장 작은 소수 쌍을 찾아 "n = a + b" 형식으로 출력해야 한다.
# 만약 불가능하면 "Goldbach's conjecture is wrong."을 출력한다.

# 입력 형식:
# 한 줄에 하나의 짝수 n이 주어진다. (6 ≤ n ≤ 1,000,000)
# 입력의 마지막 줄에는 0이 주어지며, 이를 처리하지 말고 종료해야 한다.

# 출력 형식:
# n = a + b (a, b는 소수이며, a < b)
# 가능한 `a, b`가 없으면 "Goldbach's conjecture is wrong." 출력.

# 예제 입력 1:
# 8
# 20
# 42
# 0
# 예제 출력 1:
# 8 = 3 + 5
# 20 = 3 + 17
# 42 = 5 + 37

import sys

# 🛑 [❌ 사용자가 작성한 코드] (틀린 코드)
"""
array = [True] * 1000001
array[0] = array[1] = False
for i in range(2, int(1000001 ** 0.5)+1):
    if array[i]:
        for j in range(i*i, 1000001, i):
            array[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, n//2 + 1):
        if array[i] and array[n-i]:
            print(f"{n} = {i} + {n-i}")
"""

# 📌 [❌ 사용자의 코드에서 틀린 점]
# 1. **골드바흐의 추측이 틀린 경우에 대한 예외 처리가 없음**
#    - 모든 n이 두 소수의 합으로 표현된다고 가정하고 있음.
#    - 예외적으로 표현되지 않는 경우 "Goldbach's conjecture is wrong."을 출력해야 함.
# 2. **출력 후 즉시 종료가 필요 (`break` 추가)**
#    - 가장 작은 (i, n-i) 조합을 찾으면 더 이상 탐색할 필요 없음.
#    - `break`를 추가하여 불필요한 연산을 방지해야 함.

---

# ✅ [✔ 모범 답안: 올바르게 수정된 코드]
# - 소수 판별을 효율적으로 수행하기 위해 "에라토스테네스의 체" 사용
# - 입력받은 범위 내의 모든 소수를 빠르게 출력하기 위해 `sys.stdin.read()` 사용

def sieve_of_eratosthenes(limit):
    """
    에라토스테네스의 체를 사용하여 1부터 limit까지의 소수를 판별하는 함수.
    소수이면 True, 아니면 False로 설정된 리스트를 반환.
    """
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:  # i가 소수이면
            for j in range(i * i, limit + 1, i):
                sieve[j] = False  # i의 배수들은 소수가 아님

    return sieve

# 최대 범위 설정 및 소수 판별 리스트 생성
MAX_N = 1000000
is_prime = sieve_of_eratosthenes(MAX_N)

# 입력 처리
input = sys.stdin.read
numbers = map(int, input().split())  # 여러 줄 입력 처리

# 골드바흐의 추측 계산
for n in numbers:
    if n == 0:
        break  # 0이 입력되면 종료
    
    found = False  # 소수 쌍을 찾았는지 여부 확인

    # 2부터 n//2까지 검사
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:  # 두 수가 모두 소수라면
            print(f"{n} = {i} + {n - i}")
            found = True
            break  # 가장 작은 소수 쌍을 찾으면 출력 후 종료
    
    if not found:
        print("Goldbach's conjecture is wrong.")
