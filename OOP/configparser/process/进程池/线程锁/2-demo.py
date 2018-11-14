import time
from threading import Lock,Thread

def func():
	global n
	temp = n
	time.sleep(0.2)
	n = temp - 1

n = 10
t_lst = []
for i in range(10):
	t = Thread(target=func)
	t.start()
	t_lst.append(t)
for t in t_lst:t.join()
print(n)
#这时候是输出的9 十个人取数据，因为sleep 等待cpu把时间片让出来了，别人取出的也是9
