import os
import shutil
import time
import undetected_chromedriver as uc

out1="New"
download_path=out1
if not os.path.exists(out1):
    download_path=os.mkdir(out1)

options = uc.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
options.add_argument('--version_main=108')

prefs = {
    "download.default_directory": os.path.abspath(download_path),
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
    time.sleep(5)

    while any(f.endswith('.crdownload') for f in os.listdir(download_path)):
        time.sleep(1)

    pdf_files = [f for f in os.listdir(download_path) if f.endswith(".pdf")]

    if pdf_files:
        downloaded_file = os.path.join(download_path, pdf_files[0])
        # new_file_path = os.path.join(download_path, new_filename)
        shutil.move(downloaded_file, new_filename)
        print(f"Downloaded: {new_filename}")
    else:
        pass

url="https://spj.science.org/doi/pdf/10.34133/plantphenomics.0180?download=true"

out2="New1"
new_filename=out2
if not os.path.exists(out2):
    new_filename=os.mkdir(out2)
new_filename=os.path.join(new_filename,"Esa.pdf")

get_driver_pdf(url, new_filename, download_path)
