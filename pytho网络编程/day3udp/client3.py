from socket import socket,AF_INET,SOCK_DGRAM
import time

s_address = ('192.168.1.192',8000)

c = socket(AF_INET,SOCK_DGRAM)

c.sendto('hello world'.encode(),s_address)
time.sleep(5)