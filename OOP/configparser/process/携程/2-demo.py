#协程一般是用到高IO上
from greenlet import greenlet
def eat():
	print('eating start')
	g2.switch()
	print('eating end')
	g2.switch()
def play():
	print('playing start')
	g1.switch()
	print('playing end')
g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
