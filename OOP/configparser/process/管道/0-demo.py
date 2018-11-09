from multiprocessing import Pipe
conn1,conn2=Pipe()
conn1.send('123456')
print(conn2.recv())
