# 1. Array (배열)

## ...
c언어에 존재
연속적인 메모리 공간에 원소의 값들이 저장된다
값을 가져오고 싶으면 배열의 이름, 즉 첫번쨰 값의 주소값에 자료형의 크기 * 개수 만큼을 더해서 그 주소의 값을 읽으면 된다
메모리는 임의접근이 가능하기 때문에, 인덱싱에 O(1)의 시간이 걸린다
즉, 접근과 저장은 O(1), 탐색은 O(n)이 걸린다

정적배열
처음부터 메모리 크기를 고정하고 쓰기 때문에 추가가 불가능하다
추가를 위해 필요 이상으로 크게 정의하면 메모리 공간이 낭비된다
삽입 삭제 불가
삭제는 왜 불가능한가?
정수 4개를 담을 수 있는 배열에 2, 3, 5, 7이 저장돼 있다고 가정
여기서 인덱스 1에 있는 3을 지우고 싶으면 어떻게 하면 될까?
인덱스 3에 저장되어 있던 7을 메모리에서 자연스럽게 지울 수 있는 방법이 마땅히 없다
비었다는 것을 표시하기 위해서 파이썬에서는 None, 다른 언어들에서는 Null 이런 값을 넣는 걸 생각하실 수 있으나
이미 정수형 데이터를 4 개를 저장하는 메모리 공간을 빌렸으므로 None이나 Null은 정수형이 아니며 삭제는 불가능하다

동적배열: 객체
상황에 따라 크기가 변한다
동적 배열 객체 내부의 정적 배열이 꽉 차게 되면
2배정도의 크기가 되는 동적 배열을 다시 메모리(힙)에 확보하고
값을 전부 복사해서 사용
메모리 공간적으로 O(n)이 낭비된다
언젠가 크기가 꽉 차면 또 다시 사이즈를 확보하고 위의 상황을 반복한다

추가 연산: 여유 공간이 있다면 O(1), 여유 공간이 없다면 O(n)
여유 공간이 있는 경우가 대부분인데 여유 공간이 없다면 O(n)이므로 평등성을 위해

삽입 연산: 여유 공간이 있다면 O(n), 여유 공간이 없다면 O(n)

삭제 연산: 제일 앞 삭제 O(n), 제일 뒤 삭제 O(1)
삭제를 많이 하면 적당한 비율만큼 공간이 낭비될 때 배열을 동적으로 재할당한다

삭제는 여기는 어케 가능한가?
동적 배열은 사용하는 배열의 크기와 사용하는 인덱스 범위를 따로 처리한다
동적 배열이 내부적으로 정수 4개를 저장할 수 있는 배열에 2, 3, 5, 7을 저장하고 있다고 하자
동적 배열에서 인덱스 1을 삭제하고 싶으면 인덱스 1에 5를 저장하고
인덱스 2에 7을 저장합니다
그럼 내부적으로는 2, 5, 7, 7 이렇게 저장되어 있을 텐데
그 다음에 인덱스 3에 있는 7을 지우는 게 아니라 파이썬 내부적으로
개발자가 접근할 수 있는 인덱스 범위를 0 ~ 2로 만들어 버립니다
더 이상 인덱스 3에 접근할 수 없게 만드는 것
실제로 인덱스 3에 어떤 값이 저장되어 있던 상관없이 개발자는 더 이상 거기 접근할 수 없다
동적 배열에서 접근할 수 있는 데이터가 2, 5, 7 밖에 없으니까 실질적으로 삭제됐다고 할 수 있는 거죠

결론
파이썬의 리스트: c의 동적 배열로 구현되어 있다!
파이썬의 모든 변수는 레퍼런스 변수이다
파이썬의 리스트에는 연속적인 메모리 공간에 레퍼런스 변수가 저장된다
실제로 그 레퍼런스가 가리키는 값은 공간적으로 불연속적이다
이러한 방식을 쓰면 하나의 배열 안에 다형성 있게 값을 저장하는게 가능해 진다

---
### 코드 예시
#### 정의파트
```python

```
#### 실행파트
```python

```
#### 출력결과
```python

```

# 2. Single Linked List (단일연결리스트)

## ...

---
### 코드 예시
#### 정의파트
```python
class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def set_next_node(self, next_node):
        self.next_node = next_node
```

```python
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

    # 접근: o(n)
    def find_by_index(self, index):
        count = index
        iterator = self.head
        while count != 0:
            iterator = iterator.next_node
            count -= 1
        return iterator.data

    # 추가: o(1)
    def add(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    # 삽입: o(1)
    def insert_after(self, previous_node, data):
        if previous_node == self.tail:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_after(self, previous_node):
        data = previous_node.next.data

        if previous_node.next == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next

        return data

    def pop_left(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = self.tail = None
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            return temp
```

