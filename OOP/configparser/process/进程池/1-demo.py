#进程池的概念是：可以在进程池中定义几个进程，比如五个进程，有任务的时候五个进程一起执行
#执行结束后，五个继续执行其它的任务，快速
#多进程是设置50个进程，开始就启动50个进程，效率是不如进程池的
import time
from multiprocessing import Pool,Process
def func(n):
	for i in range(10):
		print(n+1)
if __name__ == '__main__':
	start = time.time()
	pool = Pool(5)#五个进程
	pool.map(func,range(100))#100个任务
	t1 = time.time() - start
	start = time.time()
	p_lst = []
	for i in range(100):
		p = Process(target=func,args=(i,))
		p_lst.append(p)
		p.start()
	for p in p_lst :p.join()
	t2 = time.time() - start
	print(t1,t2)
