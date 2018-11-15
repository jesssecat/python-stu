from threading import Timer
def func():
	print('时间同步')

Timer(2,func).start()
