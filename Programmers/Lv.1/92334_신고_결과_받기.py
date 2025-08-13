# 92334_신고_결과_받기.py
# -----------------------------------------------------
# ✅ 제목: 신고 결과 받기
# ✅ 문제 설명(요약):
# - 이용자 목록 id_list, 신고 내역 report("신고자 피신고자"), 정지 기준 k가 주어진다.
# - 동일 신고자→피신고자 중복 신고는 1회만 인정.
# - 피신고자가 k회 이상 신고되면 정지.
# - 각 이용자는 자신이 신고해서 정지된 사람 수만큼 메일을 받는다.
#
# ✅ 입력 형식(요지):
# - id_list: List[str]
# - report: List[str]  # "a b"는 a가 b를 신고
# - k: int
#
# ✅ 규칙 요약:
# 1) (신고자, 피신고자) 쌍 중복 제거
# 2) 피신고자별 고유 신고자 수 ≥ k → 정지
# 3) 신고자별로 자신이 신고한 대상 중 정지된 인원의 수 = 받은 메일 수
#
# ✅ 입출력 예시(1개):
# - id_list = ["muzi","frodo","apeach","neo"]
# - report  = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# - k = 2  →  [2,1,1,0]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(id_list, report, k):
    n = len(id_list)                                        # 전체 이용자 수
    name_to_idx = {name: i for i, name in enumerate(id_list)}  # 이름→인덱스 매핑 O(n)
    reported_cnt = [0] * n                                  # 피신고자별 '고유 신고자 수' 카운트
    reported_targets = [set() for _ in range(n)]            # 신고자별 '신고 대상 집합'
    unique_reports = {tuple(rep.split()) for rep in report} # 중복 신고 제거(공백 안정 split)

    for giver, take in unique_reports:                      # 고유 신고 쌍들만 순회
        gi = name_to_idx[giver]                             # 신고자 인덱스
        ti = name_to_idx[take]                              # 피신고자 인덱스
        reported_targets[gi].add(ti)                        # 신고자가 신고한 대상 집합에 추가
        reported_cnt[ti] += 1                               # 피신고자 고유 신고 카운트 +1

    suspended = {i for i, c in enumerate(reported_cnt) if c >= k}  # 정지된 이용자 집합
    answer = [0] * n                                        # 반환 배열(메일 수)
    for u in range(n):                                      # 각 신고자 u에 대해
        answer[u] = sum(1 for v in reported_targets[u] if v in suspended)  # 정지자 만큼 메일 수

    return answer                                           # id_list 순서대로 메일 수 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **미도달** (2단계에서 수정 가이드 반영 후 통과)
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (이전 버전) 피신고자별 리스트 초기화 오류, O(n) index 탐색 사용, 정지/메일 집계 누락
#   → 이름→인덱스 매핑 dict로 O(1) 접근, 신고자별 집합과 피신고자별 카운트 동시 유지,
#      정지자 집합 생성 후 신고자별로 정지 대상 수 합산으로 수정.
#
# 📚 사용된/필수 개념(최소):
# - 중복 제거(set), 해시 매핑(dict), 집합 연산으로 정지자 판정 및 교집합 개수 세기
# - 시간복잡도: O(n + |report|)
