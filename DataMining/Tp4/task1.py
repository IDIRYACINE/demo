from nltk import sent_tokenize, word_tokenize
import langdetect

# Sample text

text = ''
with open('data.txt', 'r') as f:
    text = f.read()

# Task 1: Data Summary and Statistics
# Language detection
language = langdetect.detect(text)  # Assuming the text is in English

# Tokenizing into paragraphs, sentences, and words
paragraphs = text.split('\n')
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Basic statistics
avg_paragraph_length = len(sentences) / len(paragraphs)
avg_sentence_length = len(words) / len(sentences)
max_paragraph_length = max(len(sent_tokenize(p)) for p in paragraphs)
min_paragraph_length = min(len(sent_tokenize(p)) for p in paragraphs)
max_sentence_length = max(len(word_tokenize(s)) for s in sentences)
min_sentence_length = min(len(word_tokenize(s)) for s in sentences)

# Print results
print(f"Language: {language}")
print(f"Number of paragraphs: {len(paragraphs)}")
print(f"Number of sentences: {len(sentences)}")
print(f"Number of words: {len(words)}")
print(f"Average length of paragraphs: {avg_paragraph_length:.2f} sentences")
print(f"Average length of sentences: {avg_sentence_length:.2f} words")
print(f"Maximum length of paragraphs: {max_paragraph_length} sentences")
print(f"Minimum length of paragraphs: {min_paragraph_length} sentences")
print(f"Maximum length of sentences: {max_sentence_length} words")
print(f"Minimum length of sentences: {min_sentence_length} words")

