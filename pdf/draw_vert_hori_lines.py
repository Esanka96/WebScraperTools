import pdfplumber

pdf_path = "sample.pdf"

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[25]

    lines = page.extract_text_lines()

    horizontal_lines = []

    for line in lines:
        top = line["top"]
        bottom = line["bottom"]
        height = int(bottom - top)
        new_height = int(top+height+1)
        horizontal_lines.append(new_height)

    table_settings = {
        "horizontal_strategy": "explicit",
        "explicit_horizontal_lines": horizontal_lines,
        "vertical_strategy": "explicit",
        "explicit_vertical_lines": [60, 200, 550],
    }

    # when first line doesn't appear.

    # first_top = lines[0]["top"]
    # horizontal_lines.insert(0, int(first_top) - 10)
    #
    # table_settings = {
    #     "horizontal_strategy": "explicit",
    #     "explicit_horizontal_lines": horizontal_lines,
    #     "vertical_strategy": "explicit",
    #     "explicit_vertical_lines": [20, 140, 370, 450, 550],
    # }

    chem_list = []
    table = page.extract_table(table_settings)

    for row in table:
        if "1 Components of" in row[0]:
            break
        chem_list.append(row)

    for sin in chem_list:
        print(sin)