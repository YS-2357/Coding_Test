# ✅ 2번 서버 요청 처리 문제 풀이 코드
# 문제: n명까지 접속 가능한 서버에 요청이 들어오고,
# a시간 후 자리비움, b시간 후 추방.
# n명이 다 찼을 때 새로운 요청이 오면 자리비움 중 오래된 순으로 내보내고 새로 받음.
# 자리비움이 없으면 거절(-1).

# 주요 로직:
# - 시간 흐름에 따라 유저 상태 업데이트 (활동, 자리비움, 추방)
# - 새로운 요청이 들어오면 자리비움 상태를 정리하고 처리
# - 결과: 각 요청에 대해 서버 인원 수 출력 (거절 시 -1)

from collections import deque

def server_request(n, a, b, requests):
    server = deque()  # (id, 입장시간, 상태(active/wait))
    results = []

    for time, user_id in requests:
        # 현재 시간에서 b시간이 지난 유저 추방
        server = deque([(id_, t, st) for (id_, t, st) in server if time - t < b])

        # a시간이 지난 유저는 상태를 'wait'로 변경
        new_server = deque()
        for id_, t, st in server:
            if st == 'active' and (time - t) >= a:
                new_server.append((id_, t, 'wait'))
            else:
                new_server.append((id_, t, st))
        server = new_server

        # 새로운 요청 처리
        if any(id_ == user_id for (id_, _, _) in server):
            # 이미 접속 중인 id는 갱신 (재접속 처리)
            server = deque((id_, t, st) for (id_, t, st) in server if id_ != user_id)
            server.append((user_id, time, 'active'))
            results.append(len(server))
        else:
            if len(server) < n:
                server.append((user_id, time, 'active'))
                results.append(len(server))
            else:
                # 자리비움 중인 유저가 있는지 확인
                wait_users = [i for i, (_, _, st) in enumerate(server) if st == 'wait']
                if wait_users:
                    remove_idx = wait_users[0]
                    server.remove(server[remove_idx])
                    server.append((user_id, time, 'active'))
                    results.append(len(server))
                else:
                    # 거절
                    results.append(-1)

    return results


# ✅ 예제:
# n = 2 (최대 2명), a = 3, b = 5
# 요청: (1, 'A'), (2, 'B'), (4, 'C'), (6, 'D'), (7, 'E')
# 시간 흐름에 따른 유저 상태 변화 및 수용 결과 출력
requests = [(1, 'A'), (2, 'B'), (4, 'C'), (6, 'D'), (7, 'E')]
results = server_request(2, 3, 5, requests)
print(results)  # 예상 출력 예: [1, 2, 2 or -1, ...] 상황에 따라 다름
