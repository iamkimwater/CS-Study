import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))

    return result


def main():
    numbers = [3000000 + x for x in range(3)]

    start_time = time.time()
    total = find_sums(numbers)
    print(f"Total: {total}")
    duration = time.time() - start_time
    print(f"Duration: {duration}")


if __name__ == "__main__":
    main()