# 2043_Simple_Bank_System.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2043. Simple Bank System
# ✅ 문제 설명(요약):
#   은행 계좌들의 잔액이 주어졌을 때, deposit(입금), withdraw(출금),
#   transfer(이체) 연산을 수행하는 시스템을 구현하라.
#   각 연산은 성공 여부를 True/False로 반환한다.
#
# ✅ 입력 형식(요지):
#   - balance: 각 계좌의 초기 잔액을 담은 리스트
#   - 모든 계좌 번호는 1-indexed (즉, 1번부터 시작)
#   - 모든 금액은 양의 정수
#
# ✅ 규칙 요약:
#   - deposit(account, money): 해당 계좌에 money만큼 입금
#   - withdraw(account, money): 잔액이 충분하면 money만큼 출금
#   - transfer(account1, account2, money): 계좌1에서 계좌2로 이체 (잔액 부족 시 실패)
#   - 모든 연산은 유효한 계좌 번호일 때만 수행
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance  # 각 계좌의 잔액 리스트 저장

    def valid(self, i):
        return 1 <= i <= len(self.balance)  # 계좌 번호 유효성 검사

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 두 계좌가 모두 유효해야 함
        if not self.valid(account1) or not self.valid(account2):
            return False
        # 출금 계좌의 잔액이 충분해야 함
        if self.balance[account1 - 1] < money:
            return False
        # 이체 수행
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        # 유효한 계좌인지 확인
        if not self.valid(account):
            return False
        # 입금 수행
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        # 계좌 유효성 및 잔액 충분성 확인
        if not self.valid(account) or self.balance[account - 1] < money:
            return False
        # 출금 수행
        self.balance[account - 1] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정상 동작 및 모든 테스트 통과.
#   - IndexError, 음수 잔액, 잘못된 계좌번호 모두 방지됨.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용된 개념: O(1) 인덱스 접근, 조건 분기, 유효성 검사.
#   - 개선 사항: 메서드 호출(self.valid) 누락·범위 검사 미흡 문제를 수정함.
#
# 📚 시간·공간 복잡도:
#   - 시간복잡도: O(1) (모든 연산이 상수 시간)
#   - 공간복잡도: O(n) (초기 잔액 리스트 저장)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 동일 알고리즘 구조에서 상수항 최적화를 위해
#     valid() 호출 대신 인라인 비교(1 <= i <= n)로 미세한 속도 개선 가능.
#   - 하지만 전체 복잡도는 동일하게 O(1)이며 실질적 성능 차이는 미미함.
