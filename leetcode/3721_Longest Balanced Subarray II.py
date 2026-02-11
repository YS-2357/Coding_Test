# 3721_Longest Balanced Subarray II.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3721. Longest Balanced Subarray II
# 🏷️ 유형: 세그먼트 트리 / 접두사 합 존재성 질의 / 오른쪽부터 스캔 / 첫 등장 마커 유지
#
# ✅ 문제 설명(요약):
#   - nums에서 “balanced subarray”의 최대 길이를 구한다.
#   - 코드 구조 기준으로 balanced는 “서로 다른 짝수 값 개수”와 “서로 다른 홀수 값 개수”가 같은 부분배열을 의미한다.
#   - 부분배열 [l..r]에서 각 값의 “첫 등장”만 1(짝수) 또는 -1(홀수)로 카운트하여,
#     그 합이 0이 되는 가장 긴 구간을 찾는다.
#
# ✅ 입력 형식(요지):
#   - nums: List[int]
#
# ✅ 규칙 요약:
#   - 같은 값이 부분배열 안에 여러 번 있더라도, “서로 다른 값 수”만 세어야 한다.
#   - 이를 위해 l을 고정했을 때, 각 값의 “l 이상에서의 첫 등장 위치”만 마커로 남긴다.
#   - 마커 값은 짝수면 +1, 홀수면 -1로 둔다.
#   - [l..r] 구간 합이 0이면 (서로 다른 짝수 수) == (서로 다른 홀수 수) 이다.
#
# 🧠 핵심 불변식(Invariant):
#   - l을 오른쪽에서 왼쪽으로 이동시키면서, first[num]은 “현재 l에서 바라봤을 때” num의 첫 등장 인덱스를 저장한다.
#   - 세그먼트 트리의 리프 arr[i]는 i가 어떤 값의 첫 등장이면 (+1 또는 -1), 아니면 0이다.
#   - find_rightmost_prefix(target=0)는 현재 arr의 접두사 합이 0이 되는 가장 오른쪽 인덱스를 찾는다.
#   - l에서의 구간 합 sum(arr[l..r]) == 0 은 prefixsum(r) == prefixsum(l-1) 와 동치이며,
#     이 구현은 “현재 l 기준 prefixsum이 0이 되는 가장 오른쪽 r”을 찾는 방식으로 최대 길이를 갱신한다.
#
# ✅ 정답 코드(제공된 풀이; 절대 수정 금지)

