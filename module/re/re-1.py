#phone_number = input('please input your phone number ： ')
while True:
    phone_number = input('please input your phone number ： ')
    if len(phone_number) == 11 \
            and phone_number.isdigit()\
            and (phone_number.startswith('13') \
            or phone_number.startswith('14') \
            or phone_number.startswith('15') \
            or phone_number.startswith('18')):
        print('是合法的手机号码')
    else:
        print('不是合法的手机号码')
exit()
