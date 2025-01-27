import heapq

array_given = [22, 33, 9, 40, 15, 6, 21, 12]

#defining function for implementing heap sort
def heapsort_func(array_given, n, i):
    large = i  # Initialize largest as root
    LS = 2 * i + 1  # Left child index
    RS = 2 * i + 2  # Right child index

    # Check if left child is larger than root
    if LS < n and array_given[LS] > array_given[large]:
        large = LS

    # Check if right child is larger than the largest so far
    if RS < n and array_given[RS] > array_given[large]:
        large = RS

    # If largest is not root, swap and heapsort the affected subtree
    if large != i:
        array_given[i], array_given[large] = array_given[large], array_given[i]  # Swap
        heapsort_func(array_given, n, large)

def heapsort(array_given): #Sorting the array
    n = len(array_given)
    # Build a max heap, 
    for i in range(n // 2 - 1, -1, -1):
        heapsort_func(array_given, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        array_given[i], array_given[0] = array_given[0], array_given[i]  # Swap the root with the last element
        heapsort_func(array_given, i, 0)  # Heapify the reduced heap

print("Given array: ", array_given)
heapsort(array_given)
print("Final array agter sorting: ", array_given)


#Code for implementing Priority Queue
class Priority_Queue_func:
    def __init__(self):
        self._queue = []
        self._index = 0  # To handle priority ties

    def push(self, item, priority):  # Push a new item with its priority into the queue
        heapq.heappush(self._queue, (-priority, self._index, item))  # Use negative priority for max-heap behavior
        self._index += 1

    def pop(self):  # Pop and return the item with the highest priority
        return heapq.heappop(self._queue)[-1]

    def empty_check(self):
        return len(self._queue) == 0

PQ = Priority_Queue_func()
PQ.push("P1", priority=2)
PQ.push("P2", priority=3)
PQ.push("P3", priority=1)

print("Processing Priority Queue task:")
while not PQ.empty_check():
    task = PQ.pop()
    print("\nProcessed task:", task)