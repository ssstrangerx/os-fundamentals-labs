import threading
import time
from collections import defaultdict


TOTAL = 0
COUNTER_LOCK = threading.Lock()


def worker(thread_id: int, iterations: int = 100000) -> None:
    global TOTAL
    for _ in range(iterations):
        with COUNTER_LOCK:
            TOTAL += 1


def run_thread_demo() -> None:
    threads = []
    for i in range(8):
        t = threading.Thread(target=worker, args=(i, 100000))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Final counter value after synchronized threads: {TOTAL}")


if __name__ == "__main__":
    run_thread_demo()
