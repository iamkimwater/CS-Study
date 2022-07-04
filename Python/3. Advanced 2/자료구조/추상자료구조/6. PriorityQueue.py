# 우선순위 큐
# 힙으로 만든 추상 자료형이다
# 우선순위가 높은 순서대로 데이터가 나온다

# 정렬된 동적 배열 또는 링크드리스트로 만든 우선순위 큐의 삽입 연산: O(n)
# 정렬된 동적 배열 또는 링크드리스트로 만든 우선순위 큐의 팝 연산: O(1)

# 힙으로 만든 우선순위 큐의 삽입 연산: O(log n)
# 힙으로 만든 우선순위 큐의 팝(삭제) 연산: O(log n)

# 평균적으로 힙으로 구현한 우선순위 큐가 빠르다


def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:
        tree[index], tree[largest] = tree[largest], tree[index]
        heapify(tree, largest, tree_size)


# 부모 노드 인덱스 구하기
def get_parent_child_index(cbt, index):
    parent_index = index // 2
    if parent_index < 1 or parent_index > len(cbt) - 1:
        return None
    else:
        return parent_index


def reverse_heapify(tree, index):
    if index == 1:
        return

    parent_index = get_parent_child_index(tree, index)
    if parent_index is None:
        return

    if tree[index] < tree[parent_index]:
        return

    tree[index], tree[parent_index] = tree[parent_index], tree[index]
    reverse_heapify(tree, parent_index)


class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def __str__(self):
        return str(self.heap)

    # 힙에 데이터 삽입하기
    # 1. 힙의 마지막 인덱스에 데이터 삽입
    # 2. 삽입한 데이터와 부모를 비교해서 위치를 조정한다
    # 3. 올바르게 될 떄까지 2를 재귀적으로 반복
    def insert(self, data):
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap) - 1)

    # root 노드와 마지막 노드의 위치를 바꿉니다
    # 마지막 위치로 간 원래 root 노드의 데이터를 별도 변수에 저장하고, 노드는 힙에서 지웁니다
    # 새로운 root 노드를 대상으로 heapify해서 망가진 힙 속성을 복원합니다
    # 2단계에서 따로 저장해 둔 최우선순위 데이터를 리턴합니다
    def extract_max(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        max_value = self.heap[-1]
        self.heap.remove(max_value)
        heapify(self.heap, 1, len(self.heap))

        return max_value


if __name__ == "__main__":
    priority_queue = PriorityQueue()

    priority_queue.insert(6)
    priority_queue.insert(9)
    priority_queue.insert(1)
    priority_queue.insert(3)
    priority_queue.insert(10)
    priority_queue.insert(11)
    priority_queue.insert(13)

    print(priority_queue)

    print(priority_queue.extract_max())
    print(priority_queue.extract_max())
    print(priority_queue.extract_max())
    print(priority_queue.extract_max())
    print(priority_queue.extract_max())
    print(priority_queue.extract_max())
    print(priority_queue.extract_max())

    print(priority_queue)