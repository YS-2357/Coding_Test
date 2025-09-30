# 42888_오픈채팅방.py
# -----------------------------------------------------
# ✅ 제목: 오픈채팅방
# ✅ 문제 설명(요약):
# - 채팅방에서 Enter, Leave, Change 기록이 주어짐.
# - 최종적으로 모든 메시지는 가장 최신 닉네임으로 출력해야 함.
# - 출력은 Enter/Leave에 대해서만 메시지를 만든다.
#
# ✅ 입력 형식(요지):
# - record: 문자열 배열 ["Enter uid 닉네임", "Leave uid", "Change uid 닉네임", ...]
#
# ✅ 규칙 요약:
# 1) uid는 여러 번 닉네임을 바꿀 수 있다.
# 2) 출력은 Enter/Leave만 포함한다.
# 3) 모든 메시지에는 uid가 가진 "최종 닉네임"을 반영해야 한다.
#
# ✅ 정답 코드(나의 풀이; 한 줄마다 주석):
def solution(record):
    answer = []
    history = {}                         # uid → 최신 닉네임 매핑
    for rec in record:                   # 1차 순회: 닉네임 최신화
        parts = rec.split()
        cmd, uid = parts[0], parts[1]
        if cmd in ("Enter", "Change"):   # Enter/Change일 때만 닉네임 갱신
            nick = parts[2]
            history[uid] = nick
    
    for rec in record:                   # 2차 순회: 메시지 생성
        parts = rec.split()
        cmd, uid = parts[0], parts[1]
        if cmd == "Enter":
            answer.append(f"{history[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{history[uid]}님이 나갔습니다.")
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - Enter/Leave 메시지를 출력하는 구조는 맞음.
# - 그러나 Change가 닉네임을 바꿔도 출력에 반영되지 않는 문제가 있었다.

# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (실수) 1차 순회에서 Change 기록을 무시 → 최종 닉네임이 반영되지 않음.
# - (수정) Enter뿐 아니라 Change일 때도 history[uid]를 갱신하도록 변경.

# 📚 사용된/필수 개념(최소):
# - 해시맵(dict): uid → 닉네임 최신화
# - 2차 순회: 기록을 다시 돌며 Enter/Leave만 메시지 생성
# - 안정 정렬(입력 순서 유지) 보장
# - 시간복잡도: O(N), 공간복잡도: O(N)

# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 한 번의 순회로도 처리 가능: 메시지 로그에 uid만 저장해 두고,
#   마지막에 uid를 닉네임으로 변환하는 방식.
