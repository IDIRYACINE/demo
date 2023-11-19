import re

def remove_punctuation_except_quotes(text):
    pattern = r"[^\w\s'\"']+"
    clean_text = re.sub(pattern, "", text)
    return clean_text

def remove_punctuation_keep_abbreviations(text):
    pattern = r"[^\w\s\.]+"
    abbreviations = ["e.g.", "etc.", "U.S.A."]
    for abbreviation in abbreviations:
        pattern = pattern.replace(f"\.{abbreviation}", f" {abbreviation}")
    clean_text = re.sub(pattern, "", text)
    return clean_text

def remove_special_chars_except_code_blocks(text):
    pattern = r"[^\w\s\n`]+"
    code_blocks = re.findall(r"`(.*?)`", text)
    for code_block in code_blocks:
        text = text.replace(code_block, f"\n{code_block}\n")
    clean_text = re.sub(pattern, "", text)
    return clean_text