#### 실행파트
```python
if __name__ == "__main__":    # 메모리에 흩어져 있는 노드 객체들에게 데이터와 넥스트를 세팅해서 마치 순서가 있는 것 처럼 다룰 수 있는 자료구조
    singlyLinkedList = SinglyLinkedList()
    print(singlyLinkedList)
    singlyLinkedList.add(1)
    print(singlyLinkedList)
    singlyLinkedList.add(2)
    print(singlyLinkedList)

    # 접근: 시간 복잡도가 O(n) / 배열에 비해서 느리다
    data = singlyLinkedList.find_by_index(1)
    print(data)
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
```
#### 출력결과
```python
[ ]
[]
[ 2 ]
2
```

# 3. Double Linked List (이중연결리스트)

## ...

---
### 코드 예시
#### 정의파트
```python
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

```python
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
```
#### 실행파트
```python
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
```
#### 출력결과
```python
[ 2  3  5  7  11 ]
[ 2  3  5  7  11  5 ]
[ 2  3  5  7  3  11  5 ]
[ 2  3  5  7  11  2  3  5  7  3  11  5 ]

[ 2  3  7  11  2  3  5  7  3  11  5 ]
2
[ 3  7  11  2  3  5  7  3  11  5 ]
[ 3  7  11  2  3  5  7  3  11 ]
[]
```

# 4. Hash Table (해쉬테이블)

## ...
1. 다이렉트 엑세스 테이블
키 - 값의 쌍으로 데이터를 저장한다
키를 일종의 숫자로 생각하면, 최대 키값을 배열의 길이로 가지는 큰 배열을 가정하고
각각의 키를 인덱스로 해서 데이터를 저장하면 된다
이렇게 되면 배열의 접근과 마찬가지로 O(1)의 시간안에 데이터에 접근이 가능하다
이러한 구조를 다이렉트 엑세스 테이블이라고 하는데...이건 공간의 낭비가 너어무 심하다

2. 해쉬 테이블
우선 고정된 길이의 배열을 만든 다음
해쉬함수 = 특정 값을 "원하는 범위의 자연수로" 바꿔주는 함수
해쉬함수(키) = 인덱스 로 하고
배열의 해당 인덱스에 (키, 값)을 모두 저장한다
해쉬함수의 조건은
- 한 해시 테이블의 해시 함수는 결정론적이어야 된다(해시의 결과가 다르면 원래의 값도 다르다)
- 결과 해시값이 치우치지 않고 고르게 나온다(충돌되는 정도가 고르게 분포되어야 한다)
- 빨리 계산할 수 있어야 된다
해쉬 함수 예시: 나머지 연산

파이썬 hash 함수
파이썬 언어도 내부적으로 hash라는 함수를 제공합니다
근데 이건 방금 생각한 해시 함수랑 조금 다른데
파이썬 해시 함수는 파라미터로 받은 값을 그냥 아무 정수로만 바꿔주는 함수
즉, 특정 범위 안에 있는 정수가 아니라 아무 정수로 바꿔주죠

정수형, 소수형, 문자열 타입에 hash 함수를 호출했을 때 나오는 결과
중요한 점은 hash 함수에 서로 다른 두 값을 파라미터로 넣었을 때 같은 정수가 리턴될 수 없다는 것
다른 자료형들도 key로 사용할 수 있습니다
파이썬 hash 함수는 언어 자체적으로는 불변 타입 자료형에만 사용할 수 있다
불린형 정수형 소수형 튜플 문자열
이 정도가 있는데요. 이런 타입의 자료형만 hash 함수의 파라미터로 넘겨줄 수 있습니다

해쉬 충돌이 일어나면
1. 하나의 키에 링크드리스트를 넣어주자: 체이닝 방법
접근과 탐색
해시 함수 계산 o(1) => 배열 인덱스 접근 o(1) => 링크드 리스트 탐색 o(m)
최악의 경우 o(n)
해시 테이블을 만들 때 항상 충분히 여유롭게
총 저장하는 key - value 쌍 수와 해시 테이블이 사용하는 배열의 크기를 비슷하거나 작다고 가정
평균적으로 o(1)

삽입
해시 함수 계산 o(1) => 배열 인덱스 접근 o(1) => 링크드 리스트 탐색 o(m)
=> 없는 경우 추가하고 있는 경우 키률 유지하고 데이터만 변경 o(1)
최악의 경우 o(n), 평균적으로 o(1)

삭제
삽입과 동일한 시간 복잡도를 가진다


2. 오픈 어드레싱 방법
충돌이 일어나는 경우 둘 중 하나를 값이 없는 다른 인덱스에 저장하는 방법
값이 없는 인덱스를 어떻게 찾을까?
1. 선형으로 탐사해서 찾을 수 있다: 10에서 1씩 증가시키면서 체크 11, 12, 13, 14...
이 경우
탐색: 탐색을 하다가 비어있는 인덱스를 만났다면 해당 값은 없다는 뜻임
삭제: 진짜로 지워버리면 중간에 빈칸이 생겨서 다른 값을 탐색할 때 문제가 생김 => 삭제 대신 약속된 형태로 표시를 해두자
삽입: 탐색해보고 없으면 추가하면 댐
대강 최악은 o(n) 평균은 o(1)

제곱탐사도 가능: 10에서 제곱수만큼 증가시키면서 체크 11, 15, 24...

---
### 코드 예시
#### 정의파트
```python
class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스
```

```python
class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def find_node_with_key(self, key):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수

        while iterator is not None:
            if iterator.key == key:
                return iterator

            iterator = iterator.next

        return None

    def append(self, key, value):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(key, value)

        # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 이미 노드가 있으면
        else:
            self.tail.next = new_node  # 마지막 노드의 다음 노드로 추가
            new_node.prev = self.tail
            self.tail = new_node  # 마지막 노드 업데이

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.value

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = ""

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += "{}: {}\n".format(iterator.key, iterator.value)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```

```python
class HashTable:
    """해시 테이블 클래스"""

    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 저장
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """
        주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        주의: key는 파이썬 불변 타입이여야 한다.
        """
        return hash(key) % self._capacity

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        find_node = self._table[self._hash_function(key)].find_node_with_key(key)
        if find_node is None:
            return None
        else:
            return find_node.value

    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        find_node = self._table[self._hash_function(key)].find_node_with_key(key)
        if find_node is None:
            self._table[self._hash_function(key)].append(key, value)
        else:
            find_node.value = value

    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        find_node = self._table[self._hash_function(key)].find_node_with_key(key)
        if find_node is not None:
            self._table[self._hash_function(key)].delete(find_node)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]
