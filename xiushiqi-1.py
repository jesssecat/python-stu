import time
def func():
	time.sleep(0.01)
	print('hello,word')

def timmer(f):
	def inner():
		start = time.time()
		f()
		end = time.time()
		print(end - start)
	return inner

func = timmer(func)
func()
