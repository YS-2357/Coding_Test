# 178871_달리기_경주.py
# -----------------------------------------------------
# ✅ 제목: 달리기 경주 — 호출마다 앞사람과 자리 교환
# ✅ 문제 설명(요약):
# - 초기 선수 순서(players)가 있고, callings에 따라 불린 선수가 즉시 앞사람과 자리를 바꾼다.
# - 모든 호출을 처리한 뒤의 최종 순서를 반환한다.
#
# ✅ 입력 형식(요지):
# - players: List[str]  (선수 이름, 앞→뒤 순서)
# - callings: List[str] (호출된 선수 이름들, 순서대로)
#
# ✅ 규칙 요약:
# - 호출 1회: 불린 선수와 그 선수의 바로 앞 선수의 위치를 즉시 교환
# - 이를 순서대로 반복 적용
#
# ✅ 입출력 예시(간단):
# - players=["mumu","soe","poe","kai","mine"], callings=["kai","kai","mine","mine"]
#   → 최종 순서: ["mumu","kai","mine","soe","poe"]

def solution(players, callings):
    answer = []
    hash = {}
    for i, p in enumerate(players):
        hash[p] = i
    
    for c in callings:
        idx = hash[c]
        prev_p = players[idx-1]
        
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        hash[c] -= 1
        hash[prev_p] += 1
    return players

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - 이름→현재 위치를 O(1)에 조회하는 해시맵(dict)
# - 배열 내 인접 원소 swap로 자리 교환
# - 호출마다 해시/배열을 동기 업데이트(해시: 두 선수의 인덱스 증감)
