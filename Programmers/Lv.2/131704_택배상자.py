# 131704_택배상자.py
# -----------------------------------------------------
# ✅ 제목: 택배상자
# ✅ 문제 설명(요약):
# - 메인 벨트(1→n 순서로 상자 도착)와 보조 컨테이너(스택)를 사용해
#   주어진 order 순서대로 최대 몇 개의 상자를 실을 수 있는지 구한다.
#
# ✅ 입력 형식(요지):
# - order: List[int], 실어야 하는 상자 순서(1..n의 순열)
#
# ✅ 규칙 요약:
# 1) 메인 벨트에서는 현재 번호(current)만 꺼낼 수 있음.
# 2) 바로 실을 수 없으면 보조 스택에 임시 보관 가능(맨 위만 적재 가능).
# 3) 스택의 top이 다음으로 실어야 할 상자(need)와 같으면 즉시 실음.
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(order):
    loaded = 0                      # 실은 상자 개수 누적
    stack = []                      # 보조 컨테이너(스택)
    n = len(order)                  # 총 상자 수
    current, idx = 1, 0             # current: 메인 벨트 다음 번호, idx: order 인덱스(need 위치)
    
    while current <= n:             # 메인 벨트에서 꺼낼 수 있을 동안 반복
        if order[idx] == current:   # 메인에서 바로 실을 수 있으면
            loaded += 1             # 적재
            current += 1            # 메인 다음 번호로
            idx += 1                # 다음 need로 이동
        elif stack and stack[-1] == order[idx]:  # 스택 top이 need면
            stack.pop()             # 스택에서 꺼내
            loaded += 1             # 적재
            idx += 1                # 다음 need로
        else:                       # 어느 쪽도 아니면
            stack.append(current)   # 메인 번호를 스택에 임시 보관
            current += 1            # 메인 다음 번호로
    
    while stack and stack[-1] == order[idx]:  # 메인 소진 후에도 스택에서 실을 수 있으면 반복
        loaded += 1                # 적재
        idx += 1                   # 다음 need
        stack.pop()                # 스택 pop (반드시 pop해야 중복 처리/무한루프 방지)
    
    return loaded                  # 최대 적재 수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 스택과 메인 벨트를 올바르게 병행: 핵심 로직(need 비교, push/pop, 적재) 구현됨.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 스택과 비교 시 current와 비교하는 실수 → need(order[idx])와 비교로 수정.
# - (이전) 스택에 push할 때 idx를 증가시키는 실수 → “적재”가 아니므로 증가 금지로 수정.
# - (잠재) **idx 경계 체크**: 모든 상자를 다 실은 뒤(`idx == n`)에도 `order[idx]`를 참조하면 IndexError.
#   → 루프 조건에 `idx < n` 가드를 두거나, 적재 직후 `idx == n`이면 즉시 종료하는 안전장치 권장.
#
# 📚 사용된/필수 개념(최소):
# - 스택(LIFO) 시뮬레이션 + 투 포인터(current, idx)
# - 그리디: 가능할 때 즉시 적재, 아니면 스택 보관
# - 시간복잡도: O(n) (각 상자 최대 1회 push/pop), 공간복잡도: O(n)
#
# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 구현 안전성 강화를 위해:
#   * 메인 while: `while current <= n and idx < n:`
#   * 마지막 while: `while stack and idx < n and stack[-1] == order[idx]:`
#   이렇게 경계 가드를 추가하면 예외 없이 견고해진다(로직은 동일).

# -----------------------------------------------------
# 다른 풀이
# def solution(order):
#     answer = 0

#     stack = []
#     for idx, num in enumerate(order):
#         stack.append(idx+1)

#         while stack and stack[-1] == order[answer]:
#             stack.pop()
#             answer +=1

#     return answer
