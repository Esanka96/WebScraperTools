import os
import re
import zipfile
import posixpath

base_dir = r"C:\Users\SL1047\Downloads\Ref_download"
unzip_dir = os.path.join(base_dir, "Unzip_folder")
os.makedirs(unzip_dir, exist_ok=True)

# Extract pattern like "Ref_4101" or "REF_4101" from filenames
pattern = re.compile(r'ref[_\s-]*(\d{1,4})', re.IGNORECASE)

def make_unique_path(dest_folder, filename):
    """If dest_folder/filename exists, append _1, _2, ... before the extension."""
    name, ext = os.path.splitext(filename)
    candidate = filename
    i = 1
    while os.path.exists(os.path.join(dest_folder, candidate)):
        candidate = f"{name}_{i}{ext}"
        i += 1
    return os.path.join(dest_folder, candidate)

def safe_join(base, *paths):
    """Prevent path traversal attacks."""
    final = os.path.normpath(os.path.join(base, *paths))
    if not final.startswith(os.path.normpath(base) + os.sep) and final != os.path.normpath(base):
        raise Exception("Attempted Path Traversal in zip file")
    return final

for name in os.listdir(base_dir):
    if not name.lower().endswith(".zip"):
        continue

    zip_path = os.path.join(base_dir, name)

    # Normalize folder name to "Ref_####"
    m = pattern.search(name)
    if m:
        folder_name = f"Ref_{m.group(1)}"
    else:
        folder_name = os.path.splitext(name)[0].capitalize()

    target_folder = os.path.join(unzip_dir, folder_name)
    os.makedirs(target_folder, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as z:
        for info in z.infolist():
            member = info.filename
            if member.endswith('/') or member.endswith('\\'):
                continue
            if member.startswith('__MACOSX') or member.startswith('.'):
                continue

            basename = posixpath.basename(member)
            if not basename:
                continue

            dest_path = make_unique_path(target_folder, basename)
            dest_path = safe_join(target_folder, os.path.relpath(dest_path, start=target_folder))

            with z.open(info) as src, open(dest_path, 'wb') as dst:
                dst.write(src.read())

        print(f"✅ Extracted: {name} → {target_folder}")

print("🎯 All ZIP files extracted and folder names normalized (Ref_####).")
