class A:pass
a = A()
class B(A):pass
print(isinstance(B(),A))
print(isinstance(a,A))
print(isinstance(A(),B))
#isinstance 判断函数是否存在
