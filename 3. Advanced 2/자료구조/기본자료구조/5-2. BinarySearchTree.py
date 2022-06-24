# 이진 탐색 트리

# 1. 정의
# 이진 트리다(노드의 연결로 구현)
# 임의의 어떤 노드에 대해 그 왼쪽 부분 트리의 모든 데이터 < 임의 노드 데이터 < 오른쪽 부분 트리의 모든 데이터

# 2. 활용
# 데이터를 빠르게 찾을 수 있다
# 이진 탐색 트리는 딕셔너리와 셋을 구현하는데 쓰임

# 3. 성질
# 이진 탐색 트리를 in-order 방법으로 순회하면 저장된 데이터들을 정렬된 순서대로 출력할 수 있다
# 이진 탐색 트리는 완전 이진 트리가 아닌 경우가 더 많다
# 그렇기 때문에 노드가 n개 있을 때, 높이 h가 항상 O(lg(n))이라고 할 수 없다
# 최악의 경우를 예로 들자면, 이진 탐색 트리의 높이는 O(n)
# 예를 들면 이진 탐색 트리에 데이터로 1, 2, 3, 4, 5, 6을 순서대로 삽입하면 트리가 한쪽으로 편향

# 1. 접근

# 2. 탐색
# 이분 탐색과 비슷하다(시간 h)

# 3. 삽입
# 새로운 노드를 만들고 > root부터 비교하면서 알맞은 위치 발견(시간 h) > 추가

# 6. 삭제
# 우선 노드를 찾아야 한다
# 말단 노드를 삭제하는 경우는 걍
# 중간에 자식이 하나인 노드를 지우는 경우 자식 노드를 부모 자리로 올려 보내면 그만임
# 중간에 자식이 2개인 노드를 지우는 경우
def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None


class BinarySearchTree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        new_node = Node(data)

        if self.root_node == None:
            self.root_node = new_node
            return

        temp_node = self.root_node
        while True:
            if temp_node.data > new_node.data:
                if temp_node.left_child is None:
                    temp_node.left_child = new_node
                    new_node.parent = temp_node
                    break
                temp_node = temp_node.left_child
            elif temp_node.data < new_node.data:
                if temp_node.right_child is None:
                    temp_node.right_child = new_node
                    new_node.parent = temp_node
                    break
                temp_node = temp_node.right_child

    def print_sorted_tree(self):
        print_inorder(self.root_node)

    def search(self, data):
        temp = self.root_node
        while True:
            if temp is None:
                return None

            if temp.data == data:
                return temp
            elif temp.data > data:
                temp = temp.left_child
            else:
                temp = temp.right_child

    @staticmethod
    def find_min(node):
        while node.left_child is not None:
            node = node.left_child
        return node

    def delete(self, data):
        node = self.search(data)

        # 1. 아예 노드가 없는 경우
        if node is None:
            return
        # 2. 말단 노드를 삭제
        if node.left_child is None and node.right_child is None:
            if node == self.root_node:
                self.root_node = None
                return
            if node.parent.left_child == node:
                node.parent.left_child = None
            elif node.parent.right_child == node:
                node.parent.right_child = None
        elif node.left_child is None:
            if node == self.root_node:
                self.root_node = node.right_child
                self.root_node.parent = None
                return
            if node.parent.left_child == node:
                node.parent.left_child = node.right_child
                node.right_child.parent = node.parent
            elif node.parent.right_child == node:
                node.parent.right_child = node.right_child
                node.right_child.parent = node.parent
        elif node.right_child is None:
            if node == self.root_node:
                self.root_node = node.left_child
                self.root_node.parent = None
                return
            if node.parent.left_child == node:
                node.parent.left_child = node.left_child
                node.left_child.parent = node.parent
            elif node.parent.right_child == node:
                node.parent.right_child = node.left_child
                node.left_child.parent = node.parent
        # 4. 자식이 2개인 노드를 삭제
        else:
            min_node = self.find_min(node.right_child)
            node.data = min_node.data
            if min_node.parent.left_child == min_node:
                min_node.parent.left_child = None
            elif min_node.parent.right_child == min_node:
                min_node.parent.right_child = None


if __name__ == "__main__":
    bst = BinarySearchTree()

    # 데이터 삽입
    bst.insert(7)
    bst.insert(11)
    bst.insert(9)
    bst.insert(17)
    bst.insert(8)
    bst.insert(5)
    bst.insert(19)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(14)

    # 정렬
    bst.print_sorted_tree()
    print()

    # 탐색
    # print(bst.search(7).data)
    # print(bst.search(19).data)
    # print(bst.search(2).data)
    # print(bst.search(20))

    # 삭제
    print()
    bst.delete(2)
    bst.delete(4)
    bst.delete(7)
    bst.delete(11)
    bst.delete(3)
    bst.delete(5)
    bst.delete(8)
    bst.print_sorted_tree()
    print()

