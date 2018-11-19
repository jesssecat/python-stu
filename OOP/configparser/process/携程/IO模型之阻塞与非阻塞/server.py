import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()
conn_l = []
del_conn = []
while True:
	try:
		conn,addr = sk.accept()
		print('连接建立:',addr)
		conn_l.append(conn)
	except BlockingIOError:
		for con in conn_l:
			try:
				msg = con.recv(1024)
				if msg ==b'':
					del_conn.append(con)
					continue
				print(msg)
				con.send(b'byebye')
			except BlockingIOError:pass
		for con in del_conn:
			conn_l.remove(con)
		del_conn.clear()
