import re
#ret = re.findall('a','eva egohn yuan')
#print(ret)
#['a', 'a']

#ret = re.search('a','eva egohn yuan').group()
#print(ret)
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

#ret = re.match('a','abc').group()
#print(ret)
# 同search,不过尽在字符串开始处进行匹配

#ret = re.split('[ab]','abcd')
#print(ret)
# ['', '', 'cd']
# 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割

#ret = re.sub('\d','H','eva2egon4dedw9',1)
#print(ret)
##将数字替换成'H'，参数1表示只替换1个


#ret = re.subn('\d','H','eva2egon4dedw9')
#print(ret)
#将数字替换成'H'，返回元组(替换的结果,替换了多少次)

#obj = re.compile('\d{3}') #将正则表达式编译为一个正则表达式对象，规则要匹配三个数字
#ret = obj.search('dwedwdwd622wedw')#正则表达式对象调用search，参数为待匹配的字符串
#print(ret.group())#622

#ret = re.finditer('\d','dwedw3sd44w55dfr00')
#print(ret) # <callable_iterator object at 0x10195f940>
#print(next(ret).group())#查看第一个结果 3
#print(next(ret).group())#查看第二个结果 4
#print(next(ret).group())#查看第三个结果 4
#print([i.group() for i in ret]) #查看剩余的左右结果 ['5', '5', '0', '0']

#ret = re.split("\d","dwe3fer3ewdew3dew")
#print(ret)#['dwe', 'fer', 'ewdew', 'dew']

#ret1 = re.split("(\d+)","dwe3fer3ewdew3dew")
#print(ret1)#['dwe', '3', 'fer', '3', 'ewdew', '3', 'dew']
#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项，
#这个在某些需要保留匹配部分的使用过程是非常重要的。

#ret = re.search("<(?P<tag_name>\w+)>\w+</(?P=tag_name)>","<h1>hello</h1>")
#还可以在分组中利用?<name>的形式给分组起名字
#获取的匹配结果可以直接用group('名字')拿到对应的值
#print(ret.group('tag_name'))  #结果 ：h1
#print(ret.group())  #结果 ：<h1>hello</h1>

#ret = re.search(r"<(\w+)>\w+</\1>","<h1>hello</h1>")
#print(ret.group(1))
#print(ret.group())


#匹配整数
#ret=re.findall(r"\d+","1-2*(60+(-40.35/5)-(-4*3))")
#print(ret) #['1', '2', '60', '40', '35', '5', '4', '3']

#ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
ret=re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")
print(ret) #['1', '-2', '60', '', '5', '-4', '3']
#ret.remove("")
#print(ret) #['1', '-2', '60', '5', '-4', '3']
ret.remove("")
print(ret)




