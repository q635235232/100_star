from math import sqrt
from time import time, localtime, sleep


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

        # 访问器 - getter方法

    @property
    def name(self):
        return self._name

        # 访问器 - getter方法

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


class Person1(object):
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

        # 访问器 - getter方法

    @property
    def name(self):
        return self._name

        # 访问器 - getter方法

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print("%s正在玩飞行棋." % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def person_main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()


def _peoson_main():
    person = Person1('王大锤', 22)
    person.play()
    person._gender = '男'


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod  # 静态方法不用生成对象即可调用
    def is_vaild(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def tringle_main(a, b, c):
    if Triangle.is_vaild(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimter())
        print(t.area())
    else:
        print('无法构成三角形')


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self._hour += 1
        if self._hour == 24:
            self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def clock_main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == "__main__":
    clock_main()
