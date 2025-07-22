# 138476_귤_고르기.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 귤이 k개 필요하다.
# - 귤 크기별 개수가 주어질 때, k개 이상을 고르되, **서로 다른 크기의 개수를 최소화**해야 한다.
# - 가장 많이 있는 크기부터 선택하면 최소 종류로 k개를 채울 수 있다.

# ✅ 입력:
# - k: 필요한 귤 개수 (1 ≤ k ≤ 100,000)
# - tangerine: 귤 크기 리스트 (1 ≤ 길이 ≤ 1,000,000)

# ✅ 출력:
# - 귤 종류의 최소 개수

# ✅ 예시:
#   입력: k = 6, tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
#   출력: 3
#   이유: 크기별 개수 → {1:1, 2:2, 3:2, 4:1, 5:2} → 많이 있는 크기부터 선택 → [5,3,2] → 6개
# -----------------------------------------------------

from collections import Counter

def solution(k, tangerine):
    answer = 0  # 선택한 귤 종류 수
    # ✅ 1. 귤 크기별 개수 세기
    count = {}
    for idx in tangerine:
        if idx not in count:
            count[idx] = 1  # 처음 등장하면 1로 초기화
        else:
            count[idx] += 1  # 이미 있으면 개수 +1
    
    # ✅ 2. 귤 크기별 개수를 내림차순 정렬
    # count.items() → [(크기, 개수), ...]
    count = sorted(count.items(), key=lambda item: item[1])  # 개수 기준 정렬 (오름차순)
    # pop()으로 뒤에서 꺼낼 것이므로 오름차순 정렬 후 pop() 사용 → 내림차순 선택
    
    sums = 0  # 누적 선택 개수
    # ✅ 3. 가장 많은 크기부터 선택하며 k 이상이 될 때까지 반복
    while sums < k:
        # count.pop()[1]: 가장 많은 귤 개수를 꺼내 누적
        sums += count.pop()[1]
        answer += 1  # 종류 1개 추가
    
    return answer

# -----------------------------------------------------
# ✅ 사용된 개념 요약:
# - 딕셔너리 활용: 귤 크기별 개수 계산
# - 정렬: 개수 기준으로 정렬 후 pop()으로 가장 큰 값부터 선택
# - 누적합: sums로 선택 개수 추적
# ✅ 시간 복잡도:
# - Counter(또는 dict): O(n)
# - 정렬: O(m log m) (m은 귤 종류 수)
# - 반복: O(m)
# 전체: O(n + m log m), n ≤ 1,000,000에서 충분히 빠름
# -----------------------------------------------------

# import collections
# def solution(k, tangerine):
#     answer = 0
#     cnt = collections.Counter(tangerine)

#     for v in sorted(cnt.values(), reverse = True):
#         k -= v
#         answer += 1
#         if k <= 0:
#             break
#     return answer
