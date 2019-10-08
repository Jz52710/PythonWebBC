import time,datetime
#日期
#1.时间戳
print(time.time())
#2.时间元组
res = time.localtime(time.time())#把时间戳转化为时间元组
print(res)
#格式化时间
res1 = time.strftime("%Y-%m-%d (%H:%M:%S)",res)#将时间元组转化为格式化时间
print(res1)

d=datetime.date(2019,9,26)
print(d)

print("当前日期",datetime.date.today())
a = datetime.date(2019,11,11)
print(a)