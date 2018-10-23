#服务器端
import socket
sk = socket.socket()  #买手机
#sk.bind('ip',port) #绑定手机卡
sk.bind(('127.0.0.1',8080))
sk.listen() #监听

conn,addr = sk.accept()  #接别人电话connection  连接：address地址

#ret = conn.recv(1024) #听别人说话
#print(ret)
#conn.send(b'hi') #和别人说话，必须传bytes类型

#ret = conn.recv(1024)
#print(ret.decode('utf-8'))
#conn.send(bytes('服务器一切正常',encoding='utf-8'))

#上面是自动聊天，不智能，下面是智能
while True:
	ret = conn.recv(1024).decode('utf-8')
	if ret == 'bye':
		break
	print('Cient:' + ret)
	info = input('你说：>>>')
	conn.send(bytes(info,encoding='utf-8'))

conn.close()
sk.close()


