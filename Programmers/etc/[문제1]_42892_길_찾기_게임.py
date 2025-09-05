# 42892_길_찾기_게임.py
# -----------------------------------------------------
# ✅ 제목: 길 찾기 게임
# ✅ 문제 설명(요약):
# - 각 노드는 (x, y) 좌표와 1..N의 번호를 가진다(번호는 nodeinfo의 인덱스+1).
# - 규칙:
#   * 같은 레벨(y)이면 같은 y값, 자식 y < 부모 y
#   * 왼쪽 서브트리의 모든 x < 부모 x, 오른쪽 서브트리의 모든 x > 부모 x
# - 좌표로 트리를 구성한 뒤, 전위/후위 순회 결과를 반환한다.
#
# ✅ 입력 형식(요지):
# - nodeinfo: List[List[int]] 길이 N(1 ≤ N ≤ 10,000), 각 원소는 [x, y]
#
# ✅ 규칙 요약:
# 1) y 내림차순, x 오름차순으로 정렬 후, 그 순서로 BST(키=x)에 삽입하면 트리 규칙이 보장됨.
# 2) 전위(preorder): 루트 → 왼 → 오
# 3) 후위(postorder): 왼 → 오 → 루트
#
# ✅ 정답 코드(너의 풀이; 한 줄마다 주석):
import sys                                      # 재귀 한도를 넉넉히 설정하기 위함
sys.setrecursionlimit(100000)                   # 트리 깊이가 최대 1000 → 여유 있게 확장

def solution(nodeinfo):
    # 1) 노드에 번호 붙이기: (x, y, idx) 형태로 보관
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]  # enumerate로 1-based 번호 부여

    # 2) 부모가 먼저 오도록 정렬: y 내림차순, x 오름차순
    nodes.sort(key=lambda t: (-t[1], t[0]))     # 위 레벨부터, 같은 레벨에서는 x 증가 순

    # 3) 트리 구조 저장: 각 번호에 대해 좌/우 자식 번호를 기록(없으면 0/None)
    left = dict()                               # left[번호] = 왼자식 번호
    right = dict()                              # right[번호] = 오른자식 번호
    xpos = {idx: x for (x, _, idx) in nodes}    # 비교용으로 각 번호의 x 좌표 저장

    root = nodes[0][2]                          # 정렬 후 첫 노드가 루트(가장 높은 y, 가장 왼쪽 x)
    left[root] = 0; right[root] = 0             # 루트의 자식 초기화

    # 4) BST 삽입 함수 (키 = x). 현재 노드 cur, 삽입할 노드 new_idx
    def insert(cur, new_idx):
        if xpos[new_idx] < xpos[cur]:           # 새 노드 x가 현재 x보다 작으면 왼쪽으로
            if left.get(cur, 0) == 0:           # 왼자식이 비어 있으면
                left[cur] = new_idx             # 왼자식으로 연결
                left[new_idx] = 0               # 새 노드의 자식 포인터 초기화
                right[new_idx] = 0
            else:
                insert(left[cur], new_idx)      # 비어 있지 않으면 더 내려감
        else:                                   # 새 노드 x가 현재 x보다 크면 오른쪽으로
            if right.get(cur, 0) == 0:          # 오른자식이 비어 있으면
                right[cur] = new_idx            # 오른자식으로 연결
                left[new_idx] = 0               # 새 노드의 자식 포인터 초기화
                right[new_idx] = 0
            else:
                insert(right[cur], new_idx)     # 비어 있지 않으면 더 내려감

    # 5) 나머지 노드들을 순서대로 루트에 삽입
    for i in range(1, len(nodes)):              # 첫 노드는 루트로 이미 사용
        _, _, idx = nodes[i]
        insert(root, idx)                       # BST 규칙에 따라 삽입

    # 6) 전위/후위 순회 구현
    preorder_list = []                          # 전위 결과 저장
    postorder_list = []                         # 후위 결과 저장

    def preorder(cur):                          # 전위: 루트 → 왼 → 오
        if cur == 0:                            # 0은 없는 자식을 의미
            return
        preorder_list.append(cur)               # 루트 방문
        preorder(left.get(cur, 0))              # 왼쪽 방문
        preorder(right.get(cur, 0))             # 오른쪽 방문

    def postorder(cur):                         # 후위: 왼 → 오 → 루트
        if cur == 0:
            return
        postorder(left.get(cur, 0))             # 왼쪽 방문
        postorder(right.get(cur, 0))            # 오른쪽 방문
        postorder_list.append(cur)              # 루트 방문

    # 7) 순회 실행 후 반환 형식에 맞게 구성
    preorder(root)                              # 전위 순회 시작
    postorder(root)                             # 후위 순회 시작
    return [preorder_list, postorder_list]      # 2차원 배열로 반환

# -----------------------------------------------------
# 🔍 첫 시도 결과:
# - 예시 입력에서 전위: [7,4,6,9,1,8,5,2,3], 후위: [9,6,5,8,1,4,3,2,7]와 일치.
# - N=10,000에서도 정렬 O(N log N) + 삽입 O(N·평균 높이)로 충분히 통과.
#
# 🔧 오답 및 실수(무엇을 틀렸고 어떻게 고쳤는지):
# - (가능 실수) y를 비교하며 삽입 분기 → 불필요/오답. 분기는 오직 x로만 해야 함.
# - (가능 실수) 루트 선택을 x 기준으로 하면 안 됨 → 반드시 y 내림차순, x 오름차순 첫 원소가 루트.
# - (가능 실수) 자식 포인터 초기화 누락 → 순회 중 KeyError 가능 → 삽입 시 0으로 초기화.
# - (가능 실수) 재귀 한도 부족 → 깊은 트리에서 RecursionError → 재귀 한도 상향 조정.
#
# 📚 사용된/필수 개념(최소):
# - 레벨(y) 우선 정렬로 부모→자식 삽입 순서 보장
# - BST 삽입(키=x)으로 왼/오 서브트리 규칙 충족
# - 전위/후위 순회
# - 시간복잡도: 정렬 O(N log N) + 삽입 평균 O(N log N) (최악 O(N^2) 가능하지만 입력 제약상 통과)
# - 공간복잡도: O(N) (트리 포인터 + 순회 결과)
#
# 🧠 (선택) 다른 효율적인 풀이 또는 알고리즘 제안:
# - 스택 기반 “세그먼트 트리/카탈란 구조” 아이디어로 y가 높은 순서로 x-구간을 관리하며 부모를 찾는 방식도 가능.
# - 혹은 재귀 대신 반복(스택) 순회로 파이썬 재귀 한도 의존을 줄일 수 있음.
