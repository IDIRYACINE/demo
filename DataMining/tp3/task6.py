import re

from bs4 import BeautifulSoup
from html import unescape

def remove_html_tags_and_entities(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    text_without_tags = soup.get_text(separator=' ', strip=True)

    text_without_entities = unescape(text_without_tags)

    return text_without_entities

def remove_urls_and_links(text):
    pattern = r"<a href='(.*?)'>(.*?)</a>"
    processed_text = re.sub(pattern, r"\2", text)
    pattern = r"https?://\S+"
    processed_text = re.sub(pattern, "", processed_text)
    return processed_text


text =  "You can learn more about it from <a href='https://example.com'>this link</a>. Visit https://anotherlink.org for more details."

print(remove_html_tags_and_entities(text))
print(remove_urls_and_links(text))