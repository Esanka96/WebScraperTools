import requests
import time

API_KEY = 'a03589ed562de14589af1d772c2b41bb'
SITE_KEY = '6LfeqUoUAAAAANe-QBN7VYMj5D878pDgt5_mY-1S'
PAGE_URL = 'https://academic.oup.com/crawlprevention/governor?content=%2fplphys'
FORM_URL = 'https://academic.oup.com/plphys'

def send_recaptcha(api_key, site_key, page_url):
    url = "http://2captcha.com/in.php"
    data = {
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'key': api_key,
        'pageurl': page_url
    }
    response = requests.post(url, data=data)
    return response.text.split('|')[1]

def get_recaptcha_result(api_key, captcha_id):
    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}"
    while True:
        response = requests.get(url)
        if 'CAPCHA_NOT_READY' in response.text:
            time.sleep(5)
        else:
            return response.text.split('|')[1]

def submit_form_with_recaptcha(form_url, recaptcha_token, additional_data=None):
    form_data = {
        'g-recaptcha-response': recaptcha_token
    }
    if additional_data:
        form_data.update(additional_data)

    response = requests.post(form_url, data=form_data)
    return response.text

# Solve reCAPTCHA
captcha_id = send_recaptcha(API_KEY, SITE_KEY, PAGE_URL)
solution = get_recaptcha_result(API_KEY, captcha_id)
print(f'Solved reCAPTCHA: {solution}')

# Submit the form with the reCAPTCHA token and retrieve the page content
additional_form_data = {
    # Include other form fields as required by the target website
    'field1': 'value1',
    'field2': 'value2'
}
page_content = submit_form_with_recaptcha(FORM_URL, solution, additional_form_data)
print(page_content)
