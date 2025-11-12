import re
import requests
from bs4 import BeautifulSoup
import os
import common_function
import pdfplumber
from io import BytesIO
import TOC_HTML
import pandas as pd
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_fixed

def getDOI(pdf_link):
    try:
        response = requests.get(pdf_link)
        pdf_content = BytesIO(response.content)
        with pdfplumber.open(pdf_content) as pdf:
            page = pdf.pages[0].extract_text()
            text = page.split("\n")
            try:
                index = next((i for i, s in enumerate(text) if "doi.org" in s), -1)
                DOI = text[index].split(":")[-1].rsplit("org/",1)[-1]
            except:
                DOI=""
    except:
        DOI=""

    return DOI

pdf_link="https://www.aes.org.cn/nyhjkxxben/ch/reader/create_pdf.aspx?file_no=20240802&year_id=2024&quarter_id=8&flag=1"
getDOI(pdf_link)