# @Time :2019/11/9 13:17
# @Auther :Ming
# @Software: PyCharm
import requests
from lxml import etree
def get_proxy():
    proxy = []
    for i in range(1,5):
        url = 'https://www.xicidaili.com/nn/'+ str(i)
        headers ={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        }
        reponse = requests.get(url= url,headers = headers)
        html = reponse.text
        html = etree.HTML(html)
        ip = html.xpath('//tr/td[2]/text()')
        post = html.xpath('//tr/td[3]/text()')
        for a in range(len(ip)):
            proxy.append(ip[a]+':'+post[a])
        return proxy

def check(proxy):
    url = 'http://www.baidu.com'
    for proxy in proxy:
        proxies = {
            'http':'http://'+proxy,
            'https': 'http://'+proxy,
        }
        try:
            response = requests.get(url=url,proxies=proxies)
            if response.status_code == 200:
                with open('2.txt','a',encoding='utf-8') as f:
                    f.write(proxy+'\n')
        except requests.exceptions.ConnectionError as e:
            print('error',e.args)
# from selenium import webdriver
a = get_proxy()
check(a)