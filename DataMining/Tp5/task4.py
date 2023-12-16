import pandas as pd
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def perform_stemming(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return ''.join(stemmed_tokens)

def perform_lemmatization(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ''.join(lemmatized_tokens)

# Example usage:
# Read the CSV file with preprocessed data
file_path = 'output/preprocessed.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Choose either stemming or lemmatization based on your preference

# # Perform stemming
# df['stemmed_review'] = df['tokens'].apply(perform_stemming)

# # Perform lemmatization
# df['lemmatized_review'] = df['tokens'].apply(perform_lemmatization)

# output_file_path = 'output/preprocessed.csv'
# df.to_csv(output_file_path, index=False, encoding='utf-8')

# Feature extraction methods
data = df['lemmatized_review']



# print("Number of reviews: {}".format(len(data)))

# Bag of Words
vectorizer_bow = CountVectorizer(lowercase=False)
X_bow = vectorizer_bow.fit_transform(data)
df_bow = pd.DataFrame(X_bow.toarray(), columns=vectorizer_bow.get_feature_names_out())

# TF-IDF
vectorizer_tfidf = TfidfVectorizer(lowercase=False)
X_tfidf = vectorizer_tfidf.fit_transform(data)
df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=vectorizer_tfidf.get_feature_names_out())

# Display the first few rows of the DataFrames (Bag of Words and TF-IDF)
print("Bag of Words DataFrame:")
print(df_bow.head())

print("\nTF-IDF DataFrame:")
print(df_tfidf)
