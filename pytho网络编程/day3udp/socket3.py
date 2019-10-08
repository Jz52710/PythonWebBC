from socket import socket,AF_INET,SOCK_DGRAM

s = socket(AF_INET,SOCK_DGRAM)

address = ("192.168.1.192",8000)
s.bind(address)

# s.listen(5)
while True:
    con,c_addresss = s.recvfrom(1024)
    print(con,c_addresss)