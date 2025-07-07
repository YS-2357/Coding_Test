def min_total_time(tasks, speed_a, speed_b):
    total = sum(tasks)                        # ✅ [1단계] 전체 작업량의 합 (A와 B가 나눠서 처리해야 할 총량)
    max_sum = total * max(speed_a, speed_b)   # ✅ [1단계] 이론적으로 가능한 최대 시간 (초기값 설정 용도)
    
    dp = [False] * (total + 1)                # ✅ [1단계] dp[s] = True면 A가 작업량 s를 만들 수 있다는 뜻
    dp[0] = True                              # ✅ [1단계] 작업량 0은 항상 가능 (초기 상태)

    # ✅ [2단계] 각 작업량 t에 대해 dp 배열 갱신 (0-1 Knapsack 방식)
    for t in tasks:
        for s in range(total, t - 1, -1):     # ✅ 뒤에서부터 순회하여 중복 갱신 방지
            if dp[s - t]:                     # ✅ 이전에 만들 수 있었던 작업량 s-t가 있다면
                dp[s] = True                  # → 현재 작업량 s도 만들 수 있음

    result = float('inf')                     # ✅ [2단계] 최소 최대 시간 결과 저장용 변수

    # ✅ [2단계] 가능한 A 작업량을 모두 순회하며 최소 최대 시간을 계산
    for a_sum in range(total + 1):
        if dp[a_sum]:                         # ✅ A가 작업량 a_sum을 만들 수 있다면
            time_a = a_sum * speed_a          # → A가 작업을 처리하는 데 걸리는 시간
            time_b = (total - a_sum) * speed_b  # → B가 나머지를 처리하는 데 걸리는 시간
            result = min(result, max(time_a, time_b))  # ✅ 최대 시간 중 최소값을 정답으로 갱신

    return result                             # ✅ [3단계] 최소 최대 작업시간 반환
