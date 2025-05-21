# Problem 2: Generate a 6-Digit Random OTP

This solution addresses the second problem: writing a Python function to generate a random 6-digit One-Time Password (OTP).

## Code Explanation

The Python script `solution.py` contains a function `generate_otp()`:

*   It imports the `random` module.
*   The function aims to produce a 6-digit string composed of random digits.
*   It uses a loop to select 6 random digits (0-9) using `random.choice('0123456789')`.
*   These digits are joined together to form the 6-digit OTP string.
*   It returns the generated OTP string.

Example usage:

```python
import random

def generate_otp():
    """Generates a random 6-digit OTP string."""
    otp_digits = [random.choice('0123456789') for _ in range(6)]
    return "".join(otp_digits)

# Example:
# otp = generate_otp()
# print(f"Generated OTP: {otp}")
```

This implementation is optimal for generating a string-based OTP of a fixed length using random digit choices.
