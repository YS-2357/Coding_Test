# 17680_캐시.py
# -----------------------------------------------------
# ✅ 제목: 캐시 (LRU Cache 시뮬레이션)
# ✅ 문제 설명(요약):
# - 도시 이름 문자열 배열을 순서대로 처리하며 캐시 정책(LRU)에 따라 실행시간을 누적한다.
# - 규칙:
#   * 캐시 히트(hit): +1
#   * 캐시 미스(miss): +5 (가득 차 있으면 LRU 하나 제거 후 추가)
# - 도시 이름은 대소문자 구분 없음(소문자/대문자 통일 필요).
#
# ✅ 입력 형식(요지):
# - cacheSize: int, 캐시에 담을 수 있는 최대 도시 수 (0이면 항상 miss)
# - cities: List[str], 접근할 도시 이름들의 순서열
#
# ✅ 규칙 요약:
# 1) 대소문자 무시 → 전처리로 소문자 변환.
# 2) 히트: 해당 항목을 캐시의 "가장 최근" 위치로 이동(재삽입).
# 3) 미스: +5, 가득 차 있으면 LRU(가장 오래된) 제거 후 삽입.
# 4) cacheSize==0이면 전부 miss → 5 * len(cities).
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
from collections import deque

def solution(cacheSize, cities):
    answer = 0                         # 총 실행시간 누적 변수
    queue = deque([])                  # LRU 순서 관리용 덱(왼쪽=가장 오래된, 오른쪽=가장 최근)
    
    if cacheSize <= 0:                 # 캐시 용량이 0 이하인 경우
        return 5 * len(cities)         # 모든 접근이 miss → 각 5씩 누적하여 즉시 반환
    
    for city in cities:                # 도시들을 입력 순서대로 순회
        city = city.lower()            # 대소문자 구분 없으므로 통일(정규화)
        if city in queue:              # 캐시에 이미 있다면 → 캐시 히트
            answer += 1                # 히트 비용 +1
            queue.remove(city)         # 기존 위치의 city 제거(중간 어딘가에 있을 수 있음)
            queue.append(city)         # 가장 최근 사용으로 갱신(오른쪽 끝에 재삽입)
        else:                          # 캐시에 없다면 → 캐시 미스
            answer += 5                # 미스 비용 +5
            if len(queue) >= cacheSize:# 캐시가 가득 찬 상태라면
                queue.popleft()        # 가장 오래된 항목(LRU)을 왼쪽에서 제거
            queue.append(city)         # 새 도시를 최근 위치(오른쪽 끝)에 추가
            
    return answer                      # 누적된 총 실행시간 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 맞춤. 대소문자 통일, 히트/미스 분기, LRU 갱신/제거 로직 정확.
# - cacheSize==0 처리도 O(1)로 조기 반환하여 깔끔.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 잠재 이슈: from collection import deque (오타) → from collections import deque 로 수정 필요.
# - 히트 시 위치 갱신 누락 가능성 → 본 풀이에서 remove→append로 최신화 처리 OK.
# - 복잡도 측면에서 deque.remove(city)는 O(k)이지만 k≤cacheSize(작음) → 실전 제약 내에서 무방.
#
# 📚 사용된/필수 개념(최소):
# - LRU 정책: 가장 오래 사용하지 않은 항목 제거
# - 덱(deque)로 순서 관리(왼쪽=LRU, 오른쪽=MRU)
# - 대소문자 정규화로 일관 비교
# - 시간복잡도: O(n * k) (n=len(cities), k=cacheSize), k≤30 수준에서 충분히 빠름
# - 공간복잡도: O(k)
#
# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - OrderedDict 사용:
#   * 키 존재 시 pop → 재삽입으로 O(1)에 가깝게 MRU 갱신 가능.
#   * 가득 찼을 때 popitem(last=False)로 LRU 제거.
# - 리스트+세트 병행:
#   * 포함 여부는 set으로 O(1) 확인, 순서 관리는 리스트(또는 deque)로 처리.
#   * 다만 동기화를 잘못하면 버그 소지↑, 이 문제 규모에선 현재 구현이 가장 간결.
