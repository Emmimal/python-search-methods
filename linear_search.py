"""
Linear Search Example

Demonstrates how Python's 'in' operator works on lists: sequential checking.
Includes a step-by-step explanatory version and a simple benchmark.
"""

def linear_search_explained(items, target):
    """
    Perform linear search with detailed step-by-step printing.
    
    Args:
        items (list): List of items to search
        target: Value to find
    
    Returns:
        int: Index if found, -1 otherwise
    """
    print(f"Looking for: {target}")
    print(f"Searching in: {items}")
    print()
    
    for index, item in enumerate(items):
        print(f"Step {index + 1}: Checking position {index} → {item}")
        if item == target:
            print(f"✓ Found {target} at position {index}!")
            return index
    
    print(f"✗ {target} not found")
    return -1

def linear_search_simple(items, target):
    """Standard linear search without printing."""
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

if __name__ == "__main__":
    # Example usage
    numbers = [5, 12, 8, 30, 15]
    print("=== Explanatory Search ===")
    linear_search_explained(numbers, 30)
    
    print("\n=== Simple Search ===")
    result = linear_search_simple(numbers, 8)
    print(f"Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
    
    # Simple benchmark
    import time
    large_list = list(range(100000))
    start = time.perf_counter()
    _ = 99999 in large_list  # Uses Python's built-in linear search
    print(f"\nBuilt-in 'in' on 100k items: {time.perf_counter() - start:.6f} seconds")
