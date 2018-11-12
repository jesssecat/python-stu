#同步执行
import time
import os
from multiprocessing import Pool
def func(n):
	print('start func%s'%n,os.getpid())
	time.sleep(1)
	print('end func%s' % n,os.getpid())

if __name__ == '__main__':
	p = Pool(5)
	for i in range(20):
		p.apply(func,args=(i,)) #apply是同步执行的，输出的结果是一个id开始，id结束，然后下一个id

