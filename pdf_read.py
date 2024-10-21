from PyPDF2 import PdfReader
from datetime import datetime
import unicodedata

def read_pdf(pdf_path):
    file_path = pdf_path
    reader = PdfReader(file_path)
    text=reader.pages[0].extract_text()
    print(text)




path='1.pdf'

text1=read_pdf(path)

