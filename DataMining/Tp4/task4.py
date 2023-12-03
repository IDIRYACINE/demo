import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt


text = ''
with open('data.txt', 'r') as f:
    text = f.read()


tokens = word_tokenize(text)

# Task 4: N-gram Analysis
# Bi-grams and Tri-grams
bi_grams = list(nltk.bigrams(tokens))
tri_grams = list(nltk.trigrams(tokens))

# Frequency distribution
bi_gram_freq = nltk.FreqDist(bi_grams)
tri_gram_freq = nltk.FreqDist(tri_grams)

# Display top 10 bi-grams and tri-grams
print("\nTop 10 Bi-grams:")
print(bi_gram_freq.most_common(10))

print("\nTop 10 Tri-grams:")
print(tri_gram_freq.most_common(10))