import pandas as pd

# Path to your Excel file
input_file = "your_file.xlsx"
output_file = "Duplicate_Refs_Week5_vs_Week4.xlsx"

# Read sheets
week4_df = pd.read_excel(input_file, sheet_name="Week 4")
week5_df = pd.read_excel(input_file, sheet_name="Week 5")

# Convert Ref columns to lists
week4_set = week4_df['Ref'].astype(str).tolist()
week5_set = week5_df['Ref'].astype(str).tolist()

# Find duplicated refs (in both Week 5 and Week 4)
# week4_list = sorted(list(week4_set), key=int)
# week5_list = sorted(list(week5_set), key=int)

week4_list = (list(week4_set))
week5_list = (list(week5_set))

duplicated_list = [ref for ref in week5_list if ref in week4_list]

original_list = [ref for ref in week5_list if not ref in duplicated_list]

print(original_list)
