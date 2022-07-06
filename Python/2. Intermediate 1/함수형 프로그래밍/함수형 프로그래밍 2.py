# 4. 데이터가 많아지면: 함수형 프로그래밍

# 다양한 형태의 데이터를 대량으로 지연 평가 방식으로 다루기 위해 쉽게 이터레이터를 생성하고 싶다면 제너레이터 함수를 사용
# 이터러블 객체 또는 대량의 데이터 객체를 함수로 처리해야 한다면 map filter reduce take로 처리한다
# 함수의 실행을 내가 원하는 시점에 할 수 있도록 뒤로 미루고 싶다면 클로저를 활용한다

# range 처럼 숫자만 다루는게 아닌 다양한 형태의 데이터를 대량으로 다루려면 이터레이터를 직접 제작해야 한다
# 제너레이터는 이런 나만의 이터레이터를 편리하게 만들어 주는 함수다
# 다루고자 하는 데이터 앞에 yiled 키워드를 붙이면 함수는 제너레이터가 된다

# yield를 사용하면 현재 함수를 잠시 중단하고 값을 함수 바깥으로 전달하면서 함수 바깥의 코드가 실행되도록 양보

# 제너레이터 함수를 호출하면 제너레이터 객체(generator object)라는 이터레이터 객체를 반환한다
# 이터레이터이므로 __next__를 호출해보면 yield 뒤의 값을 하나씩 꺼내준다

# 결론
# 1. 직접 제작한 이터레이터보다 더 편리하게 이터레이터를 만들 수 있다
# 2. next가 호출될 때만 yield를 한다는 점을 활용하면
# => 그 사이에 로직을 만들어서 두 함수가 번갈아 가면서 제어권을 획득하게 만들 수 있다
def users_generator():
    # next가 호출될 때 무언가 로직
    yield {"name": "하하맨", "birth": 2001}
    # next가 호출될 때 또 무언가 로직
    yield {"name": "하하걸", "birth": 2002}
    # next가 호출될 때 또 무언가 로직
    yield {"name": "호호맨", "birth": 2003}


def MyIterator(start, end):
    while True:
        if start < end:
            result = start
            start += 1
            yield result


from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 반복문을 쓰지 않고 map 또는 filter 계열의 함수를 쓰는 이유는
# 1. 가독성이 뛰어나다
# 2. map filter는 제너레이터 함수이다. 즉 평가를 미루고 이터레이터를 반환한다
# a = map(lambda x: x + 1, a)
# a = filter(lambda x: True if x > 5 else False, a)
# result = reduce(lambda x, y: x + y, a)


def my_map(f, iter):
    for item in iter:
        yield f(item)


def my_filter(f, iter):
    for item in iter:
        if f(item):
            yield item


def my_take(iter, limit):
    result = []
    for item in iter:
        if limit != 0:
            result.append(item)
            limit -= 1
        else:
            break
    return result


# 함수가 함수를 리턴하는 방식을 활용하면
# 평가를 미뤘다가
# 내가 원하는 파라미터가 들어오는 시점에 함수를 평가할 수 있게 설계할 수 있다
# 이 때 변수의 범위에 대한 주의사항이 클로저 개념이다
def add_two(x):
    x = x + 2

    def multiply_two():
        return x * 2

    return multiply_two


zxczxzcx = add_two(100)
print(zxczxzcx())

# curry 함수: 함수가 인자를 다 받으면 평가, 덜 받으면 평가 지연
# go 함수: 함수들을 차례로 실행


if __name__ == "__main__":
    for i in MyIterator(0, 10000000000000000000000000000000000000000000):
        if i < 10:
            print(i, end=' ')
        else:
            break
    #
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    #
    # def my_map(f, iter):
    #     for item in iter:
    #         yield f(item)
    #
    #
    # def my_filter(f, asdasdasdasd):
    #     for item in asdasdasdasd:
    #         if f(item):
    #             yield item
    #
    #
    # # 순서1 더 깔끔하게
    # result1 = my_map(lambda x: x + 1, numbers)
    # result2 = my_filter(lambda x: True if x % 2 == 0 else False, result1)
    # result3 = result2.__next__()
    # print(result3)
    #
    #
    # # 지연 평가의 핵심
    # def func1(numbers):
    #     result1 = my_map(lambda x: x + 1, numbers)
    #
    #     def func2():
    #         result2 = my_filter(lambda x: True if x % 2 == 0 else False, result1)
    #
    #         def func3():
    #             return result2.__next__()
    #
    #         return func3
    #
    #     return func2
    # print(add_one_function(10))
    # personal_info(name="홍길동", age=30, address="서울시 용산구 이촌동")
    #
    # print_numbers(10, *[20, 30, 40])
    # print_numbers(10, *(20, 30, 40))
    # print_numbers(10, 20, 30, 40, 50, 60)

    #
    # print(f"내 나이는 {temp_function(2021, 2000)}살 입니다.")
    # print(add_two(10)())
    #
    users = users_generator()
    for user in users:
        if user["name"] == "하하맨":
            print(user)
            break
    #
    # s = time.time()
    # arr = range(1000)
    # arr = my_map(lambda num: num + 10, arr)
    # print(arr)
    # arr = my_filter(lambda num: num % 2, arr)
    # print(arr)
    # result = my_take(arr, 2)
    # print(result)
    # e = time.time()
    # print(f"{e - s}초 걸렸습니다")