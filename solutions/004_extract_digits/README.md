# Problem 4: Extracting Digits from a String

This solution addresses the fourth problem: writing a Python function to extract only digit characters from a string, preserving their order.

## Code Explanation

The Python script `solution.py` contains a function `extract_digits(input_string)`:

*   The function takes one argument: `input_string`.
*   It iterates through each character of the `input_string`.
*   For each character, it uses the `isdigit()` string method to check if the character is a digit.
*   If it's a digit, the character is appended to a list.
*   Finally, the list of digit characters is joined to form the result string, which is then returned.

Example usage:

```python
def extract_digits(input_string):
    """Extracts digit characters from a string, preserving their order."""
    digits = [char for char in input_string if char.isdigit()]
    return "".join(digits)

# Example:
# text = "abc123xyz456"
# numbers_only = extract_digits(text)
# print(f"Original string: {text}")
# print(f"Extracted digits: {numbers_only}") # Output: "123456"
```

This implementation is optimal as it uses a list comprehension for conciseness and `isdigit()` for efficient digit checking, followed by a single `join` operation.
