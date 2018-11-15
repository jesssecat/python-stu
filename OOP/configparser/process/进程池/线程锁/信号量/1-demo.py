#保护线程的分次执行
#可以设定每次执行几个
import time
from threading import Semaphore,Thread
def func(sem,a,b):
	sem.acquire()
	time.sleep(1)
	print(a+b)
	sem.release()
sem = Semaphore(4)
for i in range(20):
	t = Thread(target=func,args=(sem,i,i+5))
	t.start()
