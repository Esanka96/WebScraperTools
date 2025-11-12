import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()
import os
import time
import base64
from PyPDF2 import PdfMerger

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--kiosk-printing')
driver = uc.Chrome(options=options)

def save_as_pdf(url, output_path):
    driver.get(url)
    time.sleep(5)
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

def merge_pdfs(output_paths, merged_output_path):
    merger = PdfMerger()
    for pdf in output_paths:
        merger.append(pdf)
    merger.write(merged_output_path)
    merger.close()

def get_toc_pdf(current_out):
    English_url = 'http://cjbmb.bjmu.edu.cn/EN/1007-7626/home.shtml'
    Chines_url = 'http://cjbmb.bjmu.edu.cn/CN/1007-7626/home.shtml'

    output_fimeName_en = os.path.join(current_out, "English.pdf")
    save_as_pdf(English_url, output_fimeName_en)

    output_fimeName_cn = os.path.join(current_out, "Chines.pdf")
    save_as_pdf(Chines_url, output_fimeName_cn)

    output_TOC_file = os.path.join(current_out, "TOC_PDF.pdf")

    merge_pdfs([output_fimeName_en, output_fimeName_cn], output_TOC_file)

    os.remove(output_fimeName_en)
    os.remove(output_fimeName_cn)
    driver.quit()

