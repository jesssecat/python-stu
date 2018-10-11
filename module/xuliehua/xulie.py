#json dumps 序列化方法  loads反序列化方法
#dumps,loads是直接操作内存的，操作完成后还在内存中
dic = {"k1":'v1'}
print(type(dic),dic)
import json
str_d = json.dumps(dic)
print(type(str_d),str_d)
dic_d = json.loads(str_d)
print(type(dic_d),dic_d)


#将序列化的文件写入文件中
#正常下不能直接写入文件
import json
#存入文件
#dic = {1:"a",2:'b'}
#f = open('fff','w',encoding='utf-8')
#json.dump(dic,f)
#f.close()


#取出文件,并进行反序列化
f = open('fff')
res = json.load(f)
f.close()
print(type(res),res)
