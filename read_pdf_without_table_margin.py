import pdfplumber

pdf_path = "sample.pdf"

table_settings = {
    "vertical_strategy": "explicit",
    "explicit_vertical_lines": [60, 200, 350,550]
}

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[8]  # Page 9
    table = page.extract_table(table_settings)

    for row in table:
        print(row)
