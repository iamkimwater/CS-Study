from abc import *

# 데이터: 인스턴스 변수, 클래스 변수
# 함수: 인스턴스 메소드, 클래스 메소드, 스태틱 메소드, 매직 메소드, 추상 메소드

class User(metaclass=ABCMeta):   # 추상메소드 사용하려면 metaclass=ABCMeta, import
    # 클래스변수
    __count = 0

    # 클래스메소드
    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def plus_one_count(cls):
        cls.__count += 1

    # 스태틱메소드
    @staticmethod
    def say_hi():
        print("하이")

    # 매직메소드(자동실행)
    def __init__(self, user_id, user_password):
        # 인스턴스변수(일괄적으로 __처리)
        self.__user_id = user_id
        self.__user_password = user_password
        User.plus_one_count()

    # 인스턴스메소드(필요할 때 변수에 접근)
    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    def set_user_password(self, original_password, new_user_password):
        if self.__user_password == original_password:
            self.__user_password = new_user_password
        else:
            print("기존 비밀번호가 틀렸습니다")

    # 추상메소드
    @abstractmethod
    def introduce_myself(self, password):
        pass

if __name__ == "__main__":

    user1 = User("a", 1234)
    user2 = User("b", 1234)
    user3 = User("c", 1234)

    user1.set_user_id("aaa")
    user2.set_user_id("bbb")
    user3.set_user_id("ccc")
    user1.set_user_password(1234, 5678)
    user2.set_user_password(1234, 5678)
    user3.set_user_password(1234, 5678)

    # print(user1.__user_id)
    # print(user2.__user_id)
    # print(user3.__user_id)
    # print(user1.__user_password)
    # print(user2.__user_password)
    # print(user3.__user_password)

    # 보호되어있어서 볼 수 없음 -> get 사용
    print(user1.get_user_id())
    print(user2.get_user_id())
    print(user3.get_user_id())

    # User.say_hi()
    print(User.get_count())