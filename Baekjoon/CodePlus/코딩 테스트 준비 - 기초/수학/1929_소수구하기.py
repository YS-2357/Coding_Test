# 백준 1929번: 소수 구하기
# 문제 설명:
# M 이상 N 이하의 모든 소수를 출력하는 문제.
# 소수란 1과 자기 자신만을 약수로 가지는 자연수이다.

# 입력 형식:
# 첫째 줄에 두 개의 자연수 M과 N이 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력 형식:
# M 이상 N 이하의 모든 소수를 한 줄에 하나씩 출력한다.

# 예제 입력 1:
# 3 16
# 예제 출력 1:
# 3
# 5
# 7
# 11
# 13

# 🛑 [❌ 사용자가 작성한 코드] (틀린 코드)
"""
a, b = map(int, input().split())

array = [True] * (b+1)
array[0] = False
array[1] = False

for i in range(2, b+1):  # ❌ 오류 1: i*i 이전에 i가 소수인지 판별되지 않음
    for j in range(i*i, b+1, i):  # ✅ i의 배수를 제거하는 부분은 올바름
        array[j] = False

for k in range(a, b+1):
    if array[k]:
        print(k)
"""

# 📌 [❌ 사용자의 코드에서 틀린 점]
# 1. **소수 여부를 판별하지 않고 배수를 지우기 시작함**  
#    - `for i in range(2, b+1):`에서 `i`가 소수인지 확인하지 않고 `i*i`부터 배수를 지우기 시작함.  
#    - 따라서 `i`가 이미 `False`(소수가 아님)일 경우, 불필요한 연산이 수행될 수 있음.  
# 2. **반복문 최적화 가능 (`i*i ≤ b`까지만 검사하면 됨)**  
#    - 현재 `for i in range(2, b+1):`로 설정했으나 **`i*i > b`가 되면 더 이상 배수를 지울 필요 없음**  
#    - 최적화된 `에라토스테네스의 체`에서는 `for i in range(2, int(b**0.5) + 1):`로 설정하여 불필요한 연산 줄이기 가능.  

---

# ✅ [✔ 모범 답안: 올바른 에라토스테네스의 체 알고리즘]
# - 소수 판별을 효율적으로 수행하기 위해 "에라토스테네스의 체" 사용
# - 입력받은 범위 내의 모든 소수를 빠르게 출력하기 위해 `sys.stdout.write()` 사용

import sys

def sieve_of_eratosthenes(m, n):
    """
    M 이상 N 이하의 모든 소수를 찾는 함수.
    에라토스테네스의 체를 사용하여 빠르게 소수를 판별한다.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    # 소수 판별 및 배수 제거 (i*i ≤ n까지만 검사)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:  # i가 소수이면
            for j in range(i * i, n + 1, i):
                sieve[j] = False  # i의 배수들은 소수가 아님

    # M 이상 N 이하의 소수 출력
    return [str(k) for k in range(m, n + 1) if sieve[k]]

# 입력 처리
m, n = map(int, sys.stdin.readline().split())

# 결과 출력 (sys.stdout.write 사용하여 빠르게 출력)
sys.stdout.write("\n".join(sieve_of_eratosthenes(m, n)) + "\n")
