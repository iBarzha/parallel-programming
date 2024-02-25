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

class MyThread(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):
        is_prime_result = is_prime(self.x)
        if is_prime_result:
            print('%i is a prime number.' % self.x)

def single_thread(numbers):
    start_time = time.time()
    for num in numbers:
        is_prime(num)
    end_time = time.time()
    return end_time - start_time

def multi_thread(numbers):
    start_time = time.time()
    threads = []
    for num in numbers:
        thread = MyThread(num)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time

def compare_speeds():
    numbers_to_check = [50, 100, 500, 1000, 5000, 10000]
    single_thread_times = []
    multi_thread_times = []

    for num in numbers_to_check:
        numbers = range(2, num + 1)
        single_thread_time = single_thread(numbers)
        multi_thread_time = multi_thread(numbers)

        single_thread_times.append(single_thread_time)
        multi_thread_times.append(multi_thread_time)

    plt.plot(numbers_to_check, single_thread_times, label='Single Thread')
    plt.plot(numbers_to_check, multi_thread_times, label='Multi Thread')
    plt.xlabel('Number of integers to check')
    plt.ylabel('Time (s)')
    plt.title('Comparison of Single vs Multi Thread Performance')
    plt.legend()
    plt.show()

compare_speeds()
