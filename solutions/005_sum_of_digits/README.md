# Problem 5: Sum of Digits in a Number

This solution addresses the fifth problem: writing a Python function to calculate the sum of the digits of an integer.

## Code Explanation

The Python script `solution.py` contains a function `sum_of_digits(number)`:

*   The function takes one integer argument: `number`.
*   It first converts the integer to its absolute value to handle potential negative inputs gracefully (though the problem implies positive integers, this makes it more robust).
*   Then, it converts the number to a string to iterate over its digits.
*   It uses a generator expression `(int(digit) for digit in str(abs(number)))` to convert each digit character back to an integer.
*   The built-in `sum()` function is used to sum these digits.
*   It returns the total sum.

Example usage:

```python
def sum_of_digits(number):
    """Calculates the sum of the digits of an integer."""
    return sum(int(digit) for digit in str(abs(number)))

# Example:
# num = 12345
# digit_sum = sum_of_digits(num)
# print(f"The sum of digits in {num} is: {digit_sum}") # Output: 15

# num = -789
# digit_sum = sum_of_digits(num)
# print(f"The sum of digits in {num} is: {abs(digit_sum)}") # Output: 24
```

This implementation is optimal and Pythonic. Converting the number to a string allows easy iteration over digits, and using `sum()` with a generator expression is efficient for this task.
