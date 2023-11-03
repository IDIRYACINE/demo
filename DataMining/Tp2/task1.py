import PyPDF2
import pdfplumber


extraction_method_pyPdf = 'PyPDF2'
extraction_method_pyplumber = 'pdfplumber'

def extract_text_from_pdf(file_path, method=extraction_method_pyPdf):
    if method == extraction_method_pyPdf:

        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extractText()
        print('Using PyPDF2:', text)

    else :
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text()
        print('Using pdfplumber:', text)


extract_text_from_pdf('pdfData.pdf', extraction_method_pyPdf)