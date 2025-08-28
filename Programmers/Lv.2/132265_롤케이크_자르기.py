# 132265_롤케이크_자르기.py
# -----------------------------------------------------
# ✅ 제목: 롤케이크 자르기
# ✅ 문제 설명(요약):
# - 토핑 배열을 한 번 잘라 왼쪽/오른쪽 조각의 “서로 다른 토핑 수”가 같아지는 지점의 개수를 구한다.
# - 자르는 위치는 원소 사이여서 양쪽에 최소 1개 이상 남아야 한다.
#
# ✅ 입력 형식(요지):
# - topping: List[int], 토핑 종류가 나열된 배열
#
# ✅ 규칙 요약:
# 1) prefix[i] = 0..i 구간의 서로 다른 토핑 수
# 2) suffix[i] = i..n-1 구간의 서로 다른 토핑 수
# 3) 모든 i(0..n-2)에 대해 prefix[i] == suffix[i+1]이면 카운트 +1
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(topping):
    n = len(topping)                                  # 전체 길이 n

    prefix = [0] * n                                  # 왼쪽 고유개수 누적 배열
    seen_left = set()                                 # 왼쪽에서 본 토핑 종류 집합
    for i in range(n):                                # 왼쪽부터 스캔
        if topping[i] not in seen_left:               # 처음 보는 토핑이면
            seen_left.add(topping[i])                 # 종류 집합에 추가
        prefix[i] = len(seen_left)                    # 현재까지의 서로 다른 토핑 수 기록
        
    suffix = [0] * n                                  # 오른쪽 고유개수 누적 배열
    seen_right = set()                                # 오른쪽에서 본 토핑 종류 집합
    for i in range(n-1, -1, -1):                      # 오른쪽부터 스캔
        if topping[i] not in seen_right:              # 처음 보는 토핑이면
            seen_right.add(topping[i])                # 종류 집합에 추가
        suffix[i] = len(seen_right)                   # 현재부터 끝까지의 서로 다른 토핑 수 기록
        
    answer = 0                                        # 공평하게 나눌 수 있는 지점 수
    for i in range(n - 1):                            # 마지막 인덱스 직전까지만(오른쪽에 최소 1개 남겨야 함)
        # print(prefix[i], suffix[i+1])               # 디버깅용(왼쪽/오른쪽 고유개수)
        if prefix[i] == suffix[i+1]:                  # i에서 자를 때 왼/오 고유개수 동일하면
            answer += 1                               # 유효한 컷 위치로 카운트
    return answer                                     # 최종 개수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 맞춤. 완전탐색 O(n^2) 대비 O(n)에 해결.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 잠재 실수: 비교 범위를 n-1까지 돌면 오른쪽이 비게 됨 → 범위를 0..n-2로 제한(코드에 반영).
# - 잠재 실수: “고유개수”와 “빈도합계” 혼동 가능 → set의 크기를 사용해 고유개수만 기록.
#
# 📚 사용된/필수 개념(최소):
# - prefix/suffix로 구간의 “서로 다른 원소 수” 전처리
# - 집합(set)로 첫 등장만 카운트
# - 시간복잡도: O(n), 공간복잡도: O(n)
#
# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - Counter로 오른쪽 빈도를 모두 세고, 왼쪽으로 하나씩 옮기며
#   left_types/right_types를 실시간 갱신하는 단일 패스(O(n)) 방식도 가능.

# -----------------------------------------------------
# 다른 풀이
# def solution(topping):
#     # 오른쪽 빈도 맵으로 전부 세고(초기 상태=모두 오른쪽에 있음),
#     # 왼쪽으로 하나씩 옮기면서 “양쪽 고유개수”가 같아지는 지점 카운트.
#     from collections import Counter

#     right = Counter(topping)  # 처음엔 전부 오른쪽
#     left_types = 0
#     right_types = len(right)
#     seen_left = set()

#     answer = 0
#     for i in range(len(topping) - 1):   # 마지막은 자를 수 없으니 n-2까지
#         x = topping[i]

#         # 왼쪽으로 옮기기(처음 보는 토핑이면 왼쪽 고유개수 +1)
#         if x not in seen_left:
#             seen_left.add(x)
#             left_types += 1

#         # 오른쪽에서 제거(빈도가 0되면 오른쪽 고유개수 -1)
#         right[x] -= 1
#         if right[x] == 0:
#             right_types -= 1

#         # 비교
#         if left_types == right_types:
#             answer += 1

#     return answer
