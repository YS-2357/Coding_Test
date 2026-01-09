# 0865_Smallest Subtree with all the Deepest Nodes.py
# -----------------------------------------------------
# ✅ 제목: LeetCode 865. Smallest Subtree with all the Deepest Nodes
# 🏷️ 유형: 트리 / BFS / 부모 포인터 / LCA 아이디어
#
# ✅ 문제 설명(요약):
#   - 이진 트리에서 가장 깊은 노드들(최대 깊이의 모든 노드)을 모두 포함하는
#   - 가장 작은 서브트리의 루트 노드를 반환한다.
#
# ✅ 입력 형식(요지):
#   - root: 이진 트리의 루트 노드
#
# ✅ 규칙 요약:
#   - “가장 깊은 노드들”은 깊이가 최대인 모든 노드를 의미한다.
#   - 그 노드들을 모두 포함하는 최소 서브트리는 사실상 그 노드들의 LCA(최소 공통 조상)이다.
#
# 🧠 핵심 불변식(Invariant):
#   - BFS를 끝까지 수행하면 마지막으로 처리된 레벨의 노드 리스트(last_lvl)가 “가장 깊은 노드들”이 된다.
#   - deepest 집합을 부모로 한 단계씩 올리면, 결국 한 노드로 수렴하며 그 노드가 LCA가 된다.
#
# ✅ 정답 코드(나의 풀이; 절대 수정 금지)

class Solution:                                                                  # LeetCode 제출 형식에 맞춘 Solution 클래스 정의
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  # 가장 깊은 노드들을 모두 포함하는 최소 서브트리 루트를 반환하는 함수
        if not root:                                                               # 입력 트리가 비어있는 경우
            return None                                                            # 서브트리가 없으므로 None 반환
        
        parent = {root: None}                                                      # 각 노드의 부모를 기록하는 딕셔너리 초기화 (루트의 부모는 None)
        q = deque([root])                                                          # 레벨 순회를 위한 BFS 큐를 루트로 초기화

        while q:                                                                   # 큐가 빌 때까지 레벨 단위로 BFS 수행
            size = len(q)                                                          # 현재 레벨에 있는 노드 개수를 저장
            last_lvl = []                                                          # 현재 레벨의 노드들을 저장할 리스트 초기화
            for _ in range(size):                                                  # 현재 레벨의 모든 노드를 처리
                node = q.popleft()                                                 # 큐에서 노드를 하나 꺼냄
                last_lvl.append(node)                                              # 현재 레벨 노드 목록에 추가

                if node.left:                                                      # 왼쪽 자식이 존재하면
                    parent[node.left] = node                                       # 왼쪽 자식의 부모를 현재 노드로 기록
                    q.append(node.left)                                            # 다음 레벨 탐색을 위해 큐에 추가
                if node.right:                                                     # 오른쪽 자식이 존재하면
                    parent[node.right] = node                                      # 오른쪽 자식의 부모를 현재 노드로 기록
                    q.append(node.right)                                           # 다음 레벨 탐색을 위해 큐에 추가

        deepest = set(last_lvl)                                                    # BFS의 마지막 레벨 노드들을 집합으로 만들어 “가장 깊은 노드들”로 설정

        while len(deepest) > 1:                                                    # 가장 깊은 노드 후보가 2개 이상이면
            deepest = {parent[node] for node in deepest}                           # 모든 후보를 부모로 한 단계 올려서 공통 조상으로 수렴시킴

        return deepest.pop()                                                       # 최종적으로 남은 한 노드(최소 서브트리 루트)를 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
#   - 첫 제출에서 정답 처리됨 (Accepted).
#
# 🔧 오답 이유 및 사용한 알고리즘 개념:
#   - 오답 없음.
#   - 사용 개념: BFS로 최심부 레벨 탐색 + 부모 포인터로 후보들을 위로 끌어올려 LCA를 찾는 방식.
#
# 📚 시간·공간 복잡도:
#   - 시간: O(n)  (BFS O(n) + 부모로 끌어올리기 O(n) 이내)
#   - 공간: O(n)  (parent 딕셔너리 및 큐/집합 저장)
#
# -----------------------------------------------------
# (선택) 다른 효율적 풀이 또는 알고리즘 제안:
#   - DFS로 (서브트리 깊이, 후보 노드)를 반환하는 방식으로 한 번의 순회에서 해결하는 풀이도 가능하다 (개념만).
