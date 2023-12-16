import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

# Function to present label distribution
def present_label_distribution(df):
    label_distribution = df['sentiment'].value_counts()
    print("Labels Distribution:")
    print(label_distribution)

# Function to create word cloud
def create_wordcloud(data, max_words, title):
    wordcloud = WordCloud(width=800, height=400, max_words=max_words, background_color='white').generate(' '.join(data))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Function to explore n-grams
def explore_ngrams(data, ngram_range=(2, 3), top_n=10):
    vectorizer = CountVectorizer(ngram_range=ngram_range, stop_words='english')
    ngrams = vectorizer.fit_transform(data)

    ngram_counts = ngrams.sum(axis=0)
    ngram_features = vectorizer.get_feature_names_out()
    ngram_counts = ngram_counts.tolist()[0]

    ngram_df = pd.DataFrame({'Ngram': ngram_features, 'Count': ngram_counts})
    ngram_df = ngram_df.sort_values(by='Count', ascending=False)

    print(f"\nTop {top_n} {' and '.join(map(str, ngram_range))}-grams:")
    print(ngram_df.head(top_n))

# Example usage:
# Read the CSV file with preprocessed data
file_path = 'output/preprocessed.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Task 1: Present the labels distribution
present_label_distribution(df)

# Task 2: Create a word cloud of the most 20 frequent words using preprocessed tokens
create_wordcloud(df['review'], max_words=20, title='Word Cloud - Top 20 Frequent Words')

# Task 3: Create a word cloud of the most 55 frequent words using preprocessed tokens
create_wordcloud(df['review'], max_words=55, title='Word Cloud - Top 55 Frequent Words')

# Task 4: Explore the distributions of bi-grams and tri-grams using preprocessed tokens
explore_ngrams(df['review'], ngram_range=(2, 3), top_n=10)
