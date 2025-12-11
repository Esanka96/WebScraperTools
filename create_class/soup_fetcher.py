from scraper import WebScraper

scraper = WebScraper()

html_content = """"
<style>#pf-content img, #pf-content figure { margin: 1em auto !important; clear: both !important; display: block !important; float: none !important; }</style>

<html xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:msxsl="urn:schemas-microsoft-com:xslt" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><head>
</html>

"""

url = 'https://api.printfriendly.com/v2/pdf/create?api_key=chrome-extension-4caede54-370b-4018-a8b7-86b825930d91'

payload = {
    "html": html_content,
    "page_size": "A4",
    "title": "Title",
    "dir": "ltr",
    "hostname": "www.printfriendly.com",
    "platform": "Win32",
    "css_url": ""
}


soup = scraper.post_soup(url,data=payload)

print(soup)
