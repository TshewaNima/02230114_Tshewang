## Task 1 (Part 1): Counting Sort Implementation
def counting_sort(arr):
    """
    Sorts an array using counting sort algorithm.
    Handles duplicate values and negative numbers.
    """
    if len(arr) <= 1:
        return arr
    
    # Find range of input array
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_size
    
    # Count frequencies - Step 1
    for num in arr:
        count[num - min_val] += 1
    
    # Compute cumulative frequencies - Step 2
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array - Step 3
    output = [0] * len(arr)
    for num in reversed(arr):
        index = count[num - min_val] - 1
        output[index] = num
        count[num - min_val] -= 1
    
    return output
# Test
arr = [4, 2, 2, 8, 3, 3, 1]
print(f"Original list: {arr}")
print(f"Sorted using Counting Sort: {counting_sort(arr)}")



## Task 1 (Part 2): Radix Sort Implementation

def counting_sort_for_radix(arr, exp):
    """
    Counting sort used as subroutine for radix sort.
    Sorts array based on digit at position exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9
    
    # Count frequencies of digits at current exponent
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Compute cumulative frequencies
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Sorts an array using radix sort algorithm (LSD approach).
    Uses counting sort as subroutine for each digit position.
    """
    if len(arr) <= 1:
        return arr
    
    # Make a copy to avoid modifying original
    arr_copy = arr.copy()
    
    # Find maximum number to know number of digits
    max_val = max(arr_copy)
    
    # Process each digit position
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr_copy, exp)
        exp *= 10
    
    return arr_copy

# Test
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Original list: {arr}")
print(f"Sorted using Radix Sort: {radix_sort(arr)}")