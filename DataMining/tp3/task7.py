import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

def context_aware_stemming_lemmatization(text):
    porter_stemmer = PorterStemmer()
    wordnet_lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    processed_tokens = []

    for token in tokens:
        if token in technical_jargon_set:
            processed_tokens.append(porter_stemmer.stem(token))
        else:
            processed_tokens.append(wordnet_lemmatizer.lemmatize(token))

    processed_text = " ".join(processed_tokens)
    return processed_text

import nltk
from nltk.stem import LancasterStemmer, SnowballStemmer, WordNetLemmatizer

def multilingual_stemming_lemmatization(text):
    english_stemmer = PorterStemmer()
    french_stemmer = LancasterStemmer()
    arabic_stemmer = SnowballStemmer('arabic')
    wordnet_lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    processed_tokens = []

    for token in tokens:
        if token in english_words_set:
            processed_tokens.append(english_stemmer.stem(token))
        elif token in french_words_set:
            processed_tokens.append(french_stemmer.stem(token))
        elif token in arabic_words_set:
            processed_tokens.append(arabic_stemmer.stem(token))
        else:
            processed_tokens.append(wordnet_lemmatizer.lemmatize(token))

    processed_text = " ".join(processed_tokens)
    return processed_text
