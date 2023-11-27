# Import necessary libraries
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd

# Step 1: Tokenize each review
def tokenize(review):
    return nltk.word_tokenize(review)

# Step 2a: Create a bag of words representation
def create_bag_of_words(reviews):
    vectorizer = CountVectorizer(tokenizer=tokenize)
    X = vectorizer.fit_transform(reviews)
    return X, vectorizer

# Step 2b: Create a TF-IDF representation
def create_tfidf(reviews):
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    X = vectorizer.fit_transform(reviews)
    return X, vectorizer

# Step 3: Sentiment Analysis
def manual_sentiment_analysis():
    # Manually predict sentiment (positive or negative)
    # Replace the example reviews and sentiments with your data
    reviews = ["This product is amazing!", "I'm not satisfied with the service."]
    sentiments = ["positive", "negative"]
    return reviews, sentiments

# Step 4a: Identify top 3 words with highest importance for each sentiment
def get_top_words(X, vectorizer, sentiment, top_n=3):
    words = vectorizer.get_feature_names_out()
    word_freq = X.sum(axis=0).A1
    indices = word_freq.argsort()[-top_n:][::-1]
    top_words = [words[i] for i in indices]
    return top_words

# Step 4b: Identify top 3 words with highest TF-IDF values for each sentiment
def get_top_tfidf_words(X, vectorizer, sentiment, top_n=3):
    words = vectorizer.get_feature_names_out()
    tfidf_values = X.max(axis=0).toarray()[0]
    indices = tfidf_values.argsort()[-top_n:][::-1]
    top_words = [words[i] for i in indices]
    return top_words

# Step 5a: Provide a summary of findings
def summary(reviews, sentiments, bag_of_words_top_words, tfidf_top_words):
    for i in range(len(reviews)):
        print(f"\nReview: {reviews[i]}\nSentiment: {sentiments[i]}")
        print(f"Top words (Bag of Words): {bag_of_words_top_words[i]}")
        print(f"Top words (TF-IDF): {tfidf_top_words[i]}")

# Step 5b: Compare and contrast the results
def compare_results(bag_of_words_top_words, tfidf_top_words):
    for i in range(len(bag_of_words_top_words)):
        print(f"\nReview {i+1}:")
        print(f"Bag of Words Top Words: {bag_of_words_top_words[i]}")
        print(f"TF-IDF Top Words: {tfidf_top_words[i]}")

# Main script
if __name__ == "__main__":
    # Sample data
    reviews, sentiments = manual_sentiment_analysis()

    # Bag of Words Representation
    X_bow, vectorizer_bow = create_bag_of_words(reviews)
    bag_of_words_top_words = [get_top_words(X_bow, vectorizer_bow, sentiment) for sentiment in sentiments]

    # TF-IDF Representation
    X_tfidf, vectorizer_tfidf = create_tfidf(reviews)
    tfidf_top_words = [get_top_tfidf_words(X_tfidf, vectorizer_tfidf, sentiment) for sentiment in sentiments]

    # Step 3: Sentiment Analysis
    summary(reviews, sentiments, bag_of_words_top_words, tfidf_top_words)

    # Step 4: Compare and contrast results
    compare_results(bag_of_words_top_words, tfidf_top_words)
