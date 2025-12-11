from scraper import WebScraper
scraper = WebScraper()

def main():
    try:
        soup = scraper.get_soup("https://www.dialog.lk/")
        print(soup)
    except Exception as error:
        print(f"{error}")

if __name__ == "__main__":
    main()