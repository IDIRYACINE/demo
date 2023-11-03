import docx

def count_words_in_docx_file(file_path):
    doc = docx.Document(file_path)

    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text

    words = text.split()

    num_words = len(words)

    return num_words

count_words_in_docx_file("../Td.docx")