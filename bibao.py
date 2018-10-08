def outer():
	a = 1
	def inner():
		print(a)
	return inner
inn = outer()
inn()
