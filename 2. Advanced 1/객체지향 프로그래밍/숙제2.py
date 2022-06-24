# Basic편 기말퀴즈 보강
from user import Influencer, Advertiser

# 정의파트
def sign_up():
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")
    user_nickname = input("닉네임을 입력하세요: ")
    user_type = input("사용자의 소속을 선택하세요: 일반 유저(0) vs 회사(1): ")

    user_file_writer = open("users.txt", "a", encoding="utf8")
    user_file_writer.write(user_id + " " + user_password + " " + user_nickname + " " + user_type + "\n")
    user_file_writer.close()

def login():
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")

    me = None

    user_file_reader = open("users.txt", "r", encoding="utf8")

    while True:
        user_data = user_file_reader.readline()
        if user_data == '':
            break

        user_data = user_data.strip().split(" ")
        if user_id != user_data[0]:
            print("아이디 또는 비밀번호가 일치하지 않습니다")
            continue
        else:
            # 인플루언서인지 광고주인지 구분해서 객체를 생성
            me = User(user_data[0], user_data[1], user_data[2], user_data[3])
            break

    return me



if __name__ == "__main__":
    me = None

    while True:
        if me == None:
            choice = int(input("로그인(0) / 회원가입(1): "))
            if choice == 0:
                sign_up()
            else:
                me = login()
        else:
            menu = input(f"{me.get_user_id()}님 환영합니다\n메뉴를 선택하세요\n")
            if menu == 0:
                pass
            else:
                me = None



            # if me is not None:
            #     print(me)
            #     input("메인화면입니다")
            # else:
            #     choice = int(input("로그인(0) / 회원가입(1): "))
            #     if choice == 0:
            #         email = input("이메일을 입력하세요: ")
            #         password = input("비밀번호를 입력하세요: ")
            #         me = login(email, password)
            #         if me is None:
            #             print("일치하는 이메일 또는 비밀번호가 없습니다")
            #     elif choice == 1:
            #         email = input("이메일을 입력하세요: ")
            #         password = input("비밀번호를 입력하세요: ")
            #         user_id = input("아이디를 입력하세요: ")
            #         sign_up(email, password, user_id)
        # except Exception as e:
        #     print(e)