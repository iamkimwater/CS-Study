# 프로그래밍 환경 초급편
# 파이썬 파이참 컴파일러 인터프리터 가상환경 pip jupyter
# pip install jupyter
# jupyter notebook

# 데이터 초급편
# 데이터의 자료형(문자, 숫자, 참거짓=불린)
# 변수 연산자(=, ==, !=, 사칙연산)
# 콘솔 gui print 문자열 포멧팅 형변환

# name = "령은"
# age = 21
# is_student = True
# print(f"내 이름은 {name}입니다")
# print(str(age))

# 사전(키 - 값, 키는 무조건 문자열!)
user1 = {"name": "하하맨", "age": 20, "is_student": True}
user2 = {"name": "하하걸", "age": 21, "is_student": True}
user3 = {"name": "호호맨", "age": 22, "is_student": True}
user4 = {"name": "호호걸", "age": 23, "is_student": True}
user5 = {"name": "후후맨", "age": 24, "is_student": False}
user6 = {"name": "후후걸", "age": 25, "is_student": False}

# print(f"내 이름은 {user1['name']}입니다.")

# 배열 [] 인덱스(실제길이 - 1) 조회 변경 추가 삭제
# 튜플 () 조회
# 셋 순서가없다 합집합 차집합 교집합 여집합

users = []
users.append(user1)
users.append(user2)
users.append(user3)
users.append(user4)
users.append(user5)
users.append(user6)
# users[0] = user6

# print(users[0]["name"])
# print(f"내 이름은 {users[0]['name']}입니다.")
# print(f"나이는 {users[0]['age']}입니다.")
# print(f"저는 학생 {users[0]['is_student']}입니다.")

# 함수 초급편

def show_user_info(users, index):
    print(f"내 이름은 {users[index]['name']}입니다.")
    print(f"나이는 {users[index]['age']}입니다.")
    if users[index]["is_student"] == True:
        print(f"{users[index]['name']}은 학생입니다")
    else:
        print(f"{users[index]['name']}은 졸업생입니다")

# for 반복문
# def show_user_info(user):
#     print(f"내 이름은 {user['name']}입니다.")
#     print(f"나이는 {user['age']}입니다.")
#     if user["is_student"] == True:
#         print(f"{user['name']}은 학생입니다")
#     else:
#         print(f"{user['name']}은 졸업생입니다")

if __name__ == "__main__":
    # show_user_info(users, 0)
    # show_user_info(users, 1)
    # show_user_info(users, 2)
    # show_user_info(users, 3)
    # show_user_info(users, 4)
    # show_user_info(users, 5)

    # 제어 초급편
    # 조건문
    # if users[0]["is_student"] == True:
    #     print(f"{users[0]['name']}은 학생입니다")
    # else:
    #     print(f"{users[0]['name']}은 졸업생입니다")

    # while 반복문 flag
    # while 조건:
    #     반복중
    #
    # 이제 드디어 내 차례

    index = 0
    while index <= 5:
        show_user_info(users, index)
        index += 1
    print("드디어 끝")

    index = 0
    while True:
        show_user_info(users, index)
        index += 1
        # 음...
        if index > 5:
            break
    print("드디어 끝")

    # for user in users:
    #     show_user_info(user)