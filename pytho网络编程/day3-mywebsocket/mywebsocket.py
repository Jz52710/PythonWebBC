import socketserver

"""
HTTP/1.1 201 OK\r\n\r\n
"""

# 服务器处理程序
# class MyWebServerHandler(socketserver.BaseRequestHandler):
#     def handle(self):
#         # self.request 客户端socket
#         # self.client_addresss 客户端的地址
#         # self.server = 服务器
#         print(self.request.recv(1024))
#         self.request.sendall("<div style='width:200px;height:200px;border:1px solid red;'>this is box</div>".encode())
#
#
# if __name__ == "__main__":
#     address = ('192.168.1.238',8000)
#     with socketserver.TCPServer(address,MyWebServerHandler) as server:
#         server.serve_forever()

class MyServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.render('index.html')
    def render(self,filename):
        self.request.sendall('HTTP/1.1 201 OK\r\n\r\n'.encode())
        with open("templates/%s"%filename, "rb") as f:
            con = f.read()
        self.request.sendall(con)

class MyWebServer:
    def __init__(self):
        self.server = ""
    def createServerHandler(self):
        """
        生成服务器处理程序
        :return:
        """
        return MyServerHandler

    def run(self,address=()):
        with socketserver.TCPServer(address,self.createServerHandler()) as s:
            self.server = s
            self.server.serve_forever()