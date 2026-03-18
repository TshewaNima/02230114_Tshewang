## Task 1: Implementthe Node and List Class Structure
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("Created new LinkedList")
        self.display_status()

    def display_status(self):
        print("Current Size:", self.size)
        if self.head is None:
            print("Head: None")
        else:
            print("Head:", self.head.data)
            
## Task 2: Implement Basic Operations            
    # Append element at the end
    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        print(f"Appended {element} to the list")

    # Get element by index
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    # Set element by index
    def set(self, index, element):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set element at index {index} to {element}")

    # Return size
    def get_size(self):
        print(f"Current size: {self.size}")
        return self.size

    # Prepend element at beginning
    def prepend(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        print(f"Prepend {element} to the list")

    # Print full linked list
    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print("Print Linked list:[" + " ".join(result) + "]")


# --------------------------
# Example Usage to get [10 10 5]
# --------------------------
my_LinkedList = LinkedList()

my_LinkedList.append(5)       # Add 5 at the end
my_LinkedList.get(0)          # Check element at index 0
my_LinkedList.prepend(10)     # Add 10 at beginning
my_LinkedList.prepend(10)     # Add another 10 at beginning
my_LinkedList.print_list()    # Final list: [10 10 5]