import re

def remove_html_tags(html_text):
    pattern = r"<.*?>"
    clean_text = re.sub(pattern, "", html_text)
    clean_text = re.sub(r"&nbsp;", " ", clean_text)
    return clean_text


import re

def remove_urls_and_links(text):
    pattern = r"<a href='(.*?)'>(.*?)</a>"
    processed_text = re.sub(pattern, r"\2", text)
    pattern = r"https?://\S+"
    processed_text = re.sub(pattern, "", processed_text)
    return processed_text


text = """<p>Here is a link to <a href='https://www.google.com'>Google</a></p>"""

print(remove_html_tags(text))
print(remove_urls_and_links(text))