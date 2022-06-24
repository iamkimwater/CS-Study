class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        res_str = "["

        iterator = self.head

        while iterator is not None:
            res_str += f" {iterator.data} "
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str + "]"

    def append(self, data):
        new_node = DoublyNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_node_with_data(self, data):
        if self.head.data == data:
            return self.head
        if self.tail.data == data:
            return self.tail

        iterator = self.head.next
        while iterator != self.tail:
            if iterator.data == data:
                break
            iterator = iterator.next

        return None if iterator is self.tail else iterator

    def insert_after(self, previous_node, data):
        if previous_node == self.tail:
            self.append(data)
        else:
            new_node = DoublyNode(data)

            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node
            new_node.prev = previous_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def delete(self, node_to_delete):
        data = node_to_delete.data

        if self.head == self.tail == node_to_delete:
            self.head = None
            self.tail = None
        elif self.head == node_to_delete:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return data


if __name__ == "__main__":
    # 메모리에 흩어져 있는 노드 객체들에게 데이터와 넥스트를 세팅해서 마치 순서가 있는 것 처럼 다룰 수 있는 자료구조
    my_list = DoublyLinkedList()
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    my_list.append(7)
    my_list.append(11)
    print(my_list)

    # tail 노드 뒤에 노드 삽입
    tail_node = my_list.tail
    my_list.insert_after(tail_node, 5)
    print(my_list)

    # 링크드 리스트 중간에 데이터 삽입
    node_at_index_3 = my_list.find_node_at(3)
    my_list.insert_after(node_at_index_3, 3)
    print(my_list)

    my_list.prepend(11)
    my_list.prepend(7)
    my_list.prepend(5)
    my_list.prepend(3)
    my_list.prepend(2)
    print(my_list)
    print()

    # 두 노드 사이에 있는 노드 삭제
    node_at_index_2 = my_list.find_node_at(2)
    my_list.delete(node_at_index_2)
    print(my_list)

    # 가장 앞 노드 삭제
    head_node = my_list.head
    print(my_list.delete(head_node))
    print(my_list)

    # 가장 뒤 노드 삭제
    tail_node = my_list.tail
    my_list.delete(tail_node)
    print(my_list)

    # 마지막 노드 삭제
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    my_list.delete(my_list.head)
    print(my_list)