#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.left_child = None
#         self.right_child = None
#
#
# def print_inorder(node):
#     if node is not None:
#         print_inorder(node.left_child)
#         print(node.data)
#         print_inorder(node.right_child)
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#
#     def print_sorted_tree(self):
#         print_inorder(self.root)  # root 노드를 in-order로 출력한다
#
#     def insert(self, data):
#         new_node = Node(data)
#
#         if self.root is None:
#             self.root = new_node
#             return
#
#         node = self.root
#         while True:
#             if node.data > new_node.data:
#                 if node.left_child is not None:
#                     node = node.left_child
#                 else:
#                     node.left_child = new_node
#                     new_node.parent = node
#                     return
#             elif node.data < new_node.data:
#                 if node.right_child is not None:
#                     node = node.right_child
#                 else:
#                     node.right_child = new_node
#                     new_node.parent = node
#                     return
#
#     def search(self, data):
#         temp = self.root  # 탐색용 변수, root 노드로 초기화
#         # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
#         while temp is not None:
#             # 원하는 데이터를 갖는 노드를 찾으면 리턴
#             if data == temp.data:
#                 return temp
#             # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
#             if data > temp.data:
#                 temp = temp.right_child
#             # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
#             else:
#                 temp = temp.left_child
#         return None  # 원하는 데이터가 트리에 없으면 None 리턴
#
#     @staticmethod
#     def find_min(node):
#         """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
#         pass
#
#     def delete(self, data):
#         """이진 탐색 트리 삭제 메소드"""
#         node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
#         parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드
#
#         # 경우 1: 지우려는 노드가 leaf 노드일 때
#         if node_to_delete.left_child is None and node_to_delete.right_child is None:
#             if self.root is node_to_delete:
#                 self.root = None
#             else:
#                 if node_to_delete is parent_node.left_child:
#                     parent_node.left_child = None
#                 else:
#                     parent_node.right_child = None
#
#         # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
#         elif node_to_delete.left_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때:
#             # 지우려는 노드가 root 노드일 때
#             if node_to_delete is self.root:
#                 self.root = node_to_delete.right_child
#                 self.root.parent = None
#             # 지우려는 노드가 부모의 왼쪽 자식일 때
#             elif node_to_delete is parent_node.left_child:
#                 parent_node.left_child = node_to_delete.right_child
#                 node_to_delete.right_child.parent = parent_node
#             # 지우려는 노드가 부모의 오른쪽 자식일 때
#             else:
#                 parent_node.right_child = node_to_delete.right_child
#                 node_to_delete.right_child.parent = parent_node
#
#
#         elif node_to_delete.right_child is None:  # 지우려는 노드가 왼쪽 자식만 있을 때:
#             # 지우려는 노드가 root 노드일 때
#             if node_to_delete is self.root:
#                 self.root = node_to_delete.left_child
#                 self.root.parent = None
#             # 지우려는 노드가 부모의 왼쪽 자식일 때
#             elif node_to_delete is parent_node.left_child:
#                 parent_node.left_child = node_to_delete.left_child
#                 node_to_delete.left_child.parent = parent_node
#             # 지우려는 노드가 부모의 오른쪽 자식일 때
#             else:
#                 parent_node.right_child = node_to_delete.left_child
#                 node_to_delete.left_child.parent = parent_node
#
#         # 경우 3: 지우려는 노드가 자식이 두개인 노드일 때:
#         # 지우려는 노드의 오른쪽 자식을 루트로 가지는 부분 트리를 생각한다
#         # 부분 트리에서 가장 작은 데이터를 가지는 노드를 찾는다 = successor = find_min
#         # 이 노드는 왼쪽 자식이 없고 오른쪽 자식만 있거나, 혹은 리프 노드이다
#         # 지우려는 노드의 데이터를 이 노드로 바꾸고 이 노드는 삭제한다
#
#
# if __name__ == "__main__":
#     # 빈 이진 탐색 트리 생성
#     bst = BinarySearchTree()
#
#     # 데이터 삽입
#     bst.insert(7)
#     bst.insert(11)
#     bst.insert(9)
#     bst.insert(17)
#     bst.insert(8)
#     bst.insert(5)
#     bst.insert(19)
#     bst.insert(3)
#     bst.insert(2)
#     bst.insert(4)
#     bst.insert(14)
#
#     # 이진 탐색 트리 출력
#     bst.print_sorted_tree()
#
#     # 노드 탐색과 출력
#     print(bst.search(7).data)
#     print(bst.search(19).data)
#     print(bst.search(2).data)
#     print(bst.search(20))
#
#     # leaf 노드 삭제
#     bst.delete(2)
#     bst.delete(4)
#     print("?")
#     bst.print_sorted_tree()
#
#     # 자식이 두 개 다 있는 노드 삭제
#     bst.delete(7)
#     bst.delete(11)
#
#     bst.print_sorted_tree()