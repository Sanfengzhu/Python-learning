# -*- coding: utf-8 -*-

from functools import reduce

chars={
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
    }

def str2int(s):
    ints=map(lambda ch:chars[ch], s)
    return reduce(lambda x, y: x*10+y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

char_to_float={
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
    }
def str2float(s):
    nums=map(lambda ch: char_to_float[ch], s)
    point=0
    def to_float(f, n):
        nonlocal point
        if n==-1:
            point=1
            return f
        if point==0:
            return f*10+n
        else:
            point=point*10
            return f+n/point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

# 将英文名字规范化，首字母大写，其他字母小写

def normalize(name):
    name=name[0].upper()+name[1:].lower()
    return name
L1=['adam', 'LISA', 'barT']
L2=list(map(normalize, L1))
print(L2)

# 利用reduce对list求积

# from functools import reduce
def prod(L):
    return reduce(lambda x, y: x*y, L)
print('3*5*7*9=', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个函数，把字符串的数字转换成浮点数

def str2float2(s):
    pos=s.find('.')
    if pos==-1:
        return int(s)
    def char2num(c):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]
    return int(s[:pos])+reduce(lambda x,y: 0.1*x+y, map(char2num,s[:pos:-1]))/10
print(str2float2('0'))
print(str2float2('123.456'))
print(str2float2('123.45600'))
print(str2float2('0.1234'))
#print(str2float2('.1234'))
print(str2float2('120.0034'))

# 测试map用法
def f(x):
    return x*x
print(list(map(f, [1,2,3,4,5,6,7])))

