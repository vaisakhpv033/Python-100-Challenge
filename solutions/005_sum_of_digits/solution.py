def sum_of_digits(number):
  """Calculates the sum of the digits of an integer."""
  return sum(int(digit) for digit in str(abs(number)))
