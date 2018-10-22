#100 名字和性别不同
#set
class A:
	def __init__(self,name,sex,age):
		self.name = name
		self.sex = sex
		self.age = age
	def __eq__(self,other):
		if self.name == other.name and self.sex == other.sex:
			return True
		return False
	def __hash__(self):
		return hash(self.name + self.sex)
a = A('jesse','男',26)
b = A('jesse','男',27)
print(set((a,b)))
