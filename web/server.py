# coding: utf-8
from wsgiref.simple_server import make_server
from hello import application
#创建一个服务器，ip为空，端口80 处理函数application
httpd = make_server('',8000,application)
print('Serving HTTP on port port 8000...')
httpd.serve_forever()
