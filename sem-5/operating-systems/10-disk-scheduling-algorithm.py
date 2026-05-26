# Practical 10: Disk Scheduling Algorithms
# Simulates FCFS, SSTF, SCAN, and C-SCAN disk scheduling algorithms

def fcfs(requests, initial_head):
    total_movement = 0
    current_head = initial_head
    seek_sequence = [initial_head]

    for req in requests:
        total_movement += abs(current_head - req)
        current_head = req
        seek_sequence.append(req)

    print(f"FCFS   : Total Head Movement = {total_movement:<6} Sequence = {' -> '.join(map(str, seek_sequence))}")

def sstf(requests, initial_head):
    reqs = list(requests)
    total_movement = 0
    current_head = initial_head
    seek_sequence = [initial_head]

    while reqs:
        # Find request with minimum distance from current_head
        closest = min(reqs, key=lambda x: abs(current_head - x))
        total_movement += abs(current_head - closest)
        current_head = closest
        seek_sequence.append(closest)
        reqs.remove(closest)

    print(f"SSTF   : Total Head Movement = {total_movement:<6} Sequence = {' -> '.join(map(str, seek_sequence))}")

def scan(requests, initial_head, disk_size=200):
    total_movement = 0
    current_head = initial_head
    seek_sequence = [initial_head]

    left = [r for r in requests if r < initial_head]
    right = [r for r in requests if r >= initial_head]

    left.sort(reverse=True)
    right.sort()

    # Move right toward the end of disk, then reverse left
    for req in right:
        total_movement += abs(current_head - req)
        current_head = req
        seek_sequence.append(req)

    # Reach maximum cylinder end
    if current_head != disk_size - 1 and left:
        total_movement += abs(current_head - (disk_size - 1))
        current_head = disk_size - 1
        seek_sequence.append(current_head)

    for req in left:
        total_movement += abs(current_head - req)
        current_head = req
        seek_sequence.append(req)

    print(f"SCAN   : Total Head Movement = {total_movement:<6} Sequence = {' -> '.join(map(str, seek_sequence))}")

def cscan(requests, initial_head, disk_size=200):
    total_movement = 0
    current_head = initial_head
    seek_sequence = [initial_head]

    left = [r for r in requests if r < initial_head]
    right = [r for r in requests if r >= initial_head]

    left.sort()
    right.sort()

    for req in right:
        total_movement += abs(current_head - req)
        current_head = req
        seek_sequence.append(req)

    # Reach end of disk
    if current_head != disk_size - 1 and left:
        total_movement += abs(current_head - (disk_size - 1))
        current_head = disk_size - 1
        seek_sequence.append(current_head)

    # Circular jump to cylinder 0
    if left:
        total_movement += (disk_size - 1)  # Jump cost
        current_head = 0
        seek_sequence.append(current_head)
        for req in left:
            total_movement += abs(current_head - req)
            current_head = req
            seek_sequence.append(req)

    print(f"C-SCAN : Total Head Movement = {total_movement:<6} Sequence = {' -> '.join(map(str, seek_sequence))}")

def main():
    print("=" * 60)
    print("             DISK SCHEDULING ALGORITHMS")
    print("=" * 60)

    # Standard disk queue requests
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head = 53
    disk_size = 200

    print(f"Disk Requests Queue : {requests}")
    print(f"Initial Head Position: {initial_head}")
    print(f"Disk Cylinders Range: 0 to {disk_size - 1}\n")

    fcfs(requests, initial_head)
    sstf(requests, initial_head)
    scan(requests, initial_head, disk_size)
    cscan(requests, initial_head, disk_size)
    print("=" * 60)

if __name__ == "__main__":
    main()
