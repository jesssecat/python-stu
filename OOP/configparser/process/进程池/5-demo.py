import time
from multiprocessing import Pool
def func(i):
	time.sleep(0.5)
	return i*i

if __name__ == '__main__':
	p = Pool(5)
	res_l = []  #将数据放到一个列表里，否则是一个个出
	for i in range(20):
		res = p.apply_async(func,args=(i,))
		res_l.append(res)
	for res in res_l:print(res.get())#等待func的计算结果

#因为线程池里面有五个线程
#要处理20个数据，要处理四次
#结果就是五个五个的出现
