# -*- coding:utf-8 -*-

#1.2.1

a=0o101
print("a="+str(a))

b=64
print('b='+str(b))

c=-237
print('c='+str(c))

d=0x80
print('d='+str(d))

e=-0x92
print('e='+str(e))

print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1,)))

foo=42
bar= foo<42

print(bar)
print(bar+10)
print('%s' %bar)
print('%d' %bar)

#无_nozero_() 
class C:pass

c=C()
print(bool(c))

print(0.0)
print(-777.)
print(-5.555567119)
print(96e3 * 1.0)
print(-1.609E-19)

print(complex(2,4))
print(1.23e-045+6.7e+089j)


# 十进制浮点
# 十进制浮点
from decimal import *
 
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))

print("转换工厂....")
print(int(4.2222222))
print(float(4))
print(complex(4))

#ASCII转换
print("进制转换....")
print(chr(76))
print(ord('L'))

#扩展阅读,请自行查阅资料了解Python常用的数学函数：
a='''
ceil(x)  大于等于 x,并且与它最接近的整数
floor(x) 也写做Floor(x)，其功能是“向下取整”，或者说“向下舍入”
fabs(x)  取x的绝对值
factorial(x)  x的阶乘
hypot(x,y)  计算直角三角形的斜边长
sqrt(xx+yy)
pow(x,y)
sqrt(x)
log(x)
log10(x)
trunc(x)
isnan (x)
degree (x)
radians(x)
'''

print(a)
