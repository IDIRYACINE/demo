import re

def case_insensitive_search(text, target_word):
    lower_text = text.lower()
    lower_target_word = target_word.lower()
    indices = []
    for match in re.finditer(f"{lower_target_word}", lower_text):
        indices.append((match.start(), match.end()))
    return indices

def title_case(text, exceptions):
    words = text.split()
    titled_words = []
    for word in words:
        if word.lower() in exceptions:
            titled_words.append(word)
        else:
            titled_words.append(word.capitalize())
    return " ".join(titled_words)


text_sample = "Python is an interpreted, high-level, general-purpose programming language python. " 

print(case_insensitive_search(text_sample, "Python"))