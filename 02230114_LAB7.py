class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root_value=None):
        if root_value is not None:
            self.root = Node(root_value)
            print(f"Created new Binary Tree with root: {root_value}")
        else:
            self.root = None
            print("Created new Binary Tree")
            print("Root: None")
    # Task 2: Tree Information Methods
    def height(self):
        def _height(node):
            return 0 if node is None else 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
    def size(self):
        def _size(node):
            return 0 if node is None else 1 + _size(node.left) + _size(node.right)
        return _size(self.root)
    def count_leaves(self):
        def _count_leaves(node):
            if node is None: return 0
            if node.left is None and node.right is None: return 1
            return _count_leaves(node.left) + _count_leaves(node.right)
        return _count_leaves(self.root)
    def is_full_binary_tree(self):
        def _is_full(node):
            if node is None: return True
            if node.left is None and node.right is None: return True
            if node.left and node.right: return _is_full(node.left) and _is_full(node.right)
            return False
        return _is_full(self.root)

    def is_complete_binary_tree(self):
        if not self.root: return True
        queue, found_null = [self.root], False
        while queue:
            current = queue.pop(0)
            if current is None:
                found_null = True
            else:
                if found_null: return False
                queue.append(current.left)
                queue.append(current.right)
        return True
# ---------------------- Task 1 Test ----------------------
print("Task 1 Output:")
bt_empty = BinaryTree()
# ---------------------- Task 2 Test ----------------------
print("\nTask 2 Output:")
bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)
print(f"Tree Height: {bt.height()}")
print(f"Total Nodes: {bt.size()}")
print(f"Leaf Nodes Count: {bt.count_leaves()}")
print(f"Is Full Binary Tree: {bt.is_full_binary_tree()}")
print(f"Is Complete Binary Tree: {bt.is_complete_binary_tree()}")