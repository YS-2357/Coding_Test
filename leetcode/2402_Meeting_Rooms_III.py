# 2402_Meeting_Rooms_III.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 2402. Meeting Rooms III
# ✅ 문제 설명(요약):
#   - n개의 회의실과 여러 회의(meetings)가 주어진다.
#   - 각 회의는 [start, end]로 주어지며, 시작 시간이 빠른 순(동률 시 종료가 빠른 순)으로 처리한다.
#   - 회의를 배정할 때, start 시점에 비어 있는 회의실이 있으면 가장 번호가 작은 회의실에 배정한다.
#   - 비어 있는 회의실이 없으면, 가장 빨리 비는 회의실(동률 시 번호가 작은 회의실)이 빌 때까지 기다린 뒤
#     해당 회의실에서 회의를 진행하며, 회의 길이(end-start)만큼 종료 시간을 연장한다.
#   - 가장 많은 회의를 처리한 회의실 번호를 반환한다(동률이면 가장 작은 번호).
#
# ✅ 입력 형식(요지):
#   - n: 회의실 수
#   - meetings: [start, end] 형태의 회의 리스트
#
# ✅ 규칙 요약:
#   - 처리 순서: start 오름차순(동률이면 end 오름차순)
#   - 배정 규칙:
#     1) start 시점에 비는 방이 있으면: 가장 작은 번호 방에 즉시 배정, 종료 시간 = end
#     2) 비는 방이 없으면: 가장 빨리 비는 방을 선택(동률이면 작은 번호), 그 방의 availability에 회의 길이를 더해 연장
#   - 반환 규칙: 처리 횟수가 최대인 방 인덱스(동률이면 작은 인덱스)
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
#   - 아래는 사용자가 제출/채택한 최종 정답 코드이며,
#     이 단계에서는 코드 내용을 변경하지 않고,
#     각 줄마다 설명 주석만 추가한다.

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n                 # 각 회의실이 다음으로 비는 시각(초기에는 모두 0)
        meeting_count = [0] * n                          # 각 회의실이 배정받은 회의 횟수 카운트

        for start, end in sorted(meetings):              # start 기준 정렬(동률이면 end 기준) 후 순서대로 처리
            min_room_availability_time = inf             # (사용 가능한 방이 없을 때) 가장 빨리 비는 시간 추적용
            min_available_time_room = 0                  # 가장 빨리 비는 방의 인덱스
            found_unused_room = False                    # start 시점에 즉시 배정 가능한 방을 찾았는지 여부

            for i in range(n):                           # 모든 방을 선형 탐색
                if room_availability_time[i] <= start:   # 이 방이 start 시점에 비어 있으면
                    found_unused_room = True             # 즉시 배정 가능
                    meeting_count[i] += 1                # 해당 방의 회의 수 증가
                    room_availability_time[i] = end      # 이 방은 end 시각까지 사용됨
                    break                                # "가장 작은 번호 방"이 우선이므로 첫 발견 즉시 종료

                # 즉시 배정 가능한 방이 없는 경우를 대비하여,
                # 가장 빨리 비는 방(availability가 최소인 방)을 추적
                if min_room_availability_time > room_availability_time[i]:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i

            if not found_unused_room:                    # start 시점에 비어 있는 방을 못 찾은 경우
                room_availability_time[min_available_time_room] += end - start
                                                        # 가장 빨리 비는 방에서 기다렸다가,
                                                        # 회의 길이(end-start)만큼 종료 시간을 연장
                meeting_count[min_available_time_room] += 1
                                                        # 해당 방의 회의 수 증가

        return meeting_count.index(max(meeting_count))   # 최대 회의 수를 가진 방의 인덱스 반환(동률이면 가장 작은 인덱스)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - (기록 없음) 본 풀이는 규칙(즉시 배정 시 가장 작은 번호, 불가 시 가장 빨리 비는 방)을 선형 탐색으로 구현한다.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용한 핵심 개념:
#     - 시뮬레이션(정렬된 meetings를 순서대로 처리)
#     - 각 회의마다 방을 선형 탐색하여 즉시 배정 가능 여부 판단
#     - 즉시 배정 불가 시, 가장 빨리 비는 방을 추적해 연장 배정
#   - 성능 관점 주의:
#     - 매 회의마다 n개 방을 전부(또는 일부) 탐색하므로,
#       회의 수가 많고 n도 크면 시간 초과(TLE) 위험이 있다.
#     - 일반적인 최적 해법은 "사용 가능한 방(min-heap) + 사용 중 방(min-heap)" 두 힙으로 처리한다(코드 X).
#
# 📚 시간·공간 복잡도:
#   - 시간 복잡도: O(M log M + M * n)
#     - M = len(meetings)
#     - meetings 정렬 O(M log M)
#     - 각 회의마다 방을 선형 탐색 O(n)
#   - 공간 복잡도: O(n)
#     - room_availability_time, meeting_count 배열
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 두 개의 최소 힙을 사용하는 방식이 표준 최적 풀이:
#     1) available_rooms: 현재 비어 있는 방 번호를 담는 min-heap(가장 작은 번호 우선)
#     2) used_rooms: (끝나는 시간, 방 번호)를 담는 min-heap(가장 빨리 끝나는 방 우선)
#   - 각 회의 start마다 used_rooms에서 end_time <= start인 방을 꺼내 available로 옮기고,
#     available가 있으면 즉시 배정, 없으면 used_rooms의 최상단을 꺼내 "기다린 뒤" 배정하는 방식으로
#     전체를 O(M log n)에 처리 가능(코드 X).
