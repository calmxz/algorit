import time
import random

random_numbers = [random.randint(0, 100) for _ in range(100)]

print("Unsorted List: ")
print(random_numbers)

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    
def selection(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
    
if __name__ == "__main__":
    insertion_numbers = random_numbers.copy()
    bubble_numbers = random_numbers.copy()
    selection_numbers = random_numbers.copy()
    
    start = time.perf_counter()
    insertion(insertion_numbers)
    print("Insertion Sort Runtime: ")
    print("Midpoint at %.20f seconds" % (time.perf_counter() - start))
    print("All done at %.20f seconds" % (time.perf_counter() - start))
    
    print("Insertion Sort Method: ")
    print(insertion_numbers)
    
    start = time.perf_counter()
    bubble(bubble_numbers)
    print("Bubble Sort Runtime: ")
    print("Midpoint at %.20f seconds" % (time.perf_counter() - start))
    print("All done at %.20f seconds" % (time.perf_counter() - start))
    
    print("Bubble Sort Method: ")
    print(bubble_numbers)
    
    start = time.perf_counter()
    selection(selection_numbers)
    print("Selection Sort Runtime: ")
    print("Midpoint at %.20f seconds" % (time.perf_counter() - start))
    print("All done at %.20f seconds" % (time.perf_counter() - start))  
     
    print("Selection Sort Method: ")
    print(selection_numbers)