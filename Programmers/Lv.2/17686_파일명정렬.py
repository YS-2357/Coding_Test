# 17686_파일명정렬.py
# -----------------------------------------------------
# ✅ 제목: 파일명 정렬
# ✅ 문제 설명(요약):
# - 파일명을 HEAD, NUMBER, TAIL로 분리.
# - 정렬 규칙:
#   1) HEAD를 대소문자 구분 없이 사전순 정렬
#   2) NUMBER를 정수로 비교 (최대 5자리)
#   3) HEAD와 NUMBER가 같으면 입력 순서 유지
#
# ✅ 입력 형식(요지):
# - files: 문자열 배열 (각 문자열은 파일명)
#
# ✅ 규칙 요약:
# - HEAD: 숫자 시작 전까지 모든 문자
# - NUMBER: 처음 등장하는 숫자부터 최대 5자리
# - TAIL: 그 뒤 나머지 (정렬에 영향 없음)
# - 정렬 후 원본 문자열 반환
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
def solution(files):
    answer = []
    for file in files:
        head, num, tail = '', '', ''   # 세 부분으로 분리
        flag = False                   # 숫자 구간 시작 여부

        for i in range(len(file)):     # 파일명 순회
            if file[i].isdigit():      # 숫자라면 NUMBER 구간
                num += file[i]
                flag = True
            elif not flag:             # 아직 숫자 시작 전 → HEAD
                head += file[i]
            else:                      # 숫자 구간 끝난 뒤 → TAIL
                tail = file[i:]
                break

        answer.append((head, num, tail))  # 세 부분 저장

    # HEAD(소문자화), NUMBER(정수형) 기준으로 정렬
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # 다시 합쳐서 결과 반환
    answer = [''.join(value) for value in answer]
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - HEAD/NUMBER/TAIL 분리 성공.
# - 정렬 시 HEAD와 NUMBER 규칙을 적용해 문제 조건 충족.

# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기에 HEAD/NUMBER 추출 후 join하지 않아 결과가 튜플 상태였음 → ''.join()으로 문자열 복원.
# - NUMBER가 문자열로 정렬될 수 있으므로 반드시 int()로 변환 필요 → 정수형으로 수정.
# - 안정 정렬은 Python 기본 sort로 자동 보장.

# 📚 사용된/필수 개념(최소):
# - 문자열 파싱 (숫자 시작점 탐색)
# - 정렬 키: (HEAD.lower(), int(NUMBER))
# - 리스트 컴프리헨션
# - 시간복잡도: O(N log N) (N=파일 수)
# - 공간복잡도: O(N) (HEAD/NUMBER/TAIL 저장)

# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 정규식 사용 가능: re.match(r'^([^0-9]+)([0-9]{1,5})(.*)$')로 세 부분 추출.
# - 이 경우 파싱 코드가 더 간결해진다.
