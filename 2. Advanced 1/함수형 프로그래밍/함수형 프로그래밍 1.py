# 4. 데이터가 많아지면: 함수형 프로그래밍

# 문제: 데이터의 양이 많아진다면 메모리 공간의 문제를 어떻게 해결할까?
# 해결: 지연 평가(lazy evaluation) = 프로그램에서 실제로 요구하는 순간에만 데이터를 생산해서 메모리 공간을 효율적으로 사용

# 시퀀스 객체: 원소의 순서가 정해져 있고 원소를 하나씩 조회할 수 있는 객체
# 배열, 튜플 등은 시퀀스 객체 o
# 사전, 집합 등은 시퀀스 객체 x

# 이터러블 객체: 원소의 순서와 관계없이 원소를 하나씩 조회할 수 있는 객체
# 배열, 튜플, 사전, 집합 등은 이터러블 객체 o
# 이터러블 객체는 __iter__를 가지고 있다

# 이터레이터 객제: 이터러블 객체에서 원소를 하나씩 꺼내어 주는 객체
# 이터러블 객체의 __iter__를 호출하면 이터레이터가 반환됨 / iter(이터러블 객체)를 호출해도 이터레이터가 반환됨
# 이터레이터는 __iter__, __next__를 메소드를 가지고 있다 / 이런 객체를 이터레이터 프로토콜을 지원하는 객체라고 한다
# 이터레이터의 __iter__를 호출하면 자기자신이 반환된다
# 이터레이터의 __next__를 호출하면 이터러블 객체의 원소가 하나씩 반환된다 / next(이터레이터)를 호출해도 이터러블 객체의 원소가 하나씩 반환됨
# 더 이상 꺼낼 원소가 없으면 StopIteration 예외를 발생시킨다

# for i in range(10) 이해하기
# range(10)은 이터러블 객체
# for문을 실행하면 자동으로 __iter__를 실행해서 이터레이터를 반환 후 자동으로 __next__를 실행해서 원소를 하나씩 꺼내어 i에 할당
# 더 이상 꺼낼 원소가 없으면 StopIteration 예외를 발생시켜서 for문을 종료시킴

# 이터러블 객체 만들기
class MyIterableObject:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyIterator(self.start, self.end)


# 이터레이터 객체 만들기
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    for i in MyIterableObject(0, 1000000):
        if i < 10:
            print(i, end=' ')
        else:
            break