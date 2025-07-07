# 15662_톱니바퀴_2.py
# -------------------------------------------------------
# ✅ 문제 설명:
# - T개의 톱니바퀴가 주어지고, 각 톱니바퀴는 8개의 톱니(0: N극, 1: S극)로 구성됩니다.
# - 특정 톱니바퀴를 시계(1) 혹은 반시계(-1)로 회전시키면,  
#   그 인접 톱니바퀴도 서로 맞닿는 극이 다르면 반대 방향으로 회전합니다.
# - K개의 회전 명령이 주어졌을 때, 모든 회전 후
#   각 톱니의 12시 방향(인덱스 0)이 1(S극)인 톱니의 개수를 출력합니다.
#
# ✅ 입력 형식:
# - 첫째 줄: 톱니바퀴의 개수 T (1 ≤ T ≤ 1,000)
# - 다음 T줄: 톱니바퀴의 상태 (0 또는 1로 구성된 8자리 문자열)
# - 다음 줄: 회전 명령의 개수 K
# - 다음 K줄: 회전시킬 톱니바퀴 번호와 방향 (1-based 번호, 방향: 1=시계, -1=반시계)
#
# ✅ 출력 형식:
# - K번 회전 명령 후, 12시 방향이 S극(1)인 톱니의 개수를 출력합니다.
#
# ✅ 입출력 예제:
# 입력:
# 4
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1
#
# 출력:
# 3
# -------------------------------------------------------

import sys

# ✅ 톱니바퀴 개수 입력
gear_count = int(sys.stdin.readline().strip())

# ✅ 톱니 상태를 gear_list에 저장 (각 톱니는 0과 1로 구성된 리스트)
gear_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(gear_count)]

# ✅ 회전 명령 개수 입력
rotation_count = int(sys.stdin.readline().strip())

# ✅ 각 기어의 누적 회전 상태를 저장할 배열 (시계 +1, 반시계 -1 누적)
rotation_state = [0] * gear_count

# ✅ 회전 시 인덱스 계산 보정 함수
def adjusted_index(x):
    # 톱니 인덱스는 0~7이고 회전이 누적되므로 mod 8을 통해 인덱스를 계산
    return abs(x % 8)

# ✅ 각 회전 명령 처리 함수
def process_rotation(target_gear, direction):
    # 회전 방향을 임시로 기록할 리스트
    temp_rotation = [0] * gear_count
    temp_rotation[target_gear] = direction  # 현재 톱니바퀴는 입력 받은 방향으로 회전

    # ✅ 왼쪽으로 연쇄 전파
    prev_direction = direction
    for left in range(target_gear, 0, -1):
        # 현재 톱니 왼쪽의 2번과 이전 톱니 오른쪽(6번) 비교
        current_right = gear_list[left][adjusted_index(6 - rotation_state[left])]
        left_gear_left = gear_list[left - 1][adjusted_index(2 - rotation_state[left - 1])]

        if current_right != left_gear_left and prev_direction != 0:
            temp_rotation[left - 1] = -prev_direction  # 맞닿은 극이 다르면 반대방향 회전
            prev_direction = -prev_direction
        else:
            break  # 같은 극이면 전파 종료

    # ✅ 오른쪽으로 연쇄 전파
    prev_direction = direction
    for right in range(target_gear, gear_count - 1):
        # 현재 톱니 오른쪽의 6번과 이후 톱니 왼쪽(2번) 비교
        current_left = gear_list[right][adjusted_index(2 - rotation_state[right])]
        right_gear_right = gear_list[right + 1][adjusted_index(6 - rotation_state[right + 1])]

        if current_left != right_gear_right and prev_direction != 0:
            temp_rotation[right + 1] = -prev_direction
            prev_direction = -prev_direction
        else:
            break

    # ✅ 회전 상태 누적
    for idx in range(gear_count):
        rotation_state[idx] += temp_rotation[idx]

# ✅ K번 회전 명령을 입력 받아 처리
for _ in range(rotation_count):
    gear_number, rotate_dir = map(int, sys.stdin.readline().split())
    process_rotation(gear_number - 1, rotate_dir)  # gear_number는 1-based이므로 -1 처리

# ✅ 점수 계산 (12시 방향이 1인 톱니 개수)
result = 0
for i in range(gear_count):
    # 현재 12시 방향 톱니 상태 확인
    if gear_list[i][adjusted_index(-rotation_state[i])] == 1:
        result += 1

# ✅ 최종 결과 출력
print(result)

# -------------------------------------------------------
# ✅ 문제 풀이 방식 (상세 설명):
#
# 📚 핵심 개념:
# - 톱니바퀴 회전은 직접 deque.rotate() 하는 대신, 
#   '누적 회전 상태'로 인덱스를 간접 조절합니다.
#
# 🛠 알고리즘 단계:
# 1️⃣ 입력받은 톱니 상태를 gear_list에 저장합니다.
# 2️⃣ 회전 상태를 저장할 rotation_state 배열을 준비합니다.
#    이 배열의 각 원소는 "회전 회수(방향 포함)"를 의미합니다.
#
# 3️⃣ 각 회전 명령을 처리할 때:
#     (1) 해당 톱니의 회전 방향을 temp_rotation 배열에 기록합니다.
#     (2) 왼쪽 방향으로 전파:
#         - 현재 톱니의 6번 인덱스와 왼쪽 톱니의 2번 인덱스 극을 비교해 
#           다르면 반대방향 회전, 같으면 전파 중지.
#     (3) 오른쪽 방향 전파도 같은 원리로 진행합니다.
#     (4) 마지막으로 rotation_state에 temp_rotation을 누적합니다.
#
# 4️⃣ 모든 회전이 끝난 후, 
#     gear[i][adjusted_index(-rotation_state[i])]를 통해 
#     현재 12시 방향 톱니 극성을 확인합니다.
#
# 5️⃣ 12시 방향이 1인 톱니의 개수를 세어 출력합니다.
#
# 🧩 작은 시뮬레이션 예:
# - 톱니 A와 B의 맞닿는 극이 서로 다르면:
#     A 회전 → B는 -A 방향으로 회전 → C도 조건에 따라 회전 여부 결정
# - 최종적으로 모든 톱니의 회전상태를 계산 후 점수를 누적합니다.
#
# 🚀 시간 복잡도:
# - O(K * T) (K: 회전 횟수, T: 톱니 수) 충분히 통과 가능.
#
# ✅ 이 방법의 장점:
# - 회전 시마다 deque를 돌리지 않고, O(1)로 인덱스만 조정 가능
# - 메모리 효율 및 연산 효율이 우수
# -------------------------------------------------------
