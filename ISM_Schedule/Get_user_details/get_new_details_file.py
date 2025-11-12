import pandas as pd

# --- File paths ---
numbers_file = r"C:\Users\SL1047\Desktop\New folder (4)\ISM_Schedule\Get_user_details\Ref_number.txt"
excel_file = r"C:\Users\SL1047\Desktop\New folder (4)\ISM_Schedule\Get_user_details\User Allocation.xlsx"
output_file = r"C:\Users\SL1047\Desktop\New folder (4)\ISM_Schedule\Get_user_details\Out.txt"

# --- Read numbers from text file ---
with open(numbers_file, 'r', encoding='utf-8') as f:
    numbers = [line.strip() for line in f if line.strip().isdigit()]

# --- Read Excel file ---
df = pd.read_excel(excel_file)

# --- Ensure 'Ref' column is string for matching ---
df['Ref'] = df['Ref'].astype(str)

# --- Filter rows where Ref matches any number ---
filtered = df[df['Ref'].isin(numbers)]

# --- Write to new text file ---
with open(output_file, 'w', encoding='utf-8') as f:
    for _, row in filtered.iterrows():
        f.write(f"{row['Ref']},{row['UID']},{row['Email']},\n")

print(f"✅ Done! Output saved to: {output_file}")
