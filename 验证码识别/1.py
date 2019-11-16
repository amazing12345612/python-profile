# @Time :2019/11/9 13:53
# @Auther :Ming
# @Software: PyCharm
import requests
url = 'http://www.baidu.com'
proxy = '222.89.32.183:9999'
proxies = {
    'http':'http://'+proxy,
    'https': 'http://'+proxy,
}
try:
    response = requests.get(url=url,proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('error',e.args)