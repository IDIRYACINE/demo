
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer, RegexpTokenizer, word_tokenize, TreebankWordTokenizer
import nltk

nltk.download('punkt')

def custom_tokenization(text):
    tokens = []
    token = ""
    token_type = None

    for char in text:
        if char.isalnum():
            token += char
            token_type = "word"
        elif char.isspace():
            if token != "":
                tokens.append((token, token_type))
                token = ""
                token_type = None
        else:
            if token != "":
                tokens.append((token, token_type))
                token = ""
                token_type = None
            tokens.append((char, "punctuation"))

    if token != "":
        tokens.append((token, token_type))

    return tokens

text_example = "This is an example sentence. It contains punctuation, e.g., commas and periods!"
tokens_example = custom_tokenization(text_example)
print(tokens_example)

def sentence_tokenization_and_word_count(filename):
    with open(filename, 'r') as f:
        text = f.read()

    sentences = sent_tokenize(text)

    for sentence in sentences:
        word_count = len(sentence.split())
        print(f"Sentence: {sentence}")
        print(f"Word count: {word_count}")


filename = 'input.txt'
sentence_tokenization_and_word_count(filename)

# Existing text corpus
text_corpus = "This is a sample text. It has multiple sentences. For example, sentence one. Sentence two!"

# a. Default nltk.sent_tokenize()
sentences_default = sent_tokenize(text_corpus)
print("Default nltk.sent_tokenize():")
for i, sentence in enumerate(sentences_default, 1):
    print(f"Sentence {i}: {sentence}")
print()

# b. PunktSentenceTokenizer
punkt_tokenizer = PunktSentenceTokenizer()
sentences_punkt = punkt_tokenizer.tokenize(text_corpus)
print("PunktSentenceTokenizer:")
for i, sentence in enumerate(sentences_punkt, 1):
    print(f"Sentence {i}: {sentence}")
print()

# c. RegexpTokenizer
regexp_tokenizer = RegexpTokenizer(r'\w+|[^\w\s]')
tokens_regexp = regexp_tokenizer.tokenize(text_corpus)
print("RegexpTokenizer:")
print("Tokens:", tokens_regexp)
print()

# d. nltk.word_tokenize()
tokens_word = word_tokenize(text_corpus)
print("nltk.word_tokenize():")
print("Tokens:", tokens_word)
print()

# e. The TreebankWordTokenizer
treebank_tokenizer = TreebankWordTokenizer()
tokens_treebank = treebank_tokenizer.tokenize(text_corpus)
print("TreebankWordTokenizer:")
print("Tokens:", tokens_treebank)