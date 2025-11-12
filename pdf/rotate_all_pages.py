from PyPDF2 import PdfReader, PdfWriter

input_pdf = "sample.pdf"
output_pdf = "rotated.pdf"

reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    page.rotate(90)
    writer.add_page(page)

with open(output_pdf, "wb") as f:
    writer.write(f)

print("✅ PDF rotated and saved as", output_pdf)
