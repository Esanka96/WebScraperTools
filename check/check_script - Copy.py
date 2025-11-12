import pytesseract
from PIL import Image
import pandas as pd

# Set tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
image = Image.open("image.gif")

# Run OCR with bounding box output
ocr_data = pytesseract.image_to_data(image, lang="eng", output_type=pytesseract.Output.DATAFRAME)

# Drop empty text results
ocr_data = ocr_data.dropna(subset=["text"])

# Reset index
ocr_data = ocr_data.reset_index(drop=True)

# Group words into lines (using block_num + par_num + line_num)
lines = []
for _, line_df in ocr_data.groupby(["block_num", "par_num", "line_num"]):
    line_text = " ".join(line_df["text"].tolist())
    lines.append(line_text)

print("🔹 OCR Lines Detected:")
for l in lines:
    print(l)

# ---- Build DataFrame with a for loop ----
rows = []  # collect rows here
for line in lines:
    row = line.split()
    print(line)# split each line into words/columns
    rows.append(row)     # add to list

# df = pd.DataFrame(rows)
#
# print("\n🔹 DataFrame Table:")
# print(df)
