import pandas as pd

# Load the Excel file
file_path = "compare_excel_ref_and_id.xlsx"

# Read both sheets
new_df = pd.read_excel(file_path, sheet_name="New")
old_df = pd.read_excel(file_path, sheet_name="All_old")

# Ensure column names match exactly
new_df.columns = new_df.columns.str.strip()
old_df.columns = old_df.columns.str.strip()

# Merge with indicator to find differences
merged = new_df.merge(old_df, on=["Ref", "Source ID"], how="left", indicator=True)

# Filter rows that are only in "New"
not_in_old = merged[merged["_merge"] == "left_only"][["Ref", "Source ID"]]

# Show results
print("🔍 Records in 'New' but not in 'All_old':")
print(not_in_old)

# Optionally, save to Excel
not_in_old.to_excel("missing_in_old.xlsx", index=False)
print("\n✅ Results saved to 'missing_in_old.xlsx'")
