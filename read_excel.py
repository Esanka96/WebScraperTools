import pandas as pd

# Read the Excel file
df = pd.read_excel("Out.xlsx")

# Assuming your Links are in a column named "Links" and IDs are in a column named "ID"
links_column = df["Link"]
ids_column = df["ID"]

# Process each row
for index, row in df.iterrows():
    link = row["Link"].strip()
    id_value = row["ID"]

    # Now you can use 'link' and 'id_value' as needed
    print(f"{link},{id_value}")
    #print(f"{link}")


