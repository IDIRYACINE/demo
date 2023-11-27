import re 

def remove_excess_whitespace(text):
    pattern = r"\s+"
    clean_text = re.sub(pattern, " ", text)
    return clean_text

def preserve_formatting_preformatted_blocks(text):
    blocs_pattern = r'```[\w+\s+\n]+```'
    blocks = re.findall(blocs_pattern,text)
    temp_text = re.sub(blocs_pattern, "{}", text)
    cleaned_text = remove_excess_whitespace(temp_text)
    return cleaned_text.format(*blocks)


def retain_paragraph_newlines(text):

    text = re.sub(' +', ' ', text).strip()
    text = re.sub(r'\n{2,}', '\n', text)
    return text 


text = """The dog is laying on the bed      . I hope its confortable.'something' <another>
gdg"""

text_two = """The dog is laying on the bed   ``` gg
gg     cxs```   . I hope its confortable.'something' <another>
gdg"""

text_three = """The dog is laying on the bed   ``` gg 
    gsgs 

    


    gsgsg This is some text\n\nwith multiple   spaces\nand\nnewlines.
"""
print(remove_excess_whitespace(text))
print(preserve_formatting_preformatted_blocks(text_two))
print(retain_paragraph_newlines(text_three))