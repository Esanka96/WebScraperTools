from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import base64
from PyPDF2 import PdfMerger

def save_as_pdf(url, output_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-software-rasterizer')
    chrome_options.add_argument('--kiosk-printing')
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(2)
        print_options = {
            'landscape': False,
            'displayHeaderFooter': False,
            'printBackground': True,
            'preferCSSPageSize': True
        }
        result = driver.execute_cdp_cmd("Page.printToPDF", print_options)

        if 'data' in result:
            pdf_data = base64.b64decode(result['data'])

            with open(output_path, 'wb') as file:
                file.write(pdf_data)

            print(f"PDF saved successfully at {output_path}")

    finally:
        driver.quit()

def merge_pdfs(output_paths, merged_output_path):
    merger = PdfMerger()
    for pdf in output_paths:
        merger.append(pdf)
    merger.write(merged_output_path)
    merger.close()
    print(f"Merged PDF saved successfully at {merged_output_path}")

# URLs and output paths
url1 = 'https://hgjz.cip.com.cn/CN/1000-6613/home.shtml'
url2 = 'https://hgjz.cip.com.cn/EN/1000-6613/home.shtml'
output_path1 = 'output1.pdf'
output_path2 = 'output2.pdf'
merged_output_path = 'merged_output.pdf'

# Save the two PDFs
save_as_pdf(url1, output_path1)
save_as_pdf(url2, output_path2)

# Merge the two PDFs into one
merge_pdfs([output_path1, output_path2], merged_output_path)
