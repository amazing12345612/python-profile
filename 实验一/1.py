# @Time :2019/11/12 14:17
# @Auther :Ming
# @Software: PyCharm
import socket,argparse
import re
import os
import sys
from datetime import datetime
MAX_Bytes = 65535
def jujge(checkuser,username,password):
    a = 0
    for key in checkuser:
        if username == key and password == checkuser[key]:
            a = 1
    return a
def server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',port))
    print('listen at {}'.format(sock.getsockname()))
    checkuser = {'ming':'123456','cjm':'12345678'}
    userlist={}
    while True:
        data,address = sock.recvfrom(MAX_Bytes)
        text = data.decode('ascii')
        # print('the client at {} says {!r}'.format(address,text))
        # username = re.search('.*?is\s(.*?)\s', text).group(1)
        # password = re.search('pass.*?is\s(.*)', text).group(1)
        # if jujge(userlist,username,password):
        #     text = 'login in successful'
        #     data = text.encode('ascii')
        #     sock.sendto(data,address)
        # else:
        #     text = 'please regist'
        #     data = text.encode('ascii')
        #     sock.sendto(data,address)
        msglist = data.decode().split(',')  # 拆分数据,以空格为分隔
        if msglist[0] == 'login':  # 如果是进入聊天室请求
            doLogin(sock, checkuser,userlist, msglist, address)
        elif msglist[0] == 'speak':
            # msglist:['c','name','content']
            content = ' '.join(msglist[2:])  # 获取完整发送内容
            # 发送给其他所有成员
            doChat(sock, content, userlist, msglist)
        elif msglist[0] == 'privatespeak':
            content = ' '.join(msglist[3:])
            doprivateChat(sock,content,userlist,msglist)
        elif msglist[0] == 'quit':
            doQuit(sock, msglist, userlist)
        elif msglist[0] == 'regist':
            doRegist(sock,checkuser,userlist,msglist,address)
def doChat(sock,content,userlist,msglist):
    name = msglist[1]
    message = '\n%s 说：%s' % (name, content)
    for u in userlist:
        if u != name:  # 发给不是自身的所有客户端
           sock.sendto(message.encode(), userlist[u])
def doprivateChat(sock,content,userlist,msglist):
    name = msglist[1]
    desname = msglist[2]
    message = '\n%s 说：%s' % (name, content)
    for u in userlist:
        if u == desname:
            sock.sendto(message.encode(),userlist[u])
            return
    sock.sendto('目标用户不存在，请重新发送'.encode(),userlist[name])
def doQuit(sock,msglist,userlist):
    name = msglist[1]
    message = '\n%s 退出了聊天室' % name
    for u in userlist:
        if u != name:
            server.sendto(message.encode(), userlist[u])
        else:
            server.sendto('exit'.encode(), userlist[name])
        # 从存储结构中删除
    del userlist[name]

def doRegist(sock,checkuser,userlist,msglist,address):
    name = msglist[1]
    for u in checkuser:
        if name == u:
            sock.sendto('用户已存在'.encode(),address)
            return
    userlist[name] = address  # 加入到存储结构userlist字典中
    print(userlist)

def doLogin(sock,checkuer,userlist,msglist,address):
    name = msglist[1]
    password = msglist[2]
    if jujge(checkuer,msglist[1],msglist[2]):  #
        sock.sendto('OK'.encode(), address)
        # 通知所有人
        message = '\n欢迎%s进入聊天室' % name
        for u in userlist:
            sock.sendto(message.encode(), userlist[u])  # 全发
        userlist[name] = address
        print(userlist)
    else:
        sock.sendto('please regist'.encode('ascii'),address)
def client(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    address = ('127.0.0.1',port)
    while True:
        username = input('please enter your name')
        password = input('please enter your password')
        type = input('please enter the type')
        text = '{},{},{}'.format(type,username,password)
        data = text.encode('ascii')
        sock.sendto(data,address)
        data, address = sock.recvfrom(MAX_Bytes)
        if data.decode('ascii') == 'OK':
            print('您已经进入聊天室...')
            break

        else:  # 不允许进入
            print(data.decode('ascii'))

    pid = os.fork()
    if pid == 0:
        sendmsg(sock,username,address)
    else:
        recvmsg(sock)
def sendmsg(sock,name,address):
    #发送消息给服务器，服务器群发给所有客户端
    while True:
        content=input('请发言（输入quit 退出）：')
        if content == 'quit':
            message =  'quit ' + ','+name
            sock.sendto(message.encode(),address)
            sys.exit('已退出聊天室')#子进程退出
        message = 'speak,%s,%s' % (name,content)
        client.sendto(message.encode(),address)
def recvmsg(sock):
    while True:
        data, address = sock.recvfrom(MAX_Bytes)
        if data.decode() == 'exit':#如果收到服务器此消息，父进程退出
            os._exit(0)
        #因为print覆盖了之前的input界面，在这里重新输出一遍
        print(data.decode()+'\n请发言（quit退出）：',end='')




if __name__ == '__main__':
    choices = {'client':client,'server':server}
    parser = argparse.ArgumentParser(description = 'send and recive UDP locally')
    parser.add_argument('role',choices = choices,help = 'which role to play')
    parser.add_argument('-p',metavar ='PORT',type = int ,default = 1060,help = 'UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)