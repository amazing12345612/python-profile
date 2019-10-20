import requests
import json
def openfile():
    with open(r'C:\Users\12931\Desktop\_citycode.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data
def getCode(data,city_name):
    result = [item['city_code'] for item in data if item['city_name'] == str(city_name)]
    if result:
        city_code = result[0]
    else:
        city_code = None
    return city_code
def getweather(citycode):
    url = 'http://t.weather.sojson.com/api/weather/city/'+str(citycode)
    response = requests.get(url)
    result = response.json()
    return result['data']
def show_weather(weather):
    print('日期:',weather['forecast'][0]['ymd'])
    print('温度:',weather['shidu'])
    print('温度:',weather['wendu'])
    print('空气质量:',weather['quality'])
    print('温馨提示:',weather['ganmao'])
if __name__ == '__main__':
    data = openfile()
    cityname = input('please enter city name:')
    citycode = getCode(data,cityname)
    weather = getweather(citycode)
    print('城市:',cityname)
    show_weather(weather)

