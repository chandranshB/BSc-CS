# Practical 04: Process Synchronization - Producer-Consumer Problem
# Classical synchronization using semaphores (empty, full, mutex) and bounded buffer

import sys
import threading
import time

BUFFER_SIZE = 5
TOTAL_ITEMS = 8

buffer = [0] * BUFFER_SIZE
in_idx = 0
out_idx = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)

def safe_print(msg):
    sys.stdout.write(msg + "\n")

def producer():
    global in_idx
    for item in range(1, TOTAL_ITEMS + 1):
        empty.acquire()
        mutex.acquire()

        buffer[in_idx] = item
        safe_print(f"[Producer] Produced item {item} at buffer slot {in_idx}")
        in_idx = (in_idx + 1) % BUFFER_SIZE

        mutex.release()
        full.release()
        time.sleep(0.05)

def consumer():
    global out_idx
    for _ in range(TOTAL_ITEMS):
        full.acquire()
        mutex.acquire()

        item = buffer[out_idx]
        safe_print(f"    [Consumer] Consumed item {item} from buffer slot {out_idx}")
        out_idx = (out_idx + 1) % BUFFER_SIZE

        mutex.release()
        empty.release()
        time.sleep(0.08)

def main():
    print("=" * 60)
    print("  PRODUCER-CONSUMER PROBLEM USING SEMAPHORES")
    print("=" * 60)
    print(f"Buffer Capacity = {BUFFER_SIZE}, Total Items = {TOTAL_ITEMS}\n")

    t_prod = threading.Thread(target=producer)
    t_cons = threading.Thread(target=consumer)

    t_prod.start()
    t_cons.start()

    t_prod.join()
    t_cons.join()

    print("\nAll items produced and consumed successfully.")
    print("=" * 60)

if __name__ == "__main__":
    main()
