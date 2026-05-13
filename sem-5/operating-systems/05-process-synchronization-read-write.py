# Practical 05: Process Synchronization - Readers-Writers Problem
# Classical synchronization prioritizing multiple concurrent readers and exclusive writers

import sys
import threading
import time

mutex = threading.Semaphore(1)   # Protects read_count
wrt = threading.Semaphore(1)     # Exclusive access for writing
read_count = 0
shared_resource = 0

def safe_print(msg):
    sys.stdout.write(msg + "\n")

def reader(reader_id):
    global read_count
    for _ in range(2):
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            wrt.acquire()  # First reader locks out writers
        mutex.release()

        safe_print(f"[Reader {reader_id}] Reading shared_resource = {shared_resource} (Active readers: {read_count})")
        time.sleep(0.05)

        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            wrt.release()  # Last reader unlocks for writers
        mutex.release()
        time.sleep(0.05)

def writer(writer_id):
    global shared_resource
    for _ in range(2):
        wrt.acquire()  # Exclusive write access
        shared_resource += 10
        safe_print(f"    [Writer {writer_id}] Updated shared_resource to {shared_resource}")
        time.sleep(0.08)
        wrt.release()
        time.sleep(0.05)

def main():
    print("=" * 60)
    print("     READERS-WRITERS PROBLEM USING SEMAPHORES")
    print("=" * 60)

    threads = []
    # Create 3 readers and 2 writers
    threads.append(threading.Thread(target=reader, args=(1,)))
    threads.append(threading.Thread(target=writer, args=(1,)))
    threads.append(threading.Thread(target=reader, args=(2,)))
    threads.append(threading.Thread(target=writer, args=(2,)))
    threads.append(threading.Thread(target=reader, args=(3,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("\nAll readers and writers finished execution.")
    print("=" * 60)

if __name__ == "__main__":
    main()
