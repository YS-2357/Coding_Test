# ✅ 마지막 문제(과일 맛 조합) 풀이
# 문제: 과일 맛 상태가 이진 문자열로 주어지고,
# k개를 조합했을 때 나올 수 있는 맛 조합의 가짓수

from itertools import combinations

def fruit_combinations(fruit_list, k):
    result_set = set()
    for combo in combinations(fruit_list, k):
        taste = 0
        for f in combo:
            taste |= int(f, 2)  # 비트 OR 합치기
        result_set.add(taste)
    return len(result_set)

# ✅ 예제
fruit_list = ["1011", "1100", "0011", "0110"]
k = 2
result = fruit_combinations(fruit_list, k)
print(f"가능한 맛 조합 가짓수: {result}")
