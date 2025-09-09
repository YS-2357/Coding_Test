# 0021_merge_two_sorted_lists.py
# -----------------------------------------------------
# ✅ 제목: Merge Two Sorted Lists
# ✅ 문제 설명(요약):
# - 두 개의 정렬된 단일 연결 리스트 list1, list2가 주어진다.
# - 이 둘을 병합하여 하나의 정렬된 연결 리스트를 반환한다.
#
# ✅ 입력 형식(요지):
# - list1: Optional[ListNode]
# - list2: Optional[ListNode]
#
# ✅ 규칙 요약:
# 1) 투 포인터를 이용해 작은 값을 차례대로 이어 붙인다.
# 2) 남은 리스트가 있으면 통째로 이어 붙인다.
# 3) dummy 노드를 사용해 head 삭제 케이스까지 깔끔하게 처리한다.
#
# ✅ 입출력 예시(1개):
# - list1 = [1,2,4], list2 = [1,3,4]
#   → 결과: [1,1,2,3,4,4]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:                # 둘 다 비었으면 빈 리스트 반환
            return list1
        elif not list1:                            # list1이 비었으면 list2 반환
            return list2
        elif not list2:                            # list2가 비었으면 list1 반환
            return list1

        dummy = ListNode(0)                        # 결과 리스트 시작 dummy
        tail = dummy                               # tail 포인터로 끝 추적

        while list1 or list2:                      # 두 리스트를 모두 순회할 때까지
            if list1 and list2:                    # 두 리스트가 다 남아 있다면
                if list1.val > list2.val:          # 더 작은 값을 먼저 붙인다
                    tail.next = ListNode(list2.val)
                    tail = tail.next
                    list2 = list2.next
                else:
                    tail.next = ListNode(list1.val)
                    tail = tail.next
                    list1 = list1.next
            elif not list1:                        # list1이 끝났으면 list2를 붙인다
                tail.next = list2
                tail = tail.next
                list2 = None
            elif not list2:                        # list2가 끝났으면 list1을 붙인다
                tail.next = list1
                tail = tail.next
                list1 = None

        return dummy.next                          # dummy 다음이 병합된 리스트 head

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 조건문 방향을 반대로 주었을 때 오름차순이 깨졌지만,
#   조건을 고치니 정상적으로 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (오류) if list1.val > list2.val: list1을 붙이는 로직 → 큰 값이 먼저 와서 정렬 깨짐.
# - (수정) if list1.val > list2.val: list2를 붙이고, 아니면 list1을 붙이도록 수정.
#
# 📚 사용된/필수 개념(최소):
# - 투 포인터(two pointers)
# - dummy 노드와 tail 포인터로 연결 리스트 병합
# - 시간복잡도 O(m+n), 공간복잡도 O(m+n) (새 노드 생성 방식 기준)
