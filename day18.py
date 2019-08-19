"""
   快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(origin_items, comp=lambda x, y: x <= y):
    items = origin_items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def _use_quick_sort():
    list1 = [9, 5, 7, 8, 1, 6, 9, 12, 101, 11]
    print(quick_sort(list1))


"""
    递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。   
"""
import sys
import time


def _use_patrol():
    SIZE = 5
    total = 0

    def print_board(board):
        for row in board:
            for col in row:
                print(str(col).center(4), end='')
            print()

    def patrol(board, row, col, step=1):
        if row >= 0 and row < SIZE and \
                col >= 0 and col < SIZE and \
                board[row][col] == 0:
            board[row][col] = step
            if step == SIZE * SIZE:
                nonlocal total
                total += 1
                print(f'第{total}种走法: ')
                print_board(board)
            patrol(board, row - 2, col - 1, step + 1)
            patrol(board, row - 1, col - 2, step + 1)
            patrol(board, row + 1, col - 2, step + 1)
            patrol(board, row + 2, col - 1, step + 1)
            patrol(board, row + 2, col + 1, step + 1)
            patrol(board, row + 1, col + 2, step + 1)
            patrol(board, row - 1, col + 2, step + 1)
            patrol(board, row - 2, col + 1, step + 1)
            board[row][col] = 0

    def use_patrol():
        board = [[0] * SIZE for _ in range(SIZE)]
        patrol(board, SIZE - 1, SIZE - 1)

    use_patrol()


def main3():
    items = list(map(int, input().split()))
    size = len(items)
    overall, partial = {}, {}
    overall[size - 1] = partial[size - 1] = items[size - 1]
    for i in range(size - 2, -1, -1):
        partial[i] = max(items[i], partial[i + 1] + items[i])
        overall[i] = max(partial[i], overall[i + 1])
    print(overall[0])


def use_filter_and_map():
    items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
    items2 = [x ** 2 for x in range(1, 10) if x % 2]
    print(items1, items2)


# 装饰器
def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


"""
     月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""
from abc import ABCMeta, abstractmethod


class Emoploee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Emoploee):
    def get_salary(self):
        return 15000.0


class Programmer(Emoploee):
    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Emoploee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory():
    @staticmethod
    def create(emp_type, *args, **kwargs):
        emp_type = emp_type.upper()
        emp = None
        if emp_type == 'M':
            emp = Manager(*args, **kwargs)
        elif emp_type == 'P':
            emp = Programmer(*args, **kwargs)
        elif emp_type == 'S':
            emp = Salesman(*args, **kwargs)
        return emp


def use_factory():
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print('%s:%.2f元' % (emp.name, emp.get_salary()))


# unique会检查重复，重复报错
# enum枚举
from enum import Enum, unique
import random


@unique
class Suite(Enum):
    """花色"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):
        return self.value < other.value


class Card():
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def show(self):
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()


class Poker():
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]

    def shuffle(self):
        """洗牌（打乱顺序）"""
        random.shuffle(self.cards)
        self.index = 0

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


class Player():
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def sort(self, comp=lambda card: (card.suite, card.face)):
        """"整理手头的牌"""
        self.cards.sort(key=comp)


def use_poker():
    """使用扑克牌"""
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    while poker.has_more:
        for player in players:
            player.get_one(poker.deal())
    for player in players:
        player.sort()
        print(player.name, end=': ')
        print(player.cards)


class SetOnceMappingMixin():
    """自定义混入类,例子：自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。"""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)


class SetOneDict(SetOnceMappingMixin, dict):
    """自定义字典"""
    pass


def use_set_dict():
    """使用自定义字典"""
    my_dict = SetOneDict()
    try:
        my_dict['username'] = 'jackfrued'
        my_dict['username'] = 'hellokitty'
    except KeyError:
        pass
    print(my_dict)


if __name__ == '__main__':
    use_set_dict()
