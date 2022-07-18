from concurrent.futures import ProcessPoolExecutor
from multiprocessing import current_process, Value
import os


class DataStore:
    def __init__(self):
        self.value = Value('i', 0)

    def increase_value(self):
        self.value.value += 1
        print(current_process().name, self.value.value)

    def decrease_value(self):
        self.value.value -= 1
        print(current_process().name, self.value.value)


def main():
    parent_process_id = os.getpid()
    print(f"메인 프로세스 아이디: {parent_process_id}")

    store = DataStore()
    print(store.value.value)
    with ProcessPoolExecutor(max_workers=5) as executor:
        for _ in range(100):
            try:
                executor.submit(store.increase_value)
                executor.submit(store.decrease_value)
            except Exception as e:
                print(e)
    print(store.value.value)


if __name__ == '__main__':
    main()