# 0307_range_sum_query_mutable.py
# -----------------------------------------------------
# ✅ 제목: Range Sum Query - Mutable (LeetCode 307)
# ✅ 문제 설명(요약):
# - 정수 배열 nums가 주어질 때 다음 연산을 효율적으로 처리.
#   1) update(i, val): 인덱스 i의 값을 val로 갱신
#   2) sumRange(l, r): 구간 [l, r]의 합 반환
#
# ✅ 입력 형식(요지):
# - 초기 배열 nums: List[int]
# - 연산 시퀀스: ["NumArray","sumRange","update","sumRange", ...]
#
# ✅ 규칙 요약:
# - update와 sumRange가 섞여서 다수 호출됨
# - 두 연산 모두 평균적으로 O(log n) 이하의 효율 요구
# - 전형 해법: Fenwick Tree(BIT) 또는 Segment Tree
#
# ✅ 입출력 예시(1개):
# - 입력:
#   ["NumArray","sumRange","update","sumRange"]
#   [[[1,3,5]],[0,2],[1,2],[0,2]]
# - 출력: [null,9,null,8]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)                 # 배열 길이
        self.nums = nums[:]                # 원본 값 보관(증분 갱신용)
        self.bit = [0] * (self.n + 1)      # 1-indexed Fenwick Tree 배열
        for i, v in enumerate(nums):       # 초기 빌드: 각 원소를 BIT에 더함
            self._add(i + 1, v)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:                 # i의 하위 비트를 이용해 조상 노드로 전파
            self.bit[i] += delta
            i += i & -i

    def _prefix(self, i: int) -> int:
        s = 0
        while i > 0:                       # i의 하위 비트를 제거해가며 부분합 누적
            s += self.bit[i]
            i -= i & -i
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]     # 변경분(증분) 계산
        self.nums[index] = val             # 원본값 갱신
        self._add(index + 1, delta)        # BIT에 증분 반영

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)  # [l,r]=pref(r)-pref(l-1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - Fenwick Tree로 구현하여 모든 테스트 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - prefix sum 단독 접근 시 update마다 O(n) 재계산 필요 → 시간 초과 위험.
# - BIT로 전환해 update/sumRange 모두 O(log n)으로 개선.
# - 변수명 혼동 없음. 인덱싱은 BIT 특성상 1-index로 처리.
#
# 📚 사용된/필수 개념(최소):
# - Fenwick Tree(BIT): 부분합과 점 갱신을 로그 시간으로 처리
# - prefix(r) - prefix(l-1)로 구간 합 계산
# - 시간복잡도: update O(log n), sumRange O(log n), 초기화 O(n log n)
