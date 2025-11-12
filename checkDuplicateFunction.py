import requests
from bs4 import BeautifulSoup
import json

def check_duplicate(doi,art_title,src_id,vol_no,iss_no):
    url = 'https://ism-portal.innodata.com/api/validate-record'

    data = {'token': '6547bdf3f07202413b5daf3216e511028c14034b36ff47c514c0220a911785b3:1698740839',
            'doi': doi, 'art_title': art_title, 'srcid': src_id, 'volume_no': vol_no, 'issue_no': iss_no}

    print(json.loads(BeautifulSoup(requests.post(url, data=data).content, 'html.parser').text))

    if not json.loads(BeautifulSoup(requests.post(url, data=data).content, 'html.parser').text).get("status",{}):
        print("This is duplicated")
        return True
    else:
        print("This is not duplicated")
        return False

articleTitle='HEMODYNAMIC STUDIES OF PENILE ERECTION IN DOGS'
doi='10.5980/jpnjurol1928.79.12_1909'
issue_no="12"
srcId="76532599"
volume_no="79"

check_value = check_duplicate(doi,articleTitle,srcId,volume_no,issue_no)
