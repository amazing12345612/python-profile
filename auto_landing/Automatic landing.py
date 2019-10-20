import time
from selenium import webdriver
import csv
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://account.youdao.com/login?service=dict&back_url=http://dict.youdao.com/wordbook/wordlist%3Fkeyfrom%3Dlogin_from_dict2.index')
#driver.get('https://www.baidu.com')
#driver.get('http://account.youdao.com/login?service=dict&back_url=http://dict.youdao.com/wordbook/wordlist%3Fkeyfrom%3Dlogin_from_login_from_dict2.index')
driver.implicitly_wait(8)
#driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
driver.find_element_by_xpath("//*[@name='agreePrRule']").click()
time.sleep(1)
#driver.find_element_by_xpath("//*[@name='agreePrRule']").click()
driver.find_element_by_xpath(
    "//*[@id='username']").send_keys("1293156042@qq.com")
time.sleep(1)
driver.find_element_by_xpath(
    "//*[@id='password']").send_keys("makesense")
time.sleep(1)
# 在输入用户名和密码之后,点击登陆按钮
driver.find_element_by_xpath("//*[@class='login_btn']").click()
time.sleep(2)
#很容易被网站识别出来 重新验证
i = 0
for i in range(1,16):
    a = driver.find_element_by_xpath("//*[@id='wordlist']/table/tbody/tr[%d]"%i).text
    a = a.replace('\n','')
    print(a)
    with open('1.txt','a',encoding='utf-8') as f:
        f.write(a+'\n')



