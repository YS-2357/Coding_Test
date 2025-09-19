# 3484_design_spreadsheet.py
# -----------------------------------------------------
# ✅ 제목: Design Spreadsheet (LeetCode 3484)
# ✅ 문제 설명(요약):
# - A~Z 26열, 1..rows 행의 스프레드시트.
# - setCell(cell, value): 셀에 정수 저장.
# - resetCell(cell): 셀 값을 0으로 되돌림(여기선 삭제로 처리).
# - getValue("=X+Y"): X,Y는 정수 또는 셀 참조. 두 값을 더해 반환.
# - 설정되지 않은 셀은 값 0으로 간주.
#
# ✅ 입력 형식(요지):
# - 생성자: Spreadsheet(rows: int)
# - 메서드:
#   - setCell(cell: str, value: int) -> None
#   - resetCell(cell: str) -> None
#   - getValue(formula: str) -> int   # 포맷은 항상 "=X+Y"
#
# ✅ 규칙 요약:
# 1) 미설정 셀은 0 취급.
# 2) 수식은 합산만 지원(=X+Y).
# 3) 셀 참조는 그대로 문자열 키로 사용.
#
# ✅ 입출력 예시(1개):
# - setCell("A1", 5); getValue("=A1+7") → 12
# - getValue("=B2+3") → 3  (B2 미설정=0)
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows                 # 행 수 보관(현재 로직에 직접 사용되진 않음)
        self.cells = {}                  # 셀 값 저장소: {"A1": 5, ...}
        
    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value         # 셀에 값 기록
        
    def resetCell(self, cell: str) -> None:
        if cell in self.cells:           # 값이 있으면
            del self.cells[cell]         # 삭제하여 0 취급되게 함
        
    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")  # "=X+Y"에서 X, Y 분리

        def getVal(token: str) -> int:
            if token.isdigit():          # 숫자면 그대로 정수 변환
                return int(token)
            return self.cells.get(token, 0)  # 셀이면 저장값, 없으면 0
        
        return getVal(left) + getVal(right)  # 두 항의 합 반환

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 딕셔너리 1개 + 간단 파싱으로 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 특이사항 없음. (만약 음수 리터럴을 허용한다면 isdigit() 대신 token.lstrip('-').isdigit() 고려)
#
# 📚 사용된/필수 개념(최소):
# - 해시맵으로 셀 값 저장 및 기본값 0 처리(get with default)
# - 문자열 파싱("=X+Y" 고정 포맷)
# - 시간복잡도: set/reset O(1), get O(1)

# -----------------------------------------------------
# 다른 풀이
# class Spreadsheet:
#     def __init__(self, rows: int):
#         self.dict = defaultdict(int)
#     def setCell(self, cell: str, value: int) -> None:
#         self.dict[cell] = value
#     def resetCell(self, cell: str) -> None:
#         self.dict[cell] = 0
#     def getValue(self, formula: str) -> int:
#         ops = formula.split('=')[1].split('+')
#         res = 0
#         for op in ops:
#             if op in self.dict:
#                 res += self.dict[op]
#             elif op.isdigit():
#                 res += int(op)
#         return res
