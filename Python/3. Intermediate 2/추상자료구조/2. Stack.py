# 스택
# : 맨 뒤 추가 / 맨 뒤 삭제 / 맨 뒤 접근
# : 동적 배열과 링크드 리스트로 구현이 가능
# : 링크드 리스트가 유리하다
# : from collections import deque를 사용해서 스택을 쓴다
from collections import deque

class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    def push(self, data):
        self.sll.append(data)

    def pop(self):
        self.sll.remove()

    def peak(self):
        return self.sll.find_by_index(self.sll.size - 1)


from collections import deque

def parentheses_checker(string):
    """주어진 문자열 인풋의 모든 괄호가 짝이 있는지 확인해주는 메소드"""


    print(f"테스트하는 문자열: {string}")
    stack = deque() # 사용할 스택 정의

    # 코드를 쓰세요

case1 = "(1+2)*(3+5)"
case2 = "((3*12)/(41-31))"
case3 = "((1+4)-(3*12)/3"
case4 = "(12-3)*(56/3))"
case5 = ")1+14)/3"
case6 = "(3+15(*3"

parentheses_checker(case1)
parentheses_checker(case2)
parentheses_checker(case3)
parentheses_checker(case4)
parentheses_checker(case5)
parentheses_checker(case6)

if __name__ == "__main__":
    queue = deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)