from multiprocessing import Queue
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
print(q.full()) #判断是否满了，false或者true
#q.put(4)
#队列，容量是3，放置四个会卡住，造成进程阻塞

#往外面取出数据
print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #判断是否为空
