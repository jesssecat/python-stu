#科学家吃面
import time
from threading import Lock,Thread
#Lock是互斥锁
from threading import RLock  
#RLock 是递归锁
fork_lock = noodle_lock = RLock()# 一个钥匙串上的两把钥匙
#一串钥匙上的两把钥匙
def eat1(name):
	noodle_lock.acquire()
	print('%s拿到面条了'%name)
	fork_lock.acquire()
	print('%s拿到叉子了'%name)
	print('%s吃面'%name)
	fork_lock.release()
	noodle_lock.release()

def eat2(name):
	fork_lock.acquire()
	print('%s拿到叉子了'%name)
	time.sleep(1)
	noodle_lock.acquire()
	print('%s拿到面条'%name)
	print('%s吃面'%name)
	noodle_lock.release()
	fork_lock.release()




Thread(target=eat1,args=('jesse',)).start()
Thread(target=eat2,args=('Egon',)).start()
Thread(target=eat1,args=('zhenyu',)).start()
Thread(target=eat2,args=('haha',)).start()
