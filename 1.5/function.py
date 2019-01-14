# -*- coding: UTF-8 -*-
 #函数声明
def sayHello():
    print('Hello 玄魂!')

sayHello() #函数调用

#参数
aaa='''注意我们使用过的术语——函数中的参数名称为 形参 而你提供给函数调用的值称为 实参'''
print(aaa)
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    else:
        print(b, 'is maximum')
printMax(3, 4)
 
x = 5
y = 7
print('参数传递')
printMax(x, y)

#局部变量
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
print('局部变量')
x = 50
func(x)
print('x is still', x)

#访问外部变量
def func2():
    global x
 
    print('x is', x)
    x = 2
    print('Changed local x to', x)
print('访问外部变量')
x = 50
func2()
print('Value of x is', x)