import time
from multiprocessing import Queue, Pipe, Process
from concurrent.futures import ProcessPoolExecutor
from codecs import encode

def process_A(main_a_queue: Queue, a_b_queue: Queue):
    while True:
        txt = main_a_queue.get()
        a_b_queue.put(txt.lower())
        time.sleep(5)

def process_B(a_b_queue: Queue, b_main_queue: Queue):
    while True:
        txt = a_b_queue.get()
        txt = encode(txt, 'rot_13')
        print("Process B has text (with rot13):", txt,  "at", time.time(), flush=True)
        b_main_queue.put(txt)

if __name__ == "__main__":
    main_a_queue = Queue()
    a_b_queue = Queue()
    b_main_queue = Queue()

    process_a = Process(target=process_A, args=(main_a_queue, a_b_queue))
    process_b = Process(target=process_B, args=(a_b_queue, b_main_queue))
    process_a.start()
    process_b.start()

    while True:
        txt = input()
        print("You send msg (\"" + txt + "\") at " + str(time.time()))
        if txt == "exit":
            process_a.terminate()
            process_b.terminate()
            break
        else:
            main_a_queue.put(txt)