```
#### 실행파트
```python
if __name__ == "__main__":
    test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

    # 여러 학생들 이름과 시험 점수 삽입
    test_scores.insert("현승", 85)
    test_scores.insert("영훈", 90)
    test_scores.insert("동욱", 87)
    test_scores.insert("지웅", 99)
    test_scores.insert("신의", 88)
    test_scores.insert("규식", 97)
    test_scores.insert("태호", 90)

    print(test_scores)

    # key인 이름으로 특정 학생 시험 점수 검색
    print(test_scores.look_up_value("현승"))
    print(test_scores.look_up_value("태호"))
    print(test_scores.look_up_value("영훈"))

    # 학생들 시험 점수 수정
    test_scores.insert("현승", 10)
    test_scores.insert("태호", 20)
    test_scores.insert("영훈", 30)

    print(test_scores)
    print("삭제 ㄱㄱ")
    # 학생들 시험 점수 삭제
    test_scores.delete_by_key("태호")
    test_scores.delete_by_key("지웅")
    test_scores.delete_by_key("신의")
    test_scores.delete_by_key("현승")
    test_scores.delete_by_key("규식")
    print(test_scores)
```
#### 출력결과
```python
신의: 88
영훈: 90
현승: 85
규식: 97
동욱: 87
태호: 90
지웅: 99
85
90
90
신의: 88
영훈: 30
현승: 10
규식: 97
동욱: 87
태호: 20
지웅: 99
삭제 ㄱㄱ
영훈: 30
동욱: 87
```

# 5-1. Heap (힙)

## ...
힙(최대 힙)
1. 완전 이진 트리(CBT)
2. 부모 노드의 데이터는 자식 노드 데이터보다 크거나 같음

최소 힙
1. 완전 이진 트리(CBT)
2. 부모 노드의 데이터는 자식 노드 데이터보다 작거나 같음

활용
힙 정렬 / 우선순위 큐 구현

---
### 코드 예시
#### 정의파트
1. 힙을 만든다
완전 이진 트리의 마지막 원소부터 거꾸로 heapify 연산을 수행한다

heapify 연산이란?
특정 노드가 힙 조건을 만족하도록 원래 위치를 찾아주는 함수
```python
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
```
2. 힙 정렬을 사용한다
만든 힙으로 힙 정렬을 한다
1. 루트 노드와 마지막 노드를 교체
2. 교체되서 제일 마지막에 존재하는 노드는 이제 무시
3. 무시한 노드를 제외하고 나머지 트리에서 루트 노드를 heapify
4. 1 ~ 3을 반복
시간 복잡도 = O(n로그n)
```python
def heapsort(tree):
    count = 1
    tree_size = len(tree)
    while count < tree_size:
        tree[1], tree[-count] = tree[-count], tree[1]
        heapify(tree, 1, tree_size - count)
        count += 1
