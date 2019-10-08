from UServer import Userver,render
import pickle
"""
myserver 网站后台
"""
#s实例化应用
app = Userver()

@app.route('/')
def index():
    #读取数据库中的信息
    with open('a.txt','rb') as f:
        obj = pickle.load(f)
    return render('index.html',**obj)

@app.route('/list')
def list():
    return '<div>首页</div>'

@app.route('/con')
def con():
    return '<div>详情页</div>'

if __name__ == "__main__":
    app.run(address=('192.168.1.113',8000))