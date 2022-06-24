# 데이터 초급(숫자 문자 불린 사전 배열) 난이도 상승: 객체지향 프로그래밍
# 함수 초급 난이도 상승: 함수형 프로그래밍
# 제어(반복문 if문) 난이도 상승: 최적화 작업



# 데이터 중급

# 문제: 데이터의 관계가 복잡해 진다면 문제를 어떻게 해결할까?
# 해결: 객체지향 프로그래밍 = 복잡한 데이터를 잘 관리하는 방법 = 데이터와 함수를 하나의 객체로 관리한다

# 객체지향 프로그래밍의 4대 원칙
# 1. 추상화: 객체 사용자가 클래스 내부를 알지 못해도 편리하게 사용할 수 있도록 클래스를 잘 설계해야 한다
# 2. 캡슐화: 속성을 감추고 메소드로 컨트롤한다
# 3. 상속: 부모 클래스를 최대한 활용한다
# 4. 다형성: 이름도 같고 파라미터도 같은데 내부 로직이 다른 함수 = 오버라이딩(부모와 자식)
# 참고: 이름은 같은데 파라미터는 다른 함수를 만드는 것 = 오버로딩(파이썬은 불가능)

# 객체지향 프로그램 설계의 5대 원칙
# 1. 단일 책임 원칙
# 2. 개방 폐쇄 원칙
# 3. 리스코프 치환 원칙(부모 객체를 자식 객체가 대체할 수 있어야 한다)
# 4. 인터페이스 분리 원칙
# 5. 의존 역전 원칙
from abc import *


# 메타 클래스 = 파이썬에서는 클래스도 객체이다. 따라서 클래스 객체를 만드는 또 다른 클래스가 존재한다. 이를 메타 클래스라 한다
# 추상 메소드 존재 / metaclass=ABCMeta => 추상 클래스 => 부모 클래스가 자식 클래스에게 추상 메소드의 구현을 강제
# 추상 클래스로 인스턴스(객체)를 만들면 에러가 발생
class User(metaclass=ABCMeta):
    # 속성: 인스턴스 변수, 클래스 변수
    # 메소드: 인스턴스 메소드, 클래스 메소드, 스태틱 메소드, 매직 메소드, 추상 메소드

    # 클래스 변수
    __count = 0

    # 클래스 메소드
    # 클래스 메소드는 클래스에서 직접 접근해서 사용하는 메소드
    # 클래스 메소드는 클래스 변수를 제어할 때 사용
    @classmethod
    def get_num_of_users(cls):
        print(f"{cls.__count}명의 유저가 존재합니다")

    @classmethod
    def plus_count_of_users(cls):
        cls.__count += 1

    # 스태틱 메소드
    # 스태틱 메소드는 클래스에서 직접 접근해서 사용하는 메소드(파이썬에서는 스태틱 메소드임에도 불구하고 인스턴스에서 접근이 가능)
    # 스태틱 메소드는 인스턴스 속성과 관계가 없는 유틸성 메소드를 만들 때 사용
    @staticmethod
    def make_some_noise():
        print("아아아아아아아아아아!")

    # 매직 메소드
    # 특정 상황에서 자동으로 실행
    # __init__: 클래스() => 객체를 생성 => 생성자가 자동으로 실행
    def __init__(self, name, age, email, money, password):
        User.plus_count_of_users()
        # 인스턴스 변수
        # __변수이름: 클래스 외부에서 접근할 수 없도록 보호 => private 변수
        # _변수이름: 클래스 외부에서 접근할 수 없도록 보호 => 자식 클래스는 접근 가능 => protected 변수
        self._name = name
        self.__password = password
        self.set_age(age, password)  # set 메소드를 거쳐서 속성을 세팅하면 안전하다
        self._email = email
        self.set_money(money, password)  # set 메소드를 거쳐서 속성을 세팅하면 안전하다

    # __call__: 인스턴스() => __call__ 내부가 자동으로 실행
    def __call__(self):
        print("유저 인스턴스를 함수처럼 실행한 결과입니다")

    # __str__: print(인스턴스) => __str__ 내부에서 리턴한 문자열이 출력
    def __str__(self):
        return f"{self._name} 유저 인스턴스입니다"

    # 인스턴스 메소드 => 주로 모든 속성에 대한 get set 메소드를 먼저 만들어 준 후 다른 메소드를 추가한다
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

    # 추상 메소드
    @abstractmethod
    def introduce_myself(self, password):
        pass

    # 과제
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

    # 디스크립터
    # 프로퍼티


