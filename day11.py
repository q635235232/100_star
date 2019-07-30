import time
from math import sqrt
import json
import requests


# 一次读文件，需要手动关闭
def main1():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


# 一次读文件，需要手动关闭，使用了try except
def main2():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件解码错误')
    finally:
        if f:
            f.close()


# 一次读文件，不需要自己关闭
def main3():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


# 分开每行读文件，不需要手动关闭
def main4():
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
        print()

    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)


# 判断素数
def is_prime(n):
    assert n > 0
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False


# 读写文件
def main5():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件发生错误！')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成！')


# 二进制读写
def main6():
    try:
        with open('mm.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError as e:
        print('读写文件出现错误')
    print('程序执行结束')


def main7():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')


'''
- `dump` - 将Python对象按照JSON格式序列化到文件中
- `dumps` - 将Python对象处理成JSON格式的字符串
- `load` - 将文件中的JSON数据反序列化成对象
- `loads` - 将字符串的内容反序列化成Python对象
'''


# 天行新闻，需要key
def main8():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == "__main__":
    pass

