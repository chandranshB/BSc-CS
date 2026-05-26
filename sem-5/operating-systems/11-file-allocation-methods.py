# Practical 11: File Allocation Methods
# Simulates Contiguous, Linked, and Indexed File Allocation methods

MAX_BLOCKS = 32

def simulate_contiguous(files):
    disk = [0] * MAX_BLOCKS
    print("\n--- Contiguous File Allocation ---")
    for file_name, start_block, length in files:
        can_allocate = True
        for b in range(start_block, start_block + length):
            if b >= MAX_BLOCKS or disk[b] == 1:
                can_allocate = False
                break

        if can_allocate:
            for b in range(start_block, start_block + length):
                disk[b] = 1
            print(f"File '{file_name}' ({length} blocks) -> Allocated contiguous blocks [{start_block} to {start_block + length - 1}]")
        else:
            print(f"File '{file_name}' ({length} blocks) -> Allocation Failed (Blocks occupied or out of bounds)")

def simulate_linked(files):
    disk = [0] * MAX_BLOCKS
    print("\n--- Linked File Allocation ---")
    for file_name, length in files:
        allocated = []
        for b in range(MAX_BLOCKS):
            if len(allocated) == length:
                break
            if disk[b] == 0:
                disk[b] = 1
                allocated.append(b)

        if len(allocated) == length:
            link_str = " -> ".join(map(str, allocated)) + " -> NULL"
            print(f"File '{file_name}' ({length} blocks) -> Linked blocks: {link_str}")
        else:
            print(f"File '{file_name}' ({length} blocks) -> Allocation Failed: Disk full")

def simulate_indexed(files):
    disk = [0] * MAX_BLOCKS
    print("\n--- Indexed File Allocation ---")
    for file_name, length in files:
        # Find index block
        index_block = -1
        for b in range(MAX_BLOCKS):
            if disk[b] == 0:
                index_block = b
                disk[b] = 1
                break

        if index_block == -1:
            print(f"File '{file_name}' -> Failed: No free block for index block.")
            continue

        allocated_data = []
        for b in range(MAX_BLOCKS):
            if len(allocated_data) == length:
                break
            if disk[b] == 0:
                disk[b] = 1
                allocated_data.append(b)

        if len(allocated_data) == length:
            print(f"File '{file_name}' -> Index Block: {index_block:<3} Data Blocks: {allocated_data}")
        else:
            print(f"File '{file_name}' -> Failed: Not enough free blocks.")

def main():
    print("=" * 60)
    print("              FILE ALLOCATION METHODS")
    print("=" * 60)
    print(f"Total Disk Blocks = {MAX_BLOCKS} (Blocks 0 to {MAX_BLOCKS - 1})")

    # Contiguous sample files: (File Name, Starting Block, Length)
    contiguous_files = [
        ("file1.txt", 2, 4),
        ("file2.txt", 8, 5),
        ("file3.txt", 10, 6)  # Conflicts with file2
    ]
    simulate_contiguous(contiguous_files)

    # Linked sample files: (File Name, Length)
    linked_files = [
        ("document.pdf", 4),
        ("photo.png", 6)
    ]
    simulate_linked(linked_files)

    # Indexed sample files: (File Name, Length)
    indexed_files = [
        ("data.csv", 4),
        ("script.py", 3)
    ]
    simulate_indexed(indexed_files)

    print("=" * 60)

if __name__ == "__main__":
    main()
