# 250121_데이터_분석.py
# -----------------------------------------------------
# ✅ 제목: 데이터 분석
# ✅ 문제 설명(요약):
# - 각 행은 [code, date, maximum, remain] 형식의 데이터를 가진다.
# - 특정 열(ext)을 기준으로 주어진 값(val_ext)보다 작은 행만 필터링한다.
# - 이후 남은 행들을 sort_by 열 기준으로 오름차순 정렬한다.
# - 정렬된 2차원 리스트를 반환한다.
#
# ✅ 입력 형식(요지):
# - data: List[List[int]], 각 행은 [code, date, maximum, remain]
# - ext: str, 필터 기준 열 이름 ("code", "date", "maximum", "remain")
# - val_ext: int, 필터 값(해당 열 값보다 작은 행만 남음)
# - sort_by: str, 정렬 기준 열 이름
#
# ✅ 규칙 요약:
# 1) 열 이름을 인덱스로 매핑하여 사용.
# 2) ext 열 값 < val_ext 조건만 남김.
# 3) sort_by 열 기준으로 오름차순 정렬.
# 4) 결과 리스트 반환.
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
def solution(data, ext, val_ext, sort_by):
    answer = []  # 필터링된 결과를 저장할 리스트

    my_dict = {               # 열 이름을 열 인덱스로 매핑
        "code": 0,            # "code" → 0번째 열
        "date": 1,            # "date" → 1번째 열
        "maximum": 2,         # "maximum" → 2번째 열
        "remain": 3           # "remain" → 3번째 열
    }

    criterion = my_dict[ext]          # 필터링에 사용할 열 인덱스
    sorting_criterion = my_dict[sort_by]  # 정렬에 사용할 열 인덱스
    
    for d in data:                    # data의 각 행 d를 확인
        if d[criterion] < val_ext:    # 조건: ext 열 값이 val_ext보다 작은 경우만
            answer.append(d)          # 조건 만족 시 결과 리스트에 추가
            
    # sort_by 열 기준으로 오름차순 정렬
    answer.sort(key=lambda x: x[sorting_criterion])
    
    return answer  # 최종 정렬된 리스트 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 문제 조건을 충실히 반영하여 정상 동작.
# - 조건 필터링(<) 및 오름차순 정렬 모두 구현됨.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 실수 없이 한 번에 맞춤.
# - 잠재 오류 포인트:
#   * 비교 연산자를 <=로 잘못 쓰는 경우 (하지만 여기서는 정확히 < 로 구현).
#   * 열 인덱스 매핑에서 오타 발생 가능성 (my_dict로 안전하게 처리).
#
# 📚 사용된/필수 개념(최소):
# - 해시맵(dict)으로 문자열 열 이름을 정수 인덱스로 변환.
# - 조건 필터링 (if d[criterion] < val_ext).
# - 리스트 정렬에서 key 함수 사용 (lambda).
# - 시간복잡도: O(n log n), 공간복잡도: O(n).
