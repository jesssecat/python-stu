from multiprocessing import Pipe,Process
def func(conn1,conn2):
	conn2.close()
	while True:
		try: #如果有异常
			msg = conn1.recv()
			print(msg)
		except EOFError:
			conn1.close()
			break
if __name__ == '__main__':
	conn1,conn2 = Pipe()
	Process(target=func,args=(conn1,conn2)).start()
	conn1.close()
	for i in range(20):
		conn2.send('hello')
	conn2.close()
 #生产者消费者模型设置为none

#管道服务，就是将conn1和conn2放置在一个管道里面
#在Pipe里面的进程就可以相互通信
