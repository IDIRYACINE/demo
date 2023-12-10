import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker

def tokenize_text(text):
    return word_tokenize(text)

def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def spell_correction(tokens):
    spell = SpellChecker()
    corrected_tokens = [spell.correction(token) for token in tokens]
    return ' '.join(corrected_tokens)

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def remove_links(text):
    return re.sub(r'http\S+', '', text)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(filtered_tokens)

file_path = 'output/preprocessed.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# df['review'] = df['review'].apply(remove_links)
# df['review'] = df['review'].apply(remove_special_characters)
# df['review'] = df['review'].apply(remove_punctuation)
# df['review'] = df['review'].apply(remove_stopwords)

# df = df[df['review'].notna()]
# tokens =  df['review'].apply(tokenize_text)
tokens = df['tokens']
tokens = tokens.apply(spell_correction)
df['tokens'] = tokens

output_file_path = 'output/preprocessed.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8')

