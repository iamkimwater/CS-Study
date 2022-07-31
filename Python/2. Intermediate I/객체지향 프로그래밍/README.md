# **Python Intermediate I - 객체지향 프로그래밍 (Object-Oriented Programming)**

## **1. 개념**

### **클래스, 객체, 인스턴스**
* 클래스 (class) : 객체를 만들기 위한 설계도
* 객체 (object) : 
* 인스턴스 (instance) : 어떤 클래스의 객체인가 (관계 중심 정의)
```python
class mobile_phone:   # 클래스 : mobile_phone
    def on(self):
        print("전원을 켭니다.")

galaxy = mobile_phone()
galaxy.on()

# galaxy 는 객체
# galaxy 객체는 mobile_phone 클래스의 인스턴스
```

### **class 구성 요소**
* 인스턴스 변수 (class에 정의된 변수, 데이터)

* 메소드 (데이터를 관리할 함수)
	- 매직메소드 : `__메소드명__`
		- 특정 상황에서 자동 실행
		- .




```python
class User():
	# 인스턴스 변수 : users_id, users_password, is_solo
	# 매직메소드 : __init__
	def __init__(self):
		self.user_id = "Kimwater"
		self.user_password = 1234
		self.is_solo = True

user1 = User()
user2 = User()
user3 = User()
```

```python
# 매직메소드 실행 예시
class User():
	def __init__(self):
		print("나는야 매직메소드! 저절로 실행됩니다.")

user1 = User()
user2 = User()
user3 = User()

# 실행결과
나는야 매직메소드! 저절로 실행됩니다.
나는야 매직메소드! 저절로 실행됩니다.
나는야 매직메소드! 저절로 실행됩니다.

# user1 = User().__init__()
# 이렇게 뒤에 메소드 붙이지 않아도 실행됨
```

```python
# self : 클래스 내부 모든 메소드의 첫 번째 파라미터
# 클래스를 의미하는 것이 아니라 user 자신을 의미 (user1, user2, ...)
```

