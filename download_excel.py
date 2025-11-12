import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd

out_path='Out'
if not os.path.exists(out_path):
    os.makedirs(out_path)
out_folder=os.path.join(out_path,'New.xlsx')


headers = {
    "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "ar_debug=1",
    "pragma": "no-cache",
    "priority": "i",
    "referer": "https://comptox.epa.gov/dashboard/chemical-lists/PFAS8a7V3",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "image",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "sec-fetch-storage-access": "active",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}



pdf_link="https://www.google-analytics.com/collect?v=1&_v=j101&a=1537523209&t=event&ni=0&_s=1&dl=https%3A%2F%2Fcomptox.epa.gov%2Fdashboard%2Fchemical-lists%2FPFAS8a7V3&ul=en-gb&de=UTF-8&dt=CompTox%20Chemicals%20Dashboard&sd=24-bit&sr=1920x1080&vp=1905x911&je=0&ec=&ea=undefined&el=&_u=SACAAEABAAAAACABIAC~&jid=&gjid=&cid=1550564279.1733299973&tid=UA-32633028-1&_gid=1782061234.1751885047&gtm=45He5710n51L8ZBv542870za200&gcd=13l3l3l3l1l1&dma=0&tag_exp=101509157~103116026~103200004~103233427~103351869~103351871~104684208~104684211~104718208~104839054~104839056~104885889~104885891~104908321~104908323&z=1746984387"
pdf_content = requests.get(pdf_link,headers=headers).content
with open(out_folder, 'wb') as file:
    file.write(pdf_content)

print("downloading ok!")

