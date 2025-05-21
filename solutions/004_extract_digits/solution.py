def extract_digits(input_string):
  """Extracts digit characters from a string, preserving their order."""
  digits = [char for char in input_string if char.isdigit()]
  return "".join(digits)
