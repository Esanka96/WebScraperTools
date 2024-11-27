from playwright.sync_api import sync_playwright

def scrape_website():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for _ in range(3):
            try:
                page.goto("https://www.dialog.lk/", wait_until="domcontentloaded")
                html_content = page.content()
                print(html_content)
                browser.close()
                break
            except TimeoutError:
                print("Retrying...")


if __name__ == "__main__":
    scrape_website()
