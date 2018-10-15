#函数限制访问内部
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s :%s' %(self.__name,self__score()))
test1 = Student('xiaoming',99)
#print(test1.__name) #隐藏
#print(test1.name)
#如果直接运行的话
#Traceback (most recent call last):
#  File "4-demo-limit.py", line 10, in <module>
#    print(test1.__name)
#AttributeError: 'Student' object has no attribute '__name'

