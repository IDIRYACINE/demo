import arabic_reshaper
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def fix_arabic_text(text):

    reshaped_text = arabic_reshaper.reshape(text)

    rev_text = reshaped_text[::-1]
    return rev_text



def remove_stopwords_with_context(text,language):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Define the list of stopwords
    stop_words = set(stopwords.words(language))

    result_sentences = []

    for sentence in sentences:
        words = word_tokenize(sentence)

        pos_tags = pos_tag(words)

        filtered_words = [word for word, pos in pos_tags if word.lower() not in stop_words or pos.startswith(('VB', 'NN', 'JJ'))]

        result_sentence = ' '.join(filtered_words)
        result_sentences.append(result_sentence)

    result_text = ' '.join(result_sentences)

    return result_text

def test_with_english () :
    input_text = "The quick brown fox jumps over the lazy dog. However, the lazy dog doesn't seem to care ."
    output_text = remove_stopwords_with_context(input_text,'english')
    print("Original text:")
    print(input_text)
    print("\nText after removing stopwords with context:")
    print(output_text)

def test_with_arabic () : 

    input_arabic_text = "هذا هو نص باللغة العربية فوق الطاولة. يمكنك تجربة البرنامج مع أي نص عربي."
    output_arabic_text = remove_stopwords_with_context(input_arabic_text,'arabic')

    print("Original Arabic text:")
    print(fix_arabic_text(input_arabic_text))
    print("\nText after removing Arabic stopwords with context:")
    print(fix_arabic_text(output_arabic_text))


test_with_english()
test_with_arabic()