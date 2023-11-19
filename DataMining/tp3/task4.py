
import nltk
from nltk.tokenize import sent_tokenize

def custom_tokenization(text):
    tokens = []
    token_type = "word"
    for char in text:
        if char.isalnum():
            token += char
        elif char.isspace():
            if token != "":
                tokens.append((token, token_type, len(tokens)))
                token = ""
                token_type = "word"
        else:
            if token != "":
                tokens.append((token, token_type, len(tokens)))
                token = ""
                token_type = "punctuation"
            tokens.append((char, token_type, len(tokens)))
            token_type = "word"
    if token != "":
        tokens.append((token, token_type, len(tokens)))
    return tokens

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

text = "This is a sample text with multiple sentences. This is another sentence. And this is the third sentence."

# Default NLTK sentence tokenizer
sentence_tokenization_and_word_count(text, sent_tokenize)

# PunktSentenceTokenizer
tokenizer = PunktSentenceTokenizer()
sentence_tokenization_and_word_count(text, tokenizer)

# RegexpTokenizer
tokenizer = RegexpTokenizer(r'[^\s]+')
sentence_tokenization_and_word_count(text, tokenizer)

# Word tokenizer (tokenizes into words, not sentences)
tokens = word_tokenize(text)
print("Tokens:", tokens)

# TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)