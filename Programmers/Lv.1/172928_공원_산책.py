# 172928_공원_산책.py
# -----------------------------------------------------
# ✅ 제목: 공원 산책 — 명령 단위로 이동(경계·장애물 검증)
# ✅ 문제 설명(요약):
# - 공원 지도 `park`에서 시작점 'S'를 찾고,
# - 이동 명령 `routes`를 순서대로 처리한다. 한 명령은 방향/거리("E 2" 등).
# - 해당 명령 거리만큼 이동 경로의 모든 칸이 유효(범위 내 & 'X' 아님)일 때만 실제로 이동한다.
# - 모든 명령을 처리한 뒤 최종 좌표 `[행, 열]`을 반환한다.
#
# ✅ 입력 형식(요지):
# - park: List[str] (각 문자는 'S','O','X')
# - routes: List[str] (예: "N 2", "E 3")
#
# ✅ 규칙 요약:
# - 방향 벡터: N=(-1,0), S=(1,0), W=(0,-1), E=(0,1)
# - 명령 단위 검증: 한 칸이라도 벗어나거나 'X'를 만나면 그 명령 전체 무시(원위치 유지)
# - 시작점 'S'는 park 내에 1회 존재
#
# ✅ 입출력 예시(간단):
# - park = ["SOO","OOO","OOO"], routes = ["E 2","S 2","W 1"] → [2,1]
#
# ✅ 정답 코드:
def solution(park, routes):
    answer = []
    n, m = len(park), len(park[0])
    dir_map = {"N": (-1, 0), "E": (0, 1), "W": (0, -1), "S": (1, 0)}
    
    for i, row in enumerate(park):
        if "S" in row:
            sx, sy = i, row.index("S")
            break
    # print(sx, sy)
    
    for route in routes:
        dir, dist = route.split()
        nx, ny = sx, sy
        ok = True
        for _ in range(int(dist)):
            dx, dy = dir_map[dir]
            nx, ny = nx + dx, ny + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m or park[nx][ny] == "X":
                ok = False
        if ok:
            sx, sy = nx, ny
        # print(sx, sy)
            
    answer.append(sx)
    answer.append(sy)
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달** (힌트 참고 후 구현)
#
# 📚 문제를 풀기 위해 꼭 필요한 개념 & 이 풀이에서 사용한 개념(최소):
# - 시작점 'S' 탐색(행/열 인덱스 찾기)
# - 방향 맵(Dict)로부터 델타 적용
# - **명령 단위** 경로 검증(모든 칸 범위·장애물 확인)
# - 좌표계 일관성: 행(n=세로), 열(m=가로), 인덱스 경계 체크
