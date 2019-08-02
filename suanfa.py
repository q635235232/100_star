from time import time
import random
from multiprocessing import Process
from threading import Thread


# 选择排序,找到最小值
def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


# 低质量冒泡
def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


# 高质量冒泡
def bubble_sort1(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


# 偷懒冒泡
def bubble_sort2(origin_items, comp=lambda x, y: x > y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = True
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = False
        if swapped:
            return items
    return items


# 多进程实现
def main1(list1):
    # 打乱顺序
    # list1 = [x for x in range(10000)]
    # random.shuffle(list1)
    # 随机生成数字
    # list1 = random.sample(range(10001), 10000)
    # print(list1)
    start = time()
    p1 = Process(target=bubble_sort, args=(list1,))
    p2 = Process(target=bubble_sort1, args=(list1,))
    p3 = Process(target=bubble_sort2, args=(list1,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time()
    print(end - start)
    # print(bubble_sort(origin_items=list1))
    # print(bubble_sort1(origin_items=list1))
    # print(bubble_sort2(origin_items=list1))


# 多线程实现
def main2(list1):
    # list1 = [x for x in range(10000)]
    # random.shuffle(list1)
    start = time()
    t1 = Thread(target=bubble_sort, args=(list1,))
    t2 = Thread(target=bubble_sort1, args=(list1,))
    t3 = Thread(target=bubble_sort2, args=(list1,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    end = time()
    print(end - start)


# 直接实现
def main3(list1):
    # list1 = [x for x in range(10000)]
    # random.shuffle(list1)
    start = time()
    bubble_sort(origin_items=list1)
    bubble_sort1(origin_items=list1)
    bubble_sort2(origin_items=list1)
    end = time()
    print(end - start)


# 比较三种算法的效率
def main4():
    # 打乱顺序
    list1 = [x for x in range(10000)]
    random.shuffle(list1)
    # 随机生成数字
    # list1 = random.sample(range(10001), 10000)
    # print(list1)
    start = time()
    bubble_sort(origin_items=list1)
    end = time()
    print(end - start)
    start = time()
    bubble_sort1(origin_items=list1)
    end = time()
    print(end - start)
    start = time()
    bubble_sort2(origin_items=list1)
    end = time()
    print(end - start)


if __name__ == '__main__':
    list1 = [x for x in range(10000)]
    random.shuffle(list1)
    main1(list1)  # 多进程
    main2(list1)  # 多线程
    main3(list1)  # 直接实现
