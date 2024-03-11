import multiprocessing


class ReductionConsumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        pname = self.name
        print('Using process %s...' % pname)
        while True:
            num1 = self.queue.get()

            if num1 is None:
                print('Exiting process %s.' % pname)
                break

            num2 = self.queue.get()
            if num2 is None:
                print('Reaching the end with process %s and number %i.' % (pname, num1))
                self.queue.put(num1)
                break

            print('Running process %s on numbers %i and %i.' % (pname, num1, num2))
            self.queue.put(num1 + num2)


def reduce_sum(array):
    tasks = multiprocessing.Queue()
    result_size = len(array)
    n_consumers = multiprocessing.cpu_count()

    for item in array:
        tasks.put(item)

    consumers = [ReductionConsumer(tasks) for _ in range(n_consumers)]
    for consumer in consumers:
        consumer.start()

    for consumer in consumers:
        tasks.put(None)

    for consumer in consumers:
        consumer.join()

    return tasks.get()


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = reduce_sum(array)
    print("Final result:", result)
