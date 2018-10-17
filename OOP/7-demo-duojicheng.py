class A:
	def func(self): print('A')
class B:
	def func(self): print('B')
class C:
	def func(self): print('C')
class D(A,B,C):
	#def func(self): print('D')
	pass
d = D()
d.func()
#一般情况下
#d = D()
#会首先调取d的值，d没有找a，b，c依次查找
