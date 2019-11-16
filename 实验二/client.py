# @Time :2019/11/13 19:28
# @Auther :Ming
# @Software: PyCharm
from socket import *
import sys
dict1 = {'1':'''              
          ┌───────────┐
          │           │
          │     ●     │
          │           │
          └───────────┘
          ''',
         '2':'''
          ┌───────────┐
          │     ●     │
          │           │
          │     ●     │
          └───────────┘
          ''',
         '3':'''
          ┌───────────┐
          │ ●         │
          │     ●     │
          │         ● │
          └───────────┘
          ''',
         '4':'''
          ┌───────────┐
          │  ●     ●  │
          │           │
          │  ●     ●  │
          └───────────┘
          ''',
         '5':'''
          ┌───────────┐
          │  ●      ● │
          │      ●    │
          │  ●      ● │
          └───────────┘
          ''',
         '6':'''
          ┌───────────┐
          │  ●     ●  │
          │  ●     ●  │
          │  ●     ●  │
          └───────────┘
          '''
                }
dict2 = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六'}       #骰子点数字典
dict3 = {'tc':'头彩','dc':'大彩','kp':'空盘','qx':'七星','dd':'单对','sx':'散星','other':'其它'}    #结果字典
def oe(s):            #判断奇偶
    if (s%2) == 0:
        return 0
    else:
        return 1
def results():             #该局结果
    global n1,n2,n3,n4,ya
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)
    if (n1==n3) and (n2==n4):
        return 'tc'
    elif ((n1==n3)and(n2==n4))or((n1==n4)and(n2==n3)):
        return 'dc'
    elif (n3!=n4) and (oe(n3)==0) and (oe(n4)==0):
        return 'kp'
    elif ((n3+n4)==7):
        return 'qx'
    elif (oe(n3)==1) and (oe(n4)==1):
        return 'dd'
    elif ((n3+n4)==3)or((n3+n4)==5)or((n3+n4)==9)or((n3+n4)==11):
        return 'sx'
    else:
        return 'other'

def winorlose(money):           #金库状况
    betchose = ya['wtype']
    number = count_money(money)
    if ya['ctype'] == 'gold':
        ym = int(ya['number']) * 100
    elif ya['ctype'] == 'silver':
        ym = int(ya['number']) * 10
    elif ya['ctype'] == 'coin':
        ym = int(ya['number'])

    if betchose == results():
        print('恭喜你，你赢了')
        if betchose == 'tc':
            number += ym * 35
        elif betchose == 'dc':
            number += ym * 17
        elif betchose == 'kp':
            number += ym * 5
        elif betchose == 'qx':
            number += ym * 5
        elif betchose == 'dd':
            number += ym * 3
        elif betchose == 'sx':
            number += ym * 2
    else:
        print('你输了呢！')
        if betchose == 'tc':
            number -= ym * 17
        elif betchose == 'dc':
            number -= ym * 17
        elif betchose == 'kp':
            number -= ym * 5
        elif betchose == 'qx':
            number -= ym * 5
        elif betchose == 'dd':
            number -= ym * 3
        elif betchose == 'sx':
            number -= ym * 2
    a = number
    if number >= 0:
        coin = number%10
        gold = number//100
        silver = (number - 100*gold)//10
        print('目前金库:金子: {} 银子: {} 硬币: {}'.format(gold,silver,coin))
    else:
        number = -number
        coin = number % 10
        gold = number // 100
        silver = (number - 100 * gold) // 10
        print('目前金库:金子: {} 银子: {} 硬币: {}'.format(-gold,-silver,-coin))
    return a
#循环是为了保证能持续进行通话
def show_money(money):
    print('金子数量:{},银子数量:{},硬币数量:{}'.format(money['gold'],money['silver'],money['coin']))
def count_money(money):
    return money['gold']*100+money['silver']*10+money['coin']
