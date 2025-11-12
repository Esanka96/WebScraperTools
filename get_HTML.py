import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd


out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.html')


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

pdf_link="https://revistas.ucm.es/index.php/ESMP/issue/view/4455"
combined_html = requests.get(pdf_link,headers=headers).content
soup = BeautifulSoup(combined_html, 'html.parser')
body = soup.find('body')

combined_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Combined HTML</title>
</head>
<body>
"""

combined_html += str(body) + "<br>"

combined_html += """
</body>
</html>
"""


with open(out_folder, 'w', encoding='utf-8') as file:
    file.write(str(combined_html))
