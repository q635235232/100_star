
# set.add（x）只能是一个元素，但是不会拆开
# set.update(x),如果x是一个字符串，则会拆开
# x可以是列表，字典，元祖，而且不会拆开
# 但是字典只会添加字典名
# set1 = set(range(1, 10))
# print(set1)
# set1.update([10, 11, 12])
# print(set1)
# set1.discard(5)
# if 4 in set1:
#     set1.remove(4)
# for elem in set1:
#     print(elem ** 2, end=' ')
# print()
# set3 = set((1, 2, 3, 3, 2, 1,))
# print(set3)
# print(set3.pop())
# print(set3)
# print(set1 & set3)
# print(set3 | set1)
# print(set1 - set3)
# print(set1 ^ set3)
# print(set1 <= set3)
# print(set1 >= set3)
# scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# print(scores.get('武则天', 60))
# print(scores)
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('骆昊', 100))
# scores.clear()
# print(scores)
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


main()
