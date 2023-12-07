import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf_vectorize(corpus):

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the corpus
    vectorizer.fit(corpus)

    # Transform the corpus into TF-IDF vectors
    tfidf_matrix = vectorizer.transform(corpus)

    return tfidf_matrix, vectorizer

matrix, vector = tfidf_vectorize(["I like apples", "I like oranges", "I like bananas"])

# Display the TF-IDF matrix
print("TF-IDF Matrix:")
print(matrix.toarray())

# Display the feature names
print("Feature Names:")
print(vector.get_feature_names_out())

