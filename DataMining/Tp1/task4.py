import re

def extract_all_email_addresses(text):
  """Extracts all email addresses from a given text using regular expressions.

  Args:
    text: The text to extract email addresses from.

  Returns:
    A list of all email addresses extracted from the text.
  """

  email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
  email_addresses = email_regex.findall(text)
  return email_addresses

def validate_phone_number(phone_number):
  """Validates whether a given string is a valid phone number using regular expressions.

  Args:
    phone_number: The phone number to validate.

  Returns:
    True if the phone number is valid, False otherwise.
  """

  phone_number_regex = re.compile(r"^\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$")
  if phone_number_regex.match(phone_number):
    return True
  else:
    return False

def extract_all_urls(text):
  """Extracts all URLs from a given text using regular expressions.

  Args:
    text: The text to extract URLs from.

  Returns:
    A list of all URLs extracted from the text.
  """

  url_regex = re.compile(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})")
  urls = url_regex.findall(text)
  return urls

# Example usage of the functions:

text = """
This is a sample text with email addresses, phone numbers, and URLs.

Email addresses:
  john.doe@example.com
  jane.doe@example.com

  Phone numbers:
    (123) 456-7890
    (555) 555-5555

  URLs:
    https://www.example.com
    https://www.google.com
"""

# Extract all email addresses from the text.
email_addresses = extract_all_email_addresses(text)
print("Email addresses:", email_addresses)

# Validate a phone number.
phone_number = "(123) 456-7890"
is_valid_phone_number = validate_phone_number(phone_number)
print("Is the phone number {} valid? {}".format(phone_number, is_valid_phone_number))

# Extract all URLs from the text.
urls = extract_all_urls(text)
print("URLs:", urls)
