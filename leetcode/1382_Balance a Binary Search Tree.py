# 1382_Balance a Binary Search Tree.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1382. Balance a Binary Search Tree
# 🏷️ 유형: BST / 중위순회 / 분할정복(균형 트리 재구성)
#
# ✅ 문제 설명(요약):
#   - 이진 탐색 트리(BST)가 주어질 때, 이를 높이 균형 BST로 변환해 반환한다.
#   - BST의 중위순회 결과는 정렬된 값 리스트가 되므로, 이를 이용해 균형 트리를 재구성한다.
#
# ✅ 입력 형식(요지):
#   - root: Optional[TreeNode]
#
# ✅ 규칙 요약:
#   - 중위순회로 모든 값을 오름차순으로 수집한다.
#   - 정렬된 리스트에서 중앙값을 루트로 선택하고, 좌/우 구간을 재귀적으로 같은 방식으로 구성한다.
#   - 결과 트리는 BST 성질을 유지하면서 높이가 균형에 가깝게 된다.
#
# 🧠 핵심 불변식(Invariant):
#   - inorder(node)는 BST의 값을 오름차순으로 vals에 누적한다.
#   - build(vals, l, r)는 vals[l..r] 구간의 중앙값을 루트로 사용해 균형 BST를 만든다.
#   - 중앙값을 택하면 좌/우 서브트리 크기 차이가 최대 1로 유지되어 높이 균형에 가까운 구조가 된다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def inorder(self, node, vals):                                  # BST를 중위순회하며 값을 리스트에 담는 함수
        if not node:                                                # 현재 노드가 None이면
            return                                                  # 더 진행할 것이 없으므로 종료
        self.inorder(node.left, vals)                               # 왼쪽 서브트리를 먼저 중위순회
        vals.append(node.val)                                       # 현재 노드 값을 리스트에 추가
        self.inorder(node.right, vals)                              # 오른쪽 서브트리를 중위순회

    def build(self, vals, l, r):                                    # 정렬된 vals[l..r]로 균형 BST를 만드는 함수
        if l > r:                                                   # 구간이 비어있으면
            return None                                             # 빈 트리를 반환
        mid  = (l + r) // 2                                         # 중앙 인덱스를 선택
        node = TreeNode(vals[mid])                                  # 중앙값으로 새 노드를 생성
        node.left  = self.build(vals, l, mid - 1)                   # 왼쪽 구간으로 왼쪽 서브트리를 재귀 구성
        node.right = self.build(vals, mid + 1, r)                   # 오른쪽 구간으로 오른쪽 서브트리를 재귀 구성
        return node                                                 # 구성된 서브트리의 루트를 반환

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # BST를 균형 BST로 변환해 반환하는 함수
        vals = []                                                   # BST 값을 담을 리스트를 초기화
        self.inorder(root, vals)                                    # 중위순회로 값을 오름차순으로 수집
        return self.build(vals, 0, len(vals) - 1)                   # 수집한 정렬 리스트로 균형 BST를 재구성해 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: BST 중위순회(정렬 리스트 생성) + 분할정복으로 균형 트리 재구성.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n)  (중위순회 O(n) + 재구성 O(n))
#   - 공간: O(n)  (값 리스트 vals + 재귀 호출 스택 O(h))
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 값 리스트 대신 “중위순회로 얻은 노드 포인터들”을 재사용해 새 노드 생성 없이 재연결하는 방식도 가능하다(개념만).
