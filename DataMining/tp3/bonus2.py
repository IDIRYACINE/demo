import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import pandas as pd 

reviews = pd.read_csv("reviews.csv")

def tokenize(review):
    return nltk.word_tokenize(review)

def create_bag_of_words(reviews):
    vectorizer = CountVectorizer(tokenizer=tokenize)
    X = vectorizer.fit_transform(reviews)
    return X, vectorizer

def create_tfidf(reviews):
    vectorizer = TfidfVectorizer(tokenizer=tokenize)
    X = vectorizer.fit_transform(reviews)
    return X, vectorizer

def manual_sentiment_analysis(reviews):
    sentiments = ["positive", "negative"]
    # positive_words = ["masterpiece","loved","captivating","engaged"]
    # negative_words = ["couldn't","cry","forced"]
    
    # positive_count = 0
    # negative_count = 0
    # for review in reviews :
    #     for word in review : 
    #         if(word.tolower() in positive_words):
    #             positive_count = positive_count + 1
    #         if(word.tolower() in negative_words):
    #             negative_count = negative_count + 1


            

    
    return reviews, sentiments

def get_top_words(X, vectorizer, sentiment, top_n=3):
    words = vectorizer.get_feature_names_out()
    word_freq = X.sum(axis=0).A1
    indices = word_freq.argsort()[-top_n:][::-1]
    top_words = [words[i] for i in indices]
    return top_words

def get_top_tfidf_words(X, vectorizer, sentiment, top_n=3):
    words = vectorizer.get_feature_names_out()
    tfidf_values = X.max(axis=0).toarray()[0]
    indices = tfidf_values.argsort()[-top_n:][::-1]
    top_words = [words[i] for i in indices]
    return top_words

def summary(reviews, sentiments, bag_of_words_top_words, tfidf_top_words):
    for i in range(len(reviews)):
        print(f"\nReview: {reviews[i]}\nSentiment: {sentiments[i]}")
        print(f"Top words (Bag of Words): {bag_of_words_top_words[i]}")
        print(f"Top words (TF-IDF): {tfidf_top_words[i]}")

def compare_results(bag_of_words_top_words, tfidf_top_words):
    for i in range(len(bag_of_words_top_words)):
        print(f"\nReview {i+1}:")
        print(f"Bag of Words Top Words: {bag_of_words_top_words[i]}")
        print(f"TF-IDF Top Words: {tfidf_top_words[i]}")

# reviews, sentiments = manual_sentiment_analysis()

X_bow, vectorizer_bow = create_bag_of_words(reviews)
bag_of_words_top_words = [get_top_words(X_bow, vectorizer_bow, sentiment) for sentiment in sentiments]

X_tfidf, vectorizer_tfidf = create_tfidf(reviews)
tfidf_top_words = [get_top_tfidf_words(X_tfidf, vectorizer_tfidf, sentiment) for sentiment in sentiments]

# summary(reviews, sentiments, bag_of_words_top_words, tfidf_top_words)

compare_results(bag_of_words_top_words, tfidf_top_words)
