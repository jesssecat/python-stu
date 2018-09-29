d = {1,2,3,4,5,6}
#for key in d:
#		print(key)
#for ch in 'abcdefg':
#		print(ch)
a = list(range(1,11))
print(a)
#没有嵌套关系不用空格
c	=	[m + n for m in 'ABCD' for n in 'UXYZ']
print(c)

import os # 导入os模块，模块的概念后面讲到
e = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(e)
li = ["主机","CPU","磁盘","鼠标"]
for i in li:
	print('{}\t{}'.format(li.index(i)+1,i))

i1 = 6
i2 = 6
print(id(i1),id(i2)) #打印他们的ID是一样的


cc = [1,2,3,4,5,6,77,8,9,22,33,33]
gg = set(cc) #去重
print(gg)
gg = list(gg)
print(gg)
