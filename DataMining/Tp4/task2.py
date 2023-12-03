from nltk import download
from nltk import  word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt


# Download NLTK data stopwords
download('stopwords')


text = ''
with open('data.txt', 'r') as f:
    text = f.read()


# Task 2: Word Frequency Analysis
# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Word frequency analysis
word_counts = Counter(tokens)
filtered_word_counts = Counter(filtered_tokens)

# Print results
print("\nWord Frequency Analysis (with stopwords):")
print("20 most common words:", word_counts.most_common(20))
print("10 most common words:", word_counts.most_common(10))
print("10 rarely used words:", word_counts.most_common()[:-11:-1])

print("\nWord Frequency Analysis (without stopwords):")
print("20 most common words:", filtered_word_counts.most_common(20))
print("10 most common words:", filtered_word_counts.most_common(10))
print("10 rarely used words:", filtered_word_counts.most_common()[:-11:-1])

# Plotting
plt.figure(figsize=(12, 6))

# Plot with stopwords
plt.subplot(1, 2, 1)
plt.bar(*zip(*word_counts.most_common(10)))
plt.title('Top 10 Words (with stopwords)')
plt.xlabel('Words')
plt.ylabel('Frequency')

# Plot without stopwords
plt.subplot(1, 2, 2)
plt.bar(*zip(*filtered_word_counts.most_common(10)))
plt.title('Top 10 Words (without stopwords)')
plt.xlabel('Words')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
