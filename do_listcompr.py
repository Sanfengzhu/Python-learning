# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[]
for x in L1:
    if isinstance(x, str):
         L2.append(x)
L2=[x.lower()for x in L2]
print(L2)

#简单方法

L2=[x.lower() for x in L1 if isinstance(x, str)]
print('Test listcompr:', L2)
