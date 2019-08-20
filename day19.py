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


import glob
from PIL import Image
import os

PREFIX = 'thumbnails'


def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片文件的缩略图"""
    file, ext = os.path.splitext(infile)
    file = file[file.rfind('\\') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)


def use_more_thread():
    """"使用多线程"""
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    for infile in glob.glob('image/*.png'):
        for size in (32, 64, 128):
            # 创建并启动线程
            threading.Thread(
                target=generate_thumbnail,
                args=(infile, (size, size))
            ).start()


"""
  多线程程序如果没有竞争资源处理起来通常也比较简单
  当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
  说明：临界资源就是被多个线程竞争的资源
"""
import time
from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, money):
        self.account = account
        self.money = money
        # 自定义线程的初始化方法中必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)


def use_more_account():
    """主函数"""
    account = Account()
    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 创建线程的第1种方式
        # threading.Thread(
        #     target=account.deposit, args=(1, )
        # ).start()
        # 创建线程的第2种方式
        # AddMoneyThread(account, 1).start()
        # 创建线程的第3种方式
        # 调用线程池中的线程来执行特定的任务
        future = pool.submit(account.deposit, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    use_more_account()
