import timeit
import random
import matplotlib.pyplot as plt

k = 14000 # Array size for which merge sort should be used

# Merge sort implementation from: https://www.geeksforgeeks.org/insertion-sort-algorithm/
# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Merge sort implementation from: https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted

def timSort(arr, l, r):
    if len(arr) <= k:
        insertionSort(arr)
    elif l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        timSort(arr, l, m)
        timSort(arr, m+1, r)
        merge(arr, l, m, r)


# Measure execution time for different list lengths
list_lengths = [500*i for i in range(1, 51)]
num_executions = 100
time_sort_execution_times = []

for length in list_lengths:
    random_list = [random.randint(0, length) for _ in range(length)]

    def test_tim_sort():
        timSort(random_list, 0, length - 1)

    tim_sort_time_taken = timeit.timeit(test_tim_sort, number=num_executions) / num_executions
    time_sort_execution_times.append(tim_sort_time_taken)


# Merge sort plot results
plt.figure(figsize=(8, 5))
plt.plot(list_lengths, time_sort_execution_times, marker='o', linestyle='-')
plt.xlabel("List Length")
plt.ylabel("Execution Time (seconds)")
plt.title("Tim Sort Execution Time vs. List Length")
plt.grid()
plt.savefig("tim-sort-plot.png")
