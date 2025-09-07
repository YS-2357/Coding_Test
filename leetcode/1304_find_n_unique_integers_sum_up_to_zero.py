# 1304_find_n_unique_integers_sum_up_to_zero.py
# -----------------------------------------------------
# ✅ 제목: Find N Unique Integers Sum up to Zero
# ✅ 문제 설명(요약):
# - 정수 n이 주어졌을 때, 합이 0이 되는 서로 다른 n개의 정수를 반환한다.
# - 여러 정답 가능, 임의의 하나만 반환하면 된다.
#
# ✅ 입력 형식(요지):
# - n: int (1 ≤ n ≤ 1000)
#
# ✅ 규칙 요약:
# 1) n이 짝수라면, (i, -i) 쌍으로 n/2개를 만들면 합이 0.
# 2) n이 홀수라면, (i, -i) 쌍 n//2개 + 0 하나를 추가하면 합이 0.
# 3) 모든 원소는 서로 다른 정수여야 함.
#
# ✅ 입출력 예시(1개):
# - n=5 → [-2, -1, 1, 2, 0]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        if n % 2 == 0:                           # n이 짝수일 때
            for i in range(1, n // 2 + 1):
                answer.append(i)                 # 양수
                answer.append(-i)                # 음수
            return answer
        elif n % 2 == 1:                         # n이 홀수일 때
            for i in range(1, n // 2 + 1):
                answer.append(i)
                answer.append(-i)
            answer.append(0)                     # 0 추가
            return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 제출 시 올바른 정답 반환, 다양한 n에 대해 조건 충족.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 특별한 오류 없음. 다만 두 if문을 elif로 합치면 더 깔끔하게 작성 가능.
#
# 📚 사용된/필수 개념(최소):
# - 수학적 관찰: 짝수→대칭쌍, 홀수→대칭쌍+0
# - 시간복잡도 O(n), 공간복잡도 O(n)
