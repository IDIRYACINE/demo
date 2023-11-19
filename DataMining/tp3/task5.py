import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag

def remove_stopwords_context_aware(text):
    stopwords_set = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    filtered_tokens = []
    for token, pos_tag in pos_tags:
        if pos_tag not in ['DT', 'PRP', 'CC', 'IN', 'TO', 'JJ']:
            filtered_tokens.append(token)

    return filtered_tokens

text = "The quick brown fox jumps over the lazy dog."
filtered_tokens = remove_stopwords_context_aware(text)
print("Filtered tokens:", filtered_tokens)
