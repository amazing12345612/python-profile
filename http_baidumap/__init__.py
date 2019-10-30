#AK = jWN8jTS11GU4cVUIcGmow6wDVmKvEH98
#SK = 4ouqWc8QeyyV0sa39grhP7aBmoB6ypFE
import json
from urllib.request import urlopen, quote
import requests
def getlnglat(address):
   url = 'http://api.map.baidu.com/geocoder/v2/'
   output = 'json'
   ak = 'jWN8jTS11GU4cVUIcGmow6wDVmKvEH98' # 百度地图ak，具体申请自行百度，提醒需要在“控制台”-“设置”-“启动服务”-“正逆地理编码”，启动
   address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
   uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak
   req = urlopen(uri)
   res = req.read().decode()
   temp = json.loads(res)
   print(temp)
   lat = temp['result']['location']['lat']
   lng = temp['result']['location']['lng']
   return lat,lng   # 纬度 latitude   ，   经度 longitude  # ，
if __name__=='__main__':
    address = '北京'
    a,b = getlnglat(address)
    print(a,b)
