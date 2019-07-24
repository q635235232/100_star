# 水仙花数
# for i in range(100,1000):
#     bai = int(i / 100)
#     shi = int(i % 100 / 10)
#     ge = int(i % 10)
#     if bai ** 3 + shi ** 3 + ge ** 3 == i:
#         print(i)
#
# 完美数
# sum = 0
# # for i in range(2, 100000000):
# #     for j in range(1, i):
# #         if i % j == 0:
# #             sum += j
# #     if sum == i:
# #         print('这个是完美数%d' % i)
# #         sum = 0
# #     else:
# #         sum = 0
# 百钱百鸡
# for i in range(0, 20):
# #     for j in range(0, 33):
# #         if (i * 5 + j * 3 + (100 - i - j)/3) == 100:
# #             print('公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, (100 - i - j)))
# 斐波那契数列
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a, end=' ')
# Craps赌博游戏。
from random import randint

total = 1000
while total > 0:
    print('你的资产为%d' % total)
    needs_go_on = False
    if total <= 0:
        break
    while True:
        debt = int(input('请下注'))
        if debt > 0 and debt <= total:
            break
    one = randint(1, 6) + randint(1, 6)
    print('摇出的点数%d' % one)
    if one == 7 or one == 11:
        total += debt
        print('玩家获胜')
    elif one == 2 or one == 3 or one == 12:
        total -= debt
        print('庄家胜')
    else:
        needs_go_on = True
    while needs_go_on:
        if total <= 0:
            break
        two = randint(1, 6) + randint(1, 6)
        print('摇出的点数%d' % two)
        if two == 7:
            total -= debt
            print('庄家胜')
            needs_go_on = False
        elif two == one:
            total += debt
            print('玩家胜')
            needs_go_on = False
    print('你的资产为%d' % total)
print('破产了')
