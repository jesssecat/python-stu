print('\033[0;32;40m欢迎使用学生选课系统\033[0m')
try:
    num = int(input('请输入数字选择功能 ：'))
except Exception as e:
    print('\033[31m对不起！您输入的内容有误～\033[0m')
