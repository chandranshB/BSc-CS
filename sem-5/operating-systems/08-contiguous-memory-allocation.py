# Practical 08: Contiguous Memory Allocation
# Simulates First Fit, Best Fit, and Worst Fit memory allocation techniques

def print_allocation_table(title, block_sizes, process_sizes, allocation):
    print(f"\n--- {title} ---")
    print(f"{'Process No.':<14}{'Process Size':<16}{'Allocated Block':<18}{'Block Size'}")
    print("-" * 60)
    for i in range(len(process_sizes)):
        p_name = f"P{i + 1}"
        p_size = process_sizes[i]
        b_idx = allocation[i]
        if b_idx != -1:
            print(f"{p_name:<14}{p_size:<16}Block {b_idx + 1:<12}{block_sizes[b_idx]}")
        else:
            print(f"{p_name:<14}{p_size:<16}{'Not Allocated':<18}-")
    print("-" * 60)

def first_fit(blocks, processes):
    b = list(blocks)
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(b)):
            if b[j] >= processes[i]:
                allocation[i] = j
                b[j] -= processes[i]
                break
    print_allocation_table("First Fit Allocation", blocks, processes, allocation)

def best_fit(blocks, processes):
    b = list(blocks)
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if best_idx == -1 or b[j] < b[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            b[best_idx] -= processes[i]
    print_allocation_table("Best Fit Allocation", blocks, processes, allocation)

def worst_fit(blocks, processes):
    b = list(blocks)
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(b)):
            if b[j] >= processes[i]:
                if worst_idx == -1 or b[j] > b[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            b[worst_idx] -= processes[i]
    print_allocation_table("Worst Fit Allocation", blocks, processes, allocation)

def main():
    print("=" * 60)
    print("       CONTIGUOUS MEMORY ALLOCATION STRATEGIES")
    print("=" * 60)

    # Standard sample data
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    print(f"Memory Blocks available: {blocks}")
    print(f"Incoming Processes:      {processes}")

    first_fit(blocks, processes)
    best_fit(blocks, processes)
    worst_fit(blocks, processes)
    print("=" * 60)

if __name__ == "__main__":
    main()
