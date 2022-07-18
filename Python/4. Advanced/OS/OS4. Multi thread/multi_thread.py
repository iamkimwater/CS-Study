import threading
import logging
import time
import random


def thread_func(name):
    # 이건 원래는 내부 작업을 다 조각내서 다른 쓰레드에게 일을 나누어 주어야 한다!!!!
    logging.info("나는 자식 쓰레드. 작업을 시작한다!")
    # 파스타 조리 시작
    time.sleep(random.randint(1, 2))
    print(name)
    time.sleep(random.randint(1, 2))
    # 파스타 조리 끝
    # 파스타의 조리 시간은 쓰레드마다 랜덤이다
    logging.info("나는 자식 쓰레드. 작업을 종료한다!")


def main():
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("나는 메인 쓰레드. 작업을 시작한다!")
    thread_pool = []
    for i in range(1, 10):
        child_thread = threading.Thread(target=thread_func, args=(str(i),), daemon=True)
        logging.info("나는 메인 쓰레드. 자식 쓰레드를 생성했다!")
        thread_pool.append(child_thread)

    # 데몬 체크!
    for child_thread in thread_pool:
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.start()
        child_thread.join()  # 자식 쓰레드가 종료되기를 메인쓰레드가 대기한다

    logging.info("나는 메인 쓰레드. 작업을 종료한다!")


if __name__ == "__main__":
    main()