class SegmentTree:                                                   # 길이 n 배열 위에서 동작하는 세그먼트 트리 클래스 정의
    """Segment Tree over array of size n"""                          # 세그먼트 트리 용도를 간단히 설명하는 도큐스트링

    def __init__(self, n: int):                                      # 세그먼트 트리 초기화 함수
        self.n = n                                                   # 원본 배열 길이를 저장
        self.size = 4 * n                                            # 세그먼트 트리 배열 크기를 4n으로 잡음
        self.sum = [0] * self.size                                   # 각 노드 구간의 합을 저장할 배열
        self.min = [0] * self.size                                   # 각 노드 구간에서 가능한 최소 접두사 합을 저장
        self.max = [0] * self.size                                   # 각 노드 구간에서 가능한 최대 접두사 합을 저장

    def _pull(self, node: int):                                      # 자식 정보로 부모 노드 정보를 갱신하는 내부 함수
        """Helper to recompute information of node by it's children"""# pull 연산의 역할을 설명하는 도큐스트링

        l, r = node * 2, node * 2 + 1                                # 왼쪽/오른쪽 자식 노드 인덱스를 계산

        self.sum[node] = self.sum[l] + self.sum[r]                   # 부모 구간 합은 자식 합의 합
        self.min[node] = min(self.min[l], self.sum[l] + self.min[r]) # 부모 최소 접두사 합은 (왼쪽 최소) vs (왼쪽합+오른쪽최소)
        self.max[node] = max(self.max[l], self.sum[l] + self.max[r]) # 부모 최대 접두사 합은 (왼쪽 최대) vs (왼쪽합+오른쪽최대)

    def update(self, idx: int, val: int):                            # 원본 배열의 idx 위치 값을 val로 갱신하는 함수
        """Update value by index idx in original array"""            # update 용도를 설명하는 도큐스트링

        node, l, r = 1, 0, self.n - 1                                # 루트 노드와 전체 구간 [0..n-1]로 시작
        path = []                                                    # 리프까지 내려간 경로를 저장해 다시 pull 하기 위한 스택

        while l != r:                                                # 리프 노드(단일 인덱스)에 도달할 때까지
            path.append(node)                                        # 현재 노드를 경로에 저장
            m = l + (r - l) // 2                                     # 현재 구간의 중간값을 계산
            if idx <= m:                                             # 갱신 인덱스가 왼쪽 구간이면
                node = node * 2                                      # 왼쪽 자식으로 이동
                r = m                                                # 오른쪽 경계를 중간으로 좁힘
            else:                                                    # 갱신 인덱스가 오른쪽 구간이면
                node = node * 2 + 1                                  # 오른쪽 자식으로 이동
                l = m + 1                                            # 왼쪽 경계를 중간+1로 좁힘

        self.sum[node] = val                                         # 리프 구간 합을 val로 설정
        self.min[node] = val                                         # 리프 최소 접두사 합도 val
        self.max[node] = val                                         # 리프 최대 접두사 합도 val

        while path:                                                  # 경로를 따라 올라가며
            self._pull(path.pop())                                   # 각 부모 노드를 pull로 재계산

    def find_rightmost_prefix(self, target: int = 0) -> int:         # 접두사 합이 target인 가장 오른쪽 인덱스를 찾는 함수
        """Find rightmost index r with prefixsum(r) = target
        prefixsum(i) = sum(arr[j] for j in range(i + 1))"""          # 접두사 합 정의를 포함한 도큐스트링

        node, l, r, sum_before = 1, 0, self.n - 1, 0                 # 루트에서 시작하며 sum_before는 현재 노드 왼쪽까지의 누적합

        def _exist(node: int, sum_before: int):                      # 해당 노드 구간 내에 target을 만드는 접두사 합이 존재하는지 검사
            return self.min[node] <= target - sum_before <= self.max[node]  # target-sum_before가 구간의 [min,max] 안이면 가능

        if not _exist(node, sum_before):                             # 전체 구간에서 target 접두사 합이 불가능하면
            return -1                                                # 존재하지 않음을 -1로 반환

        while l != r:                                                # 리프에 도달할 때까지 내려가며
            m = l + (r - l) // 2                                     # 현재 구간의 중간 인덱스를 계산
            lchild, rchild = node * 2, node * 2 + 1                  # 왼쪽/오른쪽 자식 노드를 계산

            sum_before_right = self.sum[lchild] + sum_before         # 오른쪽 자식 구간으로 갈 때의 누적합을 계산
            if _exist(rchild, sum_before_right):                     # 오른쪽 구간에 해가 존재하면(더 오른쪽을 우선)
                node = rchild                                        # 오른쪽 자식으로 이동
                l = m + 1                                            # 구간을 오른쪽 절반으로 좁힘
                sum_before = sum_before_right                        # 누적합을 오른쪽 기준으로 갱신
            else:                                                    # 오른쪽에 해가 없으면
                node = lchild                                        # 왼쪽 자식으로 이동
                r = m                                                # 구간을 왼쪽 절반으로 좁힘

        return l                                                     # 최종 리프 인덱스가 가장 오른쪽 해의 위치

class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def longestBalanced(self, nums: List[int]) -> int:              # balanced 부분배열의 최대 길이를 반환하는 함수
        n = len(nums)                                               # 배열 길이를 저장

        stree = SegmentTree(n)                                      # 현재 l에 대한 balance 배열을 담는 세그먼트 트리 생성
        first = dict()                                              # 현재 l에서 각 값의 “첫 등장 인덱스”를 저장할 딕셔너리

        result = 0                                                  # 정답(최대 길이)을 저장할 변수 초기화
        for l in reversed(range(n)):                                # l을 n-1부터 0까지 오른쪽→왼쪽으로 이동
            num = nums[l]                                           # 현재 위치의 값을 num에 저장
    
            if num in first:                                        # num이 이미 오른쪽에 첫 등장 마커가 있었다면
                stree.update(first[num], 0)                         # 이전 첫 등장 위치의 마커를 0으로 제거

            first[num] = l                                          # 이제 num의 첫 등장은 l로 갱신
            stree.update(l, 1 if num % 2 == 0 else -1)              # l 위치에 짝수면 +1, 홀수면 -1 마커를 설정

            r = stree.find_rightmost_prefix(target=0)               # 접두사 합이 0이 되는 가장 오른쪽 r을 찾음
            if r >= l:                                              # 찾은 r이 현재 l 이상이면(유효 구간이면)
                result = max(result, r - l + 1)                     # [l..r] 길이로 최대값을 갱신

        return result                                               # 최종 최대 길이를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 제출 코드 기준: 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 오른쪽부터 스캔하며 “각 값의 첫 등장만 반영한 balance 배열”을 유지하고, 세그먼트 트리로 접두사 합=0의 최우측 해를 탐색.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n log n)  (각 l에서 update 1~2회 + find 1회)
#   - 공간: O(n)        (세그먼트 트리 + first 딕셔너리)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 세그먼트 트리 대신, prefix 상태를 해시로 관리하는 방식이 가능하다면 O(n)도 노려볼 수 있으나,
#     “첫 등장 마커가 l 이동에 따라 바뀌는 동적성” 때문에 추가 구조가 필요하다(개념만).
