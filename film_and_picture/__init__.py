
import requests
import re
import csv
import codecs#图片保存时图片名称中文保存方法
from lxml import etree
def get_text(i):
    url = 'https://movie.douban.com/top250?start=' + str(i) + '&filter='
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    return html
def get_message(html):
    html = etree.HTML(html)
    name = html.xpath('//div[@class="hd"]/a/span[1]/text()')
    infos = html.xpath('//div[@class="bd"]/p[1]//text()')
    roles = [j for i, j in enumerate(infos) if i % 2 == 0]
    type = [j for i, j in enumerate(infos) if i % 2 != 0]
    score = html.xpath('//div[@class="star"]/span[2]/text()')
    quote = html.xpath('//div[@class="bd"]/p[2]/span//text()')
    item = zip(name,roles,type,score,quote)
    # return director
    return item
def down_land(data,type):
    if type == 'txt':
        for item in data:
            with open('1.txt','a',encoding='utf-8') as f:
                f.write('电影名称:'+str(item[0].replace(' ',''))+'\n')
                f.write(str(re.sub(r'[\'\xa0\s ]*', '', item[1]))+'\n')#正则表达式将\,xa0等消除
                f.write('年份/类别:'+str(item[2].replace(' ','').replace('\n',''))+'\n')#去掉空格
                f.write('评分:'+str(item[3])+'\n')
                f.write('语录:'+str(item[4].replace(' ',''))+'\n')
    elif type == 'csv':
        with open('11.csv','a',encoding='utf-8-sig',newline='') as f:#保存csv时编码格式 utf-o-sig不然会乱码
            writer = csv.writer(f)
            for item in data:
                writer.writerow(item)
    else:
        print('can not find the type what you will downland')
def crow(type):
    for i in range(0,250,25):
        j = i/25+1
        text = get_text(i)
        print('正在爬取第%d页\n'%j)
        data = get_message(text)    
        down_land(data,type)
def get_picture(html):
    localPath = 'E:/python-project/text/jpg/'
    html = etree.HTML(html)
    picture = html.xpath('//div[@class="pic"]/a/img/@src')#图片的url
    image_name = html.xpath('//div[@class="hd"]/a/span[1]/text()')#图片名称
    return picture,image_name
def downland_picture(i,picture,image_name):
    localPath = 'E:/python-project/film_and_picture/jpg2/'
    x = 0
    for url in picture:
        headers = {
            'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        with codecs.open(localPath + '%d%s.jpg' %((i+x+1),image_name[x]), 'wb') as f:
            f.write(response.content)
        print('正在下载第%d张'%(i+x+1))
        x = x + 1

if __name__=='__main__':
    number = int(input('chose 1 to download message chose 2 to download picture\n'))
    if number == 2:
        for i in range(0,250,25):
            text = get_text(i)
            j = i/25+1
            picture,image_name = get_picture(text)
            print('正在下载第%d页'%j)
            downland_picture(i,picture,image_name)
    elif number == 1:
        type = input('what type do you want to dowland?\n')
        crow(type)




