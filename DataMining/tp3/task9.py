import nltk
from nltk.corpus import wordnet
from nltk.metrics.distance import Jaro_Winkler

def context_aware_spell_checking(text):
    tokens = word_tokenize(text)
    corrected_tokens = []

    for token in tokens:
        if token not in wordnet.words():
            suggestions = []
            for word in wordnet.words():
                distance = Jaro_Winkler.distance(token, word)
                if distance > 0.8:
                    suggestions.append((word, distance))

            if suggestions:
                most_similar_word, distance = max(suggestions, key=lambda x: x[1])
                corrected_tokens.append(most_similar_word)
            else:
                corrected_tokens.append(token)
        else:
            corrected_tokens.append(token)

    corrected_text = " ".join(corrected_tokens)
    return corrected_text

import nltk
from nltk.corpus import wordnet

def multilingual_spell_checking(text):
    languages = ["english", "french", "spanish"]
    corrected_tokens = []

    for token in text.split():
        language_detected = False

        for language in languages:
            if token in wordnet.words(lang=language):
                corrected_tokens.append(token)
                language_detected = True
                break

        if not language_detected:
            # Check custom words and domain-specific vocabulary
            if token in custom_words_set or token in domain_specific_vocabulary_set:
                corrected_tokens.append(token)
            else:
                # If no match found, consider it a misspelling
                corrected_tokens.append("[MISSPELLED: " + token + "]")

    corrected_text = " ".join(corrected_tokens)
    return corrected_text
