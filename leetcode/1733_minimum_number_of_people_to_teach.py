# 1733_minimum_number_of_people_to_teach.py
# -----------------------------------------------------
# ✅ 제목: Minimum Number of People to Teach
# ✅ 문제 설명(요약):
# - 사용자 1..n과 각자의 언어 목록, 친구 관계가 주어진다.
# - 서로 대화 불가한 친구 쌍이 생기지 않도록 "하나의 언어 L"만 골라 최소 몇 명에게 가르칠지 구한다.
#
# ✅ 입력 형식(요지):
# - n: int (사람 수)
# - languages: List[List[int]]  # i번째 사람의 언어 번호 리스트(1-indexed 사람)
# - friendships: List[List[int]] # [u, v] 형태의 친구 관계 (1-indexed 사람)
#
# ✅ 규칙 요약:
# 1) 대화 가능: 두 사람의 언어 교집합이 비어있지 않음.
# 2) 대화 불가 쌍에 등장하는 사람들만 교육 후보(candidates).
# 3) 언어 L을 선택했을 때, candidates 중 L을 모르는 사람 수를 세고 그 최소값을 정답으로.
#
# ✅ 입출력 예시(1개):
# - n=3, languages=[[2],[1,3],[1,2]], friendships=[[1,2],[1,3]]
#   → 대화 불가 쌍: (1,2)만 해당, 후보 {1,2}
#   → L=1: {1,2 중 1 모르는 사람}=1, L=2: 0, L=3: 1 → 최소 0
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(lang) for lang in languages]      # 각 사람의 언어를 set으로(교집합 O(1) 체크)
        candidates = set()                                  # 대화 불가 쌍에 등장한 사람들

        for u, v in friendships:
            lang_u, lang_v = languages[u-1], languages[v-1]
            if not (lang_u & lang_v):                       # 공통 언어 없으면
                candidates.add(u); candidates.add(v)        # 두 사람을 후보에 추가
        
        if not candidates:                                  # 모두 이미 대화 가능하면 0
            return 0
        
        max_lang = max(x for lang in languages for x in lang)  # 등장 언어의 최대 번호
        ans = 500                                            # 충분히 큰 초기값(또는 float('inf'))
        for L in range(1, max_lang+1):                       # 각 언어 L에 대해
            need = sum(1 for u in candidates if L not in languages[u-1])  # L을 모르는 후보 수
            ans = min(ans, need)                             # 최소값 갱신

        return ans                                           # 최소 교육 인원 수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 대화 불가 쌍만 대상으로 언어별 필요 인원 수 계산 → 정답 도출.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전) 대화 불가 "쌍의 개수"를 세었음 → 사람 수 기준으로 바꿈.
# - (주의) 언어 범위를 1..n이 아니라 실제 등장한 언어의 최대치로 순회.
#
# 📚 사용된/필수 개념(최소):
# - 집합 교집합으로 대화 가능 판정
# - 후보 축소(candidates) 후 언어별 필요 인원 계산
# - 시간복잡도: O(|friendships|·avg_lang + L·|candidates|)
