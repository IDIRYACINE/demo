import re

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

def replace_quotes(text,pattern):
    placeholder = "{}"
    new_text = re.sub(pattern, placeholder, text)
    return new_text

def remove_punctuation_except_quotes(text) : 
    quotes = extract_quotes(text)
    temp_text = replace_quotes(text,quotes_pattern)
    cleaned_text = re.sub(r"[,.?!;']", "", temp_text)

    return cleaned_text.format(*quotes)


def remove_punctuation_keep_abbreviations(text) :
    abbs_pattern = r'\b(?:([A-Z]{2,}[a-z]|[A-Z][a-z]{2,})\.)+\b'
    abbrevieations = re.findall(abbs_pattern,text)
    temp_text = replace_quotes(text,abbs_pattern)
    cleaned_text = re.sub(r"[,.?!;]", "", temp_text)
    return cleaned_text.format(*abbrevieations)

def remove_special_chars_except_code_blocks(text) : 
    blocs_pattern = r'\`\`\`(.*?)\`\`\`'
    blocks = re.findall(blocs_pattern,text)
    temp_text = replace_quotes(text,blocs_pattern)
    cleaned_text = re.sub(r"[,.?!;]", "", temp_text)
    return cleaned_text.format(*blocks)



text = "The dog is laying on the bed. I hope its confortable. 'something.?' <another>"
text_with_abbreviations = "Gojo Satoru E.g. : something something U.S.A ??"
text_with_blocks = " ``` bloc. ,?!``` outsid ??.,!"


# print(remove_punctuation_except_quotes(text))
# print(remove_punctuation_keep_abbreviations(text_with_abbreviations))
print(remove_special_chars_except_code_blocks(text_with_blocks))