```
#### 실행파트
```python
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
```
#### 출력결과
```python
[None, 15, 14, 12, 11, 9, 10, 6, 2, 5, 1]
[None, 1, 2, 5, 6, 9, 10, 11, 12, 14, 15]
```

# 5-2. Binary Search Tree (이진탐색트리)

## ...
1. 정의
이진트리(완전이진트리X, 노드의 연결로 구현)
임의의 어떤 노드에 대해 그 왼쪽 부분 트리의 모든 데이터 < 임의 노드 데이터 < 오른쪽 부분 트리의 모든 데이터

2. 활용
데이터를 빠르게 찾을 수 있다
이진 탐색 트리는 딕셔너리와 셋을 구현하는데 쓰임

3. 성질
이진 탐색 트리를 in-order 방법으로 순회하면 저장된 데이터들을 정렬된 순서대로 출력할 수 있다
이진 탐색 트리는 완전 이진 트리가 아닌 경우가 더 많다
그렇기 때문에 노드가 n개 있을 때, 높이 h가 항상 O(lg(n))이라고 할 수 없다
최악의 경우를 예로 들자면, 이진 탐색 트리의 높이는 O(n)
예를 들면 이진 탐색 트리에 데이터로 1, 2, 3, 4, 5, 6을 순서대로 삽입하면 트리가 한쪽으로 편향

1. 접근

2. 탐색
이분 탐색과 비슷하다(시간 h)

3. 삽입
새로운 노드를 만들고 > root부터 비교하면서 알맞은 위치 발견(시간 h) > 추가

6. 삭제
우선 노드를 찾아야 한다
말단 노드를 삭제하는 경우는 걍
중간에 자식이 하나인 노드를 지우는 경우 자식 노드를 부모 자리로 올려 보내면 그만임
중간에 자식이 2개인 노드를 지우는 경우
---
### 코드 예시
#### 정의파트
```python
def print_inorder(node):
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)
```

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
```
![예시그림](./img/1.png)
```python
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
```

#### 실행파트
```python
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
```
#### 출력결과
```python
2
3
4
5
7
8
9
11
14
17
19


9
14
17
19
```

# 6. Tree (트리)

## ...
용어
루트 노드 / 형제 노드 / 리프 노드 / 자식 노드 / 부모 노드 / 깊이 / 레벨 / 높이 / 부분 트리

종류
binary tree: 각 노드가 최대 2개의 자식 노드를 가질 수 있다
complete binary tree: 마지막 바로 직전 레벨까지 모든 노드가 다 채워지고 마지막 레벨은 왼쪽부터 차례대로 노드가 다 차있다
complete binary tree: 노드가 n개이면 높이 h는 O(로그n)

활용
1. 계층 관계를 가진 데이터를 저장할 때
2. 정렬(힙 정렬) 압축(후프만 코드)을 매우 똑똑하게 처리하고 싶을 때
3. 우선순위 큐(힙으로), 딕셔너리(BST), 셋(BST)와 같은 추상 자료형을 구현할 때
---
### 코드 예시
우리는 다양한 트리 중에서 이진 트리의 구현에 집중해 본다
#### 정의파트
```python
# 이진 트리의 노드
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
```

```python
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
```

```python
# 왼쪽 자식 노드 인덱스 구하기
def get_left_child_index(cbt, index):
    left_child_index = index * 2
    if left_child_index < 1 or left_child_index > len(cbt) - 1:
        return None
    else:
        return left_child_index
```

```python
# 오른쪽 자식 노드 인덱스 구하기
def get_right_child_index(cbt, index):
    right_child_index = index * 2 + 1
    if right_child_index < 1 or right_child_index > len(cbt) - 1:
        return None
    else:
        return right_child_index
```

```python
# 부모 노드 인덱스 구하기
def get_parent_child_index(cbt, index):
    parent_index = index // 2
    if parent_index < 1 or parent_index > len(cbt) - 1:
        return None
    else:
        return parent_index
```
#### 실행파트
```python
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
```
#### 출력결과
```python
7
4
8
2
5
1
6
3
9
2
11
10
5
9
1
10
12
14
```

# 7. Graph (그래프)

## ...

+ .
+ .

|  A  |  B  |  C  |
|:---:|:---:|:---:|
|  A  |  B  |  C  |
|  A  |  B  |  C  |
|  A  |  B  |  C  |
|  A  |  B  |  C  |

---
### 코드 예시
#### 정의파트
```python

```
#### 실행파트
```python

```
#### 출력결과
```python

```