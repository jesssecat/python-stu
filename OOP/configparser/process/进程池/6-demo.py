#进程和线程运行效率时间对比
#线程的优势：可以用来做高并发的操作
#效率更快，线程切换比进程切换快

import time
from threading import Thread
from multiprocessing import Process
def func(n):
	n + 1
if __name__ == '__main__':
	start = time.time()
	t_lst = []
	for i in range(1000):
		#开启1000个线程做的操作
		t = Thread(target=func,args=(i,))
		t.start()
		t_lst.append(t)
	for t in t_lst:t.join()
	t1 = time.time() -start
	
	start = time.time()
	t_lst = []
	for i in range(1000):
		#开启1000个进程所做的操作
		t = Process(target=func,args=(i,))
		t.start()
		t_lst.append(t)
	for t in t_lst:t.join()
	t2 = time.time() - start
	print(t1,t2)
