# 정의파트

def sign_up(email, password, user_id):
    file = open("users.txt", "a", encoding="utf8")
    # file.write(f"{email}, {password}, {user_id}\n")
    # 콜론 뒤에 스페이스바로 간격을 둬서 로그인 시 비밀번호 앞에 스페이스바로 간격을 주지 않으면 로그인에 실패하는 상황 발생
    file.write(f"{email},{password},{user_id}\n")
    file.close()

def login(email, password):
    file = open("users.txt", "r", encoding="utf8")
    lines = file.readlines()
    me = None
    for line in lines:
        line = line.split(',')
        if email == line[0] and password == line[1]:
            me = {"email": line[0], "user_id": line[2].strip()}   # strip: 공백제거
            break
    file.close()

    return me



if __name__ == "__main__":
    me = None

    while True:
        try:
            if me is not None:
                print(me)
                input("메인화면입니다")
            else:
                choice = int(input("로그인(0) / 회원가입(1): "))
                if choice == 0:
                    email = input("이메일을 입력하세요: ")
                    password = input("비밀번호를 입력하세요: ")
                    me = login(email, password)
                    if me is None:
                        print("일치하는 이메일 또는 비밀번호가 없습니다")
                elif choice == 1:
                    email = input("이메일을 입력하세요: ")
                    password = input("비밀번호를 입력하세요: ")
                    user_id = input("아이디를 입력하세요: ")
                    sign_up(email, password, user_id)
        except Exception as e:
            print(e)