#class A:
#	def func(self):
#		print('in func')

#a = A()
#a.name = 'jesse'
#a.age = 26
#ret = getattr(a,'name') #仝哥变量名的字符串形式取到值
#print(ret)
#test = input('>>>')
#print(getattr(a,test))

#反射对象的方法
#ret = getattr(a,'func')
#getattr('对象'，方法的字符串名)
#ret()

#反射类的属性
#class A:
#	price = 20
#	def func(self):
#		print('in func')
#A.price  普通
#print(getattr(A,'price'))

#反射类的方法classmethod,staticmethod
class A:
	price = 20
	@classmethod
	def func(cls):
		print('in func')
if hasattr(A,'func'):
	getattr(A,'func')()
