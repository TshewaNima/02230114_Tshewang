## ------------ Task 1: Quick Sort with Median-of-Three Optimization and Counters ---------

def quick_sort(arr):
    comparisons = 0
    swaps = 0
    
    def median_of_three(arr, low, high):
        """Optimization: Select median of first, middle, and last as pivot."""
        mid = (low + high) // 2
        
        # Sort low, mid, high elements
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
            nonlocal swaps
            swaps += 1
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
            swaps += 1
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
            swaps += 1
        
        # Place median at the end as pivot
        arr[mid], arr[high] = arr[high], arr[mid]
        swaps += 1
        return arr[high]
    
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = median_of_three(arr, low, high)
        i = low - 1
        
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1
    
    def _quick_sort(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    
    # Make a copy to avoid modifying original
    arr_copy = arr.copy()
    _quick_sort(arr_copy, 0, len(arr_copy) - 1)
    
    return arr_copy, comparisons, swaps


# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Original List: {arr}")

sorted_arr, comparisons, swaps = quick_sort(arr)
print(f"Sorted using Quick Sort: {sorted_arr}")
print(f"Number of comparisons: {comparisons}")
print(f"Number of swaps: {swaps}")

## ------- Part 2: Merge Sort with Counters -----------
def merge_sort(arr):
    comparisons = 0
    array_accesses = 0
    
    def merge(left, right):
        nonlocal comparisons, array_accesses
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            comparisons += 1
            array_accesses += 2  # Access left[i] and right[j]
            if left[i] <= right[j]:
                result.append(left[i])
                array_accesses += 1  # Append operation
                i += 1
            else:
                result.append(right[j])
                array_accesses += 1
                j += 1
        
        # Add remaining elements
        while i < len(left):
            result.append(left[i])
            array_accesses += 1
            i += 1
        
        while j < len(right):
            result.append(right[j])
            array_accesses += 1
            j += 1
        
        return result
    
    def _merge_sort(arr):
        nonlocal array_accesses
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        array_accesses += 2  # Access left and right halves
        left = _merge_sort(arr[:mid])
        right = _merge_sort(arr[mid:])
        
        return merge(left, right)
    
    # Make a copy to avoid modifying original
    arr_copy = arr.copy()
    array_accesses += len(arr)  # Copy operation
    
    sorted_arr = _merge_sort(arr_copy)
    
    return sorted_arr, comparisons, array_accesses


# Test
arr = [38, 27, 43, 3, 9, 82, 10]
print(f"Original List: {arr}")

sorted_arr, comparisons, accesses = merge_sort(arr)
print(f"Sorted using Merge Sort: {sorted_arr}")
print(f"Number of comparisons: {comparisons}")
print(f"Number of array accesses: {accesses}")