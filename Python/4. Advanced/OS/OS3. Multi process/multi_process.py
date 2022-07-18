from multiprocessing import Process
import logging
import time
import os
import random


def process_func(name):
    logging.info("나는 자식 프로세스. 작업을 시작한다!")
    # 여기서 데코 준비
    print("초밥 데코를 준비하자...")

    # 초밥 사러 출발 => 제어권 컨트롤 필수
    time.sleep(random.randint(1, 2))
    print(name)
    time.sleep(random.randint(1, 2))
    # 초밥 사옴
    # 초밥 사오는 시간은 프로세스마다 랜덤이다

    # 여기서부터 데코레이션 완료하자 => 초밥 오면 할 부분 => 콜백함수
    print("초밥 데코 끝")
    logging.info("나는 자식 프로세스. 작업을 종료한다!")


def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("나는 메인 프로세스. 작업을 시작한다!")
    parent_process_id = os.getpid()
    processes = []
    for i in range(1, 10):
        child_process = Process(name=str(i), target=process_func, args=(i,))
        processes.append(child_process)
        logging.info("나는 메인 프로세스. 자식 프로세스를 생성했다!")

    for child_process in processes:
        child_process.start()
        child_process.start()
        child_process.start()
        child_process.start()
        child_process.start()
        child_process.start()
        child_process.join()  # 자식 프로세스가 종료되기를 메인쓰레드가 대기한다

    logging.info("나는 메인 프로세스. 작업을 종료한다!")


if __name__ == '__main__':
    main()