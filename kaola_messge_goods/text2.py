import urllib.parse
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import pymysql
import time
import csv
import re
def crow(page,name,table_name):
    # url = 'http://www.baidu.com'
    url = 'http://www.kaola.com/'
    #不打开浏览器
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="topSearchInput"]').send_keys(name)
    # input = driver.find_element_by_id()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="topSearchBtn"]').click()
    for i in range(page):
        print('你正在爬第%d页\n'%(i+1))
        html = driver.page_source
        data = get_product(html)
        time.sleep(2)
        # downland(data)
        insert_into(data,table_name)
        time.sleep(1)
        if i < page and driver.find_element_by_xpath('//*[@class="nextPage"]'):
            driver.find_element_by_xpath('//*[@class="nextPage"]').click()
        else:
            i = page
def get_html():
    pass
def get_product(html):
    result = etree.HTML(html)
    name = result.xpath('//div[@class="img"]/img/@alt')
    price =result.xpath('//div[@class="desc clearfix"]/p[1]/span[1]/text()')
    title = '¥'
    for i in range(len(price)):
        price[i] = title + price[i]
    comments =result.xpath('//div[@class="desc clearfix"]/p[3]//text()')
    comments = ' '.join(comments)
    comments = re.findall(r'\d+',comments)
    storename = result.xpath('//div[@class="desc clearfix"]/p[4]//text()')
    storename_list = []
    for item in storename:
        if item != '' and item != ' ' and item != '  ' and item != '   ':
            storename_list.append(item)
    date = zip(name,price,comments,storename_list)
    return date
def downland(data):
    with open('2.csv', 'a', encoding='utf-8-sig', newline='') as f:  # 保存csv时编码格式 utf-o-sig不然会乱码
        writer = csv.writer(f)
        list = ['商品:','价格','评论','店铺']
        writer.writerow(list)
        for item in data:
            writer.writerow(item)
def insert_into(data,table_name):
    for item in data:
        sql = 'INSERT INTO {name} values (number,%s,%s,%s,%s);'.format(name = table_name)
        cursor.execute(sql, item)
        conn.commit()
    # for item in data
if __name__=='__main__':
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='helloworld',
        db='python',
        charset='utf8'
    )
    table_name = input('the name of sheme')
    cursor = conn.cursor()
    sql = 'CREATE TABLE %s ( number INT PRIMARY KEY AUTO_INCREMENT,name varchar(100) ,price varchar(10) not null,comment int(10) not null,store varchar(40)not null);' % table_name
    cursor.execute(sql)
    sql = 'alter table %s AUTO_INCREMENT = 1;'%table_name
    cursor.execute(sql)
    name = input('please enter the name of the goods')
    page = int(input('please enter the page'))
    crow(page,name,table_name)
    cursor.close()
    conn.close()
    print('thanks for you try')

