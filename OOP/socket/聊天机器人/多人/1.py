import socketserver
class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		#print(self.request.recv(1024).decode('utf-8'))
		while True:
			msg = self.request.recv(1024).decode('utf-8')
			if msg == 'q':
				self.request.close()
				break
			print(msg)
			info = input('>>>')
			self.request.send(info.encode('utf-8'))
if __name__ == '__main__':
	server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),MyServer)
	server.serve_forever()
