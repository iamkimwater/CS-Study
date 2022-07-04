# 모듈 패키지 from import * 정의파트 실행파트 __name__ __main__ __init__.py 예외처리
from python1 import users, show_user_info
import random

# 정의파트


# 실행파트

# 중간퀴즈
# 6명의 사람에 대한 정보를 가진 배열 users가 있다
# 이 중에서 3명의 사람을 랜덤으로 선택한다
# 3명의 정보를 출력

if __name__ == "__main__":
    i = 0
    random_list = []
    while i < 3:
        random_index = random.randint(0, 5)
        # 음... 잠깐...
        # 이 사람이 처음 뽑힌 사람인가?
        # 맞아! => 배열에 추가
        if random_index not in random_list:
            random_list.append(random_index)
            i += 1
        # 아닌데? 이미 뽑았는데? => 다시 뽑으러 돌아가기
        # else:
        #     # 아무 일도 하지 않고 다시 반복합시다
        #     continue

    for random_index in random_list:
        show_user_info(users, random_index)

    # random.sample(users, 3) 사용은 어떻게 하는걸까?