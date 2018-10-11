#打印出函数的地址
#def home():
#	print('hello,word')
#print(home) #<function home at 0x7fcb27c97e18>输出函数地址


#我们可以看到这段代码的点睛之笔就在这句：“home = wrapper(home)”，我们将home函数的地址当做参数传给了wrapper方法，在wrapper方法中进行验证，验证通过之后再将home方法的地址返回，这个之后再调用home，我们就在没有修改home方法的情况下，调用了home，是不是方便了很多？这就是装饰器的概念！
#def login(usr):
#    if usr == 'Eva_J':
#        return True
#def wrapper(funcname):
#    if login('Eva_J'):
#        return funcname
#def home():
#    print('this is the home page!')

#home = wrapper(home)
#home()


#但是很快我们发现这种方法还是不好，因为用户必须加上那句点睛之笔的代码再执行原本想执行的home方法，于是在python中就规定装饰器可以这样使用：

#def login(usr):
#	if usr == 'jesse':
#		return True

#def wrapper(funcname):
#	if login('jesse'):
#		return(funcname)
#@wrapper
#def home():
#	print('hello,word')

#home()


#下面是装饰器
def login(usr):
	if usr == 'jesse':
		return True

def wrapper1(funcname):
	print('funcname',funcname)
	def wrapper2(argv):
		if login(argv):
			print('funcname',funcname)
			return funcname(argv)
		else:
			return error
	return wrapper2

def home(usr):
	print('hello,word')
	print('hello,',usr)

home = wrapper1(home)
home('jesse')







