from multiprocessing import Pool
def func(i):
	return i*i

if __name__ == '__main__':
	p = Pool(5)
	for i in range(10):
		res = p.apply(func,args=(i,))
		print(res)
#同步
