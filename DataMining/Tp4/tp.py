import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text
text = """
Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence 
concerned with the interactions between computers and human language. In particular, how to program computers 
to process and analyze large amounts of natural language data.
"""

# Task 1: Data Summary and Statistics
# Language detection
language = "english"  # Assuming the text is in English

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

# Task 2: Word Frequency Analysis
# Tokenize the text
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words(language))
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

# Task 3: Word Clouds
# Create word clouds
def create_word_cloud(words, title):
    wordcloud = WordCloud(width=800, height=400, max_words=len(words), background_color='white').generate_from_frequencies(words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Word clouds with stopwords removed
create_word_cloud(dict(filtered_word_counts.most_common(15)), 'Word Cloud (15 most frequent words)')
create_word_cloud(dict(filtered_word_counts.most_common(50)), 'Word Cloud (50 most frequent words)')
create_word_cloud(dict(filtered_word_counts.most_common(100)), 'Word Cloud (100 most frequent words)')

# Word cloud for 20 least frequent words
create_word_cloud(dict(filtered_word_counts.most_common()[:-21:-1]), 'Word Cloud (20 least frequent words)')

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
