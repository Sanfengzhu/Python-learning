sum=0
# for x in list(range(101)):
for x in range(101):
    sum=sum+x
print(sum)

#用while实现高斯计算
sum=0
n=100
while n>=1:
    sum=sum+n
    n=n-1
print(sum)

#计算奇数之和
sum=0
n=99
while n >0:
    sum=sum +n
    n=n-2
print('100以内的奇数之和为： %d' % sum)

#100以内的整数连乘
acc=1
n=1
while n<=100:
    acc=acc*n
    n=n+1
print('100以内整数的乘积为： %d' % acc)

