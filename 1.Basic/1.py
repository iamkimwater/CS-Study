# 정의파트

if __name__ == "__main__":
    # 실행파트
    # 꺼지지 않는 프로그램
    while True:
        try:
            # 실행
            choice = int(input("로그인(0) / 회원가입(1): "))
            if choice == 0:
                pass
            elif choice == 1:
                email = input("이메일을 입력하세요: ")
                password = input("비밀번호를 입력하세요: ")
                user_id = input("아이디를 입력하세요: ")
                file = open("users.txt", "a", encoding="utf8")
                file.write("email, password, ")
        except Exception as e:
            # 에러를 에러가 아니게 처리해줌
            print(e)