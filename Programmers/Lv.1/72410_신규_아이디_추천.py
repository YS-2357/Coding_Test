# 72410_신규_아이디_추천.py
# -----------------------------------------------------
# ✅ 제목: 신규 아이디 추천 — 문자열 규칙 변환
# ✅ 문제 설명(요약):
# - 주어진 new_id 문자열을 규칙 7단계(소문자화 → 허용 문자 제외 제거 → 연속 마침표 축약 → 양 끝 마침표 제거 → 빈 문자열 처리 → 길이 조정 → 길이 최소 보장)로 변환해 최종 추천 아이디를 반환한다.
#
# ✅ 입력 형식(요지):
# - new_id: str  (길이 1~1000, 영문 대소문자/숫자/특수문자 혼합)
#
# ✅ 규칙 요약:
# 1. 모든 대문자를 소문자로 치환
# 2. 허용 문자(`소문자, 숫자, -, _, .`) 외 제거
# 3. 연속된 `.`은 하나로 축약
# 4. 문자열 양 끝의 `.` 제거
# 5. 빈 문자열이면 `"a"`
# 6. 길이가 16 이상이면 앞 15자로 자르고, 다시 끝의 `.` 제거
# 7. 길이가 2 이하라면 마지막 문자를 반복해 길이가 3이 되도록
#
# ✅ 입출력 예시(간단):
# - 입력: "...!@BaT#*..y.abcdefghijklm"
# - 출력: "bat.y.abcdefghi"
#
# ✅ 정답 코드 (원본 그대로 유지)
import re

def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2 
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)
    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # 4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    # 5
    if not new_id:
        new_id = "a"
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - 문자열 정규식 필터링: `re.sub(r'[^a-z0-9\-_.]', '', s)`으로 불필요 문자 제거
# - 문자열 치환/슬라이싱을 통한 규칙적 전처리
# - 반복적 검사(`while '..' in s`)로 연속 마침표 축약
# - 조건 분기(`startswith`, `endswith`)로 양 끝 마침표 처리
# - 문자열 길이 보정: 슬라이싱, 반복문으로 길이 최소 보장

# -----------------------------------------------------
# 다른 풀이 1
# def solution(new_id):
#     answer = ''
#     # 1
#     new_id = new_id.lower()
#     # 2
#     for c in new_id:
#         if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
#             answer += c
#     # 3
#     while '..' in answer:
#         answer = answer.replace('..', '.')
#     # 4
#     if answer[0] == '.':
#         answer = answer[1:] if len(answer) > 1 else '.'
#     if answer[-1] == '.':
#         answer = answer[:-1]
#     # 5
#     if answer == '':
#         answer = 'a'
#     # 6
#     if len(answer) > 15:
#         answer = answer[:15]
#         if answer[-1] == '.':
#             answer = answer[:-1]
#     # 7
#     while len(answer) < 3:
#        answer += answer[-1]
#    return answer

# 다른 풀이 2
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st
