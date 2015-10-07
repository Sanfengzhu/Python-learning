# -*- coding: utf-8 -*-

s=(x*x for x in range(5))
print(s)
for x in s:
    print(x)

# 杨辉三角 生成器实现
def triangles():
    L=[1]
    while True:
        yield L
        L=[L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0, 1)
        L.append(1)

n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break


# 斐波那契数列实现
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'
f = fib(10)
print('fib(10):', f)
for n in f:
    print(n)

# call generator manually:
g=fib(5)
while 1:
    try:
        x=next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
        
    
