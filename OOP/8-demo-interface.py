#接口类开发
#类似内置函数
#有一个内置的函数
#有一个内置的支付入口
#直接封装好
class Alipay:
	def pay(self,money):
		print('已经用支付宝支付了%s元' % money)

class Wechat:
	def pay(self,money):
		print('已经用微信支付了%s元' % money)
	def pas(self,money):
		print('使用现金支付了%s元' % money)

def pay(pay_obj,money):
	pay_obj.pay(money)
wechat = Wechat()
alipay = Alipay()
pay(wechat,100)
pay(alipay,200)

def pas(pay_obj,money):
	pay_obj.pay(money)
ppp = Wechat()
pas(ppp,88)


#原来的调用
#ali = Alipay()
#ali.pay(90)
#wechat = Wechat()
#wechat.pay(100)




