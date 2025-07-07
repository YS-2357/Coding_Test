# ✅ 러시안 룰렛 문제 풀이 코드
# 문제: 실린더 리스트와 방아쇠를 당길 횟수가 주어질 때, 총알이 발사되지 않을 확률 구하기

# 방법:
# 1. 첫 발은 무조건 비어있다는 가정 하에 시작.
# 2. 해당 지점에서 이후 a번 방아쇠를 당기면서 총알이 없는 칸을 확인.
# 3. 가능한 모든 시작점(0인 지점)에서 시뮬레이션하고, 총알이 안 나오는 횟수 / 전체 가능 케이스 = 확률.


def russian_roulette_probability(cylinder, pulls):
    n = len(cylinder)
    safe_starts = [i for i, val in enumerate(cylinder) if val == 0]  # 첫 발 안전한 시작점 후보

    success_count = 0  # 총알이 안 나오는 케이스
    total_cases = len(safe_starts)  # 전체 가능한 시작점 개수

    for start in safe_starts:
        # a번 방아쇠를 당기는 동안 총알이 없는지 확인
        safe = True
        for i in range(1, pulls + 1):
            idx = (start + i) % n
            if cylinder[idx] == 1:
                safe = False
                break
        if safe:
            success_count += 1

    if total_cases == 0:
        return 0.0

    probability = success_count / total_cases
    return probability


# ✅ 예제 테스트
cylinder = [1, 1, 0, 0, 0, 0, 0, 0]
pulls = 4
result = russian_roulette_probability(cylinder, pulls)
print(f"총알이 안 나올 확률: {result:.4f}")
