## Part 1: Queue Implementation using Array
# ---------------------- Task 1: Implement the ArrayQueue Class Structure -----------------------
class ArrayQueue:
    def __init__(self, capacity=10):
        self._queue = [None] * capacity  # Private array to store elements
        self._front = 0  # Index of the front element
        self._rear = -1  # Index of the rear element
        self._size = 0   # Current number of elements
        self._capacity = capacity  # Maximum capacity
        print(f"Created new Queue with capacity: {self._capacity}")

    def is_empty(self):
        """Check if the queue is empty."""
        return self._size == 0
# ----------------------- Task 2: Implement Array-based Queue Operations --------------------

    def is_full(self):
        """Check if the queue is full."""
        return self._size == self._capacity

    def enqueue(self, element):
        """Add an element to the rear of the queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        self._rear = (self._rear + 1) % self._capacity  # Circular increment
        self._queue[self._rear] = element
        self._size += 1
        print(f"Enqueued {element} to the queue")
        self.display()  # Display queue after each enqueue

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        element = self._queue[self._front]
        self._queue[self._front] = None  # Optional: clear spot
        self._front = (self._front + 1) % self._capacity  # Circular increment
        self._size -= 1
        print(f"Dequeued element: {element}")
        self.display()  # Display queue after dequeue
        return element

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._queue[self._front]

    def size(self):
        """Return the current number of elements in the queue."""
        return self._size

    def display(self):
        """Display all elements in the queue from front to rear."""
        if self.is_empty():
            print("Current queue: []")
            return
        index = self._front
        elements = []
        for _ in range(self._size):
            elements.append(self._queue[index])
            index = (index + 1) % self._capacity
        print(f"Current queue: {elements}")

# Initialize queue (Task 1)
q = ArrayQueue()
print("Queue is empty:", q.is_empty())

# Queue operations (Task 2)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(f"Front element: {q.peek()}")
q.dequeue()
print(f"Queue size: {q.size()}")


## Part 2: Queue Implementation using Linked List

# ------------ Task 3: Node and LinkedQueue Class Structure ------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        """Initialize an empty linked queue."""
        self._front = None
        self._rear = None
        self._size = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        """Check if the queue is empty."""
        return self._size == 0

# ----------------------- Task 4: Linked List-based Queue Operations -----------------------
   
    def enqueue(self, element):
        """Add element to the rear of the queue."""
        new_node = Node(element)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1
        print(f"Enqueued {element} to the queue")
        self.display()

    def dequeue(self):
        """Remove and return the front element."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        element = self._front.data
        self._front = self._front.next
        if self._front is None:  # Queue became empty
            self._rear = None
        self._size -= 1
        print(f"Dequeued element: {element}")
        self.display()
        return element

    def peek(self):
        """Return front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._front.data

    def size(self):
        """Return the number of elements."""
        return self._size

    def display(self):
        """Display queue elements in array style."""
        if self.is_empty():
            print("Display queue: []")
            return
        current = self._front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Display queue:[" + ",".join(elements) + "]")

lq = LinkedQueue()
print("Queue is empty:", lq.is_empty())

lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
print(f"Front element: {lq.peek()}")
lq.dequeue()
current = lq._front
linked_elements = []
while current:
    linked_elements.append(str(current.data))
    current = current.next
print("Current queue:", " -> ".join(linked_elements) + " -> null")
print("Queue size:", lq.size())