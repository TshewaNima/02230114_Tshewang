# Part 1 (Task 1 and 2) was carried out by Kinley Dolkar (02220118)
# Part 2 (Task 3 and 4) was carried out by Tshewang Nima (02230114)

# ---------------- Part 2: Stack Implementation using Linked List ----------------
# ---------------- Task 3: Node and LinkedStack Class Structure ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None    # Points to the top of the stack
        self._size = 0
        print("Created new LinkedStack")

    # Check if the stack is empty
    def is_empty(self):
        return self._size == 0

    # Return the number of elements in the stack
    def size(self):
        return self._size

    # ---------------- Task 4: Stack Operations ----------------

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        print(f"Popped element: {popped_node.data}")
        self.display()
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Current stack: null")
            return
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Current stack:", " -> ".join(elements) + " -> null")


# ----------------- Testing -----------------
if __name__ == "__main__":
    stack = LinkedStack()               # Task 3: Create stack
    print("stack is empty:", stack.is_empty())

    # Task 4: Perform stack operations
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())
    stack.pop()
    print("Stack size:", stack.size())