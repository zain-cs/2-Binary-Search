#Binary Search
def binary_search(arr, target):
    low = 0 
    high =  len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        print(f"Step {steps}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
        if arr[mid] == target:
            print(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Target {target} not found")
    return -1


arr = [5, 12, 19, 23, 28, 33, 42, 56, 67, 72, 88]
binary_search(arr, 42)

#Binary Search implementation in OOP

class BinarySearch:
    def __init__(self, data=None):
        self.data = data if data is not None else []

    def search(self, target):
        
        low = 0
        high = len(self.data) - 1
        steps = 0

        while low <= high:
            steps += 1
            mid = (low + high) // 2
            print(f"Step {steps}: low={low}, high={high}, mid={mid}, arr[mid]={self.data[mid]}")

            if self.data[mid] == target:
                print(f" Target {target} found at index {mid}")
                return mid
            elif self.data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        print(f" Target {target} not found")
        return -1

    def add(self, item):
       self.data.append(item)
       self.data.sort()

    def __str__(self):
        return f"BinarySearch(data={self.data})"



if __name__ == "__main__":
   
    arr = [5, 12, 19, 23, 28, 33, 42, 56, 67, 72, 88]
    searcher = BinarySearch(arr)

    searcher.search(42)
    searcher.search(100) 

    searcher.add(100)
    searcher.search(100)  
    print(searcher)  