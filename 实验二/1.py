# @Time :2019/11/16 13:10
# @Auther :Ming
# @Software: PyCharm
import random
money = {'gold':10,'silver':10,'coin':10}
bet = 'ya dd 1000 coin'
def count_money(money):
    return money['gold']*100+money['silver']*10+money['coin']
def checkinput(bet,money):
    result = ['tc','dc','kp','qx','dd','sx']
    currency =['gold','silver','coin']
    a = c = 0
    b = count_money(money)
    bet1 = bet.split(' ')
    for i in result:
        if bet1[1] == i:
            a = 1
    for i in currency:
        if bet1[3] == i:
            c = 1
    if bet1[0] != 'ya' or a == 0 or b < int(bet1[2]) or c == 0 or len(bet1) != 4:
        return 0
    else:
        return 1
betchose = ya['wtype']
number = ya['number']
results
if betchose == 'dc':
    print('恭喜你，你赢了')
    if betchose == 'tc':
        money[betchose] += number * 35
    elif ya['wtype'] == 'dc':
        money[betchose] += number * 17
    elif ya['wtype'] == 'kp':
        money[betchose] += number * 5
    elif ya['wtype'] == 'qx':
        money[betchose] += number * 5
    elif ya['wtype'] == 'dd':
        money[betchose] += number * 3
    elif ya['wtype'] == 'sx':
        money[betchose] += number * 2