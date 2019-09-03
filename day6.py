# 重名函数，实现后面的
# def foo():
#     print('hello, world!')
#
#
# def foo():
#     print('goodbye, world!')
# foo()
# 可变参数传参
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total
# 执行函数
# def foo():
#     pass
#
#
# def bar():
#     pass
#
#
# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()
# 函数练习
# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#
#
# def lcm(x, y):
#     return x * y // gcd(x, y)
#
#
# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num
#
#
# def is_prime(num):
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
#
# def is_palinddrome_is_prime(num):
#     if is_palindrome(num) and is_prime(num):
#         print('%d这是回文素数' % num)
#     else:
#         print('%d这不是回文素数' % num)
#
#
# def foo():
#     b = 'hello'
#
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#     bar()
#
#
# if __name__ == '__main__':
#     # a=is_palindrome(12321)
#     # print(a)
#     a = 100
#     foo()
# 函数不能改变全局变量用法
# def foo():
#     a = 200
#     print(a)
# # if __name__ == '__main__':
# #     a = 100
# #     foo()
# #     print(a)
# #
# 函数能改变全局变量用法
# def foo1():
#     global a
#     a=200
#     print(a)
#
# if __name__=='__main__':
#     a=100
#     print(a)
#     foo1()
#     print(a)

# 我们可以使用`global`关键字来指示`foo`函数中的变量`a`来自于全局作用域，如果全局作用域中没有`a`，
# 那么下面一行的代码就会定义变量`a`并将其置于全局作用域。
# 同理，如果我们希望函数内部的函数能够修改嵌套作用域中的变量，
# # 可以使用`nonlocal`关键字来指示变量来自于嵌套作用域，请大家自行试验。
# nonlocal嵌套函数改变局部变量
# def foo():
#     a=100
#     print(a)
#     def bar():
#         nonlocal a
#         a=200
#         print(a)
#     bar()
#     print(a)
#
# if __name__=="__main__":
#     foo()
# 用类实现加法
# class _Add(object):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#
# 用闭包函数实现加法
# def _Add1(a):
#     def add(b):
#         return a + b
#
#     return add
#
#
# ad = _Add1(1)  # 先初始化
# print(ad(1))  # 传参内部add函数，
# print(ad(2))  # 第二次调用还是和第一次一样
# print(ad(3))

# 闭包函数的错误运用
# 因为i的调用时延迟绑定，等到后面的循环结束才会找到i，所以调用时i=3
# def mutipliers():
#     return [lambda x:i*x for i in range(4)]
# x=[m(2) for m in mutipliers()]
# print(x)
# #
# #闭包的正确运用
# #因为给了默认参数i，所以每次调用i都是会找i的引用，以此类推。
# def mutipliers():
#     return [lambda x,i=i:i*x for i in range(4)]
# x=[m(2) for m in mutipliers()]
# print(x)
# # filter过滤函数
# def is_odd(n):
#     return n % 2 == 1
#
# # 过滤偶数,将参数传给函数，逐一比较，符合的留下
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 删除空字符
# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty,['A','','B',None,'C',' '])))
# Python的内置函数
# - 数学相关: abs(绝对值) / divmod(返回商和余数的元组) / pow(次方)
# / round(浮点数保留几位用法，round(n,m)/n是参数，m是保留位数)
#  / min / max / sum
# - 序列相关: len / range
# / next/next() 返回迭代器的下一个项目。
# -*- coding: UTF-8 -*-
# it = iter([1, 2, 5, 4, 3])
# while True:
#     x = next(it, 'a') #只传it就不会加入a。
#     print(x)
#     if x == 'a': #这里会无线加入a所以要遇到a跳出
#         break
# 1
# 2
# 5
# 4
# 3
# a
# / filter(过滤函数，上面有) /
# map/map() 会根据提供的函数对指定序列做映射。
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# map() 函数语法： map(function, iterable, ...)
# 参数 function -- 函数 iterable -- 一个或多个序列
# 返回值:
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
# / sorted
# / slice /slice() 函数实现切片对象，主要用在切片操作函数里的参数传递。
# class slice(stop)
# class slice(start, stop[, step])
# 参数说明：
# start -- 起始位置
# stop -- 结束位置
# step -- 间距
#>>>myslice = slice(5)    # 设置截取5个元素的切片
# >>> myslice
# slice(None, 5, None)
# >>> arr = range(10)
# >>> arr
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> arr[myslice]         # 截取 5 个元素
# [0, 1, 2, 3, 4]
# >>>
# / reversed(反转)
# locals/locals() 函数会以字典类型返回当前位置的全部局部变量。
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
# iter/iter() 函数用来生成迭代器。
# 实例：
# lst = [1, 2, 3]
#  for i in iter(lst):
#           print(i)
#
# 1
# 2
# 3
# - 类型转换: chr/chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
# chr(i)/i -- 可以是10进制也可以是16进制的形式的数字。
# print chr(0x30), chr(0x31), chr(0x61)   # 十六进制
# 0 1 a
# print chr(48), chr(49), chr(97)         # 十进制
# 0 1 a
# /ord (返回对应的 ASCII 数值，或者 Unicode 数值)
# / str / bool / int / float / complex(复数)/complex(n,m)n为实部，m为虚部 /
# bin(返回一个整数 int 或者长整数 long int 的二进制表示。返回值是str)
# / oct/oct() 函数将一个整数转换成8进制字符串。
# / hex/hex() 函数用于将10进制整数转换成16进制，以字符串形式表示。
# - 数据结构: dict / list(将元组转回列表) / set(去除重复原数) / tuple /
#  zip(zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。)
# zip在python3中返回的是对象，所以需要手动用list转换回来。
# - 其他函数: all(all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 0、空、None、False 外都算 True。)
# execfile() 函数可以用来执行一个文件。
# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
# 语法以下是 issubclass() 方法的语法:
# issubclass(class, classinfo)
# 参数 class -- 类。 classinfo -- 类。
# super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
# 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
# #语法
# 以下是 super() 方法的语法:
# super(type[, object-or-type])
# 参数
# type -- 类。
# object-or-type -- 类，一般是 self
# Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
# Python3.x 实例：
# 实例
# class A:
#      def add(self, x):
#          y = x+1
#          print(y)
# class B(A):
#     def add(self, x):
#         super().add(x)
# b = B()
# b.add(2)

# / any(any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 0、空、FALSE 外都算 TRUE。)
# id/id() 函数用于获取对象的内存地址。
# input(输入)  / open(打开文件) / print / type
# isinstance/isinstance(object, classinfo)/判断类型是否一致
# numerate/numerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中。
"""seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""
# eval/eval() 函数用来执行一个字符串表达式，并返回表达式的值.
# eval(expression[, globals[, locals]])
# expression -- 表达式。
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
# 以下展示了使用 eval() 方法的实例：
# >>>x = 7
# >>> eval( '3 * x' )
# 21
# >>> eval('pow(2,2)')
# 4
# >>> eval('2 + 2')
# 4
# >>> n=81
# >>> eval("n + 4")
# 85
