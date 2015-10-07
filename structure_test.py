# print('1024 * 768 =', 1024*768)
# name=input('Please enter your name: ')
# print('hello,',name)

# 测试行与转义
print('''line1
line2
line3''')
print(r'''\\line1
line2
line3''')
print('Test the conditional sentence: ')

# 测试条件输出，判断
age=19
if(age>18):
    print('adult')
else:
    print('teenager')

# 测试赋值运算
a='ABC'
b=a
a='XYZ'
print(b)

# 字符串相关处理操作
n=123
f=456.789
s1='Hello, world'
s2='Hello, \'Adam\''
s3=r'Hello, "Bart"'
s4=r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
