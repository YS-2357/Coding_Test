# 백준 17427번: 약수의 합 2
# 문제 설명:
# 자연수 N이 주어졌을 때, 1부터 N까지의 모든 자연수 i에 대해 i의 모든 약수의 합을 구하는 문제.
# 즉, S(N) = ∑ σ(i) (1 ≤ i ≤ N) 을 구한다.

# 입력 형식:
# 하나의 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

# 출력 형식:
# S(N)을 출력한다.

# 예제 입력 1:
# 10
# 예제 출력 1:
# 87

# ✅ 모범 답안: 시간 복잡도 O(N)으로 최적화된 접근법
# - 파이썬 내장 함수 사용: input(), print(), range()
# - 약수의 개념을 활용하여 각 숫자가 약수로 등장하는 횟수를 이용해 최적화
# - 시간 복잡도 O(N)으로 개선

# 입력 처리
n = int(input())  # 자연수 N 입력

# 약수의 합 계산
result = 0

# 1부터 N까지의 숫자 i가 약수로 등장하는 횟수를 이용
for i in range(1, n + 1):
    result += i * (n // i)  # i는 n//i 번 약수로 등장

# 결과 출력
print(result)
