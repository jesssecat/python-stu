from multiprocessing import Pipe,Process
def func(conn):
	conn.send('hello')
if __name__ == '__main__':
	conn1,conn2 = Pipe()
	Process(target=func,args=(conn1,)).start()
	print(conn2.recv())

#管道服务，就是将conn1和conn2放置在一个管道里面
#在Pipe里面的进程就可以相互通信
