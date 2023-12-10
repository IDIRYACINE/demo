import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def perform_stemming(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

def perform_lemmatization(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_tokens

# Example usage:
# Read the CSV file with preprocessed data
file_path = 'output/preprocessed.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Choose either stemming or lemmatization based on your preference
# Uncomment the line that corresponds to your choice

# Perform stemming
# df['stemmed_review'] = df['review'].apply(perform_stemming)

# Perform lemmatization
df['lemmatized_tokens'] = df['tokens'].apply(perform_lemmatization)

# Feature extraction methods

# Bag of Words
vectorizer_bow = CountVectorizer()
X_bow = vectorizer_bow.fit_transform(df['lemmatized_tokens'])
df_bow = pd.DataFrame(X_bow.toarray(), columns=vectorizer_bow.get_feature_names_out())

# TF-IDF
vectorizer_tfidf = TfidfVectorizer()
X_tfidf = vectorizer_tfidf.fit_transform(df['lemmatized_tokens'])
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=vectorizer_tfidf.get_feature_names_out())

# Display the first few rows of the DataFrames (Bag of Words and TF-IDF)
print("Bag of Words DataFrame:")
print(df_bow.head())

print("\nTF-IDF DataFrame:")
print(df_tfidf)
