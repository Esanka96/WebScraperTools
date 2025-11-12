import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    "Cookie":"_gid=GA1.2.1476392626.1713156198; JSESSIONID=7ti9gaal0cc5j.x-ic-live-03; __cf_bm=Kb_s50z2.sC5onR7fqlvco9.KPwxO6rFY0zIlChavYo-1713240101-1.0.1.1-e7BuLvfxg5ha8AX.byNrCgq552x0FSVfgVPlDR18kshDtwfoiwFbnkTfcZpcGdLmzyUC3TTmdseCa4ywyFEvaA; __cflb=0H28utxteaGoNEhf6NdDXxKJM2oERVUKU7pJg1RSqxq; _ga_G5TCNFJCYP=GS1.1.1713240195.7.0.1713240704.0.0.0; _gat_gtag_UA_1313315_1=1; _ga_FWEPW5188Q=GS1.1.1713240103.5.1.1713240705.60.0.0; _ga=GA1.1.554726943.1713156198; __gads=ID=5b8cea471745764a:T=1713156198:RT=1713240705:S=ALNI_MY_1uFQ5aB_vVcpgBQtYq42prjPPQ; __eoi=ID=7649aef02d32d5a2:T=1713156198:RT=1713240705:S=AA-AfjZtsi9QHxDKR6yMjyz52I1q",
    "Referer":"https://www.ingentaconnect.com/contentone/scimed/mppa/2024/00000039/00000001/art00003"
}

out_folder=os.path.join(out_path,'New.pdf')

pdf_link="https://www.ingentaconnect.com/cdn-cgi/rum?"

payload={"siteToken": "1468a68d648449d987ed5f15341e1865",
         "pageloadId":"414ae589-0ba0-4570-930b-f500aa7bca01",
        # "referrer":"https://www.ingentaconnect.com/content/scimed/mppa/2024/00000039/00000001;jsessionid=7ti9gaal0cc5j.x-ic-live-03",
        # "location":"https://www.ingentaconnect.com/contentone/scimed/mppa/2024/00000039/00000001/art00003"
         }

pdf_content = requests.post(pdf_link,data=payload,headers=headers).content
with open(out_folder, 'wb') as file:
    file.write(pdf_content)