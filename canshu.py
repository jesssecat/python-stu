def test(*args):
	print(args)
l = [1,2,3,4,5]
test(*l)

def test1(l = []):
	l.append(1)
	print(l)
test1()
test1()
test1()
test1()

def max(a,b):
	return a if a>b else b

def the_max(x,y,z):
	c = max(x,y)
	return max(c,z)

print(the_max(1,2,4))

def outer():
	def inner():
		print('inner')
	inner()
outer()
