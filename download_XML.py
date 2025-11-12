import requests

# Define the URL for the XML file
url = "https://aammt.tmmu.edu.cn/api/api/Web/GetXML?Id=2d43d0e4-65e6-4f6c-a407-9a069fd3f911"

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "host": "aammt.tmmu.edu.cn",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}


# Send a GET request to download the XML file
response = requests.get(url,headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to an .xml file
    with open("file.xml", "wb") as file:
        file.write(response.content)
    print("XML file downloaded successfully.")
else:
    print(f"Failed to download XML file. Status code: {response.status_code}")
