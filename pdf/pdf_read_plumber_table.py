import pdfplumber

pdf_path = "sample.pdf"


# with pdfplumber.open("sample.pdf") as pdf:
#     for page_index in range(1, 5):  # Pages 15 to 57 (inclusive)
#         page = pdf.pages[page_index]
#         all_tables = page.extract_tables()
#
#         for table_index, table in enumerate(all_tables):
#             print(f"\n--- Page {page_index + 1}, Table {table_index + 1} ---")
#             for row in table:
#                 print(row)

# with pdfplumber.open("sample.pdf") as pdf:
#     for page_index, page in enumerate(pdf.pages):  # Iterate through all pages
#         all_tables = page.extract_tables()
#
#         for table_index, table in enumerate(all_tables):
#             print(f"\n--- Page {page_index + 1}, Table {table_index + 1} ---")
#             for row in table:
#                 print(row)
#                 print(len(row))

# phase = "4 化妆品准用染发剂(1)(2)（表 7）"
# last_phase = "第四章 理化检验方法"
# first_page = last_page = ""
# chem_list = []
# print("⏳ PDF is being read...")
# with pdfplumber.open(pdf_path) as pdf:
#     for i, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         if text and phase.lower() in text.lower():
#             first_page = i
#         if text and last_phase.lower() in text.lower():
#             last_page = i - 1

with pdfplumber.open(pdf_path) as pdf:
    for page_index in range(28, 29):  # Pages 15 to 57 (inclusive)
        page = pdf.pages[page_index]
        all_tables = page.extract_tables()

        for table_index, table in enumerate(all_tables):
            print(f"\n--- Page {page_index + 1}, Table {table_index + 1} ---")
            for row in table:
                print(row)
                print(len(row))











