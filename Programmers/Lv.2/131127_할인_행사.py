# 131127_할인_행사.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 회원가입 조건: 10일 동안 구매할 상품이 want 리스트와 number 개수와 정확히 일치
# - discount 리스트에서 10일 연속 구간을 검사, 조건 만족 시 count
#
# ✅ 입력:
# - want: 원하는 제품 이름 리스트
# - number: 각 제품의 필요한 개수
# - discount: 날짜별 할인 상품 리스트
#
# ✅ 출력:
# - 조건 만족하는 시작 날짜 개수
#
# ✅ 예시:
# want = ["banana", "apple", "rice", "pork", "pot"]
# number = [3, 2, 2, 2, 1]
# discount = [...]
# 출력: 3
# -----------------------------------------------------

def solution(want, number, discount):
    answer = 0  # 조건을 만족하는 경우의 수 저장
    window = discount[:10]  # 첫 10일 구간(슬라이딩 윈도우)
    discount = discount[10:]  # 나머지 데이터

    # ✅ 윈도우가 정확히 10일일 때만 반복
    while len(window) == 10:
        # ✅ 조건 검사:
        # want와 number 쌍에 대해 모든 조건이 만족하면 True
        if all(window.count(w) == n for w, n in zip(want, number)):
            answer += 1  # 조건 만족 → 경우 수 증가
        
        # ✅ 윈도우 슬라이딩:
        # 1) 기존 윈도우에서 첫 번째 요소 제거
        # 2) discount에서 새 요소 추가
        window = window[1:10]
        if discount:
            window.append(discount[0])  # 새 요소 추가
            discount.pop(0)  # discount에서 제거

    return answer  # 조건 만족 횟수 반환

# -----------------------------------------------------
# ✅ 나의 오답 및 실수:
# ❌ 초기 시도에서 조건 체크 후 break 또는 continue 사용 → answer 업데이트 안 됨
# ❌ 매번 window.count()를 호출 → O(10) × len(want) → 비효율적
#
# ✅ GPT가 준 힌트 요약:
# - Counter를 사용하거나 dict로 윈도우 상태를 관리하면 O(1) 갱신 가능
# - 조건 비교는 all()로 깔끔하게 처리 가능
#
# ✅ 사용된 개념 요약:
# - 슬라이딩 윈도우: 10일 구간을 이동하며 검사
# - all() + zip(): 조건 일괄 검사
# - 리스트 슬라이싱과 append/pop으로 윈도우 갱신
#
# ✅ 더 효율적인 알고리즘:
# - collections.Counter 사용:
#   1) 초기 Counter(discount[:10])
#   2) 조건 검사 시 all(counter[w] == n for ...)
#   3) 윈도우 이동 시 O(1) 업데이트 (counter[item] += 1 / -= 1)
# - 시간복잡도: 현재 방식 O(n*m), Counter 방식 O(n)
# -----------------------------------------------------

# from collections import Counter

# def solution(want, number, discount):
#     answer = 0  # 조건 만족 횟수
#     n = len(discount)
    
#     # ✅ 초기 윈도우 Counter 생성
#     window_counter = Counter(discount[:10])
    
#     # ✅ 조건 비교 함수: 현재 Counter와 목표 조건 비교
#     def is_valid():
#         return all(window_counter[w] == n for w, n in zip(want, number))
    
#     # ✅ 첫 윈도우 검사
#     if is_valid():
#         answer += 1

#     # ✅ 슬라이딩 윈도우 시작 (인덱스 10부터 끝까지)
#     for i in range(10, n):
#         # 제거할 상품
#         old_item = discount[i - 10]
#         window_counter[old_item] -= 1
#         if window_counter[old_item] == 0:
#             del window_counter[old_item]  # Counter에서 0개 항목 삭제
        
#         # 새로 추가할 상품
#         new_item = discount[i]
#         window_counter[new_item] += 1
        
#         # 조건 검사
#         if is_valid():
#             answer += 1

#     return answer
