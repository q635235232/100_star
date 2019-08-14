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


if __name__ == '__main__':
    a_function_requiring_decoration()
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    print(a_function_requiring_decoration.__name__)
