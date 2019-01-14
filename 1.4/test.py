# -*- coding: UTF-8 -*-
def gogogo():
    i=2
    num=0
    for i in range(2,101):
        if i % 2 == 0:
            num = num + i
        else:
            num = num - i
        i += 1
    print(num)

while(1==1):
    user=str(input('你叫什么？seven吗？：'))
    password=str(input('你的密码呢？是123吗？'))
    if user=='seven':
        if password=='123':
            print('登陆成功！')
            gogogo()
        else:
            break
    else:
        print('登陆失败！')