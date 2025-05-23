# Problem 3: Lambda to Generate Random Number

This solution addresses the third problem: writing a Python lambda function to generate a random integer within a specified range.

## Code Explanation

The Python script `solution.py` defines a lambda function `generate_random_lambda`:

*   It imports the `random` module.
*   The lambda function is assigned to the variable `generate_random_lambda`.
*   It takes two arguments: `min_val` (the minimum value of the range) and `max_val` (the maximum value of the range).
*   It uses `random.randint(min_val, max_val)` to generate an integer within this inclusive range, similar to a regular function.
*   When called, it returns the generated random integer.

Example usage:

```python
import random

# Lambda function to generate a random number within a specified range
generate_random_lambda = lambda min_val, max_val: random.randint(min_val, max_val)

# Example:
# random_num = generate_random_lambda(10, 50)
# print(f"A random number between 10 and 50 generated by lambda: {random_num}")
```

This implementation showcases how a lambda function can be used for concise, single-expression functions. It's optimal for this specific task due to its directness.
