import re

def calculate_average_word_length(text):
  """Calculates the average word length in a given text.

  Args:
    text: The text to calculate the average word length for.

  Returns:
    The average word length in the text.
  """

  words = re.findall(r'\w+',text)

  total_num_chars = sum(len(word) for word in words)

  average_word_length = total_num_chars / len(words)

  return average_word_length

def identify_longest_word(sentence):
  """Identifies the longest word in a sentence and prints its length.

  Args:
    sentence: The sentence to identify the longest word in.

  Returns:
    The length of the longest word in the sentence.
  """

  words = re.findall(r'\w+',sentence)

  longest_word = max(words, key=len)

  return len(longest_word)

def calculate_flesch_kincaid_reading_ease(paragraph):
  """Computes the Flesch-Kincaid reading ease score for a given paragraph.

  Args:
    paragraph: The paragraph to compute the Flesch-Kincaid reading ease score for.

  Returns:
    The Flesch-Kincaid reading ease score for the paragraph.
  """

  sentences = paragraph.split(".")

  average_words_per_sentence = sum(len(sentence.split()) for sentence in sentences) / len(sentences)

  average_syllables_per_word = sum(len(word.split("-")) for word in paragraph.split()) / len(paragraph.split())

  flesch_kincaid_reading_ease = 206.835 - 1.015 * average_words_per_sentence - 84.6 * average_syllables_per_word

  return flesch_kincaid_reading_ease


text = "This is a sample text."
average_word_length = calculate_average_word_length(text)
print("The average word length in the text is:", average_word_length)

# sentence = "This is a sample sentence with some long words."
# longest_word_length = identify_longest_word(sentence)
# print("The length of the longest word in the sentence is:", longest_word_length)

# paragraph = "This is a sample paragraph. It is a simple paragraph with easy-to-understand words and sentences."
# flesch_kincaid_reading_ease = calculate_flesch_kincaid_reading_ease(paragraph)
# print("The Flesch-Kincaid reading ease score for the paragraph is:", flesch_kincaid_reading_ease)
