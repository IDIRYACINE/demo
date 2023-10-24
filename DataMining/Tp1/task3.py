def count_lines_words_chars(filename):
  """Counts the number of lines, words, and characters in a text file.

  Args:
    filename: The name of the text file.

  Returns:
    A tuple containing the number of lines, words, and characters in the text file.
  """

  num_lines = 0
  num_words = 0
  num_chars = 0

  with open(filename, "r") as f:
    for line in f:
      num_lines += 1
      words = line.split()
      num_words += len(words)
      for char in line:
        num_chars += 1

  return num_lines, num_words, num_chars

def remove_empty_lines(filename, new_filename):
  """Removes any empty lines from a text file and saves the modified content to a new file.

  Args:
    filename: The name of the text file to read from.
    new_filename: The name of the new text file to save the modified content to.
  """

  with open(filename, "r") as f:
    lines = f.readlines()

  lines = [line for line in lines if line.strip()]

  with open(new_filename, "w") as f:
    for line in lines:
      f.write(line)

def search_for_word(filename, word):
  """Searches for a specific word in a text file and prints the line numbers where it appears.

  Args:
    filename: The name of the text file to search.
    word: The word to search for.
  """

  line_numbers = []

  with open(filename, "r") as f:
    for line_number, line in enumerate(f):
      if word in line:
        line_numbers.append(line_number + 1)

  if line_numbers:
    print("The word '{}' appears on the following lines:".format(word))
    for line_number in line_numbers:
      print(line_number)
  else:
    print("The word '{}' does not appear in the text file.".format(word))


filename = "text.txt"

num_lines, num_words, num_chars = count_lines_words_chars(filename)
print("The number of lines in the text file is:", num_lines)
# print("The number of words in the text file is:", num_words)
# print("The number of characters in the text file is:", num_chars)

# new_filename = "text_without_empty_lines.txt"
# remove_empty_lines(filename, new_filename)

# word = "Python"
# search_for_word(filename, word)
