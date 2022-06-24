from abc import *

class User(metaclass=ABCMeta):
    __count = 0

    @classmethod
    def get_num_of_users(cls):
        print(f"{cls.__count}명의 유저가 존재합니다")

    @classmethod
    def plus_count_of_users(cls):
        cls.__count += 1

    @staticmethod
    def make_some_noise():
        print("아아아아아아아아아아!")

    def __init__(self, name, age, email, money, password):
        User.plus_count_of_users()

        self._name = name
        self.__password = password
        self.set_age(age, password)
        self._email = email
        self.set_money(money, password)

    def __call__(self):
        print("유저 인스턴스를 함수처럼 실행한 결과입니다")

    def __str__(self):
        return f"{self._name} 유저 인스턴스입니다"

    def get_name(self, password):
        if password == self.__password:
            return self._name
        else:
            print("비밀번호가 틀렸습니다")

    def get_age(self, password):
        if password == self.__password:
            return self._age
        else:
            print("비밀번호가 틀렸습니다")

    def get_email(self, password):
        if password == self.__password:
            return self._email
        else:
            print("비밀번호가 틀렸습니다")

    def get_money(self, password):
        if password == self.__password:
            return self._money
        else:
            print("비밀번호가 틀렸습니다")

    def get_password(self, password):
        if password == self.__password:
            return self.__password
        else:
            print("비밀번호가 틀렸습니다")

    def set_name(self, name, password):
        if password == self.__password:
            self._name = name
        else:
            print("비밀번호가 틀렸습니다")

    def set_age(self, age, password):
        if password == self.__password:
            self._age = age
        else:
            print("비밀번호가 틀렸습니다")

    def set_email(self, email, password):
        if password == self.__password:
            self._email = email
        else:
            print("비밀번호가 틀렸습니다")

    def set_money(self, money, password):
        if password == self.__password:
            if money >= 0:
                self._money = money
            else:
                print("돈은 0 이상이어야 합니다")
        else:
            print("비밀번호가 틀렸습니다")

    def set__password(self, old__password, new__password):
        if old__password == self.__password:
            self.__password = new__password
        else:
            print("비밀번호가 틀렸습니다")

    @abstractmethod
    def introduce_myself(self, password):
        pass

    def add_following(self):
        pass

    def delete_following(self):
        pass

    def show_all_followings(self):
        pass

    def get_count_of_followings(self):
        pass

    def show_all_followers(self):
        pass

    def get_count_of_followers(self):
        pass


class Influencer(User):
    def __init__(self, name, age, email, money, password, advertiser):
        # 부모님 변수 그대로 상속
        super(Influencer, self).__init__(name, age, email, money, password)
        # 나만의 재산
        self.advertiser = None
        # self.__advertisers = [advertiser]

    def get_name(self, password):
        if password == self.get_password(password):
            return f"인플루언서 {self._name}"
        else:
            print("비밀번호가 틀렸습니다")

    def introduce_myself(self, password):
        pass

    def set_advertiser(self, advertiser):
        self.advertiser = advertiser

    def show_advertiser(self):
        return self.advertiser.name

class Advertiser(User):
    # 브랜드 네임 변수 추가
    # 인프루언서 목록 변수 추가
    # 인플루언서를 추가하는 메소드
    # 모든 인플루언서의 이름만 차례대로 출력하는 메소드
    # aehms dlskfrnijfksjdkjfnkjn

    def __init__(self, name, age, email, money, password, influencer):
        super().__init__(name, age, email, money, password)
        self.__influencers = [influencer]

    def get_name(self, password):
        if password == self.get_password(password):
            return f"광고주 {self._name}"
        else:
            print("비밀번호가 틀렸습니다")

    def introduce_myself(self, password):
        pass


if __name__ == "__main__":
    Influencer = Influencer("Jilie", 1234, "뿡뿡이")
    Advertiser = Advertiser("semi", 5678, "뿅뿅이")




    influencer1 = Influencer("권예빈", 21, "q@q.com", 10000, 1234, "카카오")
    influencer2 = Influencer("권수빈", 21, "q@q.com", 10000, 1234, "네이버")
    influencer3 = Influencer("권화빈", 21, "q@q.com", 10000, 1234, "코카콜라")
    advertiser1 = Advertiser("카카오", 21, "q@q.com", 10000, 1234, "권예빈")
    advertiser2 = Advertiser("네이버", 21, "q@q.com", 10000, 1234, "권예빈")
    advertiser3 = Advertiser("코카콜라", 21, "q@q.com", 10000, 1234, "권예빈")

    # 다형성
    users = [influencer1, influencer2, influencer3, advertiser1, advertiser2, advertiser3]
    for user in users:
        print(user.get_name(1234))

    influencer1.add_following(influencer2)
    influencer1.add_following(influencer3)
    influencer2.add_following(influencer1)
    influencer3.add_following(influencer1)

    influencer1.delete_following("권화빈")

    influencer1.show_all_followings()
    influencer1.get_count_of_followings()
    influencer1.show_all_followers()
    influencer1.get_count_of_followers()

    influencer1.introduce_myself(1234)
    advertiser1.introduce_myself(1234)

    # # 클래스 데코레이터
    # class Trace:
    #     def __init__(self, func):  # 호출할 함수를 인스턴스의 초깃값으로 받음
    #         self.func = func  # 호출할 함수를 속성 func에 저장
    #
    #     def __call__(self):
    #         print(self.func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
    #         self.func()  # 속성 func에 저장된 함수를 호출
    #         print(self.func.__name__, '함수 끝')
    #
    #
    # @Trace  # @데코레이터
    # def hello():
    #     print('hello')
    #
    #
    # hello()  # 함수를 그대로 호출