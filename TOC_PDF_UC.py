import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()
import os
import time
import base64
from PyPDF2 import PdfMerger

current_out="Out"
if not os.path.exists(current_out):
    os.makedirs(current_out)

options = uc.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-software-rasterizer')
options.add_argument('--kiosk-printing')
driver = uc.Chrome(options=options)

def save_as_pdf(current_out, languageList):
    for index,language in enumerate(languageList):
        pdf_name="{}.pdf".format(index+1)
        driver.get(language)
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
            with open(pdf_name, 'wb') as file:
                file.write(pdf_data)
        pdf_paths.append(pdf_name)

def merge_pdfs(output_paths, merged_output_path):
    merger = PdfMerger()
    for pdf in output_paths:
        merger.append(pdf)
    merger.write(merged_output_path)
    merger.close()

    for pdf_path in pdf_paths:
        os.remove(pdf_path)



languageList=['https://revistas.ucm.es/index.php/ESMP/user/setLocale/en_US?source=%2Findex.php%2FESMP%2Fissue%2Fview%2F4455', 'https://revistas.ucm.es/index.php/ESMP/user/setLocale/es_ES?source=%2Findex.php%2FESMP%2Fissue%2Fview%2F4455']
pdf_paths = []

save_as_pdf(current_out, languageList)

output_TOC_file = os.path.join(current_out, "TOC_PDF.pdf")

merge_pdfs(pdf_paths, output_TOC_file)

driver.quit()

