# 求1-100的和
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)
# 求1-100的偶数和
# total=0
# for i in range(2,101,2):
#     total+=i
# print(total)
# 求1-100的偶数和，用if分支实现
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)
# 猜数字，使用到while循环，因为不知道循环次数
# import random
#
# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter+=1
#     number=int(input('请输入你猜的数字'))
#     if answer>number:
#         print('大一点')
#     elif answer<number:
#         print('小一点')
#     else:
#         print('猜对了')
#         break
# print('你一共猜了%d次'%counter)
# if counter>7:
#     print('你的智商余额明显不足，请及时充值')
# 99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()
# 判断素数
# from math import sqrt
#
# number = int(input('请输入一个正整数'))
# end = int(sqrt(number))
# is_prime = True
# for i in range(2, end + 1):
#     if number % i == 0:
#         is_prime = False
#         break
# if is_prime and number != 1:
#     print('%d是素数' % number)
# else:
#     print('%d不是素数' % number)
# 计算两个数的最小公倍数和最大公约数
# x = int(input('x='))
# y = int(input('y='))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print("%d和%d的最大公约数是%d" % (x, y, factor))
#         print("%d和%d的最大公倍数是%d" % (x, y, x * y / factor))
#         break
# 打印三角图案
row = int(input("请输入行数："))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row-i-1):
        print(' ',end='')
    for _ in range(2*i+1):
        print('*',end='')
    print()
