# 백준 10973번: 이전 순열
# 문제 설명:
# 현재 주어진 순열의 "이전 순열"을 찾는 문제.
# - 이전 순열이 존재하면 이를 출력한다.
# - 존재하지 않으면 "-1"을 출력한다.

# 입력 형식:
# - 첫 번째 줄에 정수 N이 주어진다. (1 ≤ N ≤ 10,000)
# - 두 번째 줄에 1부터 N까지의 숫자로 이루어진 순열이 주어진다.

# 출력 형식:
# - 입력된 순열의 "이전 순열"을 출력하거나, 존재하지 않으면 "-1"을 출력한다.

# 예제 입력 1:
# 4
# 1 2 3 4
# 예제 출력 1:
# -1

# 예제 입력 2:
# 6
# 3 2 1 6 5 4
# 예제 출력 2:
# 3 2 1 5 6 4

import sys

# ✅ 입력 처리
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# ✅ 이전 순열을 찾는 함수
def find_previous(nums):
    for i in range(N-2, -1, -1):
        if nums[i] > nums[i+1]:
            for j in range(N-1, i, -1):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[i+1:] = reversed(nums[i+1:])
            print(*nums)
            return
    print(-1)

# ✅ 실행
find_previous(nums)


# -----------------------------------------------------
# ❌ 내가 처음 쓴 코드부터 맞을 때까지 틀렸던 점

# 1. ✅ 입력 처리 오류
#    - 기존 코드: `nums = list(map(int, sys.stdin.readline()))`
#    - ❌ 문제점: split()이 없어서 숫자가 한 자리씩 분리되어 입력됨.
#    - ✅ 수정: `nums = list(map(int, sys.stdin.readline().split()))`로 변경하여 제대로 리스트 변환.

# 2. ✅ `reverse()` 사용 오류
#    - 기존 코드: `nums[i+1:] = reverse(nums[i+1:])`
#    - ❌ 문제점: `reverse()`는 리스트를 반환하지 않음.
#    - ✅ 수정: `nums[i+1:] = list(reversed(nums[i+1:]))`으로 변경하여 리스트 변환.

# ✅ 위 수정 후 실행하면 백준에서 정답 판정! 🚀 
