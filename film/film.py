import requests
from lxml import etree
def get_text(url_start):
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response =requests.get(url = url_start,headers = headers)
    if response:
        html = response.text
        return html
    else:
        return None
def get_real_url(html):
    list = []
    html = etree.HTML(html)
    result = html.xpath('//*[@id="content"]/div/div[1]/div[1]/div/attribute::data-cid')
    for item in result:
        url = 'https://movie.douban.com/j/review/'+str(item)+'/full'
        list.append(url)
    return list
def get_authods(list):
    for url in list:
        response = requests.get(url)
        result = response.json()
        #print(result['html'].replace('<p>','').replace('</p>',''))
html = get_text(url_start = 'https://movie.douban.com/review/best/')
list = get_real_url(html)
a = get_authods(list)
print(a)
#authods = html.xpath('')
#print(authods)