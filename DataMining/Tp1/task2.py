import re 

def count_words(sentence):
  """Counts the number of words in a sentence.

  Args:
    sentence: A sentence.

  Returns:
    The number of words in the sentence.
  """

  words = re.findall(r'\w+',sentence)
  return len(words)

def remove_punctuation(sentence):
  """Removes all punctuation from a given sentence.

  Args:
    sentence: A sentence.

  Returns:
    The sentence with all punctuation removed.
  """

  punctuation = [".", ",", "!", "?", ";", ":"]
  for char in punctuation:
    sentence = sentence.replace(char, "")
  return sentence

def get_word_frequencies(paragraph):
  """Returns a dictionary with word frequencies for a given paragraph.

  Args:
    paragraph: A paragraph.

  Returns:
    A dictionary with word frequencies.
  """

  word_frequencies = {}
  words = re.findall(r'\w+',text)
  for word in words:
    if word in word_frequencies:
      word_frequencies[word] += 1
    else:
      word_frequencies[word] = 1
  return word_frequencies

def find_most_common_word(string):
  """Finds and prints the most common word in a given string, excluding common
  English stopwords.

  Args:
    string: A string.

  Returns:
    The most common word in the string, excluding common English stopwords.
  """

  stopwords = ["the", "and", "is", "of", "to", "a", "in", "that", "have", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "when", "what", "where", "who", "into", "time", "up", "out", "about", "again", "further", "then", "once", "here", "when", "where", "who", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

  string = remove_punctuation(string)

  words = re.findall(r'\w+',text)

  words = [word for word in words if word not in stopwords]

  word_frequencies = get_word_frequencies(string)

  most_common_word = max(word_frequencies.keys(), key=(lambda word: word_frequencies[word]))

  return most_common_word

def is_palindrome(word):
  """Checks if a given word is a palindrome.

  Args:
    word: A word.

  Returns:
    True if the word is a palindrome, False otherwise.
  """

  word = word.lower()
  reversed_word = word[::-1]
  return word == reversed_word

def is_sentence_palindrome(sentence):
  """Checks if a given sentence is a palindrome, considering spaces and punctuation.

  Args:
    sentence: A sentence.

  Returns:
    True if the sentence is a palindrome, False otherwise.
  """

  sentence = remove_punctuation(sentence.lower())
  reversed_sentence = sentence[::-1]
  return sentence == reversed_sentence

def swap_first_and_last_words(sentence):
  """Swaps the positions of the first and last words in a given sentence.

  Args:
    sentence: A sentence.

  Returns:
    The sentence with the first and last words swapped.
  """

  words = re.findall(r'\w+',sentence)
  first_word = words[0]
  last_word = words[len(words) - 1]

  reversed = []

  words.removeAt(0)
  words.removeAt(len(words) - 1)

  reversed.append(last_word)

  for word in words :
    reversed.append(word)

  reversed.append(first_word) 

  return "".join(reversed) 



text = input("Enter text ")

wordsCount = count_words(text)

print("Words Count : {}".format(wordsCount))

# removedPunctationText = remove_punctuation(text)
# print('Before {} , After {}'.format(text,removedPunctationText))

# mostCommonWord = find_most_common_word(text)

# print ('Most common word {}'.format(mostCommonWord))

# isPalindrome = is_palindrome(text)

# print("Text {} Is palindrom {}".format(text,isPalindrome))

# swappedText = swap_first_and_last_words(text)

# print ("Before {} After {}".format(text,swappedText))