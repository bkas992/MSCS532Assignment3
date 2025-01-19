import time
import tracemalloc
import random

# Merge Sort
def msort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = msort(arr[:mid])
    right = msort(arr[mid:])
    return merged_arr(left, right)

def merged_arr(left, right):
    final_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final_arr.append(left[i])
            i += 1
        else:
            final_arr.append(right[j])
            j += 1
    final_arr.extend(left[i:])
    final_arr.extend(right[j:])
    return final_arr

# Quick Sort
def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

#Measuring execution time and memory usage
def measure_performance(sort_func, arr):
    tracemalloc.start()  #memory tracking
    start_time = time.time()
    sorted_arr = sort_func(arr)  #sorting
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()  #Stopping memory tracking

    return {
        "execution_time": end_time - start_time,
        "memory_usage": peak / 1024  #Converting bytes to KB
    }

# Generating datasets
def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = list(range(size, 0, -1))
    random_data = [random.randint(1, size) for _ in range(size)]
    return sorted_data, reverse_sorted_data, random_data

# Runtime comparision
def run_comparison():
    dataset_sizes = [10000, 100000, 1000000]  # Sizes of datasets to test
    results = []

    for size in dataset_sizes:
        sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

        for dataset, dataset_name in zip(
            [sorted_data, reverse_sorted_data, random_data],
            ["Sorted", "Reverse Sorted", "Random"]
        ):
            msort_result = measure_performance(msort, dataset)
            qsort_result = measure_performance(qsort, dataset)

            results.append({
                "size": size,
                "dataset_type": dataset_name,
                "msort_time": msort_result["execution_time"],
                "msort_memory": msort_result["memory_usage"],
                "qsort_time": qsort_result["execution_time"],
                "qsort_memory": qsort_result["memory_usage"]
            })

    return results

# Results in table
def display_results(results):
    print(f"{'Size':<10}{'Dataset Type':<20}{'Merge Sort Time (s)':<20}{'Quick Sort Time (s)':<20}{'Merge Sort Mem (KB)':<20}{'Quick Sort Mem (KB)':<20}")
    print("=" * 110)
    for result in results:
        print(f"{result['size']:<10}{result['dataset_type']:<20}{result['msort_time']:<20.6f}{result['qsort_time']:<20.6f}{result['msort_memory']:<20.2f}{result['qsort_memory']:<20.2f}")

# Diplay result
if __name__ == "__main__":
    results = run_comparison()
    display_results(results)
