import os
import shutil

# Base directory containing all folders
base_dir = r"D:\INNODATA\ISM\ZZZZ\Completed"

# Output directory for zip files
zip_output_dir = os.path.join(base_dir, "zip_file")

# Create the output folder if it doesn't exist
os.makedirs(zip_output_dir, exist_ok=True)

# Loop through each folder inside the base directory
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)

    # Skip the zip_file directory and only process other folders
    if folder_name == "zip_file":
        continue

    if os.path.isdir(folder_path):
        zip_path = os.path.join(zip_output_dir, folder_name)
        shutil.make_archive(zip_path, 'zip', folder_path)
        print(f"Created zip: {zip_path}.zip")

print("All folders (except 'zip_file') have been zipped successfully.")
