# Practical 09: Page Replacement Algorithms
# Simulates FIFO, LRU, and Optimal page replacement policies

def fifo(ref_string, num_frames):
    frames = [-1] * num_frames
    front = 0
    page_faults = 0
    hits = 0

    for page in ref_string:
        if page in frames:
            hits += 1
        else:
            page_faults += 1
            frames[front] = page
            front = (front + 1) % num_frames

    hit_ratio = hits / len(ref_string)
    print(f"FIFO    : Page Faults = {page_faults:<4} Hits = {hits:<4} Hit Ratio = {hit_ratio:.2%}")

def lru(ref_string, num_frames):
    frames = [-1] * num_frames
    last_used = [0] * num_frames
    filled = 0
    page_faults = 0
    hits = 0

    for current_time, page in enumerate(ref_string):
        if page in frames:
            hits += 1
            idx = frames.index(page)
            last_used[idx] = current_time
        else:
            page_faults += 1
            if filled < num_frames:
                frames[filled] = page
                last_used[filled] = current_time
                filled += 1
            else:
                # Find least recently used frame index
                lru_idx = last_used.index(min(last_used))
                frames[lru_idx] = page
                last_used[lru_idx] = current_time

    hit_ratio = hits / len(ref_string)
    print(f"LRU     : Page Faults = {page_faults:<4} Hits = {hits:<4} Hit Ratio = {hit_ratio:.2%}")

def optimal(ref_string, num_frames):
    frames = [-1] * num_frames
    filled = 0
    page_faults = 0
    hits = 0
    n = len(ref_string)

    for i in range(n):
        page = ref_string[i]
        if page in frames[:filled]:
            hits += 1
            continue

        page_faults += 1
        if filled < num_frames:
            frames[filled] = page
            filled += 1
        else:
            # Find the frame page used farthest in the future
            replace_idx = -1
            farthest = -1
            for j in range(num_frames):
                target = frames[j]
                if target not in ref_string[i + 1:]:
                    replace_idx = j
                    break
                else:
                    next_use = ref_string[i + 1:].index(target)
                    if next_use > farthest:
                        farthest = next_use
                        replace_idx = j
            frames[replace_idx] = page

    hit_ratio = hits / len(ref_string)
    print(f"Optimal : Page Faults = {page_faults:<4} Hits = {hits:<4} Hit Ratio = {hit_ratio:.2%}")

def main():
    print("=" * 60)
    print("             PAGE REPLACEMENT ALGORITHMS")
    print("=" * 60)

    # Standard reference string and frames count
    ref_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    num_frames = 3

    print(f"Reference String : {ref_string}")
    print(f"Total Requests   : {len(ref_string)}")
    print(f"Number of Frames : {num_frames}\n")

    fifo(ref_string, num_frames)
    lru(ref_string, num_frames)
    optimal(ref_string, num_frames)
    print("=" * 60)

if __name__ == "__main__":
    main()
