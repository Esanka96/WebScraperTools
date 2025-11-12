import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import warnings
warnings.simplefilter("ignore")

def getSoup(url):
    response = requests.get(url,headers=headers,verify=False)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.xlsx')


headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}


url="https://datos.abiertos.inecc.gob.mx/Datos_abiertos_INECC/CGCSA/CNSQ/CNSQ.html"

content = getSoup(url)

excel_link = content.find("a",href=re.compile(r".xlsx"))["href"]

excel_content = requests.get(excel_link,headers=headers,verify=False).content
with open(out_folder, 'wb') as file:
    file.write(excel_content)


