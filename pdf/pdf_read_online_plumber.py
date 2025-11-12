import requests
import pdfplumber
from io import BytesIO

url = "http://www.trendscarbo.com/sample-paper/1-12T-TCR-120401-Sample-paper.pdf"
response = requests.get(url)
response.raise_for_status()

pdf_bytes = BytesIO(response.content)
with pdfplumber.open(pdf_bytes) as pdf:
    all_text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

print(all_text)
