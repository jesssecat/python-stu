from multiprocessing import Pipe,Process
def func(conn):
	conn.send('hello')
if __name__ == '__main__':
	conn1,conn2 = Pipe()
	Process(target=func,args=(conn1,)).start()
	print(conn2.recv())
