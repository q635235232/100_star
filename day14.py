from time import time
from threading import Thread
import requests


class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('./Users/Hao/' + filename, 'wb') as f:
            f.write(resp.content)


def main1():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=f40a450fad88239e3f0ca62f2587221a&num=10')
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main1()
