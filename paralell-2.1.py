import threading
from math import sqrt
import time
import matplotlib.pyplot as plt


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                return False
        return True


def single_threaded_performance(input_data):
    start_time = time.time()
    for x in input_data:
        if is_prime(x):
            print('%i is a prime number.' % x)
    end_time = time.time()
    return end_time - start_time


def multi_threaded_performance(input_data):
    start_time = time.time()
    threads = []
    for x in input_data:
        t = threading.Thread(target=is_prime, args=(x,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    return end_time - start_time


def main():
    input_sizes = [50, 100, 500, 1000, 5000, 10000]
    single_thread_times = []
    multi_thread_times = []

    for size in input_sizes:
        input_data = list(range(2, size + 2))

        single_thread_time = single_threaded_performance(input_data)
        single_thread_times.append(single_thread_time)

        multi_thread_time = multi_threaded_performance(input_data)
        multi_thread_times.append(multi_thread_time)

    plt.plot(input_sizes, single_thread_times, label='Single Thread')
    plt.plot(input_sizes, multi_thread_times, label='Multi Thread')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Performance Comparison')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
