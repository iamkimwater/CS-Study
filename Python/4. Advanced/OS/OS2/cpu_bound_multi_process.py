from multiprocessing import current_process, Array, freeze_support, Process, Manager
import time
import os


def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    # print(f"Process ID: {process_id}, Process Name: {process_name}")
    total_list.append(sum(i * i for i in range(number)))


def main():
    # 이런거 하지 마셈...
    numbers = [3000000 + x for x in range(3)]

    processes = []

    # 멀티 프로세스 데이터 공유 방법
    manager = Manager()
    total_list = manager.list()

    # 일을 분할
    for i in numbers:
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list,))
        processes.append(t)

    start_time = time.time()
    for process in processes:
        process.start()
        process.join()

    print(f"Total list : {total_list}")
    duration = time.time() - start_time
    print(f"Duration : {duration} seconds")


if __name__ == "__main__":
    main()