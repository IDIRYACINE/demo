from spellchecker import SpellChecker
import nltk
from nltk import word_tokenize, pos_tag

from polyglot.text import Text
from polyglot.downloader import downloader
import language_tool_python
from langid.langid import LanguageIdentifier, model

# Install necessary resources for Polyglot (if not installed)
# downloader.download("embeddings2.en")
# downloader.download("embeddings2.fr")
# downloader.download("embeddings2.ar")
# nltk.download('punkt')
def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def spell_check_with_context(text):
    # Initialize LanguageTool
    tool = language_tool_python.LanguageTool('en-US')

    # Perform spell-checking
    matches = tool.check(text)

    # Get suggested corrections for potential misspellings
    corrections = [match.replacements for match in matches]

    return corrections

def context_aware_spell_check(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    spell = SpellChecker()

    misspelled_words = spell.unknown(words)

    corrections = {}
    for word in misspelled_words:
        suggestions = spell.candidates(word)
        
        word_pos_tag = [tag for _, tag in pos_tags if _ == word][0]

        suggestions = [s for s in suggestions if pos_tag([s])[0][1] == word_pos_tag]

        if suggestions:
            best_suggestion = max(suggestions, key=spell.word_probability)
            corrections[word] = best_suggestion

    corrected_text = ' '.join(corrections.get(word, word) for word in words)
    return corrected_text



def spell_check_multilingual(text, custom_words=None, custom_language_codes=None):
    # Initialize language identifier
    identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

    # Initialize SpellChecker
    spell = SpellChecker()

    # Add custom words to the dictionary
    if custom_words:
        for word in custom_words:
            spell.word_frequency.load_words([word])

    words = text.split()

    language_tags = [identifier.classify(word)[0] for word in words]

    corrections = {}
    for lang_code in set(language_tags):
        try:
            lang_spell = SpellChecker(language=lang_code)
        except ValueError:
            lang_spell = SpellChecker(language='en')  # Use English as default if the language is not supported
        misspelled = lang_spell.unknown([word for word, tag in zip(words, language_tags) if tag == lang_code])
        for word in misspelled:
            suggestions = lang_spell.candidates(word)
            corrections[word] = suggestions

    return corrections

def test_context_aware_spell_check():
    text = "This is a wrld of hope and happines."
    corrected_text = spell_check_with_context(text)
    print(corrected_text)

def test_multilingual_spell_check():
    input_file_path = 'multi_input.txt'

    multilingual_text = read_text_file(input_file_path)

    if multilingual_text:
        # Define custom words and language codes as needed
        custom_words = ['customword1', 'customword2']
        custom_language_codes = ['en', 'fr', 'es']  # English, French, Spanish

        corrections = spell_check_multilingual(multilingual_text, custom_words=custom_words, custom_language_codes=custom_language_codes)

        print("Original text:")
        print(multilingual_text)
        print("\nSuggested corrections:")
        for word, suggestions in corrections.items():
            print(f"{word}: {suggestions}")  

test_context_aware_spell_check()
test_multilingual_spell_check()