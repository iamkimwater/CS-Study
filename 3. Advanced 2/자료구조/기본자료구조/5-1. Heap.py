# 힙(최대 힙)
# 1. 완전 이진 트리(CBT)
# 2. 부모 노드의 데이터는 자식 노드 데이터보다 크거나 같음
#
# 최소 힙
# 1. 완전 이진 트리(CBT)
# 2. 부모 노드의 데이터는 자식 노드 데이터보다 작거나 같음
#
# 활용
# 힙 정렬 / 우선순위 큐 구현
#
# 1. 힙을 만든다
# 완전 이진 트리의 마지막 원소부터 거꾸로 heapify 연산을 수행한다
#
# heapify 연산이란?
# 특정 노드가 힙 조건을 만족하도록 원래 위치를 찾아주는 함수
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


# 2. 힙 정렬을 사용한다
# 만든 힙으로 힙 정렬을 한다
# 1. 루트 노드와 마지막 노드를 교체
# 2. 교체되서 제일 마지막에 존재하는 노드는 이제 무시
# 3. 무시한 노드를 제외하고 나머지 트리에서 루트 노드를 heapify
# 4. 1 ~ 3을 반복
# 시간 복잡도 = O(n로그n)
def heapsort(tree):
    count = 1
    tree_size = len(tree)
    while count < tree_size:
        tree[1], tree[-count] = tree[-count], tree[1]
        heapify(tree, 1, tree_size - count)
        count += 1


if __name__ == "__main__":
    # 완전 이진 트리
    tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]

    # 1. 힙으로 만들기(시간 복잡도 = O(n로그n))
    for i in reversed(range(1, len(tree))):
        heapify(tree, i, len(tree))
    print(tree)

    # 2. 만든 힙으로 힙 정렬을 수행(시간 복잡도 = O(n로그n))
    heapsort(tree)
    print(tree)

    # 힙 정렬을 하기 위해서 걸린 총 시간은 O(n로그n)