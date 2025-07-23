# 181921_배열_만들기_2.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 두 정수 l, r이 주어짐
# - l 이상 r 이하인 정수 중 각 자리 숫자가 0 또는 5로만 이루어진 모든 수를 찾기
# - 조건을 만족하는 수가 없으면 [-1] 반환
#
# ✅ 입력:
# - l, r (1 ≤ l ≤ r ≤ 1,000,000)
#
# ✅ 출력:
# - 조건을 만족하는 정수 리스트 (오름차순)
#
# -----------------------------------------------------

from collections import deque  # BFS 구현을 위한 deque 사용

def solution(l, r):
    answer = []  # 조건을 만족하는 결과 저장 리스트
    queue = deque(['5'])  # BFS 시작 (문자열 '5'부터 시작, '0'은 맨 앞자리에서 의미 없으므로 제외)

    # ✅ BFS 탐색 시작
    while queue:
        current = queue.popleft()  # 큐에서 가장 앞의 값을 꺼냄
        num = int(current)  # 문자열을 정수로 변환

        # ✅ 현재 숫자가 r보다 크면 더 이상 진행 불필요 (가지치기)
        if num > r:
            continue

        # ✅ 조건 만족 시 결과 리스트에 추가
        if num >= l:
            answer.append(num)

        # ✅ 다음 숫자 생성: '0'과 '5'를 붙여서 새로운 조합을 큐에 추가
        queue.append(current + '0')
        queue.append(current + '5')

    # ✅ 조건을 만족하는 숫자가 하나도 없으면 [-1] 반환
    if not answer:
        return [-1]

    # ✅ 오름차순 정렬 후 반환
    return sorted(answer)

# -----------------------------------------------------
# ✅ 사용된 개념:
# - BFS(너비 우선 탐색): 가능한 숫자를 큐를 이용해 차례대로 생성
# - 문자열 조합으로 숫자 생성 후 int()로 변환
# - 가지치기: 현재 숫자가 r보다 크면 확장하지 않음
# - 시간복잡도: 생성되는 숫자의 개수 ≪ (r - l) 범위 → 매우 효율적
# -----------------------------------------------------

# def solution(l, r):
#     answer = []
    
#     for i in range(l, r+1):
#         if all(num in ['0', '5'] for num in str(i)):
#             answer.append(i)
            
#     if len(answer) == 0:
#         answer.append(-1)
    
#     return answer
