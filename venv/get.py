import urllib.request
import urllib.parse
from lxml import etree
import textwrap

def query(content):
    # 请求地址
    url = 'https://baike.baidu.com/item/' + urllib.parse.quote(content)
    # 请求头部
    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' 
    }
    # 利用请求地址和请求头部构造请求对象
    req = urllib.request.Request(url=url, headers=headers, method='GET')
    # 发送请求，获得响应
    response = urllib.request.urlopen(req)
    # 读取响应，获得文本
    text = response.read().decode('utf-8')
    #fd = open(r'C:\Users\12931\Desktop\1.txt','w')
    #fd.write(text)
    # 构造 _Element 对象
    html = etree.HTML(text)
    # 使用 xpath 匹配数据，得到匹配字符串列表
    sen_list = html.xpath('//div[contains(@class,"lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
    # 过滤数据，去掉空白
    sen_list_after_filter = [item.strip('\n') for item in sen_list]
    # 将字符串列表连成字符串并返回
    comcise_show =''.join(sen_list_after_filter)
    return comcise_show
def down_lands(str1):
    with open('3.txt','a',encoding='utf-8') as f:
        f.write(str1+'\n')

if __name__ == '__main__':
    i = 1
    while (True):
        content = input('查询词语：')
        result = query(content)
        str1 = "%d.%s:%s"%(i,str(content),textwrap.fill(result,40))
        print(str1)
        print('while you to downlands the answer?')
        chice = input('(1)yes (2)no\n')
        down_lands(str1)
        i += 1




