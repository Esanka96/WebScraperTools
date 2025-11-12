import cloudscraper
from bs4 import BeautifulSoup

# Create a Cloudscraper instance
scraper = cloudscraper.create_scraper()

# URL you want to scrape
url = 'https://projecteuclid.org/browse/title/A'

headers = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

response = scraper.get(url,headers=headers)

html_content = response.content

# Step 2: Parse HTML Content
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)
