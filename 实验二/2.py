# @Time :2019/11/16 14:46
# @Auther :Ming
# @Software: PyCharm
bet = ['ya','ds','100','gold']
if bet[3] == 'gold':
    betnumber = int(bet[2]) * 100
elif bet[3] == 'silver':
    betnumber = int(bet[2]) * 10
elif bet[3] == 'coin':
    betnumber = int(bet[2])
print(betnumber)