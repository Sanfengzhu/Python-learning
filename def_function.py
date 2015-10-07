# -*- coding: utf-8 -*-
import math

def my_abs(x):
        if not isinstance(x,(int, float)):
                raise TypeError('bad operand type')
        if x>=0:
                return x
        else:
                return -x

def move(x, y, step, angle=0):
        nx=x+step*math.cos(angle)
        ny=y-step*math.sin(angle)
        return nx, ny

#测试一元二次方程的根
def quadratic(a, b, c):
    if a==0:
       return None
    elif b*b-4*a*c<0:
       return Nnoe
    else:
       x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
       x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
       return (x1, x2)
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

print(my_abs(-2))

x,y=move(100, 100, 60, math.pi/6)
print(x,y)

#TypeError: bad operand type:
my_abs('123')
