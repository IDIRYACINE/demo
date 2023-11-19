import nltk
from nltk import word_tokenize, pos_tag
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.stem import PorterStemmer
from polyglot.text import Text
from polyglot.downloader import downloader


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')

def contextual_stem_lemmatize(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    processed_words = []

    for word, posTag in pos_tags:
        if posTag.startswith('N'):  # Nouns
            processed_words.append(lemmatizer.lemmatize(word, pos='n'))
        elif posTag.startswith('V'):  # Verbs
            processed_words.append(lemmatizer.lemmatize(word, pos='v'))
        elif posTag.startswith('R'):  # Adverbs
            processed_words.append(stemmer.stem(word))
        else:
            processed_words.append(word)

    return ' '.join(processed_words)

# Example usage
text = "Running through the fields, runners ran races. Running is a healthy activity."
processed_text = contextual_stem_lemmatize(text)
print(processed_text)

# Install necessary resources for Polyglot (if not installed)
# downloader.download("embeddings2.en")
# downloader.download("embeddings2.fr")
# downloader.download("embeddings2.ar")

def multilingual_stem_lemmatize(text):
    # Create a Polyglot Text object
    polyglot_text = Text(text)

    # Process each Polyglot Word object in the text and apply stemming and lemmatization
    processed_words = []
    for poly_word in polyglot_text.words:
        if poly_word.language.encode == 'en':
            processed_words.append(PorterStemmer().stem(poly_word))
        elif poly_word.language.encode == 'fr':
            processed_words.append(poly_word.morphemes[0])  # Assuming the first morpheme is the root
        elif poly_word.language.encode == 'ar':
            processed_words.append(poly_word.root)

    return ' '.join(processed_words)

# Example usage
multilingual_text = "Hello, comment ça va? مرحبًا بك في Polyglot."
processed_multilingual_text = multilingual_stem_lemmatize(multilingual_text)
print(processed_multilingual_text)
