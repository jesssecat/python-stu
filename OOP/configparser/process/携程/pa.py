#加入上协程就会大大的减少等待时间
#在等待的时候会启动另外的进程开始执行
#大大的减少IO的时间
#更高速的爬虫运行速度
from gevent import monkey;monkey.patch_all()
import gevent

from urllib.request import urlopen
def get_url(url):
	response = urlopen(url)
	content = response.read().decode('utf-8')
	return len(content)

g1 = gevent.spawn(get_url,'http://www.baidu.com')
g2 = gevent.spawn(get_url,'http://www.sogou.com')
g3 = gevent.spawn(get_url,'http://www.taobao.com')
g4 = gevent.spawn(get_url,'http://www.jd.com')
g5 = gevent.spawn(get_url,'http://www.sohu.com')
gevent.joinall([g1,g2,g3,g4,g5])
print(g1.value)
print(g2.value)
print(g3.value)
print(g4.value)
print(g5.value)
