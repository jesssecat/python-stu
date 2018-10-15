class Student(object):
	def test1(self):
		print('test1!')

class cat(Student):
	def test2(self):
		print('test2')

#didi = Student()
#didi.test1()
didi = cat()
didi.test1()
