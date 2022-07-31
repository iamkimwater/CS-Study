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
user3 = User("ParkWater", 1234, True)

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
	def __init__(self, user_id, user_password, is_solo):
		self.user_id = user_id
		self.user_password = user_password
		self.is_solo = is_solo

	# 데이터 변경 함수 정의
	def set_user_id(self, new_user_id):   # 보통 change 대신 set 사용
		self.user_id = new_user_id
	def set_user_password(self, new_user_password):
		self.user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.is_solo = new_is_solo

user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("ParkWater", 1234, True)

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

# 외부에서 user 정보를 볼 수 없게 변수들 앞에 언더바 2개 붙이기
class User():
	def __init__(self, user_id, user_password, is_solo):
		self.__user_id = user_id
		self.__user_password = user_password
		self.__is_solo = is_solo

	def set_user_id(self, new_user_id):
		self.__user_id = new_user_id
	def set_user_password(self, new_user_password):
		self.__user_password = new_user_password
	def set_is_solo(self, new_is_solo):
		self.__is_solo = new_is_solo

user1 = User("Kimwater", 1234, True)
user2 = User("Leewater", 1234, False)
user3 = User("ParkWater", 1234, True)

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