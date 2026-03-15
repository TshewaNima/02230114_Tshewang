# Task 1: Implementation of List Class Structure
class CustomList:
    def __init__(self, length=10):   # default length
        self.length = length
        self._size = 0
        self._array = [None] * length

        print(f"Created new CustomList with capacity: {self.length}")
        print(f"Current size: {self._size}")

my_list = CustomList()  # create object

# Task 2: Implementation of Basic Operations
class CustomList:
    def __init__(self, length=10):   # default list length
        self._length = length
        self._size = 0               # number of elements in list
        self._array = [None] * length  # storage array

    def append(self, element):      # add element at end
        if self._size < self._length:
            self._array[self._size] = element
            self._size += 1
            print(f"Appended {element} to the list")

    def get(self, index):           # get element at index
        if 0 <= index < self._size:
            print(f"Element at index {index}: {self._array[index]}")

    def set(self, index, element):  # replace element
        if 0 <= index < self._size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")

    def size(self):                 # show current size
        print(f"Current size: {self._size}")

# Test operations
my_list = CustomList()
my_list.append(5)
my_list.get(0)
my_list.set(0, 10)
my_list.get(0)
my_list.size()