# ch6/example4.py

from multiprocessing import Process, current_process
import time


def f1():
    p = current_process()
    print('Starting process %s, ID %s...' % (p.name, p.pid))
    time.sleep(4)
    print('Exiting process %s, ID %s...' % (p.name, p.pid))

def f2():
    p = current_process()
    print('Starting process %s, ID %s...' % (p.name, p.pid))
    time.sleep(2)
    print('Exiting process %s, ID %s...' % (p.name, p.pid))


if __name__ == '__main__':
    p1 = Process(name='Worker 1', target=f1)
    print('p1 created.')   
    p1.daemon = True
    p2 = Process(name='Worker 2', target=f2)
    print('p2 created.')   

    p1.start()
    print('p1 started.')
    time.sleep(1)
    p2.start()
    print('p2 started.')   

    print('Main Done.')

# Коли процес оголошений як демон, закінчується основний процес,
# то він автоматично припиняє свою роботу без чекання завершення роботи інших процесів (не демонів).
# Таким чином, процеси, що є демонами, можуть бути припинені до завершення своєї роботи.