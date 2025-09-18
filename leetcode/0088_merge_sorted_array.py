# 0088_merge_sorted_array.py
# -----------------------------------------------------
# ✅ 제목: Merge Sorted Array (LeetCode 88)
# ✅ 문제 설명(요약):
# - 두 정렬된 배열 nums1, nums2가 주어짐.
# - nums1은 길이가 m+n이며, 앞쪽 m개만 유효 원소, 뒤쪽 n개는 0으로 채워짐.
# - nums2는 길이가 n.
# - 목표: 두 배열을 하나의 정렬된 배열로 병합하여 nums1에 in-place 저장.

# ✅ 입력 형식(요지):
# - nums1: List[int], 길이 m+n
# - m: int, nums1의 유효 원소 개수
# - nums2: List[int], 길이 n
# - n: int

# ✅ 규칙 요약:
# 1) nums1을 in-place로 수정 (새 리스트 반환 금지).
# 2) 두 배열은 비내림차순(오름차순).
# 3) 시간 복잡도 O(m+n), 공간 O(1) 목표.

# ✅ 입출력 예시(1개):
# - 입력: nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
# - 출력: nums1=[1,2,2,3,5,6]

# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1          # nums1 유효 구간의 끝 인덱스
        j = n - 1          # nums2의 끝 인덱스
        k = m + n - 1      # nums1 전체 길이의 끝 인덱스

        # 뒤에서부터 비교하여 큰 값을 nums1 뒤쪽에 채운다
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # nums2가 남았다면 앞쪽에 복사
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 투 포인터를 배열 뒤쪽에서 이동시키며 올바르게 병합됨.

# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - 초기 풀이에서 nums1을 새 리스트로 재할당(`nums1 = ...`)해 in-place 조건을 어김.
# - 남은 원소 처리 시 인덱스 비교(m, n)도 잘못되어 누락 발생.
# - 수정: 뒤에서부터 채우는 방식으로 변경, nums2만 남은 경우만 복사.

# 📚 사용된/필수 개념(최소):
# - 투 포인터(two pointers)
# - 배열 in-place 수정
# - 시간복잡도 O(m+n), 공간복잡도 O(1)
