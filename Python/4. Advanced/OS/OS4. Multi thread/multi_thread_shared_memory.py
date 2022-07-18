from concurrent.futures import ThreadPoolExecutor
import threading


class DataStore:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increase_value(self):
        self.lock.acquire()
        self.value = self.value + 1
        self.lock.release()

    def decrease_value(self):
        self.lock.acquire()
        self.value = self.value - 1
        self.lock.release()


def main():
    store = DataStore()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(100):
            try:
                executor.submit(store.increase_value)
                executor.submit(store.decrease_value)
            except Exception as e:
                print(e)
    print(store.value)


if __name__ == "__main__":
    main()