import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import json

def get_soup(url,param):
    response = requests.post(url,headers=headers,json=param)
    response_code=response.status_code
    return response.json()
    # soup= BeautifulSoup(response.content, 'html.parser')
    # return soup,response_code

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
}

payload = {
    "pageNumber": 0,
    "pageSize": 100,
    "tree": {
        "type": "group",
        "id": "ab889989-0123-4456-b89a-b16f139daa93",
        "children1": {
            "b8b9b9a9-cdef-4012-b456-716f139daa93": {
                "type": "rule",
                "properties": {
                    "field": "retsinfoklassifikationId",
                    "operator": "select_equals",
                    "value": ["SortIndicator_10_40"],
                    "valueSrc": ["value"],
                    "valueType": ["select"]
                },
                "id": "b8b9b9a9-cdef-4012-b456-716f139daa93"
            },
            "aaba9aa8-cdef-4012-b456-716fc3780da3": {
                "type": "rule",
                "properties": {
                    "field": "titel",
                    "operator": "starts_with",
                    "value": ["Ulykker"],
                    "valueSrc": ["value"],
                    "valueType": ["text"]
                },
                "id": "aaba9aa8-cdef-4012-b456-716fc3780da3"
            },
            "9bba98ba-cdef-4012-b456-716fc37a4f30": {
                "type": "rule",
                "properties": {
                    "field": "dokumentTypeId",
                    "operator": "select_equals",
                    "value": ["SortIndicator_10"],
                    "valueSrc": ["value"],
                    "valueType": ["treeselect"]
                },
                "id": "9bba98ba-cdef-4012-b456-716fc37a4f30"
            }
        },
        "properties": {
            "conjunction": "AND"
        }
    },
    "orderDirection": 20,
    "orderBy": 40
}




url='https://www.retsinformation.dk/api/extremesearch'


soup = get_soup(url,payload)

print(soup)