# 상속
class Influencer(User):
    def __init__(self, name, age, email, money, password, advertiser):
        # 부모 클래스의 생성자 호출
        super().__init__(name, age, email, money, password)
        # 자식 클래스의 인스턴스 변수 설정
        self.__advertisers = [advertiser]

    # 부모 클래스의 메소드를 자식이 재정의 = 오버라이딩(다른 언어에는 오버로딩도 존재한다)
    def get_name(self, password):
        if password == self.get_password(password):
            return f"인플루언서 {self._name}"
        else:
            print("비밀번호가 틀렸습니다")

    # 부모 클래스의 추상 메소드는 자식 클래스에서 필수로 구현해야 한다
    def introduce_myself(self, password):
        # 적당한 자기소개 및 팔로워 숫자를 자랑하도록 코드를 쓰세요
        pass


class Advertiser(User):
    def __init__(self, name, age, email, money, password, influencer):
        # 부모 클래스의 생성자 호출
        super().__init__(name, age, email, money, password)
        # 자식 클래스의 인스턴스 변수 설정
        self.__influencers = [influencer]

    # 부모 클래스의 메소드를 자식이 재정의 = 오버라이딩(다른 언어에는 오버로딩도 존재한다)
    def get_name(self, password):
        if password == self.get_password(password):
            return f"광고주 {self._name}"
        else:
            print("비밀번호가 틀렸습니다")

    # 부모 클래스의 추상 메소드는 자식 클래스에서 필수로 구현해야 한다
    def introduce_myself(self, password):
        # 적당한 회사 소개를 하도록 코드를 쓰세요
        pass


if __name__ == "__main__":
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

