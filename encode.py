s1 = 'jesse'
#encode编码str->bytes
s11 = s1.encode('utf-8') #gbk也行
print(s11)
s2 = '中国'
s23 = s2.encode('utf-8')
print(s23)
s24 = s2.encode('gbk')
print(s24)

set1 = set({1,2,3})
#print(set1)
#set1.add('444')
#print(set1)
#set1.update('abc')
#print(set1)
#set1.pop()#删除随机的一个字符
#print(set1)

#set1.remove({1},{2})
#print(set1)

#set1.clear()#清空
#print(set1)


