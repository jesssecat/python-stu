def generator():
	print(1)
	yield 'a'
#只要含有yield关键字的函数都是生成器函数
#yield不能和return公用且需要写在函数内
#生成器函数：执行之后会得到一个生成器作为返回值
#	return 'a'

ret = generator()
#print(ret)
#print(ret.__next__()) #1,a

def generators():
	print(1)
	yield 'a'
	print(2)
	yield 'd'
g = generators()
#ret = g.__next__()
#print(ret)
#ret = g.__next__()
#print(ret)

#也可以使用下面的方式
for i in g:
	print(i)
