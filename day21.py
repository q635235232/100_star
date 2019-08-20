"""
     多进程和进程池的使用
     多线程因为GIL的存在不能够发挥CPU的多核特性
     对于计算密集型任务应该考虑使用多进程
     time python3 example22.py
     real    0m11.512s
     user    0m39.319s
     sys     0m0.169s
     使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
     这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
"""
import concurrent.futures
import math

PRIMES = [
             1116281,
             1297337,
             104395303,
             472882027,
             533000389,
             817504243,
             982451653,
             112272535095293,
             112582705942171,
             112272535095293,
             115280095190773,
             115797848077099,
             1099726899285419
         ] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def use_more_process():
    """使用进程池"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


"""异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，
因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，
由于执行时间和顺序的不确定，因此需要通过回调式编程或者`future`对象来获取任务执行的结果。Python 3通过`asyncio`模块
和`await`和`async`关键字（在Python 3.7中正式被列为关键字）来支持异步处理。"""

"""
    异步I/O - async / await
"""

import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print(('Square =>', i * i))
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


def use_async():
    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()


"""说明：上面的代码使用`get_event_loop`函数获得系统默认的事件循环，通过`gather`函数可以获得一个`future`对象，
`future`对象的`add_done_callback`可以添加执行完成时的回调函数，
`loop`对象的`run_until_complete`方法可以等待通过`future`对象获得协程执行结果。
Python中有一个名为`aiohttp`的三方库，它提供了异步的HTTP客户端和服务器，这个三方库可以跟`asyncio`模块一起工作，
并提供了对`Future`对象的支持。Python 3.6中引入了async和await来定义异步执行的函数以及创建异步上下文，
在Python 3.7中它们正式成为了关键字。下面的代码异步的从5个URL中获取页面并通过正则表达式的命名捕获组提取了网站的标题。
"""
import re
import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def use_aiohttp():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    use_aiohttp()
