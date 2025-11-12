import requests
from bs4 import BeautifulSoup
import os
import shutil
import pdfkit
from PyPDF2 import PdfMerger

current_out="Out"
if not os.path.exists(current_out):
    os.makedirs(current_out)

def chines_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    html_content = soup.prettify()
    with open("out.html", 'w', encoding='utf-8') as file:
        file.write(html_content)

    if not os.path.exists('css'):
        os.makedirs('css')

    css_files = []
    for link in soup.find_all('link', rel='stylesheet'):
        css_url = link['href']
        if not css_url.startswith('http'):
            css_url = requests.compat.urljoin(url, css_url)
        css_files.append(css_url)

    for css_url in css_files:
        css_response = requests.get(css_url)
        css_filename = os.path.join('css', os.path.basename(css_url))
        with open(css_filename, 'w', encoding='utf-8') as css_file:
            css_file.write(css_response.text)

        html_content = html_content.replace(css_url, css_filename.replace("\\", "/"))

    with open("out.html", 'w', encoding='utf-8') as file:
        file.write(html_content)

    try:
        config = pdfkit.configuration(wkhtmltopdf='wkhtmltox/bin/wkhtmltopdf.exe')
        pdfkit.from_file('out.html', "CNout.pdf", configuration=config, options={'enable-local-file-access': ""})
    except:
        pass

def english_url(url):
    config = pdfkit.configuration(wkhtmltopdf='wkhtmltox/bin/wkhtmltopdf.exe')

    pdfkit.from_url(url, "ENout.pdf", configuration=config,
                    options={'enable-local-file-access': ""})

def merge_pdfs(pdf_paths, output_path):
    merger = PdfMerger()
    for pdf_path in pdf_paths:
        merger.append(pdf_path)
    merger.write(output_path)
    merger.close()

    for pdf_path in pdf_paths:
        os.remove(pdf_path)

    if os.path.exists("css"):
        shutil.rmtree("css")

    os.remove("out.html")

chinesUrl = "https://www.chinagp.net/CN/1007-9572/current.shtml"
englishUrl = "https://www.chinagp.net/EN/1007-9572/current.shtml"

chines_url(chinesUrl)
english_url(englishUrl)

pdf_paths = ['ENout.pdf', 'CNout.pdf']
output_TOC_file = os.path.join(current_out, "TOC_PDF.pdf")

merge_pdfs(pdf_paths, output_TOC_file)
print("The TOC file was created successfully.")


