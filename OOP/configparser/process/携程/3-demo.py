#同步和异步
#爬虫或者高网络IO请求上
from gevent import monkey;monkey.patch_all()#必须在开头
import time
import gevent

def task():
	time.sleep(1)
	print(12345)

def sync():
	for i in range(10):
		task()

def async():
	g_lst = []
	for i in range(10):
		g = gevent.spawn(task)
		g_lst.append(g)
	gevent.joinall(g_lst)
sync() #同步
async() #异步

