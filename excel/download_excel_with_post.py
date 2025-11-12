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
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    # "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
    # "cache-control": "max-age=0",
    # "connection": "keep-alive",
    # "content-type": "application/x-www-form-urlencoded",
    # "host": "echa.europa.eu",
    # "origin": "https://echa.europa.eu",
    # "referer": "https://echa.europa.eu/information-on-chemicals/ec-inventory",
    # "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
    )
}

payload = {
    "_eucleflegislationlist_WAR_euclefportlet_formDate": "1753180972645",
    "_eucleflegislationlist_WAR_euclefportlet_exportColumns": "name,ecNumber,casNumber,fld_erc4_id,fld_pref,fld_erc4_ec,fld_cas,fld_erc4_ci,fld_erc4_col,fld_erc4_physform,fld_erc4_appname,fld_erc4_rest,fld_erc4_maxthres,fld_erc4_expras,fld_erc4_function,fld_erc4_notes",
    "_eucleflegislationlist_WAR_euclefportlet_orderByCol": "rmlName",
    "_eucleflegislationlist_WAR_euclefportlet_orderByType": "asc",
    "_eucleflegislationlist_WAR_euclefportlet_searchFormColumns": "",
    "_eucleflegislationlist_WAR_euclefportlet_searchFormElements": "",
    "_eucleflegislationlist_WAR_euclefportlet_substance_identifier_field_key": "",
    "_eucleflegislationlist_WAR_euclefportlet_total": "309",
    "_eucleflegislationlist_WAR_euclefportlet_exportType": "xls"
}


pdf_link="https://echa.europa.eu/cosmetics-colorant?p_p_id=eucleflegislationlist_WAR_euclefportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=exportResults&p_p_cacheability=cacheLevelPage"
pdf_content = requests.post(pdf_link,headers=headers,data=payload).content
with open(out_folder, 'wb') as file:
    file.write(pdf_content)

print("downloading ok!")

