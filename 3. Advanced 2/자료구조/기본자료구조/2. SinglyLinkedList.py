class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return "[ ]"

        result = "["
        iterator = self.head
        while iterator.next_node is not None:
            iterator = iterator.next_node
            result += f" {iterator.data} "
        result += "]"

        return result

    def add(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node



    # def __str__(self):
    #     res_str = "["
    #
    #     iterator = self.head
    #
    #     while iterator is not None:
    #         res_str += f" {iterator.data} "
    #         iterator = iterator.next  # 다음 노드로 넘어간다
    #
    #     return res_str + "]"
    #
    # def append(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #
    # # 접근
    # def find_node_at(self, index):
    #     iterator = self.head
    #     for _ in range(index):
    #         iterator = iterator.next
    #     return iterator
    #
    # # 탐색
    # def find_node_with_data(self, data):
    #     if self.head.data == data:
    #         return self.head
    #     if self.tail.data == data:
    #         return self.tail
    #
    #     iterator = self.head.next
    #     while iterator != self.tail:
    #         if iterator.data == data:
    #             break
    #         iterator = iterator.next
    #
    #     return None if iterator is self.tail else iterator
    #
    # def insert_after(self, previous_node, data):
    #     if previous_node == self.tail:
    #         self.append(data)
    #     else:
    #         new_node = Node(data)
    #         new_node.next = previous_node.next
    #         previous_node.next = new_node
    #
    # def prepend(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.next = self.head
    #         self.head = new_node
    #
    # def delete_after(self, previous_node):
    #     data = previous_node.next.data
    #
    #     if previous_node.next == self.tail:
    #         previous_node.next = None
    #         self.tail = previous_node
    #     else:
    #         previous_node.next = previous_node.next.next
    #
    #     return data
    #
    # def pop_left(self):
    #     if self.head == None:
    #         return None
    #     elif self.head == self.tail:
    #         temp = self.head
    #         self.head = self.tail = None
    #         return temp
    #     else:
    #         temp = self.head
    #         self.head = self.head.next
    #         return temp


if __name__ == "__main__":    # 메모리에 흩어져 있는 노드 객체들에게 데이터와 넥스트를 세팅해서 마치 순서가 있는 것 처럼 다룰 수 있는 자료구조
    singlyLinkedList = SinglyLinkedList()
    print(singlyLinkedList)
    singlyLinkedList.add(1)
    print(singlyLinkedList)
    # singlyLinkedList.add(2)
    # print(singlyLinkedList)
    # singlyLinkedList.append(2)
    # singlyLinkedList.append(3)
    # singlyLinkedList.append(5)
    # singlyLinkedList.append(7)
    # singlyLinkedList.append(11)
    # print(singlyLinkedList)
    #
    # # 접근: 시간 복잡도가 O(n) / 배열에 비해서 느리다
    # print(singlyLinkedList.find_node_at(3).data)
    # singlyLinkedList.find_node_at(3).data = 100
    # print(singlyLinkedList)
    #
    # # 탐색: o(n)
    # print(singlyLinkedList.find_node_with_data(11).data)
    # singlyLinkedList.insert_after(singlyLinkedList.find_node_at(3), 999)
    # print(singlyLinkedList)
    #
    # # 삽입 삭제: o(1)이지만 삽입 또는 삭제 하기 전 이전 노드를 찾아야 하므로 o(n)
    # singlyLinkedList.prepend(0)
    # print(singlyLinkedList)
    #
    # print(singlyLinkedList.delete_after(singlyLinkedList.find_node_at(2)))
    # print(singlyLinkedList)
    #
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList.pop_left().data)
    # print(singlyLinkedList)