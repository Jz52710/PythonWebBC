from socket import socket
import json,time,hashlib
import os

md5 = hashlib.md5()

class FTPserver:
    def __init__(self):
        self.__address = ('192.168.1.102',8080)
        self.__s = ""
        self.__root = r'C:\Users\86427\Desktop\pytho网络编程\day2ftp\root'
        self.users=[
            {'username':'jz','password':'52710','home':r"\home"},
        ]
        self.tokens = []

    def createServer(self):
        self.__s = socket()
        self.__s.bind(self.__address)#绑定地址
        self.__s.listen(10)
        print("服务器已开启，等待连接...")
        while True:
            self.__c,self.__c_address = self.__s.accept()#接受客户端链接
            print(self.__c_address,"连接成功")
            self.login()
            self.ftpserver()

    #登录
    def login(self):
        while True:
            obj = json.loads(self.__c.recv(1024).decode())#接收用户名、密码
            print(obj)
            username = obj['username']
            password = obj['password']
            for user in self.users:
                if user['username']==username:
                    if user['password']==password:
                        token = str(int(time.time())).encode()
                        md5.update(token)
                        token = md5.hexdigest()
                        self.tokens.append(token)
                        res = {'status': 'ok', 'msg': "登录成功", 'home': user['home'], 'token': token}
                        print(res)
                        os.chdir(self.__root+"\\"+user['home'])
                    else:
                        res = {'status':'error','msg':'密码错误'}
                else:
                    res = {'status':'error','msg':'用户名不存在'}

            if res['status'] != "ok":
                self.__c.send(json.dumps(res).encode())#发送
            else:
                self.__c.send(json.dumps(res).encode())#发送
                break
    #quit,ls命令
    def ftpserver(self):
        while True:
            mls = self.recv().strip().split()
            print(mls)
            #quit
            if mls[0] == "quit":
                print(self.__c_address, "退出")
                self.send({'status': 'quit', 'con': ""})
                self.__c.close()
                break
            #cd
            elif mls[0] == "cd":
                if os.path.isdir(mls[1]):
                    os.chdir(os.path.join(os.getcwd(), mls[1]))
                    self.send({'status':'cd','con':os.getcwd().split("root\\")[1]})
                elif mls[1] == '..':
                    os.chdir("\\".join(os.getcwd().split("\\").pop()))
                    self.send({'status':'cd','con':os.getcwd().encode()})
            #ls
            elif mls[0] == "ls":
                con = ''
                if len(mls) > 1:
                    if mls[1] == '-l':
                        for r in os.listdir():
                            res = os.stat(os.path.join(os.getcwd(),r))
                            info = "%s %s %s %s %s %s\n"%(
                                r,
                                res.st_atime,
                                res.st_ctime,
                                res.st_mtime,
                                res.st_size,
                                res.st_ino,
                            )
                            con += info
                else:
                    con = "\n".join(os.listdir())
                self.send({'status': 'ok', 'con': con})
            #mkdir
            elif mls[0] == 'mkdir':
                if len(mls) >= 1:
                    os.mkdir(mls[1])
                    self.send({'status':'ok','con':''})
                else:
                    pass
            #touch
            elif mls[0] == 'touch':
                if len(mls) >= 1:
                    open(mls[1],'w').close()
                    self.send({'status':'ok','con':''})
                else:
                    pass
            #rm
            elif mls[0] == 'rm':
                if os.path.isdir(mls[1]):
                    os.rmdir(mls[1])
                    self.send({'status':'rm','con':'删除成功'})
                else:
                    os.remove(mls[1])
                    self.send({'status':'rm','con':'删除成功'})

    #验证身份
    def recv(self):
        con = self.__c.recv(1024)
        con = json.loads(con.decode())
        if "token" in con:
            if con['token'] in self.tokens:
                return con['con']
        print(self.__c_address, "验证失败,强制退出")
        self.__c.close()

    def send(self, con):
        self.__c.send(json.dumps(con).encode())






if __name__ == "__main__":
    ftp = FTPserver()
    ftp.createServer()


