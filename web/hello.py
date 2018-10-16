# coding: utf-8
import os
import sys
def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
  
	#return [b'<h1>Hello,Jesse</h1>']
	body = '<h1>Hello,%s!</h1>' %(environ['PATH_INFO'][1:] or 'You please ip:8000\str')
	return [body.encode('utf-8')]
#上面是一个基本的web服务器
#无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

#复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
