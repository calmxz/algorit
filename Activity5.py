import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        #find the mid of the array
        mid = len(arr) // 2
        
        #left group of the divided array
        left = arr[:mid]
        #right group of the divided array
        right = arr[mid:]
        
        #sorting the left group
        merge_sort(left)
        #sorting the right group
        merge_sort(right)
        
        i = j = k = 0
        
        #copy data to temporary arrays of left and right groups
        while i < len(left) and j < len (right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        #check if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quick_sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            _quick_sort(arr, low, pivot_index - 1)
            _quick_sort(arr, pivot_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)

# Generate random numbers
# Generate the same random numbers for both algorithms
random_numbers = [random.randint(0, 100) for _ in range(100)]
print("Unsorted List:", random_numbers)

# Copy the unsorted list for both sorting algorithms
merge_numbers = random_numbers.copy()
quick_numbers = random_numbers.copy()

# Measure the runtime performance of merge sort
start = time.perf_counter()
merge_sort(merge_numbers)

# Print merge sort runtime
print("\nMerge Sort Runtime:")
print("Midpoint at %.20f seconds" % (time.perf_counter() - start))
print("All done at %.20f seconds" % (time.perf_counter() - start))

# Print sorted list using merge sort method
print("\nMerge Sort Method:")
print(merge_numbers)

# Measure the runtime performance of quicksort
start = time.perf_counter()
quick_sort(quick_numbers)

# Print quicksort runtime
print("\nQuicksort Runtime:")
print("Midpoint at %.20f seconds" % (time.perf_counter() - start))
print("All done at %.20f seconds" % (time.perf_counter() - start))

# Print sorted list using quick sort method
print("\nQuick Sort Method:")
print(quick_numbers)