# 17677_뉴스_클러스터링.py
# -----------------------------------------------------
# ✅ 제목: 뉴스 클러스터링
# ✅ 문제 설명(요약):
# - 문자열 str1, str2를 연속된 두 글자씩 끊어 영문자만으로 구성된 “2-gram 멀티셋”을 만든다.
# - 이 두 멀티셋의 자카드 유사도 = |교집합| / |합집합|
# - 특례: 두 멀티셋이 모두 공집합일 경우 유사도=1로 간주 → 65536 반환
# - 반환 값: 유사도 × 65536 후 내림(floor).
#
# ✅ 입력 형식(요지):
# - str1, str2: 알파벳/기호/숫자가 섞여 있는 문자열
#
# ✅ 규칙 요약:
# 1) 두 글자씩 추출 → 둘 다 영문자일 때만 소문자로 저장.
# 2) 멀티셋이므로 같은 bigram 여러 번 등장 가능.
# 3) 교집합 = Σ min(count1[x], count2[x])
#    합집합 = Σ max(count1[x], count2[x])
# 4) 합집합=0이면 65536 반환, 아니면 floor(intersection/union*65536).
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(str1, str2):
    MOD = 65536
    str1, str2 = str1.lower(), str2.lower()          # 대소문자 무시를 위해 소문자로 통일
    
    bigrams1, bigrams2 = {}, {}                      # 각 문자열의 bigram 빈도 딕셔너리
    bigrams = set()                                  # 교집합/합집합 계산 시 필요한 전체 키 집합
    
    for i in range(len(str1)-1):                     # str1에서 bigram 추출
        a, b = str1[i], str1[i+1]
        if a.isalpha() and b.isalpha():              # 두 글자가 모두 영문자일 때만 유효
            bigrams1[a+b] = bigrams1.get(a+b, 0) + 1
            bigrams.add(a+b)
            
    for i in range(len(str2)-1):                     # str2에서 bigram 추출
        c, d = str2[i], str2[i+1]
        if c.isalpha() and d.isalpha():
            bigrams2[c+d] = bigrams2.get(c+d, 0) + 1
            bigrams.add(c+d)
            
    intersection, union = 0, 0
    for ch in bigrams:                               # 전체 bigram 종류 순회
        ch1 = bigrams1.get(ch, 0)
        ch2 = bigrams2.get(ch, 0)
        intersection += min(ch1, ch2)                # 교집합: 두 문자열에 모두 있는 최소 등장 횟수
        union += max(ch1, ch2)                       # 합집합: 두 문자열에서 최대 등장 횟수
        
    if union == 0:                                   # 두 멀티셋이 모두 공집합일 경우(=합집합 크기 0)
        return MOD                                   # 유사도=1 → 65536 반환
    
    answer = intersection * MOD // union             # 유사도*65536 후 내림(floor) → 정수 나눗셈
    return int(answer)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 교집합/합집합 모두 정확히 계산되고, 특례 조건도 올바르게 처리됨.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기에 `if intersection == 0:`으로 특례를 처리해 일부 케이스(교집합=0이지만 합집합≠0)에서
#   잘못 65536을 반환 → union==0 조건으로 수정.
#
# 📚 사용된/필수 개념(최소):
# - 다중집합 교집합/합집합: min, max 기반 계산
# - 자카드 유사도 정의와 특례 처리
# - 문자열 전처리(소문자화, isalpha 검증)
# - 시간복잡도: O(n+m) (bigram 추출) + O(u) (집합 순회), u=서로 다른 bigram 수
# - 공간복잡도: O(u)
#
# 🧠 왜 특례 조건이 “union==0”일까?
# - 교집합이 0인 경우는 흔하지만, 합집합이 0이라는 건 “양쪽 모두 아무 bigram도 없었다”는 뜻.
# - 이때 문제에서 정의상 유사도를 1로 간주 → 65536 반환해야 함.
