import pdfplumber
from PyPDF2 import PdfReader, PdfWriter

pdf_path = "part1.pdf"
page_number = 3  # Human-readable
index = page_number - 1

# Step 1: Rotate the page using PyPDF2
reader = PdfReader(pdf_path)
writer = PdfWriter()

page = reader.pages[index]
page.rotate(90)  # Rotate 90° clockwise
writer.add_page(page)

# Save rotated page to a temporary file
temp_path = "temp_rotated.pdf"
with open(temp_path, "wb") as f:
    writer.write(f)

# Step 2: Read the rotated page with pdfplumber
with pdfplumber.open(temp_path) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()
    print(f"--- Page {page_number} (rotated 90° clockwise) ---")
    print(text)



