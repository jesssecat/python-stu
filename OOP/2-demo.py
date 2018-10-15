class Student(object):
	pass
bart = Student()
#print(bart)
#<__main__.Student object at 0x7fb49967af28>
#print(Student)
#<class '__main__.Student'>
class stu(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
test = stu('jesse',100)
print(test.name)
print(test.score)


