# 42576_완주하지못한선수.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 마라톤에 참가한 선수들의 이름이 주어진다.
# - 완주하지 못한 선수 이름을 반환해야 한다.
# - 이름은 중복될 수 있으며, 참가자는 completion보다 1명이 많다.
#
# ✅ 입력 형식:
# - participant: 참가자 이름 리스트 (1 ≤ participant 길이 ≤ 100,000)
# - completion: 완주한 사람 이름 리스트 (길이 = participant - 1)
#
# ✅ 출력 형식:
# - 완주하지 못한 선수의 이름 (문자열)을 반환
#
# ✅ 입출력 예제:
# 🔹 participant = ["leo", "kiki", "eden"], completion = ["eden", "kiki"]
# 🔹 출력: "leo"
# -----------------------------------------------------

def solution(participant, completion):
    # ✅ 참가자와 완주자 리스트를 오름차순 정렬
    participant.sort()
    completion.sort()
    
    # ✅ 정렬된 리스트를 순서대로 비교
    for p, c in zip(participant, completion):
        if p != c:
            # ✅ 처음으로 다른 이름이 나온다면, 해당 참가자가 완주하지 못한 사람
            return p
    
    # ✅ 끝까지 차이가 없었다면, 마지막 참가자가 완주하지 못한 사람
    return participant[-1]

# -----------------------------------------------------
# ✅ 코드 설명:
# - participant와 completion을 정렬하여 순서대로 비교한다.
# - zip을 사용하여 두 리스트를 동시에 순회한다.
# - 다른 이름이 나오는 순간, 해당 이름을 반환한다.
# - 끝까지 다른 이름이 없으면 participant의 마지막 이름을 반환한다.
#
# ✅ 2단계에서 수정한 점:
# - for문 안에서 else로 답을 덮어쓰지 않고,
#   다르면 즉시 return 하도록 수정.
# - 루프를 끝까지 돌았을 때는 participant[-1]을 반환하도록 처리.
#
# ✅ 시간 복잡도:
# - 정렬 O(N log N)
# - 비교 O(N)
# - 따라서 전체 시간 복잡도는 O(N log N)이며, N ≤ 100,000이므로 시간 내 통과 가능.
# -----------------------------------------------------
"""
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
