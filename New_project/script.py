import requests
import json
import pandas as pd
import os
import configparser
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Bitness": "\"64\"",
    "Sec-Ch-Ua-Full-Version": "\"126.0.6478.127\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.127\", \"Google Chrome\";v=\"126.0.6478.127\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

error_list = []
data = []
unique_combinations = set()

def getSoup(url):
    response = requests.get(url,headers=headers)
    return response.json()

def read_ini_file():
    ini_path = os.path.join(os.getcwd(), "Info.ini")
    config = configparser.ConfigParser()
    config.read(ini_path)

    download_path = config.get("UniversityDetails", "Download Path")
    university_name = config.get("UniversityDetails", "University Name")
    university_id = config.get("UniversityDetails", "University ID")
    source_url = config.get("UniversityDetails", "Source URL")

    return download_path,university_name,university_id,source_url

def get_content(university_name,university_id,source_url):
    print("⏳ Scraping data... please wait.")
    page_number = 1
    while True:
        url = f"https://libguides.cam.ac.uk/process/az/render-list?search=&subject_id=&type_id=&vendor_id=&access_mode_id=&page={page_number}&site_id=5032&content_id=0&is_widget=0&bootstrap5=true&page_size=0&preview=&sublist_id=0&alpha="
        current_soup = getSoup(url)
        data = current_soup["data"]["html"]
        if not data:
            break
        soup = BeautifulSoup(data, 'html.parser')
        read_html_content(soup,university_name,university_id,source_url)
        page_number += 1

def read_html_content(soup,university_name,university_id,source_url):
    all_list = soup.find_all("div", class_="az-item")

    for sin in all_list:
        try:
            title_tag = sin.find(["a", "span"], class_="az-title")
            remove_tag = title_tag.find("i", attrs={"title": "This link opens in a new window"})
            if remove_tag:
                remove_tag.decompose()
            database_Name = title_tag.get_text(strip=True)

            description_tag = sin.find("div", class_="az-description-short")
            description = description_tag.get_text(strip=True)

            alt_tag = sin.find("span",string="Alternate Name(s):")
            if alt_tag:
                next_tag = alt_tag.find_next_sibling("span")
                alt_value = next_tag.get_text(strip=True)
            else:
                alt_value = ""

            if (database_Name, description) not in unique_combinations:
                unique_combinations.add((database_Name, description))

                data.append({
                    "University Name": university_name,
                    "University ID": university_id,
                    "Database Name": database_Name,
                    "Vendor Name": "",
                    #"Subject Area": alt_value,
                    "Subject Area": "",
                    "Product Description": description,
                    "Source URL": source_url
                })
            else:
                print(f"🔄 Duplicated Record: {database_Name}")
        except Exception as error:
            error_list.append(f"{error}")

def main():
    try:
        print("🚀 Scraping process started!")
        try:
            download_path,university_name,university_id,source_url = read_ini_file()
            print("✅ INI file read successfully.")
        except Exception as error:
            raise Exception("⚠️ Failed to read INI configuration")

        get_content(university_name,university_id,source_url)

        out_csv_file = os.path.join(download_path, "University_Info.csv")
        df = pd.DataFrame(data)
        df.to_csv(out_csv_file, index=False, encoding='utf-8-sig')

        print(f"✅ Total records: {len(data)}")
        print("✅ CSV file saved.")
    except Exception as error:
        error_list.append(f"{error}")

if __name__ == "__main__":
    main()

    if error_list:
        print("\n","Errors encountered:")
        for error in error_list:
            print(f"- {error}")
