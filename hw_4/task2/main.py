import math
import time
from os import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from integrate import integrate


def start_thread(n_jobs):
    start = time.time()
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor=executor)
    return time.time() - start

def start_process(n_jobs):
    start = time.time()
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor=executor)
    return time.time() - start


if __name__ == "__main__":
    for i in range(1, 2 * cpu_count() + 1):
        print("For cpu = " + str(i))
        print("--process = " + str(start_process(i)))
        print("--threads = " + str(start_thread(i)))

