from socket import socket
import requests
import lxml.etree as etree
urls = 'http://m.youdao.com/translate'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.17 Safari/537.36'}
def fanyi(con):
    res = requests.post(url=urls,data={
        'inputtext':con,
        'type':'AUTO'
    },headers=headers)
    htmlObj = etree.HTML(res.text)
    yi = htmlObj.xpath('//ul[@id="translateResult"]/li/text()')[0]
    return yi

#服务器
s = socket()
s.bind(('192.168.1.113',8080))
s.listen(5)
print("服务器建立监听")

while True:
    c,address = s.accept()
    print(address,"连接中...")
    while True:
        con = c.recv(1024).decode()
        res = fanyi(con)
        c.send(res.encode())
