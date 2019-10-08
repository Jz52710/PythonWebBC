import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 实例化 套接字对象
server.bind(('192.168.1.217',8000))  # 传入元组 address =  (ip,port)
server.listen(5)
while True:
    client,address = server.accept()
    print(address)
    client.close()

# """
# 地址簇
# socket.AF_INET IPv4
# socket.AF_INET6 IPv6
#
# 协议
# socket.SOCK_STREAM  TCP协议 (面向连接) 特点：效率要求不是很高，但是安全可靠性要求高时，例如：打电话，收发文件
# socket.SOCK_DGRAM   UDP协议 (面向无连接) 特点：对效率要求高，对内容要求不好时，例如：直播，语音。
#
# """