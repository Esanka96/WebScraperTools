import pdfplumber

def corrected_chem_name(text):
    if "\n" in text:
        if "-\n" in text:
            text = text.replace("-\n","-").replace("\n", " ")
        else:
            text = text.replace("\n", " ")
    else:
        text = text
    return text

pdf_path = "sample.pdf"

table_settings = {
    "vertical_strategy": "explicit",
    "explicit_vertical_lines": [60, 110,190, 330,550],
}

with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[7]
    chem_list = []
    table = page.extract_table(table_settings)

    for row in table:
        if "AND the\npecific chemic" in row[0]:
            break
        chem_list.append(row)

    for sin in chem_list[1:]:
        ids = sin[0]
        cas = sin[1]
        drug = sin[2]
        chem = corrected_chem_name(sin[3])
        print(ids)
        print(cas)
        print(drug)
        print(chem)
        print()
