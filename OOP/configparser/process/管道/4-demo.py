import time
import random
from multiprocessing import Pipe,Process
def producer(con,pro,name,food):
	con.close()
	for i in range(4):
		time.sleep(random.randint(1,3))
		f = '%s生产%s%s'%(name,food,i)
		print(f)
		pro.send(f)
	pro.close()
def consumer(con,pro,name):
	pro.close()
	while True:
		try:
			food = con.recv()
			print('%s吃了%s'%(name,food))
			time.sleep(random.randint(1,3))
		except EOFError:
			con.close()
			break

if __name__ == '__main__':
	con,pro = Pipe()
	p = Process(target=producer,args=(con,pro,'egon','饺子'))	
	p.start()
	c = Process(target=consumer,args=(con,pro,'jesse'))
	c.start()
	con.close()
	pro.close()
