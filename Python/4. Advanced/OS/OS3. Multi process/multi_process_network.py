# 멀티 프로세스 동기화
from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name

    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    q.put(sub_total)

    print(f"Process ID: {process_id}, Process Name: {process_name}")
    print(f"Result : {sub_total}")


def main():
    parent_process_id = os.getpid()
    print(f"Parent process ID {parent_process_id}")

    processes = []

    start_time = time.time()

    q = Queue()
    for i in range(5):
        t = Process(name=str(i), target=worker, args=(1, 100000000, q))
        processes.append(t)
        t.start()

    for process in processes:
        process.join()

    print("--- %s seconds ---" % (time.time() - start_time))
    q.put('exit')

    total = 0
    # 대기
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp

    print()
    print("Main-Processing Total_count={}".format(total))
    print("Main-Processing Done!")


if __name__ == "__main__":
    main()




# # 두 프로세스간의 통신
# import time
# from multiprocessing import Process, Pipe, current_process
# import os
#
#
# def worker(id, baseNum, conn):
#     process_id = os.getpid()
#     process_name = current_process().name
#
#     # 누적
#     sub_total = 0
#
#     # 계산
#     for _ in range(baseNum):
#         sub_total += 1
#
#     # Produce
#     conn.send(sub_total)
#     conn.close()
#
#     # 정보 출력
#     print(f"Process ID: {process_id}, Process Name: {process_name}")
#     print(f"Result : {sub_total}")
#
#
# def main():
#     parent_process_id = os.getpid()
#     print(f"Parent process ID {parent_process_id}")
#
#     start_time = time.time()
#
#     parent_conn, child_conn = Pipe()
#
#     t = Process(target=worker, args=(1, 100000000, child_conn))
#     t.start()
#     t.join()
#
#     print("--- %s seconds ---" % (time.time() - start_time))
#     print()
#     print("Main-Processing : {}".format(parent_conn.recv()))
#     print("Main-Processing Done!")
#
#
# if __name__ == "__main__":
#     main()
#
#