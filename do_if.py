# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5
bmi = weight/(height*height)
print(bmi)
if bmi<= 18.5:
    print('过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <=32:
    print('肥胖')
else:
    print('严重肥胖')

# test用户的输入

s=input('Input your age: ')
age=int(s)
if age >= 18:
    print('Adult')
elif age >= 6:
    print('Teenager')
else:
    print('Kid')
