#运行后发现，是等待了五秒后全部出来的
#并没有等待五十秒，他是异步执行的
#相当于十条马路同时等待5秒
import time
from multiprocessing import Process

def func(arg1,arg2):
	print('*'*arg1)
	time.sleep(5)
	print('*'*arg2)

if __name__ == '__main__':
	for i in range(10):
		p = Process(target=func,args=(10*i,20*i))
		p.start()
		#p.join() 加上join就变成同步了，运行五秒就在继续五秒
		print('运行完了')
