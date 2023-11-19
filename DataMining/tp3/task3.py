import re 

def remove_excess_whitespace(text):
    pattern = r"\s+"
    clean_text = re.sub(pattern, " ", text)
    return clean_text

def preserve_formatting_preformatted_blocks(text):
    pattern = r"(`(.*?)`)"
    formatted_blocks = re.findall(pattern, text)
    for formatted_block in formatted_blocks:
        text = text.replace(formatted_block, f"{formatted_block}\n")
    pattern = r"\s+"
    clean_text = re.sub(pattern, " ", text)
    return clean_text

def retain_paragraph_newlines(text):
    pattern = r"\n+"
    clean_text = re.sub(pattern, "\n", text)
    return clean_text


text = """The dog is laying on the bed      . I hope its confortable.'something' <another>
gdg"""

print(remove_excess_whitespace(text))
print(preserve_formatting_preformatted_blocks(text))
print(retain_paragraph_newlines(text))