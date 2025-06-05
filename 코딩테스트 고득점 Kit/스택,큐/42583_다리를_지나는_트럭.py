# 42583_다리를_지나는_트럭.py
# -----------------------------------------------------
# ✅ 문제 설명:
# - 트럭 여러 대가 일렬로 정해진 순서대로 다리를 건너려 함.
# - 다리 길이(bridge_length)와 최대 하중(weight)이 주어짐.
# - 각 트럭의 무게 리스트(truck_weights)가 주어짐.
# - 트럭은 1초에 1칸씩 이동하며, 다리에 동시에 올라갈 수 있음.
# - 다리를 모두 건너는 데 걸리는 시간을 계산하는 문제.

# ✅ 입력 형식:
# - bridge_length (1 ≤ bridge_length ≤ 10,000)
# - weight (1 ≤ weight ≤ 10,000)
# - truck_weights (1 ≤ len ≤ 10,000, 각 무게는 ≤ weight)

# ✅ 출력 형식:
# - 모든 트럭이 다리를 건너는 데 걸리는 총 시간 (초)

# ✅ 입출력 예제:
# 예제 입력: bridge_length = 2, weight = 10, truck_weights = [7, 4, 5, 6]
# 예제 출력: 8
# -----------------------------------------------------

from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque([0] * bridge_length)  # 다리 위 트럭 상태 (0은 빈 칸)
    trucks = deque(truck_weights)       # 대기 중인 트럭들
    total_weight = 0                    # 현재 다리 위 총 무게
    time = 0                            # 경과 시간

    while trucks or total_weight > 0:
        time += 1

        # 다리에서 트럭 하나 나감
        removed = queue.popleft()
        total_weight -= removed

        if trucks:
            # 다음 트럭이 올라갈 수 있는지 확인
            if total_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                queue.append(truck)
                total_weight += truck
            else:
                queue.append(0)  # 트럭 없음 → 0으로 채움

    return time

# -----------------------------------------------------
# ✅ 오답 및 실수 정리:
# ❌ 초안 코드에서는 sum(queue)로 현재 다리 무게를 매번 계산 → 비효율적
# ❌ 트럭이 다리를 다 건넌 이후의 처리 누락 → 마지막 while queue 블록 필요했음

# ✅ 사용된 힌트 목록:
# - deque를 이용한 다리 상태 모델링
# - total_weight 변수로 성능 개선
# - while 루프 조건: 대기 트럭이 남아 있거나 다리 위에 트럭이 존재할 때까지

# ✅ 개선 포인트:
# - 매 루프마다 time += 1로 초 단위 진행
# - popleft → 다리 진출, append → 다리 진입
# - 트럭이 올라가지 못하면 0을 append하여 흐름 유지
# -----------------------------------------------------
