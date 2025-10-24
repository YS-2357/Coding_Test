# 2048_Next_Greater_Numerically_Balanced_Number.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2048. Next Greater Numerically Balanced Number
# ✅ 문제 설명(요약):
#   어떤 양의 정수에서 숫자 d가 정확히 d번 등장하면 numerically balanced라 한다.
#   주어진 n보다 큰 수 중 가장 작은 numerically balanced 수를 구하라.
#
# ✅ 입력 형식(요지):
#   - n: 정수 (0 ≤ n ≤ 10^12 수준)
#
# ✅ 규칙 요약:
#   - 사용 가능한 숫자 d는 1..6로 제한(자릿수 제약으로 d>자릿수 불가).
#   - 각 d는 정확히 d번 등장해야 한다.
#   - 선행 0 불가(본 풀이에선 1..6만 사용).
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        if n == 0: 
            return 1  # n=0이면 가장 작은 균형수 1 반환
        elif n > 1224444: 
            return  # 7자리 최대 균형수 1224444 초과 시 처리가 비어 있음(버그 지점)
        
        l = len(str(n)) + 1  # 탐색 최대 길이(현재는 n 길이+1만 고려)
        used = [0] * 7       # 각 d(1..6)의 사용 횟수 카운터
        cand = set()         # 생성된 균형수 후보 집합(중복 제거)

        def is_balanced():
            for d in range(1, 7):
                if used[d] not in (0, d):  # d는 0번 또는 d번만 허용
                    return False
            return True

        def dfs(path):
            if path and is_balanced():                # 현재까지가 균형이면 후보에 추가
                cand.add(int("".join(path)))
            if len(path) == l:                        # 최대 길이에 도달하면 중단
                return
            for d in range(1, 7):                     # 숫자 1..6 순회
                if used[d] < d:                       # d를 d번 이하로만 사용
                    used[d] += 1                      # 선택
                    path.append(str(d))               # 경로에 추가
                    dfs(path)                         # 다음 자리 탐색
                    path.pop()                        # 복원
                    used[d] -= 1                      # 복원

        dfs([])                                       # 백트래킹 시작
        arr = sorted(cand)                            # 후보 정렬
        i = bisect_right(arr, n)                      # n보다 큰 첫 위치(미수입 상태면 NameError)
        return arr[i]                                 # 해당 원소 반환(범위 밖이면 IndexError)
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 작은 n에서는 일부 정답을 찾을 수 있으나,
#     (1) bisect_right 미수입 → NameError
#     (2) n ≥ 1224444에서 반환 비어 있음 → None 반환 또는 이후 오류
#     (3) 모든 후보 ≤ n인 경우 arr[i]에서 IndexError 발생
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 아이디어: 백트래킹으로 각 d를 최대 d번까지 사용하며 균형수 생성 후, n 초과 최소값 선택.
#   - 문제점:
#     1) 경계값 처리 누락: n > 1224444인 경우 정답은 1666666이어야 하나 공란.
#     2) 후보 생성 범위: l = len(n)+1만 사용해 같은 자릿수 해(=len(n))를 놓칠 수 있음.
#     3) 성능: 균형이 아닌 중간 경로도 전개 → 불필요한 상태가 많아 탐색량 증가.
#     4) 라이브러리 미수입: bisect_right 미수입으로 런타임 에러 발생.
#
# 📚 시간·공간 복잡도:
#   - 시간: 백트래킹 상한은 대략 O(분기^l). 분기는 최대 6이지만 used[d]<d 제약으로 실효 분기는 작아짐.
#           그래도 균형이 아닌 경로까지 전개하므로 최악은 지수적(실전 입력에선 수천~수만 노드 수준).
#   - 공간: O(l) 재귀 스택 + 후보 개수 M에 대해 O(M).
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 자릿수 합 분해: 길이 L에 대해 ∑d∈S d = L를 만족하는 S⊆{1..6}만 고려.
#   - 타이트 DFS(숫자 DP): (pos, tight, greater, remain[1..6])로 N을 직접 초과하는 최소 구성만 탐색.
#   - 경계 보완: n ≥ 1224444 → 1666666 즉시 반환. 같은 길이 L부터 시도, 실패 시 L+1 승급.
