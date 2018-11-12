import time
import os
from multiprocessing import Pool
def func(n):
	print('start func%s'%n,os.getpid())
	time.sleep(1)
	print('end func%s' % n,os.getpid())

if __name__ == '__main__':
	p = Pool(5)
	for i in range(20):
		p.apply_async(func,args=(i,)) #apply_async异步执行，带有py里async都是异步
	p.close() #结束进程池接收任务
	p.join() #感知进程池中的任务执行结束

"""
start func0 46681
start func1 46682
start func2 46683
start func3 46684
start func4 46680
end func0 46681
start func5 46681
end func1 46682
start func6 46682
end func2 46683
start func7 46683
end func3 46684
start func8 46684
end func4 46680
start func9 46680
end func5 46681
start func10 46681
end func6 46682
start func11 46682
end func7 46683
start func12 46683
end func8 46684
start func13 46684
end func9 46680
start func14 46680
end func10 46681
start func15 46681
end func11 46682
start func16 46682
end func12 46683
start func17 46683
end func13 46684
start func18 46684
end func14 46680
start func19 46680
end func15 46681
end func17 46683
end func16 46682
end func19 46680
end func18 46684
"""
