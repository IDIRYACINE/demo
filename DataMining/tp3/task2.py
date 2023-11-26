import re
import nltk
nltk.download('punkt')

quotes_pattern = r'[\'\"](.*?)[\'\"]'

def format_strings(array, format_string):
    formatted_strings = []
    for item in array:
        formatted_string = format_string.format(*item)
        formatted_strings.append(formatted_string)
    return formatted_strings

def extract_quotes(text):
    quotes = re.findall(quotes_pattern, text)    
    return quotes

def replace_quotes(text,pattern,replacement="{}"):
    new_text = re.sub(pattern, replacement, text)
    return new_text

def remove_punctuation_except_quotes(text) : 
    quotes = extract_quotes(text)
    temp_text = replace_quotes(text,quotes_pattern,replacement="'{}'")
    cleaned_text = re.sub(r"[,.?!;']", "", temp_text)

    return cleaned_text.format(*quotes)



def process_text_with_abbreviations(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Identify and replace abbreviations with placeholders
    abbreviations = [word for word in words if re.match(r'\b(?:[A-Z]\.)+', word)]
    abbreviations_map = {abbr: f'replace_{i}' for i, abbr in enumerate(abbreviations)}
    text_with_placeholders = ' '.join([abbreviations_map.get(word, word) for word in words])

    # Remove punctuation from the text (excluding placeholders)
    text_without_punctuation = re.sub(r'[^A-Za-z0-9\s]|_', '', text_with_placeholders)

    # Re-insert preserved abbreviations
    for abbr, replacement in abbreviations_map.items():
        text_without_punctuation = text_without_punctuation.replace(replacement, abbr)

    return text_without_punctuation.strip()

def remove_special_chars_except_code_blocks(text) : 
    blocs_pattern = r'\`\`\`(.*?)\`\`\`'
    blocks = re.findall(blocs_pattern,text)
    temp_text = replace_quotes(text,blocs_pattern,replacement="```{}```")
    cleaned_text = re.sub(r"[,.?!;]", "", temp_text)
    return cleaned_text.format(*blocks)



text = "The dog is laying on the bed. I hope its confortable. 'something.?' <another>"
text_with_abbreviations = "This is an example sentence , with abbreviations like U.S. and Ph.D."
text_with_blocks = " ``` bloc. ,?!``` outsid ??.,!"


print(remove_punctuation_except_quotes(text))
print(process_text_with_abbreviations(text_with_abbreviations))
print(remove_special_chars_except_code_blocks(text_with_blocks))