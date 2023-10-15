def count_vowels(string):
  """Counts the number of vowels in a given string.

  Args:
    string: A string.

  Returns:
    The number of vowels in the string.
  """

  vowels = ["a", "e", "i", "o", "u"]
  count = 0
  for char in string:
    if char.lower() in vowels:
      count += 1
  return count

def capitalize_first_letters(sentence):
  """Capitalizes the first letter of each word in a sentence.

  Args:
    sentence: A sentence.

  Returns:
    The sentence with the first letter of each word capitalized.
  """

  words = sentence.split()
  capitalized_words = []
  for word in words:
    capitalized_words.append(word.capitalize())
  return " ".join(capitalized_words)

def get_character_frequency(string):
  """Returns a dictionary containing the frequency of each character in a string.

  Args:
    string: A string.

  Returns:
    A dictionary containing the frequency of each character in the string.
  """

  char_frequency = {}
  for char in string:
    if char in char_frequency:
      char_frequency[char] += 1
    else:
      char_frequency[char] = 1
  return char_frequency

def replace_character(string, old_char, new_char):
  """Replaces all occurrences of a specific character with another character.

  Args:
    string: A string.
    old_char: The character to be replaced.
    new_char: The character to replace the old character with.

  Returns:
    The string with all occurrences of the old character replaced with the new character.
  """

  new_string = ""
  for char in string:
    if char == old_char:
      new_string += new_char
    else:
      new_string += char
  return new_string

def calculate_uppercase_lowercase_ratio(string):
  """Calculates and prints the ratio of uppercase letters to lowercase letters in a given string.

  Args:
    string: A string.
  """

  uppercase_count = 0
  lowercase_count = 0
  for char in string:
    if char.isupper():
      uppercase_count += 1
    elif char.islower():
      lowercase_count += 1

  ratio = uppercase_count / lowercase_count
  print("The ratio of uppercase letters to lowercase letters is {}.".format(ratio))

def calculate_sentence_character_frequency(sentence):
  """Calculates and prints the frequency of each character in a sentence.

  Args:
    sentence: A sentence.
  """

  char_frequency = get_character_frequency(sentence)
  for char in char_frequency:
    print("{}: {}".format(char, char_frequency[char]))

if __name__ == "__main__":
  # Example usage of the functions:

  string = "This is a test string."

  # Count the number of vowels in the string.
  num_vowels = count_vowels(string)
  print("The number of vowels in the string is:", num_vowels)

  # Capitalize the first letter of each word in the sentence.
  capitalized_sentence = capitalize_first_letters(string)
  print("The sentence with the first letter of each word capitalized is:", capitalized_sentence)

  # Get the frequency of each character in the string.
  char_frequency = get_character_frequency(string)
  print("The frequency of each character in the string is:", char_frequency)

  # Replace all occurrences of the character "a" with the character "e".
  replaced_string = replace_character(string, "a", "e")
  print("The string with all occurrences of the character 'a' replaced with the character 'e' is:", replaced_string)

  # Calculate the ratio of uppercase letters to lowercase letters in the string.
  calculate_uppercase_lowercase_ratio(string)

  # Calculate the frequency of each character in the sentence.
  calculate_sentence_character_frequency(string)
