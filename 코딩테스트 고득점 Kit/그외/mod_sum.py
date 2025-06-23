def compute_mod_sum(n, m):
    MOD = 10**9 + 7
    total = 0

    # ✅ [1단계] i % j 항들의 누적합 계산
    # 전체 합: sum_{i=1}^{n} sum_{j=1}^{m} (i % j)
    # 하지만 순서를 바꿔서 sum_{j=1}^{m} sum_{i=1}^{n} (i % j) 로 처리
    for j in range(1, m + 1):
        # i를 1~n까지 순회할 때, j로 나눈 몫이 count인 구간 개수
        count = n // j

        # [1-1] (i % j)의 반복 패턴 합: i = q*j + r 에서 r = 0~(j-1)
        # 각 q (몫)에 대해 (0 + 1 + ... + j-1)의 합 = j * count * (count - 1) // 2
        total += j * count * (count - 1) // 2

        # [1-2] 나머지 부분: i % j에서 i가 n까지 도달하지 못한 남은 부분의 합
        # 마지막 몫 이후 남은 i들에 대해: i % j = i 자체이므로 (1 + 2 + ... + r)
        r = n % j
        total += r * (r + 1) // 2

        total %= MOD  # 오버플로우 방지용

    # ✅ [2단계] j % i 항들의 누적합 계산
    # 위와 동일하게 순서를 바꿔 sum_{i=1}^{n} sum_{j=1}^{m} (j % i)
    for i in range(1, n + 1):
        count = m // i

        # [2-1] (j % i)의 반복 패턴 합
        total += i * count * (count - 1) // 2

        # [2-2] 나머지 부분 합
        r = m % i
        total += r * (r + 1) // 2

        total %= MOD

    # ✅ [3단계] 최종 결과 반환
    return total % MOD
