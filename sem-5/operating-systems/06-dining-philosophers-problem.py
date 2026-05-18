# Practical 06: Dining Philosophers Problem
# Deadlock-free solution using semaphores for forks and a room semaphore

import sys
import threading
import time

N = 5  # Number of philosophers and forks

forks = [threading.Semaphore(1) for _ in range(N)]
room = threading.Semaphore(N - 1)  # At most N - 1 philosophers can sit at once to avoid deadlock

def safe_print(msg):
    sys.stdout.write(msg + "\n")

def philosopher(pid):
    left = pid
    right = (pid + 1) % N

    for round_num in range(1, 3):
        safe_print(f"Philosopher {pid} is thinking (Round {round_num})")
        time.sleep(0.04)

        room.acquire()             # Enter dining room
        forks[left].acquire()      # Pick up left fork
        forks[right].acquire()     # Pick up right fork

        safe_print(f"    Philosopher {pid} is eating using forks {left} and {right}")
        time.sleep(0.06)

        forks[right].release()     # Put down right fork
        forks[left].release()      # Put down left fork
        room.release()             # Leave dining room

        safe_print(f"Philosopher {pid} finished eating and put down forks")

def main():
    print("=" * 60)
    print("       DINING PHILOSOPHERS PROBLEM (5 Philosophers)")
    print("=" * 60)

    threads = []
    for i in range(N):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nAll philosophers finished thinking and eating without deadlock.")
    print("=" * 60)

if __name__ == "__main__":
    main()
