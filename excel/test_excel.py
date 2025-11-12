import requests

url = "https://www.epa.gov/sites/default/files/2023-10/pmn-table.xlsx"  # replace with actual Excel file URL
output_path = "pmn_table.xlsx"

response = requests.get(url)
if response.status_code == 200:
    with open(output_path, "wb") as f:
        f.write(response.content)
    print("✅ File downloaded successfully!")
else:
    print(f"❌ Failed to download. Status code: {response.status_code}")
