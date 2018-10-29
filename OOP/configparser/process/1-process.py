import time
import os
from multiprocessing import Process
def func(args,args2):
	print(args,args2)
	time.sleep(1)
	print('子进程：',os.getpid())
	print("子进程的父进程：",os.getppid())#当前进程的父进程
	print(12345)
if __name__ == '__main__':
	p = Process(target=func,args=('参数','参数2'))
	p.start()
	print('*'*10)
	print('父进程：',os.getpid())#查看当前进程的进程号
	print("父进程的父进程：",os.getppid())#当前进程的父进程
