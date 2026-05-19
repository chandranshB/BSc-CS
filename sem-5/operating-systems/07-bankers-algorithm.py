# Practical 07: Banker's Algorithm for Deadlock Avoidance
# Implements Safety Algorithm and Resource Request Algorithm

import sys

def calculate_need(P, R, maximum, allocation):
    need = []
    for i in range(P):
        row = [maximum[i][j] - allocation[i][j] for j in range(R)]
        need.append(row)
    return need

def is_safe_state(P, R, available, allocation, need):
    work = list(available)
    finish = [False] * P
    safe_sequence = []

    while len(safe_sequence) < P:
        found = False
        for i in range(P):
            if not finish[i]:
                # Check if need[i] <= work
                if all(need[i][j] <= work[j] for j in range(R)):
                    for j in range(R):
                        work[j] += allocation[i][j]
                    safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break
        if not found:
            return False, []

    return True, safe_sequence

def request_resources(P, R, available, allocation, need, pid, request):
    print(f"\nEvaluating request from P{pid}: {request}")
    # Condition 1: request <= need
    for j in range(R):
        if request[j] > need[pid][j]:
            print(f"Error: Process P{pid} requested more than its declared maximum need.")
            return False

    # Condition 2: request <= available
    for j in range(R):
        if request[j] > available[j]:
            print(f"Request denied: Insufficient resources available for P{pid}. Process must wait.")
            return False

    # Tentative allocation
    for j in range(R):
        available[j] -= request[j]
        allocation[pid][j] += request[j]
        need[pid][j] -= request[j]

    safe, safe_seq = is_safe_state(P, R, available, allocation, need)
    if safe:
        print(f"Request granted safely! New Safe Sequence: {' -> '.join(f'P{x}' for x in safe_seq)}")
        return True
    else:
        # Rollback
        for j in range(R):
            available[j] += request[j]
            allocation[pid][j] -= request[j]
            need[pid][j] += request[j]
        print("Request denied: Granting this request would lead to an unsafe state (potential deadlock).")
        return False

def main():
    print("=" * 60)
    print("        DEADLOCK AVOIDANCE: BANKER'S ALGORITHM")
    print("=" * 60)

    # Standard textbook problem: 5 processes (P0 to P4), 3 resource types (A, B, C)
    P = 5
    R = 3
    available = [3, 3, 2]

    allocation = [
        [0, 1, 0],  # P0
        [2, 0, 0],  # P1
        [3, 0, 2],  # P2
        [2, 1, 1],  # P3
        [0, 0, 2]   # P4
    ]

    maximum = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3]   # P4
    ]

    need = calculate_need(P, R, maximum, allocation)

    print(f"Number of Processes: {P}, Number of Resource Types: {R}")
    print(f"Initial Available Resources: {available}\n")
    print(f"{'Process':<9}{'Allocation':<16}{'Maximum':<16}{'Need':<16}")
    print("-" * 55)
    for i in range(P):
        alloc_str = " ".join(str(x) for x in allocation[i])
        max_str = " ".join(str(x) for x in maximum[i])
        need_str = " ".join(str(x) for x in need[i])
        print(f"P{i:<8}{alloc_str:<16}{max_str:<16}{need_str:<16}")
    print("-" * 55)

    safe, safe_seq = is_safe_state(P, R, available, allocation, need)
    if safe:
        print("\nStatus: System is in a SAFE state.")
        print(f"Safe Execution Sequence: {' -> '.join(f'P{x}' for x in safe_seq)}")
    else:
        print("\nStatus: System is in an UNSAFE state!")

    # Test Resource Request
    req_pid = 1
    req_vector = [1, 0, 2]
    request_resources(P, R, available, allocation, need, req_pid, req_vector)

    print("=" * 60)

if __name__ == "__main__":
    main()
