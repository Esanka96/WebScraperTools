# Path to your text file
file_path = r"C:\Users\SL1047\Desktop\New folder (4)\ISM_Schedule\Get_user_details\Ref_number.txt"

# Constants
ref_code = "SL1728"
email = "PDissanayake@innodata.com"

# Read and process the file
with open(file_path, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# Print formatted output
for number in lines:
    print(f"{number},{ref_code},{email},")
