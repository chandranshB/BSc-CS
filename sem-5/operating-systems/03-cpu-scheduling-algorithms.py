# Practical 03: CPU Scheduling Algorithms
# Implements FCFS, SJF, Priority, and Round Robin scheduling algorithms

from collections import deque

class Process:
    def __init__(self, pid, at, bt, pr=0):
        self.pid = pid
        self.at = at      # Arrival Time
        self.bt = bt      # Burst Time
        self.pr = pr      # Priority (lower number = higher priority)
        self.ct = 0       # Completion Time
        self.tat = 0      # Turnaround Time (CT - AT)
        self.wt = 0       # Waiting Time (TAT - BT)
        self.rem = bt     # Remaining Burst Time

def print_table(title, procs):
    n = len(procs)
    total_wt = sum(p.wt for p in procs)
    total_tat = sum(p.tat for p in procs)

    print(f"\n--- {title} ---")
    print(f"{'PID':<6}{'AT':<6}{'BT':<6}{'PR':<6}{'CT':<6}{'TAT':<6}{'WT':<6}")
    print("-" * 42)
    for p in sorted(procs, key=lambda x: x.pid):
        print(f"P{p.pid:<5}{p.at:<6}{p.bt:<6}{p.pr:<6}{p.ct:<6}{p.tat:<6}{p.wt:<6}")
    print("-" * 42)
    print(f"Average Turnaround Time = {total_tat / n:.2f}")
    print(f"Average Waiting Time    = {total_wt / n:.2f}")

def reset(procs):
    for p in procs:
        p.ct = p.tat = p.wt = 0
        p.rem = p.bt

def fcfs(procs):
    reset(procs)
    plist = sorted(procs, key=lambda x: (x.at, x.pid))
    curr_time = 0
    for p in plist:
        if curr_time < p.at:
            curr_time = p.at
        curr_time += p.bt
        p.ct = curr_time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt
    print_table("First-Come, First-Served (FCFS)", procs)

def sjf_non_preemptive(procs):
    reset(procs)
    n = len(procs)
    completed = 0
    curr_time = 0
    done = [False] * n

    while completed < n:
        idx = -1
        min_bt = 10**9
        for i in range(n):
            if not done[i] and procs[i].at <= curr_time and procs[i].bt < min_bt:
                min_bt = procs[i].bt
                idx = i
        if idx == -1:
            curr_time += 1
            continue
        curr_time += procs[idx].bt
        procs[idx].ct = curr_time
        procs[idx].tat = procs[idx].ct - procs[idx].at
        procs[idx].wt = procs[idx].tat - procs[idx].bt
        done[idx] = True
        completed += 1
    print_table("Shortest Job First (SJF - Non-Preemptive)", procs)

def priority_scheduling(procs):
    reset(procs)
    n = len(procs)
    completed = 0
    curr_time = 0
    done = [False] * n

    while completed < n:
        idx = -1
        best_pr = 10**9
        for i in range(n):
            if not done[i] and procs[i].at <= curr_time and procs[i].pr < best_pr:
                best_pr = procs[i].pr
                idx = i
        if idx == -1:
            curr_time += 1
            continue
        curr_time += procs[idx].bt
        procs[idx].ct = curr_time
        procs[idx].tat = procs[idx].ct - procs[idx].at
        procs[idx].wt = procs[idx].tat - procs[idx].bt
        done[idx] = True
        completed += 1
    print_table("Priority Scheduling (Non-Preemptive)", procs)

def round_robin(procs, quantum=2):
    reset(procs)
    n = len(procs)
    plist = sorted(procs, key=lambda x: (x.at, x.pid))
    curr_time = 0
    completed = 0
    queue = deque()
    in_queue = [False] * n

    for i in range(n):
        if plist[i].at <= curr_time:
            queue.append(i)
            in_queue[i] = True

    while completed < n:
        if not queue:
            curr_time += 1
            for i in range(n):
                if not in_queue[i] and plist[i].at <= curr_time:
                    queue.append(i)
                    in_queue[i] = True
            continue

        curr = queue.popleft()
        exec_time = min(quantum, plist[curr].rem)
        curr_time += exec_time
        plist[curr].rem -= exec_time

        # Check for newly arrived processes during execution
        for i in range(n):
            if not in_queue[i] and plist[i].at <= curr_time:
                queue.append(i)
                in_queue[i] = True

        if plist[curr].rem > 0:
            queue.append(curr)
        else:
            plist[curr].ct = curr_time
            plist[curr].tat = plist[curr].ct - plist[curr].at
            plist[curr].wt = plist[curr].tat - plist[curr].bt
            completed += 1

    print_table(f"Round Robin (Time Quantum = {quantum})", procs)

def main():
    # Sample processes: (PID, Arrival Time, Burst Time, Priority)
    sample_data = [
        Process(1, at=0, bt=5, pr=2),
        Process(2, at=1, bt=3, pr=1),
        Process(3, at=2, bt=8, pr=4),
        Process(4, at=3, bt=6, pr=3)
    ]

    print("=" * 60)
    print("            CPU SCHEDULING ALGORITHMS")
    print("=" * 60)
    print("Processes: P1 (AT=0, BT=5), P2 (AT=1, BT=3), P3 (AT=2, BT=8), P4 (AT=3, BT=6)")

    fcfs(sample_data)
    sjf_non_preemptive(sample_data)
    priority_scheduling(sample_data)
    round_robin(sample_data, quantum=2)
    print("=" * 60)

if __name__ == "__main__":
    main()
