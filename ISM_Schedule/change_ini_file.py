import os
import configparser

# Base folders
base_dir = r"C:\Users\SL1047\Downloads\Ref_download\Unzip_folder"
details_file = r"C:\Users\SL1047\Downloads\Ref_download\details.txt"

# Constant values (same for all)
static_values = {
    "download path": r"\\sgpcloud\awsdfs01\MDE_ESPSP-P-IMAGES\SRI LANKA USERS\INTERNET PROCESS FLOW\Files for WC\IA",
    "source id": "78397099",
    "email_sent": "true",
    "check_duplicate": "true",
    "sending address": "ism_monitoring@innodata.com",
    "cc": "arodrigo@innodata.com,mariyarathna@innodata.com,gdias@innodata.com,snambugoda@innodata.com,djayawardena@innodata.com,dchathurani@innodata.com",
    "port": "587"
}

# Read mapping file
mappings = {}
with open(details_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            ref_no, user, recv_addr, cc_extra = [x.strip() for x in line.split(",")]
            mappings[ref_no] = {"user": user, "recv": recv_addr, "cc_extra": cc_extra}
        except ValueError:
            print(f"⚠️ Skipping invalid line: {line}")

# Process each folder
for ref_no, info in mappings.items():
    folder_name = f"Ref_{ref_no}"
    folder_path = os.path.join(base_dir, folder_name)

    if not os.path.exists(folder_path):
        print(f"❌ Folder not found for Ref {ref_no}: {folder_path}")
        continue

    # Find the .ini file in that folder
    ini_file = None
    for file in os.listdir(folder_path):
        if file.lower().endswith(".ini"):
            ini_file = os.path.join(folder_path, file)
            break

    if not ini_file:
        print(f"⚠️ No INI file found in {folder_path}")
        continue

    # Load and update INI
    config = configparser.ConfigParser()
    config.optionxform = str  # preserve case
    config.read(ini_file, encoding="utf-8")

    if "DETAILS" not in config:
        config.add_section("DETAILS")

    # Apply updates
    config.set("DETAILS", "download path", static_values["download path"])
    config.set("DETAILS", "download user", info["user"])
    config.set("DETAILS", "source id", static_values["source id"])
    config.set("DETAILS", "email_sent", static_values["email_sent"])
    config.set("DETAILS", "check_duplicate", static_values["check_duplicate"])
    config.set("DETAILS", "sending address", static_values["sending address"])
    config.set("DETAILS", "receiving address", info["recv"])

    # Combine base CC list with unique CC
    full_cc = static_values["cc"] + "," + info["cc_extra"]
    config.set("DETAILS", "cc", full_cc)
    config.set("DETAILS", "port", static_values["port"])

    # Write back to file
    with open(ini_file, "w", encoding="utf-8") as configfile:
        config.write(configfile)

    print(f"✅ Updated INI for Ref_{ref_no}: {ini_file}")

print("🎯 All INI files updated successfully based on details.txt.")
