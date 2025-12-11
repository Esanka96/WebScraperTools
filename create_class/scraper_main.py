from cloud_bypass import WebCloudScraper
scraper = WebCloudScraper()

def main():
    try:
        url = "https://julkaisut.valtioneuvosto.fi/items/705e5345-033a-4e44-85aa-cee534f0caa2"
        try:
            soup = scraper.get_soup(url,max_retries=1)
        except:
            try:
                soup = scraper.get_cloudscraper_soup(url,max_retries=1)
            except:
                scraper.cookie_update_undetected(url)

                soup = scraper.get_soup(url, max_retries=1)
                scraper.driver_close()
        print(soup)

    except Exception as error:
        scraper.driver_close()
        print(f"{error}")

if __name__ == "__main__":
    main()