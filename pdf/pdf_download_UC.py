from datetime import datetime
import os
import requests
import time
import shutil
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver

chromedriver.install()

temPdfOut = "Temp"
if not os.path.exists(temPdfOut):
    os.makedirs(temPdfOut)

download_path = "Final"
if not os.path.exists(download_path):
    os.makedirs(download_path)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
#options.add_argument(f'--user-agent={user_agent}')
options.add_argument('--version_main=108')

prefs = {
    "download.default_directory": os.path.abspath(temPdfOut),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}

options.add_experimental_option('prefs', prefs)

driver = uc.Chrome(options=options)

def get_driver_pdf(url, new_filename, download_path):

    for file in os.listdir(download_path):
        os.remove(os.path.join(download_path, file))

    driver.get(url)
    print("Wait until the PDF is downloaded")

    # current_url = driver.current_url
    #
    # while current_url


    time.sleep(50)

    while any(f.endswith('.crdownload') for f in os.listdir(download_path)):
        time.sleep(1)

    pdf_files = [f for f in os.listdir(download_path) if f.endswith(".pdf")]

    downloaded_file = os.path.join(download_path, pdf_files[0])
    shutil.move(downloaded_file, new_filename)
    print("PDF file has been successfully downloaded")


def download_pdf(session, url, current_out):
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        with open(current_out, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded: {current_out}")
    except Exception as e:
        print(f"PDF download failed from {url}: {e}")


pdf_list = [
    "https://dlt.ri.gov/sites/g/files/xkgbur571/files/documents/pdf/wrs/HazardousABC.pdf",
]

for index, i in enumerate(pdf_list):
    pdfLink = str(i) + "?download=true"
    print(pdfLink)
    output_fileName = os.path.join(download_path, "{}.pdf".format(index + 1))
    get_driver_pdf(pdfLink, output_fileName, temPdfOut)

driver.quit()