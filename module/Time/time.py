import time
#time.localtime()
#l= time.time()

#时间字符串
#l = time.strftime("%Y-%m-%d %X")

l = time.strftime("%Y-%m-%d %H-%M-%S")
#print(l)
#print(time.strftime("%Y-%m-%d %X", time.localtime()))

true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
struct_time=time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))
