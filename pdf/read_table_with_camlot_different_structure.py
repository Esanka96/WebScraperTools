import camelot

pdf_path = "sample.pdf"

# Load tables from page 2 to 5 (inclusive) of the PDF
# file_path = "sample.pdf"
# pages = "10-11"  # Camelot uses 1-based indexing and inclusive ranges
#
# # flavor="stream" is good for PDFs without visible table lines
# tables = camelot.read_pdf(file_path, pages=pages, flavor="lattice")  # or flavor="stream"
#
# # Iterate through tables
# for i, table in enumerate(tables):
#     print(f"\n--- Table {i + 1} ---")
#     for row in table.data:
#         print(row)
#         print(len(row))


# tables = camelot.read_pdf(pdf_path, pages='all')
#
# # Iterate through the tables and print row data
# for i, table in enumerate(tables):
#     for index, row in table.df.iterrows():
#         print(f"Row {index + 1}: {row.tolist()}")
#         print(len(row))
#     print()
#
# tables = camelot.read_pdf(pdf_path, pages='169')
#
# # Iterate through the tables and print row data
# for i, table in enumerate(tables):
#     print(f"\n--- Table {i + 1} ---")
#     for index, row in table.df.iterrows():
#         print(f"Row {index + 1}: {row.tolist()}")
#         print(len(row))

tables = camelot.read_pdf(pdf_path, pages='24')

# Iterate through the tables and print row data
for i, table in enumerate(tables):
    print(f"\n--- Table {i + 1} ---")
    for index, row in table.df.iterrows():
        print(f"Row {index + 1}: {row.tolist()}")
        print(len(row))

