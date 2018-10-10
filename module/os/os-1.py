import os
#import os.path
#创建一个文件夹，可以递归创建，但是存在报错
#os.makedirs('test/test')

#删除文件夹，删除后判断上面的文件夹如果为空，也会把上面的删除，类推
#os.removedirs('test/test/test')

#生成单级目录
#os.mkdir('test')

#只删除一个文件夹，不进行递归
#os.rmdir('1')

#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
#os.listdir('test')
#l = os.listdir('test')
#l = os.listdir('/')
#print(l)


#删除一个文件,文件夹不可以
#os.remove('1.txt')

#重命名某个文件的信息
#os.rename("test","test-1")

#获取文件、目录信息
#l = os.stat('test-1')
#print(list(l))
#print(list(l)[2])


#运行shell命令，直接显示
#os.system("free -m")

#os.system("top")

#运行shell命令，获取执行结果
#l = os.popen("free -m").read()
#print(l)

#获取当前py的工作目录
#l = os.getcwd()
#print(l)

#改变当前的工作目录，相当于cd
#os.chdir("/root")
#print(os.getcwd())

#返回path规范化的绝对路径
#l = os.path.abspath("/root")
#print(l)

#将path分割成目录和文件名二元组返回 
#l = os.path.split("/usr/bin")
#print(l)

#返回path的目录。其实就是os.path.split(path)的第一个元素
#l = os.path.dirname("/usr/bin")
#print(l)  #/usr

#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
#l = os.path.basename("/usr/bin")
#print(l)  #bin

#如果path存在，返回True；如果path不存在，返回False
#l = os.path.exists("/usr/bin")
#print(l)

#如果path是绝对路径，返回True
#print(os.path.isabs("/usr/bin"))


#如果文件存在，返回true，否则返回false
#l = os.path.isfile("test-1.txt")
#print(l)

#判断目录是否存在，true false
#print(os.path.isdir("test-1"))

#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
#seq1 = ['hello','good','jesse']
#print(' '.join(seq1)) #hello good jesse


#seq2 = ['/hello/','/good/','/jesse/']
#print(list(seq2))
#print(os.path.join('/hello/','/good/','jesse'))
#/good/jesse

#返回path所指向的文件或者目录的最后访问时间
#print(os.path.getatime("test-1.txt"))

#返回path所指向的文件或者目录的最后修改时间
#print(os.path.getmtime("test-1.txt"))

#返回path的大小
#print(os.path.getsize("./test-1"))

#输出当前的系统是linux还是windows
#import sys
#print(sys.platform) #linux
