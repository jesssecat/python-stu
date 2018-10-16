#ret = int(input('number >>>'))
#print(ret*'*')
#程序只能输入数字，数字才可以转换成init
#这样就会报错

#设置异常处理机制，并且捕获错误
#异常处理机制
#try except
#except支持多分支
#except Exception万能错误处理异常
try:
	ret = int(input('number >>>'))
	print(ret*'*')
except ValueError:
	print('您输入的内容有错误，请输入一个数字')
