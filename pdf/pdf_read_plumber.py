import pdfplumber

# pdf_path = "sample.pdf"

pdf_path = "sample.pdf"
#
# with pdfplumber.open(pdf_path) as pdf:
#     first_page = pdf.pages
#     page_text = first_page.extract_text()
#     print(page_text)


# with pdfplumber.open(pdf_path) as pdf:
#     for i, page in enumerate(pdf.pages, start=1):
#         text = page.extract_text()
#         print(f"--- Page {i} ---")
#         print(text)

# with pdfplumber.open(pdf_path) as pdf:
#     for i, page in enumerate(pdf.pages, start=1):
#         text = page.extract_text()
#
#         # Check if the marker exists on this page
#         marker = "Name of Volatile Substances Products"
#         if marker in text:
#             # Extract everything after the marker
#             after_text = text.split(marker, 1)[1].strip()
#             print(f"--- Page {i} After Marker ---")
#             print(after_text.split("\n"))


# with pdfplumber.open(pdf_path) as pdf:
#     # pdf.pages is 0-based, so page 23 = index 22, page 24 = index 23
#     for page_num in [0]:
#         page = pdf.pages[page_num]
#         text = page.extract_text()
#         print(f"--- Page {page_num + 1} ---")
#         print(text)


with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[8]
    text = page.extract_text().split("\n")
    print(text)




