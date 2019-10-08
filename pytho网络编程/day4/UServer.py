from socketserver import TCPServer,BaseRequestHandler
import re
"""
Userver 轻量级 web服务器框架

需求：
1、可以创建服务器
2、创建路由

"""
# 服务器 服务器处理程序
class UserverHandler(BaseRequestHandler):
    def handle(self):
        resText = self.request.recv(1024).decode("utf-8")
        resList = resText.split("\r\n")
        obj = {key:value for key,value in [tuple(item.split(": ")) for item in resList[1:] if item!='']}
        info = resList[0].split()
        obj['method'],obj['url'],obj['protocol'] = info
        self.req =obj
        if 'favicon' in obj['url']:
            #logo
            self.request.sendall(('HTTP/1.1 201 OK \r\n\r\n'+"").encode("utf-8"))
        elif 'static' in obj['url']:
            #静态
            with open('.'+obj['url'],'r',encoding='utf-8') as f:
                self.request.sendall(('HTTP/1.1 201 OK \r\n\r\n' + f.read()).encode("utf-8"))
        else:
            con = self.routes[obj['url']]()
            self.request.sendall(('HTTP/1.1 201 OK \r\n\r\n'+con).encode("utf-8"))

class Userver:
    def __init__(self):
        self.routes = {}

    def run(self,address):#创建web服务器并且运行
        UserverHandler.routes = self.routes
        with TCPServer(address,UserverHandler) as s:
            s.serve_forever()

    def route(self, dirname):
        def routewrap(fun):
            self.routes[dirname] = fun
            return fun()

        return routewrap

# def render(templateName,**kwargs):
#     with open('templates/%s'%templateName,'r',encoding='utf-8') as f:
#         con = f.read()
#     if kwargs:
#         return replaceVariable(con,kwargs)
#     else:
#         return con
#
# def replaceVariable(con,kwargs):
#     #只替换变量
#     keyArr = re.findall('\{% if.*?\%}(.*?)\{%else\%}(.*?)\{% endif\%}',con)
#     print(keyArr)
#     for key in kwargs:
#         for item in keyArr:
#             if key in item:
#                 con = con.replace(item,kwargs[key])
#     return con

def render(templateName,**kwargs):
    with open('templates/%s'%templateName,'r',encoding='utf-8') as f:
        con = f.read()
    if kwargs:
        return replaceVariable(con,kwargs)
    else:
        return con

def replaceVariable(con,kwargs):
    #只替换变量
    keyArr = re.findall('(\{\{.*?\}\})',con)
    for key in kwargs:
        for item in keyArr:
            if key in item:
                con = con.replace(item,kwargs[key])
    print(item,key)
    return con
