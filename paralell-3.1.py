import threading
import requests
import time
import random

def ping(url):
    res = requests.get(url)
    print(f'{url}: {res.status_code}')

def run_sequential_block(urls):
    start = time.time()
    for url in urls:
        ping(url)
    print(f'Sequential block took {time.time() - start : .2f} seconds')

def run_parallel_block(urls):
    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=ping, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Parallel block took {time.time() - start : .2f} seconds')

def main():
    supported_codes = [
        '100', '101', '102', '103', '200', '201', '202', '203', '204', '205', '206', '207', '208', '226', '300',
        '301', '302', '303', '304', '305', '306', '307', '308', '400', '401', '402', '403', '404', '405', '406',
        '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '418', '421', '422', '423',
        '424', '425', '426', '428', '429', '431', '451', '500', '501', '502', '503', '504', '505', '506', '507',
        '508', '510', '511', '419', '420', '440', '444', '449', '450', '460', '463', '494', '495', '496', '497',
        '498', '499', '520', '521', '522', '523', '524', '525', '526', '527', '530', '561'
    ]

    for _ in range(4):
        print("Running block:")
        selected_codes = random.sample(supported_codes, 10)
        urls = [f'http://httpstat.us/{code}' for code in selected_codes]

        run_sequential_block(urls)
        run_parallel_block(urls)

if __name__ == "__main__":
    main()

