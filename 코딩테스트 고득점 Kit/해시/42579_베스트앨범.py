# 42579_베스트앨범.py
# ------------------------------------------------------
# ✅ 문제 설명:
# - 장르 별로 가장 많이 재생된 노래를 두 개씩 모아서 베스트 앨범을 만든다.
# - 노래 정보: 장르와 재생 횟수가 주어진다.
# - 같은 장르 내에서는 재생 횟수가 많은 노래를 먼저 수록하고,
#   재생 횟수가 같으면 고유 번호가 낮은 노래를 먼저 수록한다.
#
# ✅ 입력 형식:
# - genres: 노래의 장르를 담은 문자열 배열
# - plays: 노래별 재생 횟수를 담은 정수 배열
#
# ✅ 출력 형식:
# - 베스트 앨범에 들어갈 노래 고유 번호 배열을 반환
#
# ✅ 입출력 예제:
# 🔹 입력:
# genres = ["classic", "pop", "classic", "classic", "pop"]
# plays = [500, 600, 150, 800, 2500]
#
# 🔹 출력:
# [4, 1, 3, 0]
# ------------------------------------------------------

from collections import defaultdict

def solution(genres, plays):
    # ✅ 1. 장르별로 곡 정보 저장 (play 수, 인덱스)
    songs = defaultdict(list)
    # ✅ 2. 장르별 총 재생 횟수 저장
    total_play = defaultdict(int)
    
    # ✅ 곡 정보 저장 및 총 재생 수 계산
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs[genre].append((play, idx))
        total_play[genre] += play

    # ✅ 3. 총 재생 수 기준으로 장르 정렬
    sorted_genres = sorted(total_play.keys(), key=lambda x: total_play[x], reverse=True)

    answer = []
    
    # ✅ 4. 각 장르별로 곡을 정렬 (재생 수 내림차순, 인덱스 오름차순) 후 상위 2개 선택
    for genre in sorted_genres:
        # 플레이 수 내림차순, 고유 번호 오름차순 정렬
        songs[genre].sort(key=lambda x: (-x[0], x[1]))
        
        # 상위 2개까지 고유 번호 추가
        for play, idx in songs[genre][:2]:
            answer.append(idx)

    return answer

# ------------------------------------------------------
# ✅ 핵심 요약:
# - defaultdict(list), defaultdict(int)로 자료구조 초기화
# - zip을 이용한 장르/재생 수 동시 순회
# - sorted를 이용한 다중 조건 정렬
# - 각 장르별 최대 2개 노래를 골라 리스트에 추가
# ------------------------------------------------------
