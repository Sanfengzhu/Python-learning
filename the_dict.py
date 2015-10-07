# -*- coding: utf-8 -*-
# 测试dict
print('This it a test for using dict')
d={'Susan': 90, 'Linda': 91, 'Lisa': 99}
print('d[\'Susan\'] =', d['Susan'])
print('d[\'Linda\'] =', d['Linda'])
print('d[\'Lisa\'] =', d['Lisa'])
print('d.get(\'Tom\', -2) =', d.get('Tom', -2))

#测试set
print('This it a test for using set')
s1=set([1,1,2,2,3,3])
print(s1)
s2=set([2,2,3,4])
print('求集合的交集： ', s1 & s2)
print('求集合的并集： ', s1 | s2)
