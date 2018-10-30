#守护进程
#子进程 =》守护进程
import time
from multiprocessing import Process
def func():
	while True:
		time.sleep(0.2)
		print("子进程还存在")
if  __name__ == '__main__':
	p = Process(target=func)
	p.daemon = True
	p.start()
	#Process(target=func).start()
	i = 0
	while i<5:
		print('我是socket server:主进程')
		print(p.is_alive())
		time.sleep(1)
		print(p.is_alive()) #判断进程是否存活，返回true或者false
		i+=1
#p.terminate()  #结束一个守护进程，结束后并不能马上就结束，需要操作系统的回收
#守护进行会随着主进程的代码结束而结束
# p.name 进程的名字
# p.id	进程的进程号
