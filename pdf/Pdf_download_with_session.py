import requests
import os

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)

def get_session(Article_link,url):
    new_session=requests.session()
    session_login = new_session.get(Article_link)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    out_folder = os.path.join(out_path, 'New.pdf')

    pdf_content = new_session.get(url, headers=headers).content
    with open(out_folder, 'wb') as file:
        file.write(pdf_content)

Article_link='https://www.minervamedica.it/en/journals/gazzetta-medica-italiana/article.php?cod=R22Y2024N01A0008'
url="https://dlt.ri.gov/sites/g/files/xkgbur571/files/documents/pdf/wrs/HazardousABC.pdf"

get_session(Article_link,url)


