class Animal:
	def __init__(self,name,aggr,hp):
		self.name = name
		self.aggr = aggr
		self.hp = hp
	def eat(self):
		print('喝水---')
		self.hp+=100

class Dog(Animal):
		def __init__(self,name,aggr,hp,kind):
			super().__init__(name,aggr,hp)#只在p3中有
			self.kind = kind
		def eat(self):print('dog')
jin  = Dog('xiaoming',200,500,'ttt')
print(jin.name)
jin.eat() 
#如果在dog中有eat就会输出dog，否则会集成上面的喝水
super(Dog,jin).eat()
