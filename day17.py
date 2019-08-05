# 归并排序
def merge_sort(items, comp=lambda x, y: x <= y):
    # 分治法
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    # 合并
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


# 顺序查找
def seq_serch(items, key):
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


# 二分查找
def bin_serch(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


# 使用生成式（推导式）语法
def create():
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


# 嵌套的列表
def input_score():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    scores = [[None] * len(courses) for _ in range(len(names))]
    for row, name in enumerate(names):
        for col, course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}的成绩'))
        print(scores)


# 字典嵌套列表
def dict_list():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    scores = {names[i]: {courses[j]: None for j in range(3)} for i in range(5)}
    print(scores)
    for name, total in scores.items():
        for course in total:
            scores[name][course] = float(input(f'请输入{name}的{course}成绩'))
    print(scores)


"""
     从列表中找出最大的或最小的N个元素
     堆结构(大根堆/小根堆)
 """

import heapq


def use_heapq():
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


"""
     迭代工具 - 排列 / 组合 / 笛卡尔积
"""
import itertools


def use_itertools():
    i1 = itertools.permutations('ABCD')  # 组合
    i2 = itertools.combinations('ABCDE', 3)  # 三种组合，3是参数
    i3 = itertools.product('ABCD', '123')  # 两个一起组合


"""
     找出序列中出现次数最多的元素
 """
from collections import Counter


def use_Counter():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3))


'''
 - 穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
     - 贪婪法 - 在对问题求解时，总是做出在当前看来
     - 最好的选择，不追求最优解，快速找到满意解。
     - 分治法 - 把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
     - 回溯法 - 回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
     - 动态规划 - 基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。

'''


# 穷举法例子：百钱百鸡和五人分鱼。
# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
def chicken():
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if x * 5 + y * 3 + z // 3 == 100 and z % 3 == 0:
                print('公鸡%s只,母鸡%s只,小鸡%s只' % (x, y, z))


# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
def catch_fish():
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5


'''
     贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

     |  名称  | 价格（美元） | 重量（kg） |
     | :----: | :----------: | :--------: |
     |  电脑  |     200      |     20     |
     | 收音机 |      20      |     4      |
     |   钟   |     175      |     10     |
     |  花瓶  |      50      |     2      |
     |   书   |      10      |     1      |
     |  油画  |      90      |     9      |
'''
"""
     贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
     输入：
     20 6
     电脑 200 20
     收音机 20 4
     钟 175 10
     花瓶 50 2
     书 10 1
     油画 90 9
"""


class Thing(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        return self.price / self.weight


def input_thing():
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main2():
    max_weight, num_of_thing = map(int, input().split())
    all_thing = []
    for _ in range(num_of_thing):
        all_thing.append(Thing(*input_thing()))
    all_thing.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_thing:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight +=thing.weight
            total_price+=thing.price
    print('小偷拿走了价值%d美元的物品'%total_price)


if __name__ == '__main__':
    main2()
