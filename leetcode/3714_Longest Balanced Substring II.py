# 3714_Longest Balanced Substring II.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3714. Longest Balanced Substring II
# 🏷️ 유형: 접두사 카운트 / 해시맵(최초 인덱스) / 차분 벡터 상태 / 1·2·3문자 균형 동시 처리
#
# ✅ 문제 설명(요약):
#   - 문자열 s에서 “balanced substring”의 최대 길이를 구한다.
#   - 코드 기준으로 balanced는 다음 케이스 중 하나라도 만족하면 된다:
#     - 1문자 균형: 한 종류 문자만으로 이루어진 부분문자열(연속 동일 문자 구간)
#     - 2문자 균형: 두 종류 문자의 등장 횟수가 같고(세 번째 문자는 0), 또는 구현에서 추적하는 2문자 상태 조건을 만족
#     - 3문자 균형: 'a','b','c'의 등장 횟수가 모두 같은 부분문자열
#
# ✅ 입력 형식(요지):
#   - s: str
#
# ✅ 규칙 요약:
#   - 1문자 균형은 연속 동일 문자 길이의 최대값으로 계산한다.
#   - 3문자 균형은 접두사에서 (B-A, C-A) 상태가 같을 때 구간 (i0+1..i)에서 A,B,C 증가량이 동일해진다는 성질로 찾는다.
#   - 2문자 균형은 (A-B, C), (B-C, A), (C-A, B) 형태의 상태를 해시로 저장해 해당 두 문자 균형(그리고 나머지 문자 고정)을 찾는다.
#
# 🧠 핵심 불변식(Invariant):
#   - cnt는 (A,B,C) = ('a','b','c')의 접두사 누적 카운트이다.
#   - 어떤 상태 key가 처음 등장한 인덱스를 해시맵에 저장해 두면,
#     같은 key가 다시 등장하는 i에서, 그 사이 구간은 해당 균형 조건을 만족한다.
#   - abc는 3문자 균형용이며 key=(B-A, C-A)를 사용한다.
#   - ab/bc/ca는 2문자 균형용이며 각기 다른 key 정의로 “두 문자 차분 + 나머지 문자 고정”을 동시에 강제한다.
#   - 모든 맵에 (0,0)->-1을 초기로 넣어, 문자열 시작부터의 구간도 자연스럽게 처리한다.
#
# ✅ 정답 코드(제공된 풀이; 절대 수정 금지)

class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def longestBalanced(self, s: str) -> int:                       # balanced 부분문자열의 최대 길이를 반환하는 함수
        n=len(s)                                                    # 문자열 길이를 저장
        # Deal with 1-letter balance                                # 1문자 균형(연속 동일 문자) 처리를 위한 주석
        ans, Len=1, 1                                               # ans는 최대 길이, Len은 현재 연속 구간 길이로 초기화
        for c0, c1 in pairwise(s):                                  # 인접한 문자 쌍을 순회하며 연속 구간을 계산
            if c0==c1: Len+=1                                       # 같은 문자면 연속 길이를 증가
            else:                                                   # 문자가 바뀌면
                ans=max(ans, Len)                                   # 지금까지 연속 길이로 ans를 갱신
                Len=1                                               # 새 연속 구간을 1로 초기화
        ans=max(ans, Len)                                           # 마지막 연속 구간도 반영하여 ans 갱신

        ab, bc, ca, abc={},{},{},{}                                 # 2문자/3문자 균형 상태의 최초 인덱스를 저장할 해시맵들
        abc[(0, 0)]=ab[(0, 0)]=bc[(0, 0)]=ca[(0, 0)]=-1             # 공집합 접두사 상태를 -1 인덱스로 초기화

        cnt=[0, 0, 0]                                               # 접두사 누적 카운트 (A,B,C)를 0으로 초기화
        for i, c in enumerate(s):                                   # 문자열을 인덱스 i와 함께 순회
            cnt[ord(c)-97]+=1                                       # 현재 문자를 'a'~'c'로 가정하고 해당 카운트를 증가
            A, B, C=cnt                                             # 누적 카운트를 A,B,C로 언패킹

            # 3-letter balance: A=B=C                               # 3문자 균형 조건(A=B=C)을 처리하는 블록 주석
            key=(B-A, C-A)                                          # (B-A, C-A) 차분 상태를 key로 생성
            if  key in abc: ans=max(ans, i-abc[key])                # 같은 상태가 이전에 있었다면 그 구간 길이로 ans 갱신
            else: abc[key]=i                                        # 처음 본 상태면 최초 인덱스를 저장

            # 2-letter balance:                                     # 2문자 균형 조건들을 처리하는 블록 주석
            key=(A-B, C)                                            # (A-B, C) 상태를 key로 생성(AB 균형 + C 고정)
            if  key in ab: ans=max(ans, i-ab[key])                  # 이전에 본 상태면 길이로 ans 갱신
            else: ab[key]=i                                         # 처음 본 상태면 인덱스를 저장

            key=(B-C, A)                                            # (B-C, A) 상태를 key로 생성(BC 균형 + A 고정)
            if  key in bc: ans=max(ans, i-bc[key])                  # 이전에 본 상태면 길이로 ans 갱신
            else: bc[key]=i                                         # 처음 본 상태면 인덱스를 저장

            key=(C-A, B)                                            # (C-A, B) 상태를 key로 생성(CA 균형 + B 고정)
            if  key in ca: ans=max(ans, i-ca[key])                  # 이전에 본 상태면 길이로 ans 갱신
            else: ca[key]=i                                         # 처음 본 상태면 인덱스를 저장
        return ans                                                  # 계산된 최대 길이를 반환
