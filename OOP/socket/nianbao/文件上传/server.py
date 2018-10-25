#大文件上传下载
#配置文件，ip地址 端口号
import time
import struct
import json
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()
buffer = 1024  #别的数值可能传输文件不完整
conn,addr = sk.accept()
#接收
head_len = conn.recv(4)
head_len = struct.unpack('i',head_len)[0]
json_head = conn.recv(head_len).decode('utf-8')
head = json.loads(json_head)
filesize = head['filesize']
print(filesize)
with open(r'新文件-%s' %head['filename'],'wb') as f:
	while filesize:
		if filesize >= buffer:
			print(filesize)
			content = conn.recv(buffer)
			f.write(content)
			filesize -= buffer
		else:
			content = conn.recv(filesize)
			f.write(content)
			filesize = 0
		print('===>',len(content))
	print(filesize)

print('服务端。。。')
conn.close()
sk.close()
