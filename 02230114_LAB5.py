## Part 1: Sequential Search Implementation
def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Test the function
numbers = [23, 45, 12, 89, 67, 34, 56,]
target = 67

print(f"List: {numbers}")
print(f"Searching for {target} using Sequential Search")

index, count = sequential_search(numbers, target)

if index != -1:
    print(f"Found at index {index}")
    print(f"Number of comparisons: {count}")
else:
    print("Not found")

## Part 2: Binary Search Implementation
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons
# Test the function
numbers = [12, 23, 34, 45, 56, 67, 89]
target = 67

print(f"Sorted List: {numbers}")
print(f"Searching for {target} using Binary Search")

index, count = binary_search(numbers, target)
if index != -1:
    print(f"Found at index {index}")
    print(f"Number of comparisons: {count}")
else:
    print("Not found")
    