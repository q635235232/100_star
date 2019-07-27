from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod
from random import randint, randrange
import random


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


class Person2(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在快乐的玩耍' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)


class Student(Person2):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person2):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s' % (self._name, self._title, course))


def student_tecach_main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('曾志', 38, '老教师')
    t.teach('Python程序设计')
    t.watch_av()


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print("%s：汪汪汪..." % self._nickname)


class Cat(Pet):
    def make_voice(self):
        print("%s：喵...喵..." % self._nickname)


def pet_main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s奥特曼~~~\n' % self._name + \
               '生命值: %d\n' % self._hp + \
               '魔法值: %d\n' % self._mp


class Monster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def fright_main():
    u = Ultraman('曾志', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击' % u.name)
            else:
                print('%s使用了魔法攻击失败' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了终极必杀技虐杀了%s' % (u.name, m.name))
            else:
                u.attack(m)
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


class Card(object):
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, self._face)

    def __repr__(self):  # 重写显示函数，print对象时输出的值不再是内存地址
        return self.__str__()


class Poker(object):
    def __init__(self):
        self._cards = [Card(suite, face)
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """随机洗牌"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):  # 发牌
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):  # 还有没有牌
        return self._current < len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def card_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        self._cards_on_hand.sort(key=card_key)


def get_key(card):
    return (card.suite, card.face)


def poker_main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.card_on_hand)


"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""


class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200 + self._sales * 0.05


def emoplee_main():
    emps=[
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp,Programmer):
            emp.working_hour=int(input('请输入%s本月工作时间'%emp.name))
        elif isinstance(emp,Salesman):
            emp.sales=float(input('请输入%s本月销售额'%emp.name))
        print('%s本月工资为：%s元'%(emp.name,emp.get_salary()))


if __name__ == "__main__":
    emoplee_main()
