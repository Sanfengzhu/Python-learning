# -*- coding: utf-8 -*-
# 测试输出格式：
a = 72 
b = 85
r = (b - a)/a
print('小明成绩提升的百分点为: %.1f %%' %r)
# 测试Unicode的str和UTF-8的bytes相互转换
s='Python-中文'
print(s)
b=s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
