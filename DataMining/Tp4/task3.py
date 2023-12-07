import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = ''
with open('data.txt', 'r') as f:
    text = f.read()

tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

filtered_word_counts = Counter(filtered_tokens)

# Task 3: Word Clouds
# Create word clouds
def create_word_cloud(words, title):
    wordcloud = WordCloud(width=800, height=400, max_words=len(words), background_color='white').generate_from_frequencies(words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.show()

# Word clouds with stopwords removed
create_word_cloud(dict(filtered_word_counts.most_common(15)), 'Word Cloud (15 most frequent words)')
create_word_cloud(dict(filtered_word_counts.most_common(50)), 'Word Cloud (50 most frequent words)')
create_word_cloud(dict(filtered_word_counts.most_common(100)), 'Word Cloud (100 most frequent words)')

# Word cloud for 20 least frequent words
create_word_cloud(dict(filtered_word_counts.most_common()[:-21:-1]), 'Word Cloud (20 least frequent words)')
