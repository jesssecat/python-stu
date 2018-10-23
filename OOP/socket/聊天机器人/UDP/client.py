import socket
ip_port = ('127.0.0.1',9000)
sk = socket.socket(type=socket.SOCK_DGRAM)

sk.sendto(b'hello',ip_port)
ret,addr = sk.recvfrom(1024)
print(ret.decode('utf-8'))

sk.close()
