# 정의파트
def sign_up() :
    # 변수 선언 (id, password, nickname, type)
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")
    user_nickname = input("닉네임을 입력하세요: ")
    user_type = input("일반유저(0)입니까 vs 회사(1)입니까?: ")

    user_file_write = open("users.txt", "a", encoding="utf8")
    user_file_write.write(user_id + " " + user_password + " " + user_nickname + " " + user_type + "\n")
    user_file_write.close()

def login():
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")



# 실행파트