def checkinput(bet,money):
    result = ['tc','dc','kp','qx','dd','sx']
    currency =['gold','silver','coin']
    a = 0
    c = 0
    b = count_money(money)
    bet1 = bet.split(' ')
    for i in result:
        if bet1[1] == i:
            a = 1
    for i in currency:
        if bet1[3] == i:
            c = 1
    if len(bet1) != 4:
        print('请输入正确的格式')
        return 0
    if bet1[0] != 'ya':
        print('请输入正确的开头(ya)')
        return 0
    if a == 0:
        print('请输入正确的种类')
        return 0
    if c == 0:
        print('请输入正确的货币单位')
        return 0
    if bet1[3] == 'gold':
        betnumber = int(bet1[2]) * 100
    elif bet1[3] == 'silver':
        betnumber = int(bet1[2]) * 10
    elif bet1[3] == 'coin':
        betnumber = int(bet1[2])
    if b < betnumber:
        print('您投注大于您的余额')
        return 0
    return 1
def client():
    address = ('127.0.0.1', 8880)
    cliSocket = socket(AF_INET, SOCK_STREAM)
    cliSocket.connect(address)  # 建立连接
    money = {'gold':10,'silver':10,'coin':10}

    print('-------------------------------------------')
    print('欢迎来到风月赌场,规则如下：')
    rules = """
    ya tc <数量> <coin|silver|gold> 押头彩(两数顺序及点数均正确)       一赔三十五
    ya dc <数量> <coin|silver|gold> 押大彩(两数点数正确)               一赔十七
    ya kp <数量> <coin|silver|gold> 押空盘(两数不同且均为偶数)         一赔五
    ya qx <数量> <coin|silver|gold> 押七星(两数之和为七)               一赔五
    ya dd <数量> <coin|silver|gold> 押单对(两数均为奇数)               一赔三
    ya sx <数量> <coin|silver|gold> 押散星(两数之和为三、五、九、十一)  一赔二
                            """
    print(rules)
    print('---一金子等于十银子，一银子等于十硬币，破产退出---')
    print('----初始财产----')
    show_money(money)
    a = 1
    while True:
        print("""
            庄家唱道：新开盘！预叫头彩！
            庄家将两枚玉骰往银盘中一撒。
            """)
        global n1,n2,n3,n4,ya
        n1 = (cliSocket.recv(1).decode('utf-8'))   # 1字节接受服务器端发来的点数
        n2 = (cliSocket.recv(1).decode('utf-8'))
        print(dict1[n1],dict1[n2])         #输出预叫头彩
        print('庄家唱道：头彩骰号是 {}、{}'.format(dict2[n1],dict2[n2]))
        while True:
            bet = input('输入你押的值  (ya <玩法> <数量> <coin|silver|gold>) ：')
            if checkinput(bet,money):
                break
        if bet== 'exit':          #退出
            cliSocket.send(bet.encode('utf-8'))
            sys.exit()
        else:                               #将玩家输入的信息切割为字典形式存放
            ya2 = bet.split(' ')
            ya1 = ['ya','wtype','number','ctype']
            ya = dict(zip(ya1,ya2))
            cliSocket.send(bet.encode('utf-8'))           #将玩家下的赌注发送给服务器端
            print("""
            庄家将两枚玉骰扔进两个金盅，一手持一盅摇将起来。
            庄家将左手的金盅倒扣在银盘上，玉骰滚了出来。""")
            n3 = (cliSocket.recv(1).decode('utf-8'))
            print(dict1[n3])
            print("""
                庄家将右手的金盅倒扣在银盘上，玉骰滚了出来。""")
            n4 = (cliSocket.recv(1).decode('utf-8'))
            print(dict1[n4])
            print('庄家叫道：{}、{}'.format(dict2[n3],dict2[n4]))
            print('摇骰子结果:{}'.format(dict3[results()]))           #结果
            a = winorlose(money)
            if a > 0:#金库情况
               print('资产足够，可以继续')
            else:
                print('你破产了，现在强制退出')
                cliSocket.send(str(results()+'玩家破产').encode('utf-8'))
                #以字节流的形式发送数据，需编码
                cliSocket.send('exit'.encode('utf-8'))
                sys.exit()
    cliSocket.close()        #关闭客户端
if __name__=='__main__':
    client()