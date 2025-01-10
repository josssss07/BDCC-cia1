from multiprocessing import Pool
import os

def merge(left, right):
    """Merge two sorted arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    """Sequential merge sort."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def parallel_merge_sort(arr):
    """Parallel merge sort using multiprocessing."""
    if len(arr) <= 1:
        return arr

    if len(arr) < 1000:  # For small arrays, use sequential merge sort
        return merge_sort(arr)

    mid = len(arr) // 2

    with Pool(processes=2) as pool:
        left, right = pool.map(merge_sort, [arr[:mid], arr[mid:]])

    return merge(left, right)

if __name__ == "__main__":
    import time
    import random

    # Generate a random array
    array = [random.randint(0, 10000) for _ in range(100000)]

    # Sequential Merge Sort
    start_time = time.time()
    sorted_array_seq = merge_sort(array)
    print(f"Sequential Merge Sort took {time.time() - start_time:.2f} seconds")

    # Parallel Merge Sort
    start_time = time.time()
    sorted_array_par = parallel_merge_sort(array)
    print(f"Parallel Merge Sort took {time.time() - start_time:.2f} seconds")

    # Verify correctness
    print(f"Arrays are sorted the same: {sorted_array_seq == sorted_array_par}")
