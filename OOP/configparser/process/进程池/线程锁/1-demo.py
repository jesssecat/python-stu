from threading import Lock
lock = Lock() #线程锁
lock.acquire()
#lock.acquire()#一个会直接输出，两个线程锁生效
print(123)
