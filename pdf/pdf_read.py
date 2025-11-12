import re
from PyPDF2 import PdfReader
from datetime import datetime
# import unicodedata

def convert_fullwidth_to_halfwidth(s):
    return s.translate(str.maketrans('０１２３４５６７８９', '0123456789'))

def read_pdf(pdf_path):
    file_path = pdf_path
    reader = PdfReader(file_path)
    text=reader.pages[23].extract_text()
    print(text)




path='sample.pdf'

text1=read_pdf(path)

