import re
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
import common

chromedriver.install()

uniqueIdentity = "AR0253"
region = "Latin America"
jurisdiction = "BR"
category = "Controlled Drugs & Precursors"
title = "Brazil. Narcotics Subject to Control (ANVISA Ordinance No. 344/98, Annex I, Lists A1 & A2, lasted updated by RDC 244 of 27 November of 2023)"
casKeyValue = ""

data = []
errors = []

url = "https://anvisalegis.datalegis.net/action/ActionDatalegis.php?acao=abrirTextoAto&link=S&tipo=RDC&numeroAto=00000974&seqAto=000&valorAno=2025&orgao=RDC/DC/ANVISA/MS&codTipo=&desItem=&desItemFim=&cod_modulo=134&cod_menu=9451"


def get_user_agent():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")
    driver = uc.Chrome(options=options)
    driver.get("https://www.example.com")
    user_agent = driver.execute_script("return navigator.userAgent;")
    driver.quit()
    return user_agent.replace("Headless", "")


def init_driver(user_agent):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f'--user-agent={user_agent}')
    return uc.Chrome(options=chrome_options)


def extract_list_data(soup, target_list_id):
    results = []
    heading_pattern = re.compile(rf'\bLISTA\s*[-]?\s*{target_list_id}\b', re.IGNORECASE)
    next_list_pattern = re.compile(r'\bLISTA\s*[-]?\s*[A-Z0-9]+\b', re.IGNORECASE)

    heading_p = None
    for b_tag in soup.find_all("b"):
        text = b_tag.get_text(strip=True)
        if heading_pattern.search(text):
            heading_p = b_tag.find_parent("p")
            break

    if not heading_p:
        errors.append(f"❌ Could not find heading for LISTA - {target_list_id}")
        return results

    i = 1
    for sibling in heading_p.find_next_siblings("p"):
        txt = sibling.get_text(strip=True)
        if next_list_pattern.search(txt) and i > 1:
            break
        if not re.match(r'^\d+\.\s+', txt):
            continue

        name = re.sub(r'^\d+\.\s*', '', txt)
        results.append({
            "Lista": target_list_id,
            "Número(Number)": str(i),
            "Nome da substância(Substance Name)": name.strip()
        })
        i += 1

    if not results:
        errors.append(f"⚠️ Found heading LISTA - {target_list_id} but no items extracted.")

    return results


def create_final_json_file():
    if not data:
        errors.append("❌ No data extracted.")
        return
    df = pd.DataFrame(data)
    df = df.fillna("").astype(str)
    df.columns = [c.replace(" ", "_") for c in df.columns]
    df = common.clean_newlines_in_dataframe(df)
    common.save_output_to_json(
        UniqueIdentity=uniqueIdentity,
        region=region,
        jurisdiction=jurisdiction,
        category=category,
        title=title,
        errors=errors,
        data=df,
        jsonPath=common.returnJsonPath(uniqueIdentity),
        casKeyValue=casKeyValue
    )
    print("✅ JSON file created.")


def main():
    global data

    try:
        common.deleteTodayFiles(uniqueIdentity)

        user_agent = get_user_agent()
        driver = init_driver(user_agent)

        print(f"🌐 Fetching page via Selenium: {url}")
        driver.get(url)
        time.sleep(8)

        # wait until form appears
        count = 0
        max_count = 40
        while count < max_count:
            if BeautifulSoup(driver.page_source, "html.parser").find("form", attrs={"name": "formGerarLink"}):
                break
            time.sleep(5)
            count += 1

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        lista_a1 = extract_list_data(soup, "A1")
        lista_a2 = extract_list_data(soup, "A2")

        if not lista_a1 and not lista_a2:
            errors.append("❌ No LISTA A1 or A2 entries found.")

        data.extend(lista_a1)
        data.extend(lista_a2)

        create_final_json_file()

    except Exception as e:
        errors.append(f"❌ Exception in main(): {e}")

    finally:
        if errors:
            print("\n❗ Errors encountered:")
            for err in errors:
                print(f"- {err}")
        else:
            print("✅ Script completed successfully.")


if __name__ == "__main__":
    main()
