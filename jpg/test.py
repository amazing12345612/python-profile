import requests
url = 'https://image.baidu.com/search/acjson'
params = {
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': '加藤惠',
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': '加藤惠',
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': 0,
            'rn': 30,
            'gsm': '3c',
            '1488942260214': ''
        }
response = requests.get(url,params=params).json()
url = response.get('data')
get_jpg = requests.get(url[0]['thumbURL']).content
with open('demo.jpg', 'wb') as fp:
    fp.write(get_jpg)