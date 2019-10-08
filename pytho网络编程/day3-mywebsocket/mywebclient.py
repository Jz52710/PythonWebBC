from mywebsocket import MyWebServer

app = MyWebServer()

if __name__ == "__main__":
    app.run(address=('192.168.1.107',8000))
