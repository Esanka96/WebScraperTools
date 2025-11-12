import requests
import fitz
from io import BytesIO

url = "http://www.trendscarbo.com/sample-paper/1-12T-TCR-120401-Sample-paper.pdf"
response = requests.get(url)
response.raise_for_status()

pdf_bytes = BytesIO(response.content)
doc = fitz.open(stream=pdf_bytes, filetype="pdf")

# Extract all text at once
all_text = ""
for page in doc:
    all_text += page.get_text().replace("\n","") + "\n"

print(all_text)
