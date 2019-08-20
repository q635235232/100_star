import threading

"""用原类实现单例模式"""


class SingletonMeta(type):
    """自定义元类"""

    def __init__(cls, *args, **kwargs):
        cls._instance = None
        cls._lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class President(metaclass=SingletonMeta):
    """总统类"""
    pass


"""可插拔的哈希算法"""


class StreamHasher():
    """哈希摘要生成器(策略模式)"""

    def __init__(self, alg='md5', size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__('hashlib'), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b''):
            self.hasher.update(buf)
        return self.hasher.hexdigest()


def use_StreamHasher():
    """使用哈希生成器"""
    hasher1 = StreamHasher()
    with open('Python-3.7.1.tgz', 'rb') as stream:
        print(hasher1.to_digest(stream))
    hasher2 = StreamHasher('sha1')
    with open('Python-3.7.1.tgz', 'rb') as stream:
        print(hasher2(stream))


# 两种创建生成器的方式（生成器表达式和`yield`关键字）
def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


# 和迭代器相关的魔术方法（`__iter__`和`__next__`）
class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration


def use_fib():
    """"使用迭代器和生成器"""
    for i in fib(10):
        print(i)
    f = Fib(10)
    for i in f:
        print(i)


if __name__ == '__main__':
    pass
