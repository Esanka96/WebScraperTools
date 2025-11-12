from requests_html import HTMLSession

session = HTMLSession()

def get_dynamic_content(url):
    response = session.get(url)
    response.html.render(timeout=20)  # Adjust timeout as needed
    return response.html.html

url = "https://www.whxb.pku.edu.cn/EN/1000-6818/home.shtml"
html_content = get_dynamic_content(url)
print(html_content)
