# 761_Special Binary String.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 761. Special Binary String
# 🏷️ 유형: 재귀 / 분할정복 / 그리디(정렬) / 스택-밸런스 분해
#
# ✅ 문제 설명(요약):
#   - 문자열 s는 “special binary string”이다.
#   - special의 성질은 (1) '1'과 '0'의 개수가 같고, (2) 어떤 접두사에서도 '1' 개수 >= '0' 개수이다.
#   - special 문자열 내부의 special 서브문자열들을 적절히 교환하여(재배열하여) 사전순으로 가장 큰 문자열을 만든다.
#
# ✅ 입력 형식(요지):
#   - s: str
#
# ✅ 규칙 요약:
#   - s를 밸런스(count)가 0이 되는 지점마다 “균형 잡힌 조각(chunk)”으로 분해한다.
#   - 각 chunk는 항상 "1 ... 0" 형태로 감싸진 special 조각이다.
#   - chunk 내부(감싼 부분)는 다시 같은 문제이므로 재귀적으로 최대화한다.
#   - 최대 사전순을 위해 chunk들을 내림차순 정렬 후 이어 붙인다.
#
# 🧠 핵심 불변식(Invariant):
#   - count는 현재 구간에서 (1의 개수 - 0의 개수)를 나타낸다.
#   - special 성질 때문에 count는 구간 중간에서 음수가 되지 않으며,
#     count가 0이 되는 순간 [i..j]는 하나의 완전한 special chunk가 된다.
#   - 각 chunk는 '1' + (내부 재귀 최대화 결과) + '0'으로 표현된다.
#   - chunk들을 사전순 내림차순으로 정렬하면, 연결 결과 전체가 최대가 된다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def makeLargestSpecial(self, s: str) -> str:                    # s를 사전순으로 가장 크게 만드는 special 변환 함수
        count = 0                                                   # 현재 구간의 밸런스(1개수-0개수)를 저장할 변수
        i = 0                                                       # 현재 chunk의 시작 인덱스를 저장
        res = []                                                    # 분해된 chunk들의 결과 문자열을 담을 리스트
        
        for j in range(len(s)):                                     # 문자열을 왼쪽부터 끝까지 순회
            # Track balance: +1 for '1', -1 for '0'                 # 밸런스 업데이트 규칙을 설명하는 주석
            count += 1 if s[j] == '1' else -1                       # 현재 문자가 1이면 +1, 0이면 -1로 밸런스 갱신
            
            # Found a balanced chunk when count returns to 0        # count가 0이면 하나의 chunk가 완성됨을 설명하는 주석
            if count == 0:                                          # 밸런스가 0이 되면 [i..j]는 완전한 special chunk
                # Recursively maximize inner part, wrap with 1...0  # 내부를 재귀 최대화 후 1..0으로 감싼다는 주석
                res.append('1' + self.makeLargestSpecial(s[i + 1:j]) + '0')  # 내부(s[i+1..j-1])를 재귀로 최대화해 감싸서 저장
                i = j + 1                                           # 다음 chunk 탐색을 위해 시작점을 다음 위치로 이동
        
        # Sort chunks in descending order for largest arrangement   # chunk 내림차순 정렬이 최대 사전순을 만든다는 주석
        res.sort(reverse=True)                                      # chunk들을 사전순 내림차순으로 정렬
        return ''.join(res)                                         # 정렬된 chunk들을 이어 붙여 최종 문자열 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 밸런스 기반 chunk 분해 + 각 chunk 내부 재귀 최적화 + chunk 정렬(그리디).
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n)~O(n^2) 수준(재귀 분해 및 각 레벨 정렬/문자열 생성 비용에 따라 달라질 수 있음)
#   - 공간: O(n) (재귀 스택 및 chunk 저장)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 문자열 대신 “chunk 트리 구조”로 파싱해 정렬/재조합하는 방식으로도 동일 원리를 구현할 수 있다(개념만).
