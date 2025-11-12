import camelot

# Path to the PDF file
pdf_path = 'part1.pdf'

# Extract all tables from all pages
tables = camelot.read_pdf(pdf_path, pages='all')

# Iterate through the tables and print row data
for i, table in enumerate(tables):
    for index, row in table.df.iterrows():
        print(f"Row {index + 1}: {row.tolist()}")
        print(len(row))
    print()
