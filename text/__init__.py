from urllib.parse import quote
import requests
from lxml import etree
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd='+quote(keyword)
print(url)
response =requests.get(url)
result =response.text
with open('1.html','w',encoding='utf-8') as f:
    f.write(result)
