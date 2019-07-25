import random
import os
from random import randrange, randint, sample
import copy


# 随机验证码
def get_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# 获取文件后缀名
def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


# 获取文件名和路径
def get_file_name(file_url):
    file_url = "D:\\xunlei\\UninstallXLWFP.exe"
    input_file_path = os.path.dirname(file_url)
    input_file_name = os.path.basename(file_url)
    file = {"name": input_file_name, "path": input_file_path}
    return file


# 取两个最大的数
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else [x[1], x[0]]
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# 筛选——如果闰年就是第二列，普通就是第一列
def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


# 杨辉三角
def yanghui():
    num = int(input('please enter the number'))
    yh = [[]] * num  # 行复制，决定了有多少行
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()


# 双色球问题
# 分开输出
def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


# 并排输出
def display1(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('%02d' % ball, end='|')
        else:
            print('%02d' % ball, end=' ')


# 随机选球
def random_select():
    red_balls = [x for x in range(1, 34)]
    select_balls = []
    select_balls = sample(red_balls, 6)
    select_balls.sort()
    select_balls.append(randint(1, 16))
    return select_balls


# 双色球问题
def qiu_main():
    n = int(input('机选几注'))
    for _ in range(n):
        display(random_select())


# 约瑟夫环问题
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，
# 由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
# 15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
def yue_se_fu():
    persons = [True] * 30
    counter, index, number = 0, 0, 0  # counter是淘汰的人数，index是每个人的序号，number是计数
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                number = 0
                counter += 1
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')


# 直接赋值和浅拷贝和深拷贝
def low_copy_and_deep_copy():
    a = [1, 2, 3, [4, 5, 6], 7]
    b = a  # 直接赋值，a改变,b也要跟着改变
    c = copy.copy(a)  # 浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
    d = copy.deepcopy(a)  # 深拷贝，与原始对象没有关系，原始对象a改变而d不变
    print('增加子对象')  # b会跟着变，而c，d不变
    a.append(8)
    print(a)
    print(b)
    print(c)
    print(d)
    print('第二次改变父对象的原来对象')  # c也会跟着变，d不会变
    a[3].append(8)
    print(a)
    print(b)
    print(c)
    print(d)

# 井字棋游戏
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def qi_main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == "__main__":
    qi_main()
