import random

def randomized_quicksort(arr, low, high):
    if low < high:
        # Randomly choose a pivot index and swap it with the high index
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        
        # Partition the array around the pivot
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the two subarrays
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Set the pivot to be the last element (after randomization)
    pivot = arr[high]
    i = low - 1  # pointer for the smaller element
    
    for j in range(low, high):
        # If the current element is less than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Wrapper function for Randomized Quicksort
def quicksort(arr):
    randomized_quicksort(arr, 0, len(arr) - 1)

# Test Cases
if __name__ == "__main__":
    # Test case 1: Normal array
    arr1 = [3, 1, 4, 7, 2, 5, 6]
    quicksort(arr1)
    print(f"Sorted array: {arr1}")  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 2: Already sorted array
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    quicksort(arr2)
    print(f"Sorted array: {arr2}")  # Output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 3: Array with repeated elements
    arr3 = [4, 5, 6, 6, 7, 5, 4, 6]
    quicksort(arr3)
    print(f"Sorted array: {arr3}")  # Output: [4, 4, 5, 5, 6, 6, 6, 7]

    # Test case 4: Empty array
    arr4 = []
    quicksort(arr4)
    print(f"Sorted array: {arr4}")  # Output: []

    # Test case 5: Array with one element
    arr5 = [10]
    quicksort(arr5)
    print(f"Sorted array: {arr5}")  # Output: [10]




class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]
        self.A = (5**0.5 - 1) / 2  # The golden ratio

    def _hash(self, key):
        return int(self.capacity * ((self.A * key) % 1))

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:  # If the key already exists, update the value
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return
        print("Key not found.")

    def load_factor(self):
        return self.size / self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for chain in self.table:
            for key, value in chain:
                new_index = int(new_capacity * ((self.A * key) % 1))
                new_table[new_index].append([key, value])
        self.capacity = new_capacity
        self.table = new_table



