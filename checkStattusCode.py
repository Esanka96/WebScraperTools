import re
import requests
from bs4 import BeautifulSoup
import os
import common_function
import pandas as pd
from datetime import datetime

def get_soup(url):
    global statusCode
    response = requests.get(url,headers=headers,stream=True)
    statusCode = response.status_code
    soup= BeautifulSoup(response.content, 'html.parser')
    return soup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #"Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}



statusCode=None

try:
    url="https://www.jle.com/en/revues/jpe/sommaire.phtml"
    soup=get_soup(url)
except Exception as error:

    error_messages = {
        200: "An error occurred on the site.",
        400: "Error in the site: 400 Bad Request",
        401: "Error in the site: 401 Unauthorized",
        403: "Error in the site: Error 403 Forbidden",
        404: "Error in the site: 404 Page not found!",
        408: "Error in the site: Error 408 Request Timeout",
        500: "Error in the site: Error 500 Internal Server Error"
    }
    Error_message = error_messages.get(statusCode)

    if Error_message == None:
        Error_message = "Error in the site : "+str(error)

    print(Error_message, "\n")

