import pandas as pd

# --- File paths ---
excel_path = r"C:\Users\SL1047\Desktop\New folder (4)\text_file\Web Automation.xlsx"
text_path = r"C:\Users\SL1047\Desktop\New folder (4)\text_file\Ref_num.txt"

# --- Read Excel file ---
df = pd.read_excel(excel_path)

# Ensure the column name matches exactly
excel_numbers = df["Ref"].astype(str).str.strip()

# --- Read text file ---
with open(text_path, "r") as f:
    text_numbers = [line.strip() for line in f if line.strip()]

# --- Find numbers not in Excel ---
missing_numbers = [num for num in text_numbers if num not in excel_numbers.values]

# --- Show or save results ---
print("Numbers NOT in Excel:")
for num in missing_numbers:
    print(num)

# Optionally save to a file
with open("missing_numbers.txt", "w") as f:
    f.write("\n".join(missing_numbers))
