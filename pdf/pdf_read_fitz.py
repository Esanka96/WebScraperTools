import fitz  # PyMuPDF

pdf_path = "sample.pdf"

# Open the PDF
doc = fitz.open(pdf_path)

# Get the first page (index 0)
page = doc[0]

# Extract text
text = page.get_text()

print(text)

# Close the document
doc.close()
