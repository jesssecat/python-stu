std1 = {'name':'jesse','score':98}
std2 = {'name':'zhenyu','score':100}
def print_score(std):
	print('%s:' '%s' % (std['name'],std['score']))
#print_score(std1)
#print_score(std2)

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s:%s' %(self.name,self.score))
#jesse = Student('jesse xiaoyu',59)
#esse.print_score()

class Add(object):
	def __init__(self,num1,num2):
		self.num1 = num1
		self.num2 = num2
	def print_code(self):
		self.num3 = self.num1 * self.num2
		print('%s' %(self.num3))
test1 = Add(7,5)
test1.print_code()
