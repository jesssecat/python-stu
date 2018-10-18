class Teacher:
  dic = {'查看XS信息':'show_student123','查看LS信息':'show_teacher321'}
  def show_student(self):
    print('show student')
  def show_teacher(self):
    print('show_teacher')
	
  @classmethod 
  def func(cls):
    print('haha')
  #@classmethod
	#def func(cls)
	#	print('haha')
ret = getattr(Teacher,'dic') #Teacher.dic类也是对象
print(ret) #{'查看XS信息': '', '查看LS信息': ''} 可以直接查看信息

ret2 = getattr(Teacher,'func') #类.方法
print(ret2)
#<bound method Teacher.func of <class '__main__.Teacher'>>
jee = Teacher()
for k in Teacher.dic:
	print(k)
key = input('输入需求：')
print(Teacher.dic[key])
if hasattr(jee,Teacher.dic[key]):
	func = getattr(jee,Teacher.dic[key])
else:
	print('no')
#print(Teacher.dic[key])




