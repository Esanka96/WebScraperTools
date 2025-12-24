from bypass_without_request import WebCloudScraper
scraper = WebCloudScraper()

def session_update_with_cookie(url):
    try:
        scraper.get_cloudscraper_soup(url, max_retries=1)
        return
    except Exception as error:
        print(f"{error}")

    try:
        scraper.cookie_update_undetected(url,max_wait_time=10)
        return
    except Exception as error:
        print(f"\r{error}")
    finally:
        scraper.driver_close()

    try:
        scraper.cookie_update_undetected_with_click(url,max_wait_time=10)
        return
    except Exception as error:
        print(f"\r{error}")
    finally:
        scraper.driver_close()

def get_content(url):
    try:
        soup = scraper.get_cloudscraper_soup(url, max_retries=1)
        return soup
    except Exception as error:
        print(f"{error}")

def main():
    try:
        #url = "https://spj.science.org/journal/bmef"
        url = "https://indiankanoon.org/doc/184182041/"
        # url = "https://emb.gov.ph/"
        session_update_with_cookie(url)
        main_soup = get_content(url)
        print(main_soup)

    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()
