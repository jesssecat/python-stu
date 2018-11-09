from multiprocessing import Pipe,Process
def func(conn):
	while True:
		msg = conn.recv()#将信息接收
		if msg is None:break #是否为none
		print(msg)
if __name__ == '__main__':
	conn1,conn2 = Pipe()
	Process(target=func,args=(conn1,)).start()
	for i in range(20):
		conn2.send('hello')
	conn2.send(None) #生产者消费者模型设置为none

#管道服务，就是将conn1和conn2放置在一个管道里面
#在Pipe里面的进程就可以相互通信
