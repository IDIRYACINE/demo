from spellchecker import SpellChecker
import nltk
from nltk import word_tokenize, pos_tag

from polyglot.text import Text
from polyglot.downloader import downloader


nltk.download('punkt')

def context_aware_spell_check(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)

    spell = SpellChecker()

    misspelled_words = spell.unknown(words)

    corrections = {}
    for word in misspelled_words:
        suggestions = spell.candidates(word)
        # Consider only suggestions that have the same POS tag
        suggestions = [s for s in suggestions if pos_tag([s])[0][1] == pos_tag([word])[0][1]]

        if suggestions:
            best_suggestion = max(suggestions, key=spell.word_probability)
            corrections[word] = best_suggestion

    # Apply corrections to the original text
    corrected_text = ' '.join(corrections.get(word, word) for word in words)
    return corrected_text

# Example usage
text = "The dog is laying on the bed. I hope its confortable."
corrected_text = context_aware_spell_check(text)
print(corrected_text)

# Install necessary resources for Polyglot (if not installed)
downloader.download("embeddings2.en")
downloader.download("embeddings2.fr")
downloader.download("embeddings2.ar")

def multilingual_spell_check(text, custom_words=None):
    polyglot_text = Text(text)

    # Combine custom words with default spellchecker vocabulary
    if custom_words:
        spell = SpellChecker(custom_words=custom_words)
    else:
        spell = SpellChecker()

    misspelled_words = [word for word in polyglot_text.words if word not in spell.word_frequency]

    corrections = {}
    for word in misspelled_words:
        suggestions = spell.candidates(word)
        if suggestions:
            best_suggestion = max(suggestions, key=spell.word_probability)
            corrections[word] = best_suggestion

    # Apply corrections to the original text
    corrected_text = ' '.join(corrections.get(word, word) for word in polyglot_text.words)
    return corrected_text

# Example usage with custom words
custom_words = {'confortable', 'Polyglot'}
multilingual_text = "Hello, comment ça va? مرحبًا بك في Polyglot."
corrected_multilingual_text = multilingual_spell_check(multilingual_text, custom_words)
print(corrected_multilingual_text)
