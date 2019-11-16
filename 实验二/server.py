# @Time :2019/11/13 19:26
# @Auther :Ming
# @Software: PyCharm
from socket import *
import socket
import random,sys
def send_roll(cli):
    print('四次投的数字分别是:')
    list = []
    for i in range(1, 5):  # 循环筛4次
        number = random.randint(1, 6)
        number = str(number)
        list.append(number)
        cli.send(number.encode('utf-8'))  # 每次筛好都发送到tcp传输队列中
        i = i+1
    string = ','.join(list)
    print(string)
def server():
    address = ('127.0.0.1',8880)
    tcpSer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #创建套接字
    tcpSer.bind(address)       #绑定地址（端口号）
    tcpSer.listen(1000)    #设置监听（最大连接数）
    while True:
        print('RemoteBet {}'.format(address))
        cli, add = tcpSer.accept()
        print('{} 加入了游戏'.format(add))        #记录玩家信息
        while True:
            send_roll(cli)      #每次筛好都发送到tcp传输队列中
            data = cli.recv(1024).decode('utf-8')    #接受客户数据并解码
            if not data or data == 'exit':
                sys.exit()
            print('玩家{}说：'.format(add)+data)        #玩家结果
        cli.close()
    tcpSer.close()                 #关闭套接字
if __name__ =='__main__':
    server()