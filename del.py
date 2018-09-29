a = [1, 2, 3, 12, 12, 5, 6, 8, 9]
for i in a[:]: #备注a[:]代表的是一个新串，如果a的话，所有会发生变化
    a.remove(i)
    print(a)
#print(a)
