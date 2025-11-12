import os
import re

base_path = r"D:\INNODATA\ISM\Completed"

output_file = "my_ref_num.txt"

folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

ref_numbers = []
for folder in folders:
    match = re.search(r"Ref_(\d+)", folder)
    if match:
        ref_numbers.append(int(match.group(1)))

ref_numbers.sort()

with open(output_file, "w") as file:
    for num in ref_numbers:
        file.write(f"{num}\n")

print(f"Ref numbers saved to {output_file}")
