import requests
from bs4 import BeautifulSoup
import os
import re
import time
import common_function
import seperate_parameters
from datetime import datetime
import pandas as pd
from PyPDF2 import PdfReader

def get_soup(url):
    response = requests.get(url,headers=headers)
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

def get_current_issue(list):
    count=0
    publication_statuses = ['Preprint','Advance publication','Issue in print','Issue in progress','A head of print','Early Access',
        'Internet prepublication','Prepublication','Online First issue','Early view','Advance Publishing','Advance Access','Ahead of Print',
        'Early Release Articles',"12th East-West Philosopher's Conference \"Trauma and Healing\" to appear in Philosophy East and West 73-3",
        "Accepted for Publication","Preprint Articles","Online Advanced Publication","Digital-Only Special Issues"]

    for i,sin_item in enumerate(list):
        if not sin_item.text.strip() in publication_statuses:
            count=i
            break
    return count

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,da;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'muse.jhu.edu',
    'Origin': 'https://muse.jhu.edu',
    'Referer': 'https://muse.jhu.edu/account/',
    'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

with open('link1.txt', 'r', encoding='utf-8') as f1:
    list1 = [line.strip() for line in f1 if line.strip()]

Month_list=['spring','fall','autumn','autumne','winter','augusto','avril','juin','junio','marzo','oktober','summer','dezember'
            ,'abril','mayo','mars','décembre','septembre','juillet','octobre']

Last_Month_list = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def monthCheck(season):
    month_mapping = {
        'spring': 'March','fall': 'September','autumn': 'September','autumne': 'September','winter': 'December','augusto': 'August','avril': 'April',
        'juin': 'June','junio': 'June','marzo': 'March','oktober': 'October','octobre': 'October','summer': 'June','dezember': 'December',
        'abril': 'April','mayo': 'May','mars':'March','Décembre':'December','Septembre':'September','juillet':'July'
    }
    return month_mapping.get(season)

for key1 in list1:
    try:
        url = key1.split(",")[0]

        All_issue_list = get_soup(url).find('div', {'id': 'available_issues_list_text'}).findAll('h3')
        issue_link = 'https://muse.jhu.edu' + \
                     get_soup(url).find('div', {'id': 'available_issues_list_text'}).findAll('div', class_="vol_group")[
                         get_current_issue(All_issue_list)].find('a').get('href')
        # Volume_issue=get_soup(issue_link).find('div', class_='card_text').find('h3').text.strip().split(',')
        Volume_issue = get_soup(issue_link).find('div', class_='card_text').find('h3').text.strip()
        print(url)
        print(Volume_issue)


        volume_match = re.search(r"Volume\s*(\d+)",Volume_issue, re.IGNORECASE)
        issue_match = re.search(r"(?:Number|Numbers?|Numéro|Issue|No\.)\s*([\d &-]+)", Volume_issue, re.IGNORECASE)
        year_match = re.search(r"(\d{4})", Volume_issue, re.IGNORECASE)
        month_match = re.search(r"\b([A-Za-zÀ-ÿ/-]+) \d{4}", Volume_issue, re.IGNORECASE)
        part_match = re.search(r"Part\s*(\d+)",Volume_issue, re.IGNORECASE)

        Volume = volume_match.group(1) if volume_match else ""
        Issue = issue_match.group(1) if issue_match else ""
        Year = year_match.group(1) if year_match else ""
        Month = month_match.group(1) if month_match else ""
        Part = part_match.group(1) if part_match else ""

        if Month:
            Month = re.split(r"[-/]", Month)[0]
            Month = monthCheck(Month.lower()) if Month.lower() in Month_list else Month
            Month = Month if Month in Last_Month_list else ""

        print(Volume,Issue,Year,Month,Part)
    except:
        print(url)