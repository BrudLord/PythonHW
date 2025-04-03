from multiprocessing import Process
from threading import Thread
import time
import sys

def fib(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def test_sync(times, n):
    start = time.time()
    for i in range(times):
        fib(n)
    return time.time() - start

def test_processes(times, n):
    processes = []
    for i in range(times):
        processes.append(Process(target=fib, args=(n,)))
    start = time.time()
    for i in range(times):
        processes[i].start()
    for i in range(times):
        processes[i].join()
    return time.time() - start

def test_threads(times, n):
    threads = []
    for i in range(times):
        threads.append(Thread(target=fib, args=(n,)))
    start = time.time()
    for i in range(times):
        threads[i].start()
    for i in range(times):
        threads[i].join()
    return time.time() - start


if __name__ == '__main__':
    sys.setrecursionlimit(250)
    print("sync_time:", test_sync(10, 30))
    print("process_time:", test_processes(10, 30))
    print("thread_time:", test_threads(10, 30))