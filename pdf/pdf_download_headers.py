import os
import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
# }

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'COB_SessionId=jrwd5minsa5nonub2dq3uplk; The_Company_of_BiologistsMachineID=638459049533323876; fpestid=uYn14HWIXTs22duepq5lZPYKph71QAGfmOGKbAT6xBXqxQsxXtBbHT_k0tFhccIwm2Cobw; _gid=GA1.2.267079484.1710308157; __stripe_mid=2d6d60e7-f225-45da-8e3c-5ad153043483c4e68d; __stripe_sid=0ba5e4eb-504d-47c0-b405-ce89e9c8b99dde6888; _ga_G5TCNFJCYP=GS1.1.1710310669.2.1.1710313146.0.0.0; __gads=ID=fe2b143eae6a203b:T=1710308157:RT=1710313151:S=ALNI_Mb9BgVnqj7t6PLIpguK7ApIk47wYA; __eoi=ID=6dfde17baadb0c8e:T=1710308157:RT=1710313151:S=AA-AfjZTC4yG4lBbCgaTBFslMRrW; _ga=GA1.1.1321160367.1710308156; _ga_YXBDEHVL2V=GS1.1.1710310212.2.1.1710313201.0.0.0',
    'Host': 'journals.biologists.com',
    'Pragma': 'no-cache',
    'Referer': 'https://journals.biologists.com/jeb/issue/227/4',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

out_path = 'Out'  # Replace with your desired output path
out_folder = os.path.join(out_path, 'New.pdf')
pdf_link = 'https://journals.biologists.com/jeb/article-pdf/227/4/jeb247495/3368389/jeb247495.pdf'

try:
    pdf_content = requests.get(pdf_link, headers=headers)
    pdf_content.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx status codes)

    with open(out_folder, 'wb') as file:
        file.write(pdf_content.content)
    print("PDF downloaded successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error downloading PDF: {e}")
