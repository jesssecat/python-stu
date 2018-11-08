#队列
#生产者消费者模型
#生产者进程
#消费者进程
#可以解决供需不平衡的问题
#生产者生产数据
#消费者处理数据
import time
import random
from multiprocessing import Process,Queue
def consumer(q,name):
	while True:
		food = q.get()
		if food is None:
			print('%s获得一个空'%name)
			break
		print('\033[31m%s消费了%s\033[0m' %(name,food))
		time.sleep(random.randint(1,3))
def producer(name,food,q):
	for i in range(4):
		time.sleep(random.randint(1,3))
		f = '%s生产了%s%s'%(name,food,i)
		print(f)
		q.put(f)
if __name__ == '__main__':
	q = Queue(20)
	p1 = Process(target=producer,args=('Egon','包子',q))
	p2 = Process(target=producer,args=('Jesse','饺子',q))
	c1 = Process(target=consumer,args=(q,'alex'))
	c2 = Process(target=consumer,args=(q,'zhenyu'))
	p1.start()
	p2.start()
	c1.start()
	c2.start()
	p1.join() #感知生产是否结束
	p2.join() #感知生产是否结束
	q.put(None) #两个人拿到两个空
	q.put(None)
