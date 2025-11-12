import requests
from requests.exceptions import ChunkedEncodingError, ConnectionError
from tenacity import retry, stop_after_attempt, wait_fixed

pdf_link = 'http://www.gyqx.ac.cn/EN/PDF/10.7522/j.issn.1000-0534.2023.00090?token=e79b4f040a11403f8e4edb0bda6f32ef'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def download_pdf(url, headers):
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open('downloaded_file.pdf', 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

try:
    download_pdf(pdf_link, headers)
    print("PDF downloaded successfully.")
except (ChunkedEncodingError, ConnectionError) as e:
    print(f"Failed to download PDF: {e}")
