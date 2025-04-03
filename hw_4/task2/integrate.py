from concurrent.futures import Executor

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor: Executor = None):
    if not (executor is None):
        n_iter_new = n_iter // n_jobs
        step = (b - a) / n_jobs
        works = [
            executor.submit(integrate, f, a + i * step, a + (i + 1) * step, n_jobs=1, n_iter=n_iter_new)
            for i in range(n_jobs)
        ]
        return sum([i.result() for i in works])
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc