import string

def check_password_strength(password):
  """Checks the strength of a password based on length and character types.

  Args:
    password: The password to be checked.

  Returns:
    A string indicating the password strength (weak, medium, strong, very strong).
  """

  strength = 0
  has_upper = False
  has_lower = False
  has_digit = False
  has_special = False

  if len(password) >= 8:
    strength += 1
  if any(char in string.ascii_uppercase for char in password):
    has_upper = True
    strength += 1
  if any(char in string.ascii_lowercase for char in password):
    has_lower = True
    strength += 1
  if any(char in string.digits for char in password):
    has_digit = True
    strength += 1
  if any(char in string.punctuation for char in password):
    has_special = True
    strength += 1

  if strength == 0:
    return "Very weak"
  elif strength == 1:
    return "Weak"
  elif strength == 2:
    return "Medium"
  elif strength == 3:
    return "Strong"
  else:
    return "Very strong"

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
