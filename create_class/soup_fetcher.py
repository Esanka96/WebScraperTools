from scraper import WebScraper
scraper = WebScraper()

def main():
    try:
        soup = scraper.get_cloudscraper_soup("https://dlt.ri.gov/sites/g/files/xkgbur571/files/documents/pdf/wrs/HazardousABC.pdf")
        print(soup)

    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()