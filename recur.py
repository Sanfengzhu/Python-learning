# -*- coding: utf-8 -*-

print('阶乘的递归实现：')
print('-------------')
def fact(n):
    if n==1:
        return 1
    else:
        return n* fact(n-1)

print('fact(100)=', fact(100))
print('fact(4)=', fact(4))
#这里会溢出栈，需要特别注意一下print('fact(1000)=', fact(1000))
#fact(1000)
print('汉诺塔的递归实现：')
print('-------------')
def move(n, a, b, c):
    if n==1:
        print('Move %2s from %s' % (a, c))
        return
    else:
        move(n-1, a, c, b)
        print('Move %2s from %s' % (a, c))
        move(n-1, b, a, c)


move(4, 'A', 'B', 'C')
