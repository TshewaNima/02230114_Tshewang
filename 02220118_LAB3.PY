##Part 1: task 1 and 2 carried out by Kinley Dolkar

##Part 1:Task 1:Implementing the ArrayStack Class structure.
class ArrayStack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * capacity  # underlying array
        self.top = -1  # indicates empty stack
        print(f"Created new ArrayStack with capacity: {capacity}")
        print(f"Stack is empty: {self.is_empty()}")
    ##Task 2: Implementing Array-based Stack operation.
    # Push element onto stack
    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot push element.")
            return
        
        self.top += 1
        self.stack[self.top] = element
        print(f"Pushed {element} to the stack")

    # Pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop element.")
            return None
        
        element = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        print(f"Popped element: {element}")
        return element

    # Peek top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        
        print(f"Top element: {self.stack[self.top]}")
        return self.stack[self.top]

    # Check if empty
    def is_empty(self):
        return self.top == -1

    # Get size
    def size(self):
        return self.top + 1

    # Display stack
    def display(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            print("Display stack:", self.stack[:self.top + 1])


# -------------------------------
# Example Usage (Test Output)
# -------------------------------
stack = ArrayStack()

stack.push(10)
stack.display()

stack.push(20)
stack.display()

stack.push(30)
stack.display()

stack.peek()

stack.pop()

print(f"Stack size: {stack.size()}")
stack.display()