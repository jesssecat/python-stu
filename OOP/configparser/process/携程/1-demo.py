#本质是一个线程
#能够在多任务中切换来节省一些IO时间
def consumer():
	while True:
		x = yield
		print('处理了数据:',x)
def producer():
	c = consumer()
	next(c)
	for i in range(10):
		print('生产了数据：',i)
		c.send(i)

producer()
