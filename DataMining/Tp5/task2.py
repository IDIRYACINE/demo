import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

def tokenize_text(text):
    print("tokenizing")
    return word_tokenize(text)

def remove_special_characters(text):
    print("removing special characters")
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def spell_correction(text):
    print("spell correction")
    blob = TextBlob(text)
    return  blob.correct()

def remove_punctuation(text):
    print("removing punctuation")
    return re.sub(r'[^\w\s]', '', text)

def remove_links(text):
    print("removing links")
    cleaned_text = re.sub(r"<.*?>", "", text)
    re.sub(r'http\S+', '', cleaned_text)
    return cleaned_text

def convert_to_lowercase(text):
    print("converting to lowercase")
    return text.lower()

def remove_stopwords(text):
    print("removing stopwords")
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(filtered_tokens)

file_path = 'output/preprocessed.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# df['review'] = df['review'].apply(convert_to_lowercase)
# df['review'] = df['review'].apply(remove_links)
# df['review'] = df['review'].apply(remove_special_characters)
# df['review'] = df['review'].apply(remove_punctuation)
# df['review'] = df['review'].apply(remove_stopwords)
# df = df[df['review'].notna()]
# df['review'] = df['review'].apply(spell_correction)
# tokens =  df['review'].apply(tokenize_text)

# df['tokens'] = tokens

output_file_path = 'output/preprocessed.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8')

