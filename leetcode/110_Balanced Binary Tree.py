# 110_Balanced Binary Tree.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 110. Balanced Binary Tree
# 🏷️ 유형: 이진 트리 / DFS / 높이 계산
#
# ✅ 문제 설명(요약):
#   - 이진 트리가 주어졌을 때, 높이 균형 트리인지 판별한다.
#   - 모든 노드에 대해 왼쪽·오른쪽 서브트리의 높이 차이가 1 이하이면 균형 트리이다.
#
# ✅ 입력 형식(요지):
#   - root: Optional[TreeNode]
#
# ✅ 규칙 요약:
#   - 빈 트리는 균형 트리로 간주한다.
#   - 어느 한 노드라도 높이 차이가 2 이상이면 전체 트리는 균형이 아니다.
#
# 🧠 핵심 불변식(Invariant):
#   - dfs(node)는 해당 서브트리의 높이를 반환한다.
#   - 단, 불균형이 발견되면 높이 대신 -1을 반환하여 상위로 즉시 전파한다.
#   - 한 번 -1이 반환되면, 이후 계산은 의미 없으므로 그대로 -1을 유지한다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                                                     # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def isBalanced(self, root: Optional[TreeNode]) -> bool:         # 트리가 균형인지 여부를 반환하는 함수
        def dfs(node):                                              # 서브트리 높이를 계산하는 DFS 함수 정의
            if not node:                                            # 현재 노드가 None이면
                return 0                                            # 높이 0 반환 (빈 트리)
            
            left = dfs(node.left)                                  # 왼쪽 서브트리 높이를 재귀적으로 계산
            if left == -1:                                          # 왼쪽 서브트리가 이미 불균형이면
                return -1                                          # 즉시 -1 반환하여 상위로 전파
            
            right = dfs(node.right)                                # 오른쪽 서브트리 높이를 재귀적으로 계산
            if right == -1:                                         # 오른쪽 서브트리가 이미 불균형이면
                return -1                                          # 즉시 -1 반환하여 상위로 전파
            
            if abs(left - right) > 1:                               # 현재 노드에서 높이 차이가 1을 초과하면
                return -1                                          # 불균형 상태이므로 -1 반환
            
            return 1 + max(left, right)                            # 현재 노드의 높이를 반환
            
        return dfs(root) != -1                                     # 최종적으로 -1이 아니면 균형 트리

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: DFS 기반 높이 계산 + 불균형 조기 종료.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n)  (모든 노드를 한 번씩 방문)
#   - 공간: O(h)  (재귀 호출 스택, h는 트리 높이)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - BFS로 각 노드의 높이를 저장하는 방식도 가능하지만,
#     DFS에서 불균형을 조기에 감지하는 현재 방식이 더 효율적이다(개념만).
