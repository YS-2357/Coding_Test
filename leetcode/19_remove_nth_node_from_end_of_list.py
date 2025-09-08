# 19_remove_nth_node_from_end_of_list.py
# -----------------------------------------------------
# ✅ 제목: Remove Nth Node From End of List
# ✅ 문제 설명(요약):
# - 단일 연결 리스트 head가 주어진다.
# - 끝에서 n번째 노드를 삭제한 뒤 리스트의 head를 반환한다.
#
# ✅ 입력 형식(요지):
# - head: ListNode (단일 연결 리스트의 시작 노드)
# - n: int (1 ≤ n ≤ 리스트 길이)
#
# ✅ 규칙 요약:
# 1) 끝에서 n번째 노드를 삭제.
# 2) head 자체가 삭제될 수도 있음 → dummy 노드를 앞에 추가해 안전하게 처리.
# 3) 투포인터 사용:
#    - fast를 n칸 먼저 이동.
#    - slow와 fast를 같이 이동.
#    - fast가 끝에 도착하면 slow는 삭제할 노드의 직전 위치에 있음.
# 4) slow.next = slow.next.next로 삭제 수행.
#
# ✅ 입출력 예시(1개):
# - head = [1,2,3,4,5], n=2
#   → 삭제: 값 4 노드 → 결과 [1,2,3,5]
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)              # head 앞에 dummy 추가
        slow = dummy                           # slow는 dummy에서 시작
        fast = head                            # fast는 head에서 시작

        for _ in range(n):                     # fast를 n칸 먼저 전진
            fast = fast.next

        while fast:                            # fast가 끝에 도달할 때까지
            slow = slow.next                   # slow와 fast를 동시에 전진
            fast = fast.next

        slow.next = slow.next.next             # slow 다음 노드 삭제
        return dummy.next                      # head가 삭제될 수도 있으므로 dummy.next 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 다양한 입력(head 삭제 포함)에서도 정상 작동.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (초안) slow를 dummy와 연결하지 않고 ListNode(0, head)로만 둠 → 리스트와 연결되지 않아 삭제 위치 계산 실패.
# - (수정) dummy 노드 생성 후 slow=dummy로 설정, 마지막 반환도 dummy.next로 교체.
#
# 📚 사용된/필수 개념(최소):
# - 투 포인터(two pointers): fast-slow 기법
# - dummy 노드: head 삭제 케이스 안전 처리
# - 시간복잡도 O(L), 공간복잡도 O(1)
