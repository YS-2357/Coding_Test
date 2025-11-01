# 3217_Delete_Nodes_From_Linked_List_Present_in_Array.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 3217. Delete Nodes From Linked List Present in Array
# ✅ 문제 설명(요약):
#   연결 리스트 head가 주어지고, nums 배열에 포함된 값들은 모두 삭제해야 한다.
#   삭제 후 새로 갱신된 연결 리스트의 head를 반환하라.
#
# ✅ 입력 형식(요지):
#   - head: 단일 연결 리스트의 시작 노드 (ListNode)
#   - nums: 삭제해야 할 값들이 담긴 리스트
#
# ✅ 규칙 요약:
#   - nums 안에 포함된 값들을 리스트에서 모두 제거.
#   - head 노드가 삭제 대상일 수도 있으므로 더미(dummy) 노드 필요.
#   - 한 번의 순회로 처리해야 함 (O(n)).
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ban = set(nums)                   # 삭제할 값들을 빠른 탐색용 집합으로 변환 (O(1) 탐색)
        dummy = ListNode(0)               # 더미 노드 생성 (head 삭제 시 안전하게 처리)
        dummy.next = head
        prev, cur = dummy, head           # prev는 마지막 유효 노드, cur은 현재 검사 중 노드

        while cur:                        # 리스트 끝까지 순회
            if cur.val in ban:            # 삭제 대상이면
                prev.next = cur.next       # 연결을 건너뛰어 cur 노드 제거
            else:
                prev = cur                 # 유효 노드면 prev를 cur로 전진
            cur = cur.next                 # 다음 노드로 이동

        return dummy.next                 # 실제 head 반환 (더미 다음 노드)
# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 모든 테스트케이스 통과.
#   - 삭제 대상이 head에 포함되거나 연속된 경우도 정상 처리됨.
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 사용 개념: 연결 리스트 포인터 재연결(Linked List manipulation)
#   - 핵심 아이디어:
#       • 더미(dummy) 노드로 head 삭제를 안전하게 처리.
#       • prev(유효 노드)와 cur(검사 노드) 포인터로 1패스 순회.
#       • 삭제는 포인터만 재연결(prev.next = cur.next)로 구현.
#   - nums → set 변환으로 탐색 시간 O(1) 보장.
#
# 📚 시간·공간 복잡도:
#   - 시간복잡도: O(n + m)
#       • n: 연결 리스트 길이
#       • m: nums 길이 (set 변환)
#   - 공간복잡도: O(m) (집합 저장)
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 값 복사 방식 (노드 삭제 없이 덮어쓰기):
#       유효한 값만 리스트에 저장 후 head부터 차례로 덮어쓰고 꼬리 절단.
#       포인터 조작이 불편한 언어에서 구현 단순.
#   - 하지만 현재 dummy 기반 1패스 방식이 가장 효율적이며, 공간 최소.
