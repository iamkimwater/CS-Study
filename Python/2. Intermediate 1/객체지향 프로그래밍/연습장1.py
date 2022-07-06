class User():
    # 매직메소드
    def __init__(self, user_id, user_password):
        # 인스턴스변수(일괄적으로 __처리)
        self.__user_id = user_id
        self.__user_password = user_password

    # 인스턴스메소드(필요할 때 변수에 접근)
    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    # def get_user_password(self):
    #     return self.__user_password

    def set_user_password(self, original_password, new_user_password):
        if self.__user_password == original_password:
            self.__user_password = new_user_password
        else:
            print("기존 비밀번호가 틀렸습니다")



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
