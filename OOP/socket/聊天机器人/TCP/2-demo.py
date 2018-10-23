#客户端

#send -- recv
#recv -- send
#send -- recv
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8080))
#sk.send(b'hello,jesse')
#ret = sk.recv(1024)
#print(ret)
#sk.send(bytes('中午服务器怎么样'.encode('utf-8')))
#ret = sk.recv(1024)
#print(ret.decode('utf-8'))

#智能聊天
while True:
	info = input('你说:>>>')
	sk.send(bytes(info,encoding='utf-8'))
	ret = sk.recv(1024).decode('utf-8')
	print('Server:' + ret)
	if ret == 'bye':
		sk.send(b'bye')
		break
sk.close()
