from PyPDF2 import PdfReader, PdfWriter

pdf_path = "sample.pdf"

reader = PdfReader(pdf_path)

# First part: pages 1 to 100
writer1 = PdfWriter()
for i in range(0, 13):
    writer1.add_page(reader.pages[i])
with open("part1.pdf", "wb") as f:
    writer1.write(f)

# Second part: pages 101 to end
writer2 = PdfWriter()
for i in range(13, len(reader.pages)):
    writer2.add_page(reader.pages[i])
with open("part2.pdf", "wb") as f:
    writer2.write(f)

print("PDF split complete.")
