from socket import socket

s = socket()
address = ('192.168.1.113',8080)
try:
    s.connect(address)
    print("欢迎使用有道翻译")
    while True:
        con = input("请输入内容：").encode()
        s.send(con)
        fy = s.recv(1024).decode()
        print(fy)
except:
    print("连接失败")