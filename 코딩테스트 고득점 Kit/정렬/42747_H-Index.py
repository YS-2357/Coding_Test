# 42747_H-Index.py
# ------------------------------------------------------
# ✅ 문제 설명:
# - 연구자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고,
#   나머지 논문이 h번 이하 인용되었다면 h를 H-Index라고 한다.
# - 주어진 citations 리스트로 가능한 최대 H-Index를 구하는 문제.
#
# ✅ 입력 형식:
# - citations: 논문의 인용 횟수가 담긴 리스트 (1 ≤ 길이 ≤ 1000, 0 ≤ 인용 횟수 ≤ 10000)
#
# ✅ 출력 형식:
# - 가능한 최대 H-Index를 정수로 반환
#
# ✅ 입출력 예제:
# 🔹 입력:
# citations = [3, 0, 6, 1, 5]
# 🔹 출력:
# 3
#
# 🔹 설명:
# - 3편의 논문이 각각 3회 이상 인용됨.
# ------------------------------------------------------

def solution(citations):
    answer = 0
    n = len(citations)

    # ✅ 1. h-index 후보를 큰 값부터 차례로 검사
    for i in reversed(range(n+1)):  # i: 0부터 n까지
        # ✅ 2. 인용 수가 i 이상인 논문의 개수 세기
        count = sum(1 for citation in citations if citation >= i)
        
        # ✅ 3. h-index 조건을 만족하는지 검사
        if count >= i:
            return i  # 만족하면 바로 반환

    # ✅ 4. 기본적으로 0 반환 (모두 실패한 경우)
    return answer

# ------------------------------------------------------
# ✅ 핵심 요약:
# - "인용 수가 i 이상인 논문이 i편 이상"을 만족하는 최대 i를 찾는다.
# - 큰 값부터 검사하여 가능한 최대 h를 바로 반환.
# ------------------------------------------------------
