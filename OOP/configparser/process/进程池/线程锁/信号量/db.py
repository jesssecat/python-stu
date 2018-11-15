import time
import random
from threading import Thread,Event
def connect_db(e):
	count = 0
	while count < 3:
		e.wait(1)#状态为false时候，等待1s就结束
		if e.is_set() == True:
			print('连接数据库成功')
			break
		else:
			count+=1
			print('第%s连接失败'%count)
	else:
		raise TimeoutError('数据库连接超时') #设置个错误，弹出错误

def check_web(e):
	time.sleep(random.randint(0,3))
	e.set()

e = Event()
t1 = Thread(target=connect_db,args=(e,))
t2 = Thread(target=check_web,args=(e,))
t1.start()
t2.start()
