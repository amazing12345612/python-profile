#总的来说就是在有道词典上进行爬取单词本的词语以及自动上传单词
import time
from selenium import webdriver
import csv
# 从txt文件中添加单词到a列表中,split()函数通过, 号分割字符串
def input_words():
    with open('2.txt','r',encoding='utf-8') as f:
        a = f.read().split(',')
    return a
def driver_land(driver,username,password):
    # driver.get('https://www.baidu.com')
    # driver.get('http://account.youdao.com/login?service=dict&back_url=http://dict.youdao.com/wordbook/wordlist%3Fkeyfrom%3Dlogin_from_login_from_dict2.index')
    driver.implicitly_wait(8) #静态等待
    # driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
    driver.find_element_by_xpath("//*[@name='agreePrRule']").click()#登陆时服从网站的协议的打勾按钮
    time.sleep(1)
    # driver.find_element_by_xpath("//*[@name='agreePrRule']").click()
    driver.find_element_by_xpath("//*[@id='username']").send_keys(username)#账号
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='password']").send_keys(password)#密码
    time.sleep(1)
    # 在输入用户名和密码之后,点击登陆按钮
    driver.find_element_by_xpath("//*[@class='login_btn']").click()#点击登陆按钮
    time.sleep(3)
#下载单词本里的单词
def download():
    i = 0
    #number = driver.find_element_by_xpath("//*[@id='wordfoot']/div[2]/strong[2]").text
    #print(number)
    for i in range(1,16):
        a = driver.find_element_by_xpath("//*[@id='wordlist']/table/tbody/tr[%d]"%i).text #单词在worlist中通过text爬取
        a = a.replace('\n','')#去除空格
        print(a) #测试用，查看下载的单词
        with open('1.txt','a',encoding='utf-8') as f:
            f.write(a+'\n')
#添加单词到有道单词本中
def add_word(driver):
    i = 0
    a = input_words()
    for i in range(len(a)):
        driver.find_element_by_xpath("//*[@id='addword']").click() #找到网页添加单词的按钮，输入后添加单词
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='word']").send_keys(a[i])
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='editwordform']/form/div/button").click()
        i += 1
if __name__=='__main__':
    j = 1
    username = "1293156042@qq.com"
    password = "makesense"
   # username = input('please enter your user name')
    #password = input('pleease enter your password')
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'http://account.youdao.com/login?service=dict&back_url=http://dict.youdao.com/wordbook/wordlist%3Fkeyfrom%3Dlogin_from_dict2.index'
    driver.get(url)
    driver_land(driver,username,password)
    #download()
    #driver.find_element_by_xpath("//*[@id='pagination']/a[%d]"%j).click()
    time.sleep(1)
    elect_1= int(input('will you to add the word?(1)yes,(else)no\n'))
    if (elect_1 == 1):
        add_word(driver)
    else:
        print('thank you')
    elect_2 = int(input('will you to downland the word? (1)yes,(else)no)\n'))
    if(elect_2 == 1):
        page = int(input('please enter the number of page'))
        time.sleep(2)
        while j <= page:
            #driver.find_element_by_xpath("//*[@id='pagination']/a[3]").click()
            driver.find_element_by_xpath("//*[@id='pagejumpform']/input").send_keys(j)#找到页码输入部分
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='pagejumpform']/button").click()
            time.sleep(2)
            download()
            if j == 3:
                print('down successful')
            j = j + 1

    else:
        print('thank you')