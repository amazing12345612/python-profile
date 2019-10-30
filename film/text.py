from lxml import etree
import requests
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPDigestAuthHandler,build_opener
url = 'http://www.baidu.com'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

