import requests
url = 'http://dict.youdao.com/wordbook/wordlist?keyfrom=login_from_dict2.index'
response = requests.get(url)
print(response.text)


