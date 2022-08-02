"""
# 매직메소드
class User():
	def __init__(self):
		print("나는야 매직메소드! 저절로 실행됩니다.")

user1 = User()
user2 = User()
user3 = User()
"""


"""
# 파라미터값 추가하지 않을 경우 각 객체의 실행결과 모두 같게 나옴
class User():
	def __init__(self):
		self.user_id = "Kimwater"
		self.user_password = 1234
		self.is_solo = True

user1 = User()
user2 = User()
user3 = User()

print(user1.user_id)
print(user2.user_id)
print(user3.user_id)
"""


"""
# user1, user2, user3 정보 출력
class User():
	def __init__(self, user_id, user_password, is_solo):
		self.user_id = user_id
		self.user_password = user_password
		self.is_solo = is_solo

user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("Parkwater", 1234, True)

print(user1.user_id)
print(user2.user_id)
print(user3.user_id)

print(user1.user_password)
print(user2.user_password)
print(user3.user_password)

print(user1.is_solo)
print(user2.is_solo)
print(user3.is_solo)
"""


"""
# user1 데이터 변경
class User():
	# 인스턴스변수 정의
	def __init__(self, user_id, user_password, is_solo):
		self.user_id = user_id
		self.user_password = user_password
		self.is_solo = is_solo

	# 인스턴스메소드 정의
	def set_user_id(self, new_user_id):   # 보통 change 대신 set 사용
		self.user_id = new_user_id
	def set_user_password(self, new_user_password):
		self.user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.is_solo = new_is_solo

user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("Parkwater", 1234, True)

# 데이터 변경 메소드 적용
user1.set_user_id("Seowater")
user1.set_user_password(4321)
user1.set_is_solo(False)

print(user1.user_id)
print(user2.user_id)
print(user3.user_id)

print(user1.user_password)
print(user2.user_password)
print(user3.user_password)

print(user1.is_solo)
print(user2.is_solo)
print(user3.is_solo)
"""


"""
# 외부에서 user 정보를 볼 수 없게 변수들 앞에 언더바 2개 붙이기
class User():
	# 인스턴스변수 정의
	def __init__(self, user_id, user_password, is_solo):
		self.__user_id = user_id
		self.__user_password = user_password
		self.__is_solo = is_solo

	# 인스턴스메소드 정의 (변경 : set)
	def set_user_id(self, new_user_id):
		self.__user_id = new_user_id
	def set_user_password(self, new_user_password):
		self.__user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.__is_solo = new_is_solo

# 객체 생성
user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("Parkwater", 1234, True)

# 변경 메소드 적용
user1.set_user_id("Seowater")
user1.set_user_password(4321)
user1.set_is_solo(False)

# user1 정보 출력
print(user1.__user_id)
print(user1.__user_password)
print(user1.__is_solo)
# user2 정보 출력
print(user2.__user_id)
print(user2.__user_password)
print(user2.__is_solo)
# user3 정보 출력
print(user3.__user_id)
print(user3.__user_password)
print(user3.__is_solo)

# 실행결과 : User 객체에는 __user_id 속성이 없다고 거짓말을 해줌
# AttributeError: 'User' object has no attribute '__user_id'
# id, password 등을 볼 수 없게 됨
# password는 그렇다 쳐도 id는 봐야할 거 아님?
"""


"""
# 숨겼던 id 볼 수 있게 get 메소드 생성
class User():
	# 인스턴스변수 정의
	def __init__(self, user_id, user_password, is_solo):
		self.__user_id = user_id
		self.__user_password = user_password
		self.__is_solo = is_solo

	# 인스턴스메소드 정의 (변경 : set)
	def set_user_id(self, new_user_id):
		self.__user_id = new_user_id
	def set_user_password(self, new_user_password):
		self.__user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.__is_solo = new_is_solo

	# 인스턴스메소드 정의 (보여주기 : get)
	def get_user_id(self):
		return self.__user_id

# 객체 생성
user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("Parkwater", 1234, True)

# 변경 메소드 적용
user3.set_user_id("Seowater")
user3.set_user_password(4321)
user3.set_is_solo(False)

# 숨겼던 id 보여주기
print(user1.get_user_id())
print(user2.get_user_id())
print(user3.get_user_id())

# # user1 정보 출력
# print(user1.__user_id)
# print(user1.__user_password)
# print(user1.__is_solo)
# # user2 정보 출력
# print(user2.__user_id)
# print(user2.__user_password)
# print(user2.__is_solo)
# # user3 정보 출력
# print(user3.__user_id)
# print(user3.__user_password)
# print(user3.__is_solo)
"""


"""
# 다시 보여줄 거면 굳이 왜 숨겼지? -> set으로 인해 get이 생겨날 수 밖에
# 내부 정보는 함부로 변경되면 안되니 __ 로 보호해두고, 변경시 제한 조건을 걸어두었는데(set), 볼 수는 있어야하니 get 함수 추가
class User():
	# 인스턴스변수 정의
	def __init__(self, user_id, user_password, is_solo):
		self.__user_id = user_id
		self.__user_password = user_password
		self.__is_solo = is_solo

	# 인스턴스메소드 정의 (변경 : set)
	def set_user_id(self, original_id, new_user_id):
		if self.__user_id != original_id:
			print("기존 아이디와 일치하지 않습니다.")
			return
		else:
			self.__user_id = new_user_id
	def set_user_password(self, original_password, new_user_password):
		if self.__user_password != original_password:
			print("기존 비밀번호와 일치하지 않습니다.")
			return
		else:
			self.__user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.__is_solo = new_is_solo

	# 인스턴스메소드 정의 (보여주기 : get)
	def get_user_id(self):
		return self.__user_id
	def get_user_password(self):
		return self.__user_password
	def get_is_solo(self):
		return self.__is_solo

# 객체 생성
user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("Parkwater", 1234, True)

# 변경 메소드 적용
user3.set_user_id("Parkwater", "Seowater")
user3.set_user_password(0, 4321)
user3.set_is_solo(False)

# 숨겼던 정보 보여주기
print(user1.get_user_id())
print(user1.get_user_password())
print(user1.get_is_solo())

print(user2.get_user_id())
print(user2.get_user_password())
print(user2.get_is_solo())

print(user3.get_user_id())
print(user3.get_user_password())
print(user3.get_is_solo())
"""

