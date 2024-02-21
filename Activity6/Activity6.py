import csv
import time

class Car:
    def __init__(self, car_model):
        self.car_model = car_model

def load_csv(file_path):
    cars = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            car_model = row[0] 
            car = Car(car_model)
            cars.append(car)
    return cars

def linear_search(arr, keyword):
    for i in range(len(arr)):
        if keyword.lower() == arr[i].car_model.lower():
            return i
    return -1

def binary_search(arr, keyword):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid].car_model.lower()
        
        if mid_value == keyword.lower():
            return mid
        elif mid_value < keyword.lower():
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

if __name__ == "__main__":
    file_path = "car_models.csv"
    car_list = load_csv(file_path)
    
    search_term = input("Search your car model: ")

    # Linear search
    start = time.perf_counter()
    linear_index = linear_search(car_list, search_term)
    print("\nLinear search runtime: ")
    print("All done at %.20f seconds" % (time.perf_counter() - start))
    if linear_index != -1:
        print("Linear search result:")
        print(f"Car Model: {car_list[linear_index].car_model}\n")
    else:
        print("Your car model doesn't exist")

    # Binary search (using a sorted list)
    start = time.perf_counter()
    car_list.sort(key=lambda car: car.car_model.lower())  # Sort the list
    binary_index = binary_search(car_list, search_term)
    print("Binary search runtime:")
    print("All done at %.20f seconds" % (time.perf_counter() - start))
    if binary_index != -1:
        print("\nBinary search result:")
        print(f"Car Model: {car_list[binary_index].car_model}")
    else:
        print("Your car model doesn't exist")
