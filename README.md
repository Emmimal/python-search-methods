# python-search-methods
Examples of linear search, binary search, and hash lookup in Python – with performance insights

# Python Search Methods: Linear, Binary, and Hash Lookup Examples

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains practical Python examples demonstrating how the `in` operator works differently depending on the data structure:

- **Linear Search** (lists)
- **Binary Search** (sorted lists with `bisect`)
- **Hash Lookup** (sets and dictionaries)

These examples are based on my in-depth blog post:  
👉 **[How Python Searches Data: Linear Search, Binary Search, and Hash Lookup Explained](https://emitechlogic.com/how-python-searches-data/)**  

The full article includes detailed explanations, performance comparisons, common mistakes, decision guides, and a quiz. Check it out for the complete guide!

## Why This Matters

A simple check like:
```python
if item in collection:
    print("Found!")

can be slow or instant depending on whether collection is a list, set, or dict.
