# @Time :2019/11/12 15:59
# @Auther :Ming
# @Software: PyCharm
# import re
import pymysql
def getcursor():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='helloworld',
        db='python',
        charset='utf8'
    )
    cursor = conn.cursor()
    return conn,cursor
def checkuser(cursor,conn):
    sql = 'select * from message;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        a = len(result)
        print(a)
        for s in result:
            print(s[0])
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
def insertuser(cursor,conn,message):
    sql = 'INSERT INTO message VALUES (%s);'
    try:
        cursor.execute(sql, message)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
if __name__=='__main__':
    message = 'dasdadasda大师'
    conn, cursor = getcursor()
    insertuser(cursor,conn,message)
    conn, cursor = getcursor()
    checkuser(cursor,conn)
# print('现在在线的用户有:')
# for name in userlist:
#     print(name)
# content= 'cjm,sdasdasd'
# print(type(content))
# privatename = re.match(r'@(.*?),(.*)',content)
# print(privatename)
# # a = {'username':'ming','sdad':'12311'}
# text = 'login,happy,123456'
# a = text.split(',')
# name = a[1:]
# name = ''.join(name)
# print(name)
# def judgr(a,name,password):
#     c = 0
#     for key in a:
#         if key == name and a[key] == password:
#             c = 1
#     return c
# if judgr(a,name,password):
#     print('dada')
# else:
#     print('dasdad')


