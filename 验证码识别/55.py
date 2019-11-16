# @Time :2019/11/12 19:06
# @Auther :Ming
# @Software: PyCharm

import PIL
import requests
import json
url = 'http://www.anishathalye.com/media/2017/07/25/imagenet.json'
response = requests.get(url)
data =response.json()
with open('data.json', 'w') as f:
    json.dump(data, f)
# img = PIL.Image.open(img_path)
