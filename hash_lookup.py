"""
Hash Lookup Example

Demonstrates O(1) average lookups with sets and dictionaries.
Includes membership testing and simple timing comparison.
"""

def hash_lookup_demo():
    """Show basic set and dict usage."""
    print("=== Set Membership Test ===")
    blocked_emails = {"spam1@bad.com", "spam2@bad.com", "spam3@bad.com"}
    email = "spam2@bad.com"
    
    if email in blocked_emails:
        print(f"{email} is blocked! (instant lookup)")
    else:
        print(f"{email} is allowed")
    
    print("\n=== Dictionary Key Lookup ===")
    grades = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 92,
        "Diana": 88
    }
    
    name = "Bob"
    print(f"{name}'s grade: {grades.get(name, 'Not found')}")

if __name__ == "__main__":
    hash_lookup_demo()
    
    # Simple benchmark vs list
    import time
    
    size = 1000000
    data_set = set(range(size))
    data_list = list(range(size))
    target = size - 1
    
    print("\n=== Performance Comparison ===")
    
    start = time.perf_counter()
    _ = target in data_set
    print(f"Set lookup (1M items): {time.perf_counter() - start:.6f} seconds")
    
    start = time.perf_counter()
    _ = target in data_list
    print(f"List lookup (1M items): {time.perf_counter() - start:.6f} seconds")
