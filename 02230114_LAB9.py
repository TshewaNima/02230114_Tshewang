## ------------------Task 1 & Task 2: Selection Sort with Counters ------------------
def selection_sort(arr):
    print(f"Original list: {arr}")
    
    # Initialize counters for Task 2
    comparisons = 0  # Counts total comparisons made
    swaps = 0         # Counts total swaps performed
    
    # Outer loop - goes through each position
    for i in range(len(arr)):
        min_index = i  # Assume current index has minimum element
        
        # Inner loop - finds smallest element in unsorted part
        for j in range(i + 1, len(arr)):
            comparisons += 1  # Task 2: Increment comparison counter
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap if a smaller element was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1  # Task 2: Increment swap counter
        
        # Task 1: Display list after each pass
        print(f"Pass {i + 1}: {arr}")
    
    # Task 2: Display final results with counters
    print(f"\nSorted list: {arr}")
    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    return arr
arr = [29, 10, 14, 37, 13]   #Test the Function
selection_sort(arr)

## ------------------Task 3 and 4: Implementation of Indexed Search Algorithm with Index Table --------------------
# Task 3: Create Index Table

def create_index_table(arr, block_size):
    index_table = []
    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
    
    return index_table


# Task 4: Indexed Search

def indexed_search(arr, index_table, key):
    # Step 1 & 2: Search index table to determine possible range
    block_start = 0
    block_end = 0
    
    for i in range(len(index_table)):
        if key <= index_table[i][0]:
            # Key belongs to this block or previous block
            if i == 0:
                block_start = 0
            else:
                block_start = index_table[i - 1][1]
            block_end = index_table[i][1] + (len(arr) // len(index_table))
            break
    else:
        # Key is greater than last block's value
        block_start = index_table[-1][1]
        block_end = len(arr) - 1
    
    # Step 3: Search sequentially inside the selected range
    for i in range(block_start, min(block_end + 1, len(arr))):
        if arr[i] == key:
            return i  # Step 4: Key found
    
    return -1  # Step 5: Key not found


# Testing
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

print("TASK 3: Creating Index Table")
index_table = create_index_table(arr, block_size)
print("Index table created (value -> position):")
for value, pos in index_table:
    print(f"  {value} -> {pos}")

print("\nTASK 4: Indexed Search")
key = 45
print(f"Searching for key: {key}")

result = indexed_search(arr, index_table, key)

if result != -1:
    print(f"Key {key} found at index {result}")
else:
    print(f"Key {key} not found")
    
    
    