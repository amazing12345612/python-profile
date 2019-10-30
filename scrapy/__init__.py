import urllib.request
import urllib.parse
import requests
import json
from lxml import etree
import textwrap
url ='https://cas.hdu.edu.cn/cas/login?service=https%3A%2F%2Fi.hdu.edu.cn%2Ftp_up%2F'
data = {'un' :'17081610','pw':'helloworld,.123'}
response = requests.post(url=url,data=data)
print(response.status_code)
print(response.text)