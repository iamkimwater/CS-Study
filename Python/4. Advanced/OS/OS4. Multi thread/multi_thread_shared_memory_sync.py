"""
Python Event 객체
Flag 초기값(0)
Set() -> 1
Clear() -> 0
Wait(1 -> 리턴, 0 -> 대기)
isSet() -> 현 플래그 상태 리턴
"""
# 쓰레드를 활용한 협업
import concurrent.futures
import logging
import queue
import random
import threading
import time


# 생산자 = 서버로 이해
def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


# 소비자 = 클라이언트로 이해
def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()  # 초기 플래그 값은 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.1)
        logging.info("Main: about to set event")
        # 프로그램 종료
        event.set()