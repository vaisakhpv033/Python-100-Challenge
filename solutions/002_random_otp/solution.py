import random

def generate_otp():
  """Generates a random 6-digit OTP string."""
  otp_digits = [random.choice('0123456789') for _ in range(6)]
  return "".join(otp_digits)
