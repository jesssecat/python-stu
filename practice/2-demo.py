list=[
	{"name":"jesse","body":"youxi"},
	{"name":"feiyu","body":"wangzhe"},
	{"name":"jesse","body":"chifan"},
	{"name":"feiyu","body":"wow"},
	{"name":"jesse","body":"CF"},
	{"name":"jesse","body":"LOL"},
]
list4=[]
for item in list:
	for dic in list4:
		if item['name'] == dic['name']:
			dic['hobby_list'].append(item['body'])
			break
	else:
		list4.append({"name":item['name'],"hobby_list":[item['body']]})
print(list4)

"""
[{'name': 'jesse', 'hobby_list': ['youxi', 'chifan', 'CF', 'LOL']}, {'name': 'feiyu', 'hobby_list': ['wangzhe', 'wow']}]
"""
