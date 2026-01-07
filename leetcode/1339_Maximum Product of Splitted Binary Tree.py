# 1339_Maximum Product of Splitted Binary Tree.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 1339. Maximum Product of Splitted Binary Tree
# 🏷️ 유형: 트리 / DFS / 서브트리 합
#
# ✅ 문제 설명(요약):
#   - 이진 트리에서 간선 하나를 끊어 트리를 두 개의 서브트리로 분리한다.
#   - 두 서브트리의 노드 값 합을 각각 S1, S2라 할 때, S1 * S2의 최댓값을 구한다.
#   - 결과는 10^9 + 7로 나눈 나머지를 반환한다.
#
# ✅ 입력 형식(요지):
#   - root: 이진 트리의 루트 노드
#
# ✅ 규칙 요약:
#   - 반드시 간선 하나를 제거하여 정확히 두 트리로 분리한다.
#   - 각 트리의 합은 해당 트리에 포함된 노드들의 val 합이다.
#   - 최댓값을 구한 뒤 MOD로 나눈 값을 반환한다.
#
# 🧠 핵심 불변식(Invariant):
#   - 어떤 노드의 서브트리 합 sub를 알면, 분리 시 다른 쪽 합은 total - sub로 고정된다.
#   - 모든 노드의 sub에 대해 sub * (total - sub)를 비교하면 전역 최댓값을 얻는다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                              # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def maxProduct(self, root: Optional[TreeNode]) -> int:    # 간선 하나를 끊어 얻는 곱의 최댓값을 반환하는 함수
        MOD = 10**9 + 7                                       # 문제에서 요구하는 모듈러 상수 설정

        def tree_sum(node):                                   # 트리 전체 합을 구하는 DFS 함수 정의
            if not node:                                      # 현재 노드가 None이면 합은 0
                return 0                                      # 빈 서브트리의 합 반환
            return node.val + tree_sum(node.left) + tree_sum(node.right)  # 현재 노드 + 좌/우 서브트리 합 반환
        
        total = tree_sum(root)                                # 트리의 전체 노드 합을 미리 계산
        ans = 0                                               # 최대 곱을 저장할 변수 초기화

        def subtree_sum(node):                                # 각 노드의 서브트리 합을 계산하며 최대 곱을 갱신하는 DFS 함수
            nonlocal ans                                      # 바깥 스코프의 ans를 갱신하기 위해 nonlocal 선언

            if not node:                                      # 현재 노드가 None이면 서브트리 합은 0
                return 0                                      # 빈 서브트리의 합 반환

            left_sum = subtree_sum(node.left)                 # 왼쪽 서브트리 합을 재귀적으로 계산
            right_sum = subtree_sum(node.right)               # 오른쪽 서브트리 합을 재귀적으로 계산

            sub = node.val + left_sum + right_sum             # 현재 노드를 루트로 하는 서브트리의 총합 계산

            ans = max(ans, sub * (total - sub))               # 이 서브트리로 분리했을 때의 곱으로 최대값 갱신
            
            return sub                                        # 현재 서브트리 합을 상위 호출로 반환

        subtree_sum(root)                                     # 루트부터 서브트리 합 계산 DFS를 실행하여 ans를 채움

        return ans % MOD                                      # 최대 곱을 MOD로 나눈 값을 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: 트리 전체 합 계산 DFS + 서브트리 합 DFS를 통한 전역 최댓값 갱신.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n)  (각 DFS가 모든 노드를 한 번씩 방문하므로 총 O(n))
#   - 공간: O(h)  (재귀 호출 스택, h는 트리 높이; 최악 O(n))
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - 한 번의 DFS에서 서브트리 합을 리스트로 수집한 뒤, total을 이용해 후처리로 최댓값을 계산하는 방식도 가능하다.
