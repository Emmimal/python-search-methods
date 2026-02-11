"""
Binary Search Example

Shows how to use Python's bisect module for efficient search on sorted data.
Includes step-by-step explanation and warnings about unsorted data.
"""

import bisect

def binary_search_explained(sorted_list, target):
    """
    Binary search with detailed step-by-step printing using bisect.
    
    Args:
        sorted_list (list): Must be sorted!
        target: Value to find
    
    Returns:
        int: Index if found, -1 otherwise
    """
    print(f"Looking for: {target}")
    print(f"In sorted list: {sorted_list}")
    print()
    
    left, right = 0, len(sorted_list) - 1
    step = 0
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        print(f"Step {step}: Checking middle position {mid} → {mid_value}")
        
        if mid_value == target:
            print(f"✓ Found {target} at position {mid}!")
            print(f"Total steps: {step}")
            return mid
        elif mid_value < target:
            print(f"  {mid_value} < {target} → search right half")
            left = mid + 1
        else:
            print(f"  {mid_value} > {target} → search left half")
            right = mid - 1
        print()
    
    print(f"✗ {target} not found after {step} steps")
    return -1

if __name__ == "__main__":
    # Must be sorted!
    numbers = [3, 7, 12, 18, 24, 29, 35, 41, 48, 55, 62, 70]
    
    print("=== Binary Search Demo ===")
    binary_search_explained(numbers, 41)
    
    # Using bisect directly
    print("\n=== Bisect Usage ===")
    index = bisect.bisect_left(numbers, 29)
    if index < len(numbers) and numbers[index] == 29:
        print(f"Found 29 at index {index} using bisect")
    
    # Simple benchmark
    import time
    large_sorted = list(range(1000000))
    start = time.perf_counter()
    index = bisect.bisect_left(large_sorted, 999999)
    _ = large_sorted[index] == 999999
    print(f"\nBinary search on 1M items: {time.perf_counter() - start:.6f} seconds")
