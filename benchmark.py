"""
Simple Benchmark: List vs Set vs Binary Search
"""

import time
import bisect

def benchmark(size=1000000, searches=100):
    data_list = list(range(size))
    data_sorted = sorted(data_list)  # Already sorted
    data_set = set(data_list)
    
    targets = [size // 2 + i for i in range(searches)]
    
    # Linear search
    start = time.perf_counter()
    for t in targets:
        _ = t in data_list
    print(f"Linear search ({searches} searches): {time.perf_counter() - start:.4f}s")
    
    # Binary search
    start = time.perf_counter()
    for t in targets:
        i = bisect.bisect_left(data_sorted, t)
        _ = i < len(data_sorted) and data_sorted[i] == t
    print(f"Binary search ({searches} searches): {time.perf_counter() - start:.4f}s")
    
    # Hash lookup
    start = time.perf_counter()
    for t in targets:
        _ = t in data_set
    print(f"Hash lookup ({searches} searches): {time.perf_counter() - start:.4f}s")

if __name__ == "__main__":
    benchmark()
