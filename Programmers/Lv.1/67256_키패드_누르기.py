# 67256_키패드_누르기.py
# -----------------------------------------------------
# ✅ 제목: 키패드 누르기 — 현재 손 위치와 목표 좌표의 맨해튼 거리 비교
# ✅ 문제 설명(요약):
# - 숫자 배열 numbers를 왼손/오른손으로 누르며, 1/4/7은 L, 3/6/9는 R 고정.
# - 2/5/8/0은 양손 중 더 가까운 손, 같으면 hand(“left”/“right”) 선호에 따름.
# - 각 선택 후 해당 손의 위치를 그 숫자 좌표로 갱신.
#
# ✅ 입력 형식(요지):
# - numbers: List[int], hand: str ("left" 또는 "right")
#
# ✅ 규칙 요약:
# - 키패드 좌표 매핑 후, 매 수마다 L·R 고정 열은 즉시 결정.
# - 가운데 열은 맨해튼 거리 비교 → 동률 시 hand 선호.
# - 선택한 손의 좌표를 업데이트하며 문자열로 누적 반환.
#
# ✅ 입출력 예시(간단):
# - numbers=[1,3,4,5,8,2,1,4,5,9,5], hand="right"
#   → "LRLLLRLLRRL"

def solution(numbers, hand):
    answer = ''
    pos = {
        1: (0,0), 2: (0,1), 3: (0,2),
        4: (1,0), 5: (1,1), 6: (1,2),
        7: (2,0), 8: (2,1), 9: (2,2),
        0: (3, 1)
    }
    lx, ly, rx, ry = 3, 0, 3, 2
    
    for num in numbers:
        x, y = pos[num]
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            lx, ly = x, y
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            rx, ry = x, y
        else:
            ld = (abs(lx - x) + abs(ly - y)) 
            rd = (abs(rx - x) + abs(ry - y)) 
            if ld == rd:
                if hand == "right":
                    answer += "R"
                    rx, ry = x, y
                else:
                    answer += "L"
                    lx, ly = x, y
            elif ld > rd:
                answer += "R"
                rx, ry = x, y
            else:
                answer += "L"
                lx, ly = x, y
            
    return answer

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 한 번에 정답 **도달**
#
# 📚 꼭 필요한 개념 & 사용 개념(최소):
# - 키패드 숫자→좌표 딕셔너리 매핑
# - 왼손/오른손 현재 좌표 유지
# - 맨해튼 거리 비교, 동률 시 hand 선호 반영
# - 선택 후 해당 손 위치 갱신
