#读
#f = open('./1.txt',mode='r',encoding='utf-8')
#content = f.read()
#print(content)
#f.close()

#写
#f = open('./1.txt',mode='wb')
#f.write('hello,word'.encode('utf-8'))
#f.close()

#追加
#f = open('./1.txt',mode='a',encoding='utf-8')
#f.write('zhuijia---')
#f.close()

#读写
f = open('./1.txt',mode='r+',encoding='utf-8')
print(f.read())
f.write('jesse,zhenyu')
print(f.read())
f.close()
