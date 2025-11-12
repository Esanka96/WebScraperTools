import ssl
import requests

from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT:@SECLEVEL=1')
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

session = requests.Session()
adapter = TLSAdapter()
session.mount('https://', adapter)

response = session.get('https://www.jcdronline.org/index.php')
print(response.text)
