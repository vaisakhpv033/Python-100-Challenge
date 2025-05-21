# Problem 1: Generate a Random Number

This solution addresses the first problem: writing a Python function to generate a random integer within a specified range.

## Code Explanation

The Python script `solution.py` contains a function `generate_random_integer(min_val, max_val)`:

*   It imports the `random` module.
*   The function takes two arguments: `min_val` (the minimum value of the range) and `max_val` (the maximum value of the range).
*   It uses `random.randint(min_val, max_val)` to generate an integer within this inclusive range.
*   It returns the generated random integer.

Example usage:

```python
import random

def generate_random_integer(min_val, max_val):
    """Generates a random integer within a specified range (inclusive)."""
    return random.randint(min_val, max_val)

# Example:
# random_num = generate_random_integer(1, 100)
# print(f"A random number between 1 and 100: {random_num}")
```

This implementation is optimal as `random.randint()` is the standard and most direct way to achieve this in Python.
