import os
import zipfile

# Path to your main folder
base_dir = r"C:\Users\SL1047\Desktop\New folder (4)\check\New folder"

# Folder where zip files will be saved
zip_folder = os.path.join(base_dir, "Zip_folder")

# Create Zip_folder if it doesn't exist
os.makedirs(zip_folder, exist_ok=True)

# Loop through all items in the base directory
for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)

    # Only process subfolders (ignore files and Zip_folder itself)
    if os.path.isdir(item_path) and item != "Zip_folder":
        # Define zip file path
        zip_path = os.path.join(zip_folder, f"{item}.zip")

        # Create a zip file for this subfolder
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(item_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, item_path)
                    zipf.write(file_path, arcname)

        print(f"✅ Zipped folder: {item} -> {zip_path}")

print("\n🎉 All subfolders have been zipped into 'Zip_folder' successfully!")
