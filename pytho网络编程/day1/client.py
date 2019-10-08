from socket import socket
client = socket()

try:
    client.connect(('192.168.1.217',8000))
except:
    print("连接失败")