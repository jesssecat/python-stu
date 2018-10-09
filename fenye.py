with open('file',encoding='utf-8') as f:
	l = f.readlines()
page_num = int(input('请输入页码：'))
#1 1-5
#2 6-10
#3 11-15
#4 16-20
#(n-1)*5+1
pages,mod = divmod(len(l),5)
#print(mod)
if mod:
	pages += 1 #一个多少页
if page_num >pages or page_num <= 0:
	print('输入有误！')
elif page_num == pages and mod !=0:
	for i in range(mod):
		print(l[(page_num-1)*5 +i].strip())
else:
	for i in range(5):
		print(l[(page_num-1)*5 +i].strip())
