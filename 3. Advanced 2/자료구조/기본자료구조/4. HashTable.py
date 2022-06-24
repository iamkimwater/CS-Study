# 해쉬테이블

# 1. 다이렉트 엑세스 테이블
# 키 - 값의 쌍으로 데이터를 저장한다
# 키를 일종의 숫자로 생각하면, 최대 키값을 배열의 길이로 가지는 큰 배열을 가정하고
# 각각의 키를 인덱스로 해서 데이터를 저장하면 된다
# 이렇게 되면 배열의 접근과 마찬가지로 O(1)의 시간안에 데이터에 접근이 가능하다
# 이러한 구조를 다이렉트 엑세스 테이블이라고 하는데...이건 공간의 낭비가 너어무 심하다

# 2. 해쉬 테이블
# 우선 고정된 길이의 배열을 만든 다음
# 해쉬함수 = 특정 값을 "원하는 범위의 자연수로" 바꿔주는 함수
# 해쉬함수(키) = 인덱스 로 하고
# 배열의 해당 인덱스에 (키, 값)을 모두 저장한다
# 해쉬함수의 조건은
# - 한 해시 테이블의 해시 함수는 결정론적이어야 된다(해시의 결과가 다르면 원래의 값도 다르다)
# - 결과 해시값이 치우치지 않고 고르게 나온다(충돌되는 정도가 고르게 분포되어야 한다)
# - 빨리 계산할 수 있어야 된다
# 해쉬 함수 예시: 나머지 연산

# 파이썬 hash 함수
# 파이썬 언어도 내부적으로 hash라는 함수를 제공합니다
# 근데 이건 방금 생각한 해시 함수랑 조금 다른데
# 파이썬 해시 함수는 파라미터로 받은 값을 그냥 아무 정수로만 바꿔주는 함수
# 즉, 특정 범위 안에 있는 정수가 아니라 아무 정수로 바꿔주죠

# 정수형, 소수형, 문자열 타입에 hash 함수를 호출했을 때 나오는 결과
# 중요한 점은 hash 함수에 서로 다른 두 값을 파라미터로 넣었을 때 같은 정수가 리턴될 수 없다는 것
# 다른 자료형들도 key로 사용할 수 있습니다
# 파이썬 hash 함수는 언어 자체적으로는 불변 타입 자료형에만 사용할 수 있다
# 불린형 정수형 소수형 튜플 문자열
# 이 정도가 있는데요. 이런 타입의 자료형만 hash 함수의 파라미터로 넘겨줄 수 있습니다

# 해쉬 충돌이 일어나면
# 1. 하나의 키에 링크드리스트를 넣어주자: 체이닝 방법
# 접근과 탐색
# 해시 함수 계산 o(1) => 배열 인덱스 접근 o(1) => 링크드 리스트 탐색 o(m)
# 최악의 경우 o(n)
# 해시 테이블을 만들 때 항상 충분히 여유롭게
# 총 저장하는 key - value 쌍 수와 해시 테이블이 사용하는 배열의 크기를 비슷하거나 작다고 가정
# 평균적으로 o(1)

# 삽입
# 해시 함수 계산 o(1) => 배열 인덱스 접근 o(1) => 링크드 리스트 탐색 o(m)
# => 없는 경우 추가하고 있는 경우 키률 유지하고 데이터만 변경 o(1)
# 최악의 경우 o(n), 평균적으로 o(1)

# 삭제
# 삽입과 동일한 시간 복잡도를 가진다


# 2. 오픈 어드레싱 방법
# 충돌이 일어나는 경우 둘 중 하나를 값이 없는 다른 인덱스에 저장하는 방법
# 값이 없는 인덱스를 어떻게 찾을까?
# 1. 선형으로 탐사해서 찾을 수 있다: 10에서 1씩 증가시키면서 체크 11, 12, 13, 14...
# 이 경우
# 탐색: 탐색을 하다가 비어있는 인덱스를 만났다면 해당 값은 없다는 뜻임
# 삭제: 진짜로 지워버리면 중간에 빈칸이 생겨서 다른 값을 탐색할 때 문제가 생김 => 삭제 대신 약속된 형태로 표시를 해두자
# 삽입: 탐색해보고 없으면 추가하면 댐
# 대강 최악은 o(n) 평균은 o(1)

# 제곱탐사도 가능: 10에서 제곱수만큼 증가시키면서 체크 11, 15, 24...

class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스


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