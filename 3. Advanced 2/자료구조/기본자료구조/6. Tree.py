# 트리

# 용어
# 루트 노드 / 형제 노드 / 리프 노드 / 자식 노드 / 부모 노드 / 깊이 / 레벨 / 높이 / 부분 트리

# 종류
# binary tree: 각 노드가 최대 2개의 자식 노드를 가질 수 있다
# complete binary tree: 마지막 바로 직전 레벨까지 모든 노드가 다 채워지고 마지막 레벨은 왼쪽부터 차례대로 노드가 다 차있다
# complete binary tree: 노드가 n개이면 높이 h는 O(로그n)

# 활용
# 1. 계층 관계를 가진 데이터를 저장할 때
# 2. 정렬(힙 정렬) 압축(후프만 코드)을 매우 똑똑하게 처리하고 싶을 때
# 3. 우선순위 큐(힙으로), 딕셔너리(BST), 셋(BST)와 같은 추상 자료형을 구현할 때

# 우리는 다양한 트리 중에서 이진 트리의 구현에 집중해 본다

# 이진 트리의 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# 이진 트리의 순회
def preorder(node):
    pass


def inorder(node):
    if node.left_child is not None:
        inorder(node.left_child)
    print(node.data)
    if node.right_child is not None:
        inorder(node.right_child)


def postorder(node):
    pass


def preorder_list(cbt, node_index):
    pass


def inorder_list(cbt, node_index):
    left_child_index = get_left_child_index(cbt, node_index)
    if left_child_index is not None:
        inorder_list(cbt, left_child_index)
    print(cbt[node_index])
    right_child_index = get_right_child_index(cbt, node_index)
    if right_child_index is not None:
        inorder_list(cbt, right_child_index)


def postorder_list(cbt, node_index):
    pass


# 왼쪽 자식 노드 인덱스 구하기
def get_left_child_index(cbt, index):
    left_child_index = index * 2
    if left_child_index < 1 or left_child_index > len(cbt) - 1:
        return None
    else:
        return left_child_index


# 오른쪽 자식 노드 인덱스 구하기
def get_right_child_index(cbt, index):
    right_child_index = index * 2 + 1
    if right_child_index < 1 or right_child_index > len(cbt) - 1:
        return None
    else:
        return right_child_index


# 부모 노드 인덱스 구하기
def get_parent_child_index(cbt, index):
    parent_index = index // 2
    if parent_index < 1 or parent_index > len(cbt) - 1:
        return None
    else:
        return parent_index


if __name__ == "__main__":
    # 1. 노드로 구현한 이진 트리
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node6 = Node("6")
    node7 = Node("7")
    node8 = Node("8")
    node9 = Node("9")

    node1.left_child = node2
    node1.right_child = node3
    node2.left_child = node4
    node2.right_child = node5
    node3.left_child = node6
    node3.right_child = node9
    node4.left_child = node7
    node4.right_child = node8

    # 노드를 활용한 이진 트리의 순회
    # 프리오더: 루트 출력 => 왼쪽 재귀 호출 => 오른쪽 재귀 호출
    # 인오더: 왼쪽 재귀 호출 => 루트 출력 => 오른쪽 재귀 호출
    # 포스트오더: 왼쪽 재귀 호출 => 오른쪽 재귀호출 => 루트 출력
    preorder(node1)
    inorder(node1)
    postorder(node1)

    # 특별히, 완전 이진 트리(CBT)는 리스트로 구현할 수 있다

    # 2. 리스트로 구현한 이진 트리
    cbt = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]

    # 리스트로 구현한 이진 트리의 순회
    # 프리오더: 루트 출력 => 왼쪽 재귀 호출 => 오른쪽 재귀 호출
    # 인오더: 왼쪽 재귀 호출 => 루트 출력 => 오른쪽 재귀 호출
    # 포스트오더: 왼쪽 재귀 호출 => 오른쪽 재귀호출 => 루트 출력
    preorder_list(cbt, 1)
    inorder_list(cbt, 1)
    postorder_list(cbt, 1)