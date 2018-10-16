#在本函数内部直接自己调用
class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 80:
			return 'B'
		elif self.score >= 60:
			return 'C'
		else:
			return 'D'
jesse = Student('jesse',100)
print(jesse.name,jesse.get_grade())

make = Student('make',59)
print(make.name,make.get_grade())