# 정리되지 않은 보충 설명
# 상속1 : 데이터간의 질서를 설계하는데 사용한다
# : c++의 다중 상속은 다이아몬드 상속의 문제를 반드시 피한다
# : 자바의 다중 상속 대신 다중 인터페이스로 구현한다
# : 파이썬의 다중 상속은 다이아몬드 상속의 문제를 반드시 피한다
#
# 상속2 :
# 폴리모피즘 + 가상함수 + 순수 가상함수 + 추상 클래스 + 가상 소멸자
# : 부모 포인터로 자식 객체를 동적할당하면 부모 포인터 하나로 다 해결볼 수 있다
# : 부모 포인터를 선언하는 순간 정적 바인딩으로 부모 포인터는 부모 클래스의 메소드를 호출할 수 있게 된다
# : 따라서 동적 할당으로 자식 객체를 만들어도 부모 포인터는 부모의 메소드만 호출할 수 있다
# : 이런 상황에서 자식 객체의 메소드를 호출하는 방법은 다음의 2가지가 존재한다
#
# 상속2 방법 1
# : 다이나믹 캐스팅을 사용해서 부모 객체의 포인터 타입을 자식 객체의 포인터 타입으로 바꾼 후에 자식 객체의 메소드를 호출 방법 2 : 부모 포인터로 메소드를 호출해도 자식 객체의 메소드를 사용하고 싶다면 부모
# 객체의 함수를 가상함수로 선언해서 동적으로 함수를 할당한다
#
# : 부모 클래스에서 메소드를 가상함수로 선언했다면 자식 클래스에서 그 메소드는 오버라이딩 해도 되고 안해도 된다 : 부모 클래스에서 메소드를 순수가상함수로 선언했다면 자식 클래스에서 그 메소드는 반드시
# 오버라이딩한다 : 순수가상함수가 존재하는 부모클래스는 객체를 생성할 수 없고, 이러한 부모 클래스를 특별히 추상 클래스고 부른다 : 추상 클래스를 상속받은 자식 클래스는 순수가상함수를 반드시 오버라이딩해야 객체를
# 생성할 수 있다
#
# : 가상함수만 존재하는 클래스를 자바는 특별히 인터페이스라고 부른다
#
# : 폴리모피즘으로 객체를 생성하고 부모 포인터의 소멸자를 호출하면 정적으로 바인딩된 부모 클래스의 소멸자만 호출되기 때문에, 자식 객체의 메모리가 해제되지 않고 남아있게 된다 : 그래서 부모의 소멸자를 가상함수로
# 선언하고, 소멸자를 호출해서 자식의 소멸자가 동적으로 바인딩되서 호출된 후에, 부모의 소멸자까지 호출될 수 있도록 한다
#
# : 자바는 다중상속이 불가능하다
#
# c++의 일반 클래스(멤버변수 존재 + 메소드 존재 + 메소드 오버라이딩이 어쩌면 필요한 함수를 가상함수로 선언(딱히 뭐가 없어도 되지만 기왕이면 가상함수로 선언하자)) : 인스턴스 생성 가능 c++의 추상 클래스(
# 멤버변수 존재 + 메소드 존재 + 메소드 오버라이딩이 반드시 필요한 함수를 순수 가상함수로 선언) : 인스턴스 생성 불가
#
# 자바의 일반 클래스(멤버변수 존재 + 메소드 존재 + 메소드 오버라이딩은 딱히 뭔가 없어도 알아서 된다(가상함수 선언하면 안됨) 자바의 추상 클래스(멤버변수 존재 + 메소드 존재 + 메소드 오버라이딩이 반드시 필요한
# 함수를 가상함수로 선언(자바의 가상함수는 c++의 순수 가상함수와 같다)) : 인스턴스 생성 불가 자바의 인터페이스(메소드를 모두 가상함수로 선언) : 인스턴스 생성 불가
#
# c++의 상속형태 부모 클래스 : 프라이빗 나만 씀 자식 예외 없음 / 프로텍티드 나랑 자식만 씀 / 퍼블릭 걍 다 써라
#
# public 상속 : 부모의 프라이빗은 못씀 / 부모의 프로텍티드는 씀 / 부모의 퍼블릭은 씀 프라이빗 상속 : 부모의 프라이빗은 못씀 / 부모의 프로텍티드는 씀 / 부모의 퍼블릭을 쓰는데 본인은 프로텍티드로 사용함
# 프라이빗 상속 : 부모의 프라이빗은 못씀 / 부모의 프로텍티드는 쓰는데 본인은 프라이빗으로 씀 / 부모의 퍼블릭을 쓰는데 본인은 프라이빗으로 씀
#
# 자바의 접근제이자 public 어떤 클래스든 접근 가능 protected 자기자신, 같은패키지, 서로다른 패키지라 하더라도 상속받은 자식클래스에선 접근가능 private 자기 자신만 접근가능 default(
# 접근제어자를 따로 적지않으면 default) 자기자신과 같은 패키지에서만 접근할 수 있음
#
# 자바의 상속형태 ?
#
# 자바는 객체를 동적으로만 생성할 수있다 힙 메모리는 자동으로 해제됨 연산자 오버로딩 안됨 메소드 오버로딩 됨(그러니까 같은 함수인데 들어가는 파라미터에 따라 다르게 실행되는거임)
#
# 자바는 객체a의 자식이 객체b인 경우 a[]의 자식이 b[]지만 어레이의 자식관계로 어레이가 되지 않는다 즉 배열은 자식관계에 영향을 받지만, 제네릭은 아무런 관계가 없는 두 객체가 만들어진다 따라서 a[]배열을
# 선언하고 b객체를 담는것은 가능하지만(업캐스팅 원리) 어레이를 선언하고 b객체를 담는건 당연히 불가능하다(애초에 캐스팅이 아니다. 전혀 무관하기 때문) 따라서 List myList = new ArrayList();
# 이런건 캐스팅과 무관한거라서 컴파일부터 안된다. 타입이 일치하지 않기때문
#
# 파이널 : 캐릭터를 계속 추가생성하면 / 생성된 캐릭터마다 새로운 메모리가 할당되지만 / 똑같은 값으로 저장되는 / 불변의 값 스태틱 : 캐릭터를 계속 추가생성해도 / 생성된 캐릭터 모두 하나의 메모리를 공유하기
# 때문에 / 바꾸면 모든 캐릭터가 다 바뀌는 / 공유의 값 파이널 스태틱 : 새로운 캐릭터가 생성되도 하나의 메모리에 공유된, 그리고 절대 바뀌지 않을, 불변의 공유값
#
# 상속 : 메소드를 상속받을때 메소드를 그대로 상속받아야 한다(변수랑 메소드만) (제네릭을 쓰면 상속도 중첩할 수 있다)
#
# 인터페이스 : 빈 메소드 이름만 공유/의무상속을 약속하고 실제 메소드는 달리 할 수 있다(추상메소드만) (숨어있는 특수인터페이스 컴페어러블이 있다)
#
# 추상클래스 : 상속 인터페이스 다 동시에 쓰고싶으면 이걸 쓰자(변수 메소드 추상메소드) (추상클래스를 상속받는 여러 클래스를 일일히 만들지 않고 바로 main파일에서 인스턴스가 생성되도록 할 수 있다)
#
# public = 다른곳에서 사용 가능 private = 다른곳에서 사용 불가능(게터, 세터함수로 값에 접근할 수 있다)
#
# final
# > > 클래스 정의 >> 클래스 10개 생성 >> 메모리 공간 10개 할당 >> 변수공간 10개 생성
# > > 변수공간 10개에 할당하는 값이 항상 일정
#
# static
#
# 1. 임의의 클래스 x 내부에 static 변수 y를 정의하면
#
# > > 클래스 x 정의
# > > 메모리 공간 1개 할당
# > > 변수공간 y 1개 지정(클래스 x를 생성하지 않아도, y가 정의만 되어있다면, 변수공간이 이미 생성되어 있으며, y를 사용할 수 있다)
# > > 메인 함수에서 클래스 10개 생성
# > > 이미 생성되어 있는 변수공간 1개에, 할당되는 y값을 매번 덮어쓴다
#
# 2. 임의의 클래스 x 내부에 static 변수 y(클래스, 메소드, 변수 모두 포함)를 정의하면
#
# > > 클래스 x를 생성하지 않아도, y가 정의만 되어있다면, 클래스든, 메소드든, 변수든, y를 사용할 수 있다