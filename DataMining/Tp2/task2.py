import docx
import os
import os

def count_words_in_docx_file(filne_name):


    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    file_path = os.path.join(parent_dir, filne_name)

    doc = docx.Document(filne_name)

    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text

    words = text.split()

    num_words = len(words)

    return num_words

count = count_words_in_docx_file("Td.docx")

print(count)