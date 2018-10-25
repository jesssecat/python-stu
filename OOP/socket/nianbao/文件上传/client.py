#发送端
import os
import json
import struct
import socket
sk = socket.socket()
sk.connect(('127.0.0.1',8000))
buffer = 1024
#buffer = 4096

head = {
	'filepath':r'./',
	'filename':r'1.tar.gz',
	'filesize':None
}

file_path = os.path.join(head['filepath'],head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
json_head = json.dumps(head) #字段转化为字符串
bytes_head = json_head.encode('utf-8')
#计算head长度
head_len = len(bytes_head) #报头的长度
pack_len = struct.pack('i',head_len)
sk.send(pack_len) #先发报文的长度
sk.send(bytes_head) #再发bytes类型的报文
with open(file_path,'rb')as f:
	while filesize:
		print(filesize)
		if filesize >= buffer:
			content = f.read(buffer) #每次读出来的内容
			sk.send(content)
			filesize -= buffer
		else:
			content = f.read(filesize)
			sk.send(content)
			break
sk.close()
