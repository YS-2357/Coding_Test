# 1356_sort_integers_by_the_number_of_1_bits.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1356. Sort Integers by The Number of 1 Bits
# 🏷️ 유형: Sorting, Bit Manipulation
#
# ✅ 문제 설명(요약):
#   - 정수 배열 arr을 정렬한다.
#   - 1차 기준: 각 수의 이진수에서 1의 개수(popcount)가 작은 순.
#   - 2차 기준: popcount가 같으면 수 자체가 작은 순.
#
# ✅ 입력 형식(요지):
#   - arr: List[int]
#
# ✅ 규칙 요약:
#   - 각 원소 x에 대해 (popcount(x), x)를 정렬 키로 사용한다.
#   - popcount는 내장(bit_count) 또는 직접 계산으로 구할 수 있다.
#
# 🧠 핵심 불변식(Invariant):
#   - 정렬 키 (popcount(x), x)는 항상 “popcount 우선, 값 자체 다음”의 우선순위를 보장한다.
#   - 파이썬 sort는 key에 의해 생성된 튜플을 사전식으로 비교하므로, 1차/2차 정렬이 동시에 성립한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
# [풀이 1] bit_count() 사용

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:                 # popcount 기준 → 값 기준으로 정렬
        arr.sort(key = lambda num: (num.bit_count(), num))             # (1의 개수, 수 자체) 튜플 키로 정렬
        return arr                                                     # 정렬된 배열 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답(내장 popcount를 활용한 가장 간단한 정렬).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 가능 포인트(참고):
#     - 2차 기준(num)을 누락하면 popcount가 같은 값들의 상대 순서가 요구와 달라질 수 있음.
#   - 사용 개념:
#     - 정렬 key 함수
#     - popcount(bit_count)
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n) (정렬) + key 평가 비용(각 원소 popcount)
#   - 공간: O(1) 추가 (정렬 내부 메모리는 구현 의존)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 범위가 작다면 counting sort(버킷)로 popcount별로 모아 정렬하는 방식도 가능(개념만).


# -----------------------------------------------------
# ✅ 제목: LeetCode 1356. Sort Integers by The Number of 1 Bits
# 🏷️ 유형: Sorting, Bit Manipulation
#
# ✅ 문제 설명(요약):
#   - 정수 배열 arr을 (popcount, 값) 기준으로 오름차순 정렬한다.
#
# ✅ 입력 형식(요지):
#   - arr: List[int]
#
# ✅ 규칙 요약:
#   - popcount는 직접 비트를 훑으며 계산한다.
#   - 정렬은 (popcount(x), x) 기준이다.
#
# 🧠 핵심 불변식(Invariant):
#   - find_weight(num)은 num의 1비트를 하나씩 확인해 누적한 weight가 popcount와 일치한다.
#   - 정렬 과정에서 각 원소는 (find_weight(num), num) 키로만 비교되어 요구 순서가 유지된다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
# [풀이 2] 마스크 이동 + 비트 제거(XOR) 방식

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:                 # popcount 기준 정렬 함수
        def find_weight(num):                                          # num의 1비트 개수를 직접 계산
            mask = 1                                                   # 현재 확인할 비트 마스크(LSB부터 시작)
            weight = 0                                                 # 1의 개수 누적 변수
            
            while num:                                                 # num이 0이 될 때까지 반복(남은 1비트가 있을 때)
                if num & mask:                                         # 현재 mask 위치에 1비트가 있으면
                    weight += 1                                        # 1의 개수 증가
                    num ^= mask                                        # 해당 1비트를 0으로 만들어 진행 보장
                
                mask <<= 1                                             # 다음 비트로 이동
            
            return weight                                              # 최종 popcount 반환
        
        arr.sort(key = lambda num: (find_weight(num), num))            # (popcount, 값) 기준으로 정렬
        return arr                                                     # 정렬된 배열 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답(직접 popcount 계산 후 정렬).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 주의 포인트(참고):
#     - mask를 올리면서 num을 줄이지 않으면 무한 루프 위험이 있으나, 여기서는 num ^= mask로 1비트를 제거하여 종료됨.
#     - 입력이 0이면 while num이 즉시 종료되어 popcount=0 처리됨.
#   - 사용 개념:
#     - 비트 마스크 순회
#     - 1비트 제거(XOR)
#     - 정렬 key 튜플
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n) + popcount 계산 비용(각 원소당 비트 길이만큼)
#   - 공간: O(1) 추가
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 더 빠른 popcount는 Brian Kernighan(num &= num-1) 방식이 일반적으로 효율적(아래 풀이 3).


# -----------------------------------------------------
# ✅ 제목: LeetCode 1356. Sort Integers by The Number of 1 Bits
# 🏷️ 유형: Sorting, Bit Manipulation
#
# ✅ 문제 설명(요약):
#   - arr을 popcount 오름차순, tie는 값 오름차순으로 정렬한다.
#
# ✅ 입력 형식(요지):
#   - arr: List[int]
#
# ✅ 규칙 요약:
#   - popcount는 Brian Kernighan 알고리즘으로 계산한다.
#   - 정렬 키는 (popcount(x), x)이다.
#
# 🧠 핵심 불변식(Invariant):
#   - num &= (num - 1)은 num에서 “가장 낮은 1비트”를 정확히 하나 제거한다.
#   - while num 루프는 1비트 개수만큼 반복되며, weight는 제거 횟수이므로 popcount와 동일하다.
#   - 정렬 키 비교는 (weight, num) 튜플의 사전식 비교로 요구 순서를 보장한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
# [풀이 3] Brian Kernighan(popcount) 방식

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:                 # popcount 기준 정렬 함수
        def find_weight(num):                                          # num의 1비트 개수를 빠르게 계산
            weight = 0                                                 # 1비트 개수 누적 변수
            
            while num:                                                 # 1비트가 남아있는 동안 반복
                weight += 1                                            # 1비트를 하나 제거할 것이므로 카운트 증가
                num &= (num - 1)                                       # 최하위 1비트를 제거
            
            return weight                                              # 최종 popcount 반환
        
        arr.sort(key = lambda num: (find_weight(num), num))            # (popcount, 값) 기준으로 정렬
        return arr                                                     # 정렬된 배열 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 정답(1비트 개수만큼만 반복하는 popcount로 효율적).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 가능 포인트(참고):
#     - num &= (num - 1)의 의미를 모르고 다른 연산으로 바꾸면 popcount가 틀어질 수 있음.
#   - 사용 개념:
#     - Brian Kernighan 알고리즘(최하위 1비트 제거)
#     - 정렬 key 튜플 (popcount, 값)
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n) + popcount 계산(각 원소당 set bit 수만큼)
#   - 공간: O(1) 추가
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - bit_count()를 쓸 수 있는 환경이면 풀이 1이 가장 간단하고 빠른 편이다(개념만).
