portfolio = [
{'name':'gupiao1','shares':200,'price':22.5},
{'name':'gupiao2','shares':400,'price':32},
{'name':'gupiao3','shares':700,'price':33},
{'name':'gupiao4','shares':900,'price':44},
{'name':'gupiao5','shares':100,'price':76},
{'name':'gupiao6','shares':122,'price':56.6},
{'name':'gupiao7','shares':223,'price':65.3}
]
#计算购买每个的总价
#ret = map(lambda dic : {dic['name']:round(dic['shares']*dic['price'],2)},portfolio)

#用filter过滤出，单价大于10的有哪些
ret = filter(lambda dic:True if dic['price'] >70 else False,portfolio)
#ret.list()
#print(list(ret))
ret=list(ret)
print(ret)
