import time
from math import sqrt


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def study_main():
    stu1 = Student('曾志', 22)
    stu1.study('Python程序设计')
    stu1.watch_movie()
    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def Test_main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)


def Test_main2():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)


class parent(object):
    parent_name = 'parent'
    age = 100

    def __init__(self, address, sex):
        self.address = address
        self.sex = sex
        print('my name is parent')

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class child(parent):
    child_name = "child"

    def __init__(self, address, sex):
        super().__init__(address, sex)

    def hello(self):
        print('hello {0}'.format(self.name))

    def get_name(self):
        print('nice day!')


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self.hour, self.minute, self.second)


def clock_main():
    now = time.strftime("%H:%M:%S", time.localtime())
    hour = int(now.split(':')[0])
    minute = int(now.split(':')[1])
    second = int(now.split(':')[2])
    clock = Clock(hour=hour, minute=minute, second=second)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 移动到新的位置
    def move_to(self, x, y):
        self.x = x
        self.y = y

    # 移动指定增量
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def Point_main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

# 单下划线表示保护方法，只有自己和子类能访问。双下划线表示私有，只有自己才能访问，子类也不能重写
# 使用supper可以继承__init__，否则不能继承
# 继承时要用super().__init__才能继承初始化方法
