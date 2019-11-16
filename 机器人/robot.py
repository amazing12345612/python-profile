import requests

def get_response(msg):
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    KEY = 'f7859e4850754f2ab2b308bc2c9b757c'
    data = {
        'key'    : KEY,
        'info'   : msg,
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

def chat(a):
    while True:
        if a == 0:
            print("TL: ",get_response('你好'))
        else:
            tt = get_response(input("MY: "))
            print("TL: ",tt)
        a = 1

if __name__ == "__main__":
    chat(0)