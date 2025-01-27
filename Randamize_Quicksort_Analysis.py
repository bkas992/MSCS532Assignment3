import time
import random
import tabulate
import sys

# For larger data, resursion limit increased
sys.setrecursionlimit(1000000)

def Qsort(example_array):
    if len(example_array) <= 1:
        return example_array
    
    pivot = example_array[0]
    LS = [x for x in example_array[1:] if x <= pivot]
    RS = [x for x in example_array[1:] if x > pivot]

    return Qsort(LS) + [pivot] + Qsort(RS)

def rand_Qsort(example_array, low, high):
    if low < high:
        pivot_index = randomized_partition(example_array, low, high)
        rand_Qsort(example_array, low, pivot_index - 1)
        rand_Qsort(example_array, pivot_index + 1, high)

def first_element_pivot(example_array, low, high): #First Element Pivot
    pivot = example_array[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if example_array[j] < pivot:
            example_array[i], example_array[j] = example_array[j], example_array[i]
            i += 1
    example_array[low], example_array[i - 1] = example_array[i - 1], example_array[low]
    return i - 1

def randomized_partition(example_array, low, high):
    rand_pv = random.randint(low, high) #Random pivot
    example_array[low], example_array[rand_pv] = example_array[rand_pv], example_array[low]  #Swapping pivot
    return first_element_pivot(example_array, low, high)

def measure_time(sort_func, example_array, *args):
    start_time = time.perf_counter()
    sort_func(example_array, *args)
    return time.perf_counter() - start_time

def generate_data(size, data_type):
    if data_type == 'sorted':
        return list(range(size))
    elif data_type == 'reverse_sorted':
        return list(range(size, 0, -1))
    elif data_type == 'random':
        return [random.randint(0, size) for _ in range(size)]
    elif data_type == 'repeated':
        return [random.randint(0, 10) for _ in range(size)]  #Repeated Elements Array

data_sizes = [100, 1000, 10000]
data_types = ['sorted', 'reverse_sorted', 'random', 'repeated']

results = []

for size in data_sizes:
    for data_type in data_types:
        data = generate_data(size, data_type)
        time_Qsort = measure_time(Qsort, data.copy())
        time_rand_Qsort = measure_time(rand_Qsort, data.copy(), 0, len(data) - 1)
        results.append([size, data_type, time_Qsort, time_rand_Qsort])

Title = ["Data Size", "Data Type", "Quicksort Time (s)", "Randomized Quicksort Time (s)"]
print(tabulate(results, Title=Title, floatfmt=".6f"))