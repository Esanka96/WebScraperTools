import pdfplumber

pdf_path = "sample.pdf"

txt_path = "rows.txt"
with open(txt_path, "w", encoding="utf-8") as f:
    f.write("")
chem_list = []

with pdfplumber.open(pdf_path) as pdf:
    for page_index in range(5, 375):
        page = pdf.pages[page_index]
        all_tables = page.extract_tables()

        for table_index, table in enumerate(all_tables):
            for row in table:
                with open(txt_path, "a", encoding="utf-8") as f:
                    f.write(str(row) + "\n")
