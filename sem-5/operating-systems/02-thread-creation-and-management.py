# Practical 02: Thread Creation and Management
# Computes partial sum of an array using multiple threads and joins them

import sys
import threading

NUM_THREADS = 4

def safe_print(msg):
    sys.stdout.write(msg + "\n")

class PartialSum:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0

def compute_sum(p):
    p.sum = sum(range(p.start, p.end))
    thread_id = threading.get_ident() % 100000
    safe_print(f"Thread {thread_id}: sum[{p.start}..{p.end}) = {p.sum}")

def main():
    n = 1000000
    chunk = n // NUM_THREADS
    threads = []
    data = []

    print("=" * 60)
    print("       THREAD CREATION AND MANAGEMENT")
    print("=" * 60)
    print(f"Calculating sum from 0 to {n - 1} using {NUM_THREADS} threads:\n")

    for i in range(NUM_THREADS):
        start = i * chunk
        end = n if i == NUM_THREADS - 1 else (i + 1) * chunk
        item = PartialSum(start, end)
        data.append(item)
        t = threading.Thread(target=compute_sum, args=(item,))
        threads.append(t)
        t.start()

    total_sum = 0
    for i in range(NUM_THREADS):
        threads[i].join()
        total_sum += data[i].sum

    print("\nAll threads joined.")
    print(f"Total computed sum: {total_sum}")
    print("=" * 60)

if __name__ == "__main__":
